import xml.etree.ElementTree as etree


class Corpus:
    def __init__(self):
        self.sentences = []

    def load(self, path_to_corpus):
        tree = etree.parse(path_to_corpus)
        for text in tree.findall('text'):
            for paragraph in text.find('paragraphs').findall('paragraph'):
                for sentence in paragraph.findall('sentence'):
                    self.sentences.append(Sentence(sentence))

    def getNthSentence(self, n=-1):
        if n > len(self.sentences):
            return self.sentences[-1]
        else:
            return self.sentences[n]

    def getString(self):
        return f'\n'.join([i.string for i in self_sentences])




class Sentence:
    def __init__(self, sentence_tag):
        self.wordforms = []
        self.string = sentence_tag.find('source').text
        for token in sentence_tag.find('tokens').findall('token'):
            self.wordforms.append(Wordform(token))

    def getString(self):
        return self.string

    def getNthWordform(self, n=-1):
        if n > len(self.wordforms):
            return self.wordforms[-1]
        else:
            return self.wordforms[n]



class Wordform:
    def __init__(self, token):
        self.grammemes = []
        self.string = token.get('text')
        l = token.find('tfr').find('v').find('l')
        self.lexeme = l.get('t')
        for grammeme in l.findall('g'):
            self.grammemes.append(grammeme.get('v'))

    def __str__(self):
        return self.string

    def getString(self):
        return self.string

    def getLexeme(self):
        return self.lexeme

    def getGrammemes(self):
        return self.grammemes

    def getNthGrammeme(self, n=-1):
        if n > len(self.grammemes):
            return self.grammemes[-1]
        else:
            return self.grammemes[n]
