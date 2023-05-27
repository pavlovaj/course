import unittest
from task13 import Corpus


class CorpusTest(unittest.TestCase):
    def setUp(self):
        path = '/Users/jul/PycharmProjects/course/task_13/annot.opcorpora.no_ambig.xml'
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
