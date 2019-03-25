from simple_NER.annotators import NERWrapper
from simple_NER import Entity


def extract_hitler(text):
    if "hitler" in text.lower():
        yield Entity("hitler", "bad_guy", source_text=text, data={
            "known_for": ["killing jews", "world war 2"]})


ner = NERWrapper()
ner.add_detector(extract_hitler)

for ent in ner.extract_entities("hitler only had one ball"):
    assert ent.as_json() == {'confidence': 1,
                             'data': {
                                 'known_for': ['killing jews', 'world war 2']},
                             'end': 6,
                             'entity_type': 'bad_guy',
                             'rules': [],
                             'source_text': 'hitler only had one ball',
                             'start': 0,
                             'value': 'hitler'}
