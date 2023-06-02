import unittest
from task14 import TFIDFCalculator


class TestTFIDF(unittest.TestCase):

    def setUp(self):
        self.tf_idf = TFIDFCalculator('sci.med')


    def test_term_frequency(self):
        text = "This is a sample text for testing term frequency"
        expected_tf_idf_values = {'a': 0.1111111111111111, 'for': 0.1111111111111111, 'frequency': 0.1111111111111111, 'is': 0.1111111111111111, 'sample': 0.1111111111111111, 'term': 0.1111111111111111, 'testing': 0.1111111111111111, 'text': 0.1111111111111111, 'this': 0.1111111111111111}
        self.assertEqual(self.tf_idf._TFIDFCalculator__term_frequency(text), expected_tf_idf_values)

    def test_tf_idf(self):
        text = "This is a sample text for testing tf-idf"
        expected_tf_idf_values = {'a': 0.02241546243057024, 'for': 0.06017461876676109, 'is': 0.02696027496836194, 'sample': 0.7575419579034344, 'testing': 0.6099704271982067, 'text': 0.7575419579034344, 'tf-idf': 0.0, 'this': 0.07870054460543574}
        self.assertEqual(self.tf_idf.tf_idf(text), expected_tf_idf_values)


if __name__ == '__main__':
    unittest.main()