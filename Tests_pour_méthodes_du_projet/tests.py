import unittest

from utils import *
from preprocess_data import PreprocessData
from extract_data import ExtractData

dic = {'paper_id': 'ABC00001', 'metadata': {'title': 'Covid', 'authors': []}, 'body_text': [{'text': 'Covid is coron virus', 'cite_spans': [], 'section': '', 'ref_spans': []}], 'ref_entries': {}, 'back_matter': [], 'bib_entries': {'BIBREF0': {'title': 'The possible macroeconomic effect on the UK of an influenza pandemic', 'authors': [], 'year': 2009, 'venue': '', 'volume': '', 'issn': '', 'pages': None, 'other_ids': {'DOI': []}}}}
path_file = "/Users/youssefbencheikh/Desktop/ABC00001.json"
class Test_utils(unittest.TestCase):

    def test_isnumber(self):
        self.assertEqual(is_number(12), True, "Should be True")
        self.assertEqual(is_number("Covid"), False, "Should be False")	

    def test_read_json(self):
    	self.assertEqual(read_json(path_file), dic, "Should be a dictionnary")

data = ExtractData(dic)
class Test_extract_data(unittest.TestCase):
	def test_get_paper_id(self):
		self.assertEqual(data.get_paper_id(), 'ABC00001', "Should be 'ABC00001'")
	def test_get_title(self):
		self.assertEqual(data.get_title(), 'covid', "Should be Covid")
	def test_get_text(self):
		self.assertEqual(data.get_text(), 'Covid is coron virus', "Should be Covid is coron virus")


preprocess = PreprocessData("test")

class Test_preprocess_data(unittest.TestCase):
	def test_remove_number(self):
		self.assertEqual(preprocess.remove_number("hello number 1 and 2"), 'hello number and', "Should be 'hello number and'")
	def test_lower_case(self):
		data = preprocess = PreprocessData("Hello Number 1 AND 2")
		self.assertEqual(preprocess.convert_lowercase(), 'hello number 1 and 2', "Should be 'hello number 1 and 2'")
	def test_remove_punctuation(self):
		self.assertEqual(preprocess.remove_punctuation("hello !, number : 1 and 2."), 'hello number 1 and 2', "Should be 'hello number 1 and 2'")
	def test_remove_stop_words(self):
		self.assertEqual(preprocess.remove_stop_words("hello number 1 and 2"), 'hello number 1 2', "Should be 'hello number 1 2'")
	def test_remove_special_character(self):
		self.assertEqual(preprocess.remove_special_character("hello number @1 and #2"), 'hello number 1 and 2', "Should be 'hello number 1 2'")
	def test_lemmatization_text(self):
		self.assertEqual(preprocess.lemmatization_text("oranges and apples"), 'orange and apple', "Should be 'orange and apple'")
	
if __name__ == '__main__':
    unittest.main()
	
	
