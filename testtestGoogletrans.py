#-*- coding: utf-8 -*-
from googletrans import Translator

def translate(sendwords):
    translator = Translator()
    return (translator.translate(sendwords,dest='zh-CN').text)



if __name__ == "__main__":
    print ('20')
    words= "We trained a large, deep convolutional neural network"
    translate(words)