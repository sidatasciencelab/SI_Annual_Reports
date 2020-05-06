import stanza
import json
import sys

def nlp_pipeline(text_file):
    nlp = stanza.Pipeline(lang='en', processors='tokenize,pos,lemma,ner')
    with open(input_file) as f:
        doc = nlp(f.read())
        dicts = doc.to_dict()
        print(dicts)
      
	
if __name__ == "__main__":
    input_file = sys.argv[1]
    nlp_pipeline(input_file)