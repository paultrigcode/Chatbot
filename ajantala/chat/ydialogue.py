#----------------------------------------------------------------------
#  Yorùbádialogue.py
# A dialogue system on kinship logic of Yorùbá Language
#
#----------------------------------------------------------------------

import string
import re
import random

from . converse import gReflections,gPats
#from __classes__.dialogueGui import Dialogue

class YorubaDialogue:
    def __init__(self):
        self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),gPats))
        self.values = list(map(lambda x:x[1],gPats))
        print(self.keys)

  #----------------------------------------------------------------------
  # translate: take a string, replace any words found in dict.keys()
  #  with the corresponding dict.values()
  #----------------------------------------------------------------------
    def translate(self,str,dict):
        words = str.lower().split()
        keys = dict.keys()
        for i in range(0,len(words)):
            if words[i] in keys:
                words[i] = dict[words[i]]
                print(words[i])
        return ' '.join(words)

  #----------------------------------------------------------------------
  #  respond: take a string, a set of regexps, and a corresponding
  #    set of response lists; find a match, and return a randomly
  #    chosen response from the corresponding list.
  #----------------------------------------------------------------------
    def respond(self,str):
        # find a match among keys
        print(len(self.keys))
        for i in range(0, len(self.keys)):
            match = self.keys[i].match(str)
            if match:
                # found a match ... stuff with corresponding value
                # chosen randomly from among the available options
                resp = random.choice(self.values[i])
                # we've got a response... stuff in reflected text where indicated
                pos = resp.find('%')
                while pos > -1:
                    num = int(resp[pos+1:pos+2])
                    resp = resp[:pos] + self.translate(match.group(num),gReflections) + resp[pos+2:]
                    pos = resp.find('%')
                # fix munged punctuation at the end
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp

    #----------------------------------------------------------------------
    # gReflections, a translation table used to convert things you say
    #    into things the computer says back, e.g. "I am" --> "you are"
    #----------------------------------------------------------------------
    '''gReflections = {
    "mi":"yín",
    "èmi": "ẹ̀yin",
    "àwa": "ẹ̀yin",
    "àwọn": "àwọn",
    "ìwọ": "èmi",
    "ẹ̀yin": "èmi",
    "tèmi": "ti yín",
    "tiwa": "ti yín"
    }'''






    #----------------------------------------------------------------------
    #  command_interface
    #----------------------------------------------------------------------



    def getResponse(self,str):
        return str



if __name__ == "__main__":
  yordial = YorubaDialogue()
  yordial.command_interface()
