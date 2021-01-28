# -*- coding: utf-8 -*-
 
r"""
file_renamer.py
python file_renamer.py "C:\Users\ibrahim\Desktop\Python_egitim_part1\dosyalar"
 
https://docs.python.org/3/
https://docs.python.org/3/py-modindex.html
https://docs.python.org/3/library/index.html
"""
 
import glob
import os
import sys
import re
 
def show_usage():
    print(r"""
böyle kullan:
python file_renamer.py "C:\Users\ibrahim\Desktop\dosyalar"    
parametre, bir directory olmalidir.
    """)

 #def convert_ascii_two(tail_char):
  #  if tail_char == "ı":
   #    return "i"
    #elif tail_char == "ö":
     #  return "o"
   # elif tail_char == "ç":
    #   return "c"   
   # elif tail_char == "ş":
    #   return "s"
   # elif tail_char == "Ç":
    #   return "C"
   # elif tail_char == "Ş":
    #   return "S"
   # elif tail_char == "Ü":
   #    return "U"
   # elif tail_char == "İ":
   #    return "I"      
   # else:
    #    return "_"       

def convert_ascii(tail_char):

    non_ascii={
        "ı":"i",
        "ö":"o",
        "ç":"c",
        "ş":"s",
        "Ç":"C",
        "Ş":"S",
        "Ü":"U",
        "İ":"I"
    }
    if tail_char in non_ascii :
     
        new_char= tail_char.translate(tail_char.maketrans(tail_char,non_ascii[tail_char]))

    return new_char




def tailReplace(tail:str):
    replace_tail=""
    for char in tail:
        if (re.sub('[ -~]', '', char)) != "":   #   non-ascii
            replace_tail+=convert_ascii(char)
        else:
           replace_tail+=char
    return replace_tail
 
def build_new_file_name(old_file_name):
    r"""
    c:\a\b\c\d
    head: c:\a\b\c
    tail: d
 
    c:\a\b\c\d\d1.txt
    head: c:\a\b\c\d
    tail: d1.txt
 
    https://docs.python.org/3/library/os.path.html#module-os.path
    """
    head, tail = os.path.split(old_file_name)
    new_file_name=head+"""\\""" +tailReplace(tail)

    print(new_file_name)
    return new_file_name
    

     
def process_dir(target_dir):
    def build_file_list():
        file_list_inner = glob.glob(pattern)
        return file_list_inner
 
    # pattern = target_dir + "\*.*"
    pattern = os.path.join(target_dir, "*.*")
    file_list = build_file_list()
    # print(file_list)
    for old_file_name in file_list:
        new_file_name = build_new_file_name(old_file_name)
      #  os.rename(old_file_name,new_file_name)      

       
 
def main():
    # print(sys.argv)
    # print(type(sys.argv))
    if len(sys.argv) == 2:
        target_dir = sys.argv[1]
        try:
            if not os.path.isdir(target_dir):
                msg = target_dir
                raise NotADirectoryError(msg)
            process_dir(target_dir)
        except NotADirectoryError as err1:
            print("Directory not found: ", err1)
            show_usage()
    else:
        show_usage()
 
main()