import os
import shutil
import pathlib

file_path = os.path.dirname(os.path.abspath(__file__))
epub_names = os.listdir(file_path)

pathlib.Path('over').mkdir(parents=True, exist_ok=True)

for book_name in epub_names:
    if ".epub" in book_name:
        os.system('kindlegen %s -c0'%(book_name))
        mobi_name = book_name[:-4]+'mobi'
        mobi_path = os.path.abspath(mobi_name)
        over2 = os.path.abspath("over")
        shutil.move(mobi_path,over2)