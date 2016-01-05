import sys
import ast
from sum_all_nums import sum_all_nums

class ElfBooks():
    def __init__(self, txns):
        self.txns = txns

    def clean_red(self, parent_type, key_or_idx):
        if type(item) is list:
            for m, ite in enumerate(item):
                if type(ite) is list:
                    self.clean_red(ite, list, m)
                if type(ite) is dict:
                    self.clean_red(ite, dict, m)
        if type(item) is dict:
            for key, value in item:
                if value == 'red':
                    self.txns
                
def main():
    text = sys.stdin.read()

    list_x = ast.literal_eval(text)

    elf_books = ElfBooks(list_x)
    
    for idx, item in enumerate(elf_books.txns):
        
