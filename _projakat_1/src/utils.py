import sys
sys.path.append('../')

in_path = "output//random-ascii.bin"
out_path_bajt_entropy = ""
out_path_huff = ""
out_path_fanno = ""
out_path_lz77 = ""
text = ''

def ucitajPodatke(in_path, out_path=""):
    with open(in_path, "r") as file:
        text = file.read()
        if not text:
            print(f"Citanje fajla nije moguce! Doslo je do greske.")
        else:
            print(f"Uneti podaci iz fajla: ", text)
            return text



__all__ = ["ucitajPodatke","in_path"]