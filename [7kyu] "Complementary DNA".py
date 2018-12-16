import string
def DNA_strand(dna):
    o = "ATCG"
    n = "TAGC"
    tab = str.maketrans(o,n)
    return dna.translate(tab)
