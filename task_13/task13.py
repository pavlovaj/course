import xml.etree.ElementTree as etree


class Corpus:
    def __init__(self):
        self._sentences = []

    def load(self, path_to_corpus):
        tree = etree.parse(path_to_corpus)
        for text in tree.findall('text'):
            for paragraph in text.find('paragraphs').findall('paragraph'):
                for sentence in paragraph.findall('sentence'):
                    self._sentences.append(Sentence(sentence))

    def getNthSentence(self, n=-1):
        if n > len(self._sentences):
            return self._sentences[-1]
        else:
            return self._sentences[n]

    def getString(self):
        return f'\n'.join([i.string for i in self._sentences])




class Sentence:
    def __init__(self, sentence_tag):
        self._wordforms = []
        self._string = sentence_tag.find('source').text
        for token in sentence_tag.find('tokens').findall('token'):
            self._wordforms.append(Wordform(token))

    def getString(self):
        return self._string

    def getNthWordform(self, n=-1):
        if n > len(self._wordforms):
            return self._wordforms[-1]
        else:
            return self._wordforms[n]



class Wordform:
    def __init__(self, token):
        self._grammemes = []
        self._string = token.get('text')
        l = token.find('tfr').find('v').find('l')
        self._lexeme = l.get('t')
        for grammeme in l.findall('g'):
            self._grammemes.append(grammeme.get('v'))

    def __str__(self):
        return self._string

    def getString(self):
        return self._string

    def getLexeme(self):
        return self._lexeme

    def getGrammemes(self):
        return self._grammemes

    def getNthGrammeme(self, n=-1):
        if n > len(self._grammemes):
            return self._grammemes[-1]
        else:
            return self._grammemes[n]
