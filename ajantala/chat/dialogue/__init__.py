import os


class Dialogue:
    def __init__(self):
        # holds a k:v pair of tag and words(a list) that have been subbed for belonging to that tag
        self.substitutions = {}

    def sentence_classifier(self, sentence):
        """ 
        Tries to classify what the user might be saying into any of the predefined categories
        """


        # Approach A: Direct mathching i.e looks up the entire sentence in db
        pass


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
                
                new_word = "%{0}%".format(tag) if tag else word
                new_sentence.append(new_word)

            print(self.substitutions)
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
        files = [files for _, __, files in os.walk('tags')][0]
        for _file in files:
            tag_name = _file.replace('.txt', '')
            with open(os.path.join('tags', _file), 'r') as fp:
                words = [word.replace('\n', '') for word in fp.readlines()]
            tags[tag_name] = words

        return tags

if __name__ == '__main__':
     d = Dialogue()
     print(d.label_tags("ekáàrọ, Túndé ati Ìyábọ́ bawo ni?"))