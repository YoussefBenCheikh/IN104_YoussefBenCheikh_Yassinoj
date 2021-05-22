import os.path

from whoosh.fields import Schema, TEXT
from whoosh.analysis import *
from whoosh import qparser
from whoosh.qparser import QueryParser
import time
from nltk import word_tokenize
import argparse
import glob
import time
import sys
from whoosh.index import create_in, open_dir, exists_in


class RedefineIndex:
    def __init__(self):
        pass

    def get_content(self, path_name_file_index):
        """
        It returns the content of a text file
        :return: file content
        :rtype: str
        """
        f= open(path_name_file_index,'r') 
        content = f.read()
        return content
    


def create_index(save_index_folder, index_name, num_docs_index, lst_articlesIndex, schema):
    """
        It create an index for the documents in the list, in the save folder,
        if the index doesn't exist already
        :return: index or nothing
        :rtype: index
        """
    t0 = time.time()
    
    if not exists_in(save_index_folder, index_name):
        
        print('*' * 10 + ' Building the index for {} documents '.format(num_docs_index) + '*' * 10)
        ix = create_in(save_index_folder, schema, index_name)  # it returns an index.
        writer = ix.writer(procs=6, multisegment=True, limitmb=4096)  # procs=6, limitmb=4GB## OR 8192

        for idx, path_name_file_index in enumerate(lst_articlesIndex):
            
            if idx % 10000 == 0:
                t1 = time.time()
                print("  {}/{}. elapsed time : {}s".format(idx, num_docs_index, round(t1 - t0, 3)));
                sys.stdout.flush()
            # Object
            redefine_index = RedefineIndex()
            
            article_content = redefine_index.get_content(path_name_file_index)

            writer.add_document(path=path_name_file_index, content=article_content)  # , time=modtime
        writer.commit(merge=False)
        t1 = time.time()
        print('*' * 10 + ' Index built in {}s '.format(round(t1 - t0, 3)) + '*' * 10)  # It's CPU seconds elapsed (floating point)
    
    ix = open_dir(save_index_folder, index_name)

    return ix

def main():

    path_read_docs_index = sys.argv[1]
    path_save_index_folder = sys.argv[2]
    index_name = "index_Articles"
    num_docs_index = 5000
    number_docs_result_search = 10

    lst_index_docs = glob.glob(path_read_docs_index + '*.txt')
    
  
    Schemah = Schema(path=TEXT(stored=True), content=TEXT(analyzer=StemmingAnalyzer(), spelling=True))
    

    ix = create_index(path_save_index_folder, index_name, num_docs_index, lst_index_docs, Schemah)
    
    
    searcher = ix.searcher()
    parser_query = QueryParser("content", schema=Schemah)
    q = parser_query.parse(sys.argv[3])
    
    

    results = searcher.search(q, limit=number_docs_result_search)
    
  
    
    docs = []
    for x in list(results):
            
            doc_name = x['path']
            docs.append(doc_name)
    
    print("Best",len(docs),"results for you research are :")
    for doc in docs:
       print(doc)

    corrector = searcher.corrector("content")
    corrected = searcher.correct_query(q, sys.argv[3])
    if corrected.query != q:
        mistyped_words = word_tokenize(sys.argv[3])
        for mistyped_word in mistyped_words:
            Listecorr = corrector.suggest(mistyped_word, limit=3)
            print("Did you mean",", ".join(Listecorr),"instead of",mistyped_word,"?")
if __name__ == "__main__":
    main()
