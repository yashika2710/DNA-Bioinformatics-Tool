from dna_functions import *
from codon_table import *
     
dna_sequence = input("Enter a DNA sequence: ").upper()
try:
        analyze_dna_sequence(dna_sequence)
        print("length:", count_nucleotides(dna_sequence))
        print("GC Content:", gc_content(dna_sequence))
        print("AT Content:", at_content(dna_sequence))
        print("Complementary strand:",complement(dna_sequence))
        print("mRNA:", transcribe(dna_sequence))
        print("Protein Sequence:", translate(transcribe(dna_sequence)))

        f=open("dna_sequence.txt", "a")

        f.write(f"DNA Sequence: {dna_sequence}\n")
        f.write(f"Length: {count_nucleotides(dna_sequence)}\n")
        f.write(f"GC Content: {gc_content(dna_sequence)}%\n")
        f.write(f"AT Content: {at_content(dna_sequence)}%\n")
        f.write(f"Complementary Strand: {complement(dna_sequence)}\n")
        f.write(f"mRNA: {transcribe(dna_sequence)}\n")
        f.write(f"Protein Sequence: {translate(transcribe(dna_sequence))}\n")
        f.write("\n")
        f.close()

except ValueError as e:
        print(e)



while True:
     again= input("enter dna sequnce(y/n): ")
     if again=="y":
          dna_sequence = input("Enter a DNA sequence: ").upper()
          analyze_dna_sequence(dna_sequence)
          print("length:", count_nucleotides(dna_sequence))
          print("GC Content:", gc_content(dna_sequence))
          print("AT Content:", at_content(dna_sequence))
          print("Complementary strand:",complement(dna_sequence))
          print("mRNA:", transcribe(dna_sequence))
          print("Protein Sequence:", translate(transcribe(dna_sequence)))

          f=open("dna_sequence.txt", "a")

          f.write(f"DNA Sequence: {dna_sequence}\n")
          f.write(f"Length: {count_nucleotides(dna_sequence)}\n")
          f.write(f"GC Content: {gc_content(dna_sequence)}%\n")
          f.write(f"AT Content: {at_content(dna_sequence)}%\n")
          f.write(f"Complementary Strand: {complement(dna_sequence)}\n")
          f.write(f"mRNA: {transcribe(dna_sequence)}\n")
          f.write(f"Protein Sequence: {translate(transcribe(dna_sequence))}\n")
          f.write("\n")
          f.close()
     elif again =="n":
          print("thanks")
          break
     else:
          print('invalid response')







 
