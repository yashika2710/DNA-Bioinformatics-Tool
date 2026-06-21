#translate an mRNA sequence to a protein sequence from codon table
def table(codon):
    return codon_table.get(codon, "")

codon_table = {
        "UUU": "phe","UCU": "ser","UAU": "tyr","UGU": "cys",
        "UUC": "phe","UCC": "ser","UAC": "tyr","UGC": "cys",
        "UUA": "leu","UCA": "ser","UAA": "stop","UGA": "stop", 
        "UUG": "leu","UCG": "ser","UAG": "stop","UGG": "trp",
        "CUU": "leu","CCU": "pro","CAU": "his","CGU": "arg",
        "CUC": "leu","CCC": "pro","CAC": "his","CGC": "arg",
        "CUA": "leu","CCA": "pro","CAA": "gln","CGA": "arg",
        "CUG": "leu","CCG": "pro","CAG": "gln","CGG": "arg",
        "AUU": "ile","ACU": "thr","AAU": "asn","AGU": "ser",
        "AUC": "ile","ACC": "thr","AAC": "asn","AGC": "ser",
        "AUA": "ile","ACA": "thr","AAA": "lys","AGA": "arg",
        "AUG": "met","ACG": "thr","AAG": "lys","AGG": "arg",
        "GUU": "val","GCU": "ala","GAU": "asp","GGU": "gly",
        "GUC": "val","GCC": "ala","GAC": "asp","GGC": "gly",
        "GUA": "val","GCA": "ala","GAA": "glu","GGA": "gly",
        "GUG": "val","GCG": "ala","GAG": "glu","GGG": "gly"
        }