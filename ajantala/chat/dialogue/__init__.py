import os
from chat.dialogue.story import FLOW
import random

class Dialogue:
    def __init__(self):
        # holds a k:v pair of tag and words(a list) that have been subbed for belonging to that tag
        self.substitutions = {}

    def sentence_classifier(self, sentence):
        """ 
        Tries to classify what the user might be saying into any of the predefined categories
        """
        pass

    def parse_sentence(self, sentence):
        # tag sentence
        tagged_sentence = self.label_tags(sentence)
        print('tagged sentence: ', tagged_sentence)
        # Approach A: Direct mathching i.e looks up the entire sentence in db
        response_list = FLOW.get(tagged_sentence)
        response = random.choice(response_list) if response_list else None
        return response if response else None
        


    def label_tags(self, sentence):
        """ 
        Replaces words in sentences with corresponding tags if they are in our db.
        eg. A name gets labelled as %name%
        """

        # simple hack to handle sentences seperated by comma at once
        simple_sentences = sentence.split(',')
        parsed_sentences = []
        for sentence in simple_sentences:
            new_sentence = []
            for word in sentence.split(" "):
                tag = self.detect_tag(word)
                if tag:
                    # print("tag, word", tag, word)
                    sub_tag_list = self.substitutions.get(tag)
                    if not sub_tag_list:
                        sub_tag_list = []
                    sub_tag_list.append(word)
                    self.substitutions[tag] = sub_tag_list
                
                new_word = "{%" + tag + "%}" if tag else word
                new_sentence.append(new_word)

            # print(self.substitutions)
            parsed_sentences.append(" ".join(new_sentence))
        return ",".join(parsed_sentences)


    def detect_tag(self, word):
        """
        Goes through the list of words in our db, if a word is discovered, it returns its corresponding tag.
        """
        
        tags = self.load_word_tags()

        for tag in tags:
            word_list = tags[tag]
            if word in word_list:
                return tag[:-1]
    
    def load_word_tags(self):
        tags = {}
        print(os.getcwd())
        tag_path = os.path.join('ajantala', 'chat', 'dialogue', 'tags')
        files = [files for _, __, files in os.walk(tag_path)][0]
        for _file in files:
            tag_name = _file.replace('.txt', '')
            with open(os.path.join(tag_path, _file), 'r') as fp:
                words = [word.replace('\n', '') for word in fp.readlines()]
            tags[tag_name] = words

        return tags

    def refill_tags(self, tagged_response):
        # result = []

        # for simple_sentence in tagged_response.split(', '):
        #     simple_sentence_token = simple_sentence.split(' ')
        #     untagged_simple_sentence = []
        #     for word in simple_sentence_token:
        #         if self.substitutions.get(word[1:-1]):
        #             if

        for tag in self.substitutions:
            # find the occurence of the tag
            result = ''
            sentence_parts = tagged_response.split("{%"+tag+"%}")
            subs = self.substitutions[tag]
            for i in range(len(subs)):
                result += sentence_parts[i] + subs[i]
            tagged_response = result + sentence_parts[-1]
        return tagged_response


                

if __name__ == '__main__':
     d = Dialogue()
     # print(d.label_tags("ekáàrọ, Túndé ati Ìyábọ́ bawo ni?"))
     print(d.sentence_classifier("Ẹkú ojúmọ́"))