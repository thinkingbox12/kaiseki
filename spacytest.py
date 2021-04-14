import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc
from spacy.pipeline import EntityRuler

terms = ["気になる", "手も足も出ない", "んだ", "手を取る"]

nlp = spacy.load("ja_core_news_lg")

doc = nlp("健太郎はアスカの手を取りながら歩いていた")

print([(token.lemma_) for token in doc])

class EntityRetokenizeComponent:
  def __init__(self, nlp):
    pass
  def __call__(self, doc):
    with doc.retokenize() as retokenizer:
        for ent in doc.ents:
            retokenizer.merge(doc[ent.start:ent.end], attrs={"LEMMA": str(doc[ent.start:ent.end])})
    return doc

ruler = EntityRuler(nlp)

ruler.add_patterns([{"label": "EXPRESSION", "pattern": term} for term in terms])
nlp.add_pipe(ruler) 

retokenizer = EntityRetokenizeComponent(nlp)
nlp.add_pipe(retokenizer, name='merge_phrases')

doc = nlp("健太郎はアスカの手を取りながら歩いていた")

print([(token.text, token.lemma_) for token in doc])
