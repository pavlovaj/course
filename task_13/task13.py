import xml.etree.ElementTree as etree
import unittest

path = '/Users/jul/PycharmProjects/course/task_13/annot.opcorpora.no_ambig.xml'


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
        self.string = sentence_tag.find('source').text
        for token in sentence_tag.find('tokens').findall('token'):
            self._wordforms.append(Wordform(token))

    def getString(self):
        return self.string

    def getNthWordform(self, n=-1):
        if n > len(self._wordforms):
            return self._wordforms[-1]
        else:
            return self._wordforms[n]

    def __str__(self):
        return self.sting


class Wordform:
    def __init__(self, token):
        self._grammemes = []
        self.string = token.get('text')
        l = token.find('tfr').find('v').find('l')
        self._lexeme = l.get('t')
        for grammeme in l.findall('g'):
            self._grammemes.append(grammeme.get('v'))

    def __str__(self):
        return self.string

    def getString(self):
        return self.string

    def getLexeme(self):
        return self._lexeme

    def getGrammemes(self):
        return self._grammemes

    def getNthGrammeme(self, n=-1):
        if n > len(self._grammemes):
            return self._grammemes[-1]
        else:
            return self._grammemes[n]




a = Corpus()
a.load(path)

class CorpusTest(unittest.TestCase):
    def setUp(self):
        self.Corpus = Corpus()
        self.Corpus.load(path)
    def test_sent_string(self):
        self.assertIsInstance(self.Corpus.getNthSentence().string, str)
    def test_wf_string(self):
        self.assertIsInstance(self.Corpus.getNthSentence().getNthWordform().getString(), str)
    def test_grammemes(self):
        self.assertGreater(len(self.Corpus.getNthSentence().getNthWordform().getGrammemes()), 0)
    def test_POS_is_caps(self):
        part_of_speech = self.Corpus.getNthSentence().getNthWordform().getNthGrammeme(0)
        self.assertEqual(part_of_speech, part_of_speech.upper())
    def tearDown(self):
        del self.Corpus
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

if __name__ == '__main__':
    unittest.main()