# kaiseki
kaiseki is a Python tool to aid in recognition of idiomatic expressions, colloquialisms, collocations, and dialectal speech in Japanese. It is built with [spaCy](https://spacy.io/models), using the pretrained Japanese statistical models and NLP tools.

**This project is currently a work in progress, so not all the features may be available at this time. Development is welcome.**

## About
kaiseki was built with language learners in mind. Many Japanese morphological analyzers parse to the smallest unit of language- this can be troublesome when many smaller units form one idiomatic expression. The issue is especially prevalent when generating i+1 learning queues, ala Stephen Krashen's [input hypothesis](https://en.wikipedia.org/wiki/Input_hypothesis) and Anki's [MorphMan addon](https://github.com/kaegi/MorphMan)

Take the example of the idiomatic phrase **"気になる"**, with one of its translations **"to weigh on one's mind"**. Let's see how a functioning analyzer would interpret it.

| Morph | Interpretation |
| --- | -------------- |
| 気　 | NOUN (mind)      |
| に　 | PARTICLE (into) |
| なる | VERB (to become) |

 ... this creates some trouble for a learner who has learned these three components in isolation. While this is a straightforward example, especially with context clues, there are many cases where additional semantic clues would be very helpful beyond the typical morphological analysis.
 
### Features
- POS tagging
- Furigana
- Dictionary form

- Supports
   - Dialects
   - Figures of speech
   - Spoken language
   - Japanese names
   - Gairaigo

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

## To-Do

- Implement JEDict files into the spaCy implementation
   - begin testing with small quantities, e.g. limiting to just expressions
- Identify strings that are entries in the dictionary
- Make the model re-parse based on those entries
- Add parts of speech
- Add readings
- Check for errors / overlaps in expressions
   - hard-code exceptions
   
## License

JSON files were converted from the original JMdict XML files with scriptin's [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) repository. The following information is from that repository.

The original XML files, JMdict_e.xml and JMnedict.xml are property of the Electronic Dictionary Research and Development Group, and are used in conformance with the Group's licence. The project was started in 1991 by Jim Breen.

All derived files are distributed under the same license, as the original license requires it.

Source files of this project (excluding distribution archives containing JSON files) are available under Creative Commons Attribution-ShareAlike License v4.0.
