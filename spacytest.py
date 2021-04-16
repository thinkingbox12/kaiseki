#!/usr/bin/env python
#-*- coding: utf-8 -*-
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc
from spacy.pipeline import EntityRuler

from jamdict import Jamdict
jam = Jamdict()

nlp = spacy.load("ja_core_news_lg")

doc1 = nlp("心に受け止める")
doc2 = nlp("お体大事にしてください")
doc3 = nlp("話が一つ二つあります")
doc4 = nlp("人生にはもっと大事なことがある")
doc5 = nlp("体を大事にしなさい")
doc6 = nlp("あの木の下のほうにいる")
doc7 = nlp("明らかになる")
doc8 = nlp("全部上手く行くよ")
doc9 = nlp("あなたは手も足も出ないんだぞ")
doc10 = nlp("いつもの一日だった")
doc11 = nlp("そこでこの日病院に連れて行くと")

print([(token.text, token.pos_) for token in doc1])
print([(token.text, token.pos_) for token in doc2])
print([(token.text, token.pos_) for token in doc3])
print([(token.text, token.pos_) for token in doc4])
print([(token.text, token.pos_) for token in doc5])
print([(token.text, token.pos_) for token in doc6])
print([(token.text, token.pos_) for token in doc7])
print([(token.text, token.pos_) for token in doc8])
print([(token.text, token.pos_) for token in doc9])
print([(token.text, token.pos_) for token in doc10])
print([(token.text, token.pos_) for token in doc11])

class EntityRetokenizeComponent:
  def __init__(self, nlp):
    pass
  def __call__(self, doc):
    with doc.retokenize() as retokenizer:
        for ent in doc.ents:
            retokenizer.merge(doc[ent.start:ent.end], attrs={"LEMMA": str(doc[ent.start:ent.end])})
    return doc

ruler = EntityRuler(nlp, phrase_matcher_attr="LEMMA")

# find all idseq of lexical entry (i.e. words) that have at least 1 sense with pos = suru verb - irregular
with jam.jmdict.ctx() as ctx:
    # query all word's idseqs
    rows = ctx.select(
        query="SELECT DISTINCT idseq FROM Sense WHERE ID IN (SELECT sid FROM pos WHERE text = ?)",
        params=("expressions (phrases, clauses, etc.)",))
    for row in rows:
        # reuse database connection with ctx=ctx for better performance
        word = jam.jmdict.get_entry(idseq=row['idseq'], ctx=ctx)
        ruler.add_patterns([{"label": "EXPRESSION", "pattern": x.text} for x in word.kanji_forms])
        ruler.add_patterns([{"label": "EXPRESSION", "pattern": x.text} for x in word.kana_forms])
        print("Working on expressions...")

with jam.jmdict.ctx() as ctx:
    # query all word's idseqs
    rows = ctx.select(
        query="SELECT DISTINCT idseq FROM Sense WHERE ID IN (SELECT sid FROM pos WHERE text = ?)",
        params=("Ichidan verb",))
    for row in rows:
        # reuse database connection with ctx=ctx for better performance
        word = jam.jmdict.get_entry(idseq=row['idseq'], ctx=ctx)
        ruler.add_patterns([{"label": "ICHIDANVERB", "pattern": x.text} for x in word.kanji_forms])
        ruler.add_patterns([{"label": "ICHIDANVERB", "pattern": x.text} for x in word.kana_forms])
        print("Working on ichidan verbs...")

nlp.add_pipe(ruler) 

retokenizer = EntityRetokenizeComponent(nlp)
nlp.add_pipe(retokenizer, name='merge_phrases')

print("\n")
doc1 = nlp("心に受け止める")
doc2 = nlp("お体大事にしてください")
doc3 = nlp("話が一つ二つあります")
doc4 = nlp("人生にはもっと大事なことがある")
doc5 = nlp("体を大事にしなさい")
doc6 = nlp("あの木の下のほうにいる")
doc7 = nlp("明らかになる")
doc8 = nlp("全部上手く行くよ")
doc9 = nlp("あなたは手も足も出ないんだぞ")
doc10 = nlp("いつもの一日だった")
doc11 = nlp("そこでこの日病院に連れて行くと")

print([(token.text, token.pos_) for token in doc1])
print([(token.text, token.pos_) for token in doc2])
print([(token.text, token.pos_) for token in doc3])
print([(token.text, token.pos_) for token in doc4])
print([(token.text, token.pos_) for token in doc5])
print([(token.text, token.pos_) for token in doc6])
print([(token.text, token.pos_) for token in doc7])
print([(token.text, token.pos_) for token in doc8])
print([(token.text, token.pos_) for token in doc9])
print([(token.text, token.pos_) for token in doc10])
print([(token.text, token.pos_) for token in doc11])
