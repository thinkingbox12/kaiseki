# kaiseki
kaiseki is a Python tool to aid in recognition of idiomatic expressions, colloquialisms, collocations, and dialectal speech in Japanese. It is built with [spaCy](https://spacy.io/models), using the pretrained Japanese statistical models and NLP tools.

**This project is currently a work in progress, so not all the features may be available at this time. Development is welcome.**

## Features
kaiseki was built with language learners in mind. Many Japanese morphological analyzers parse to the smallest unit of language- this can be troublesome when many smaller units form one idiomatic expression. The issue is especially prevalent when generating i+1 learning queues, ala Stephen Krashen's [input hypothesis](https://en.wikipedia.org/wiki/Input_hypothesis) and Anki's [MorphMan addon](https://github.com/kaegi/MorphMan)

Take the example of the idiomatic phrase **"気になる"**, with one of its translations **"to weigh on one's mind"**. Let's see how a functioning analyzer would interpret it.

| Morph | Interpretation |
| --- | -------------- |
| 気　 | NOUN (mind)      |
| に　 | PARTICLE (into) |
| なる | VERB (to become) |

 ... this creates some trouble for a learner who has learned these three components in isolation. While this is a straightforward example, especially with context clues, there are many cases where additional semantic clues would be very helpful beyond the typical morphological analysis.
 
Future implementations will include dialectal phrase support, better breakdown of spoken language, proper nouns, native Japanese names, and much more.

## Usage
First, install spaCy and its dependencies need to be installed. This can be done through **pip:**
```bash
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download ja_core_web_lg
```

### Samples
```bash
parse("あなたは手も足も出ないんだぞ")
[("あなた", PRONOUN), ("は", PARTICLE), ("手も足も出ない", EXPRESSION), ("んだ" EXPRESSION), ("ぞ" PARTICLE)]

dict_form("ハト胸はアスカの手を取りながら歩いていた")
[("ハト胸"), （"は"), ("アスカ"), ("の"), ("手を取る"), ("ながら"), ("歩く"), ("いる"), ("た")]
```
