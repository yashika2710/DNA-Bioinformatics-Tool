from dna_functions import *
from codon_table import *

print("Welcome to the DNA Analysis Tool")


def print_menu():
    print("analysis options:")
    print("1. Sequence length")
    print("2. GC content")
    print("3. reverse complement")
    print("4. Transcription(mRNA)")
    print("5. Translation(Protein)")
    print("6. save results")
    print("7. Exit")


def run_analysis(dna_sequence, choice):
    try:
        if choice == "1":
            length = count_nucleotides(dna_sequence)
            print("Length of the DNA sequence: ", length)
        elif choice == "2":
            gc_percent = gc_content(dna_sequence)
            print("GC content of the DNA sequence: ", gc_percent, "%")
        elif choice == "3":
            reverse_complement = complement(dna_sequence)
            print("Reverse complement of the DNA sequence: ", reverse_complement)
        elif choice == "4":
            mrna_sequence = transcribe(dna_sequence)
            print("Transcribed mRNA sequence: ", mrna_sequence)
        elif choice == "5":
            mrna_sequence = transcribe(dna_sequence)
            protein_sequence = translate(mrna_sequence)
            print("Translated protein sequence: ", protein_sequence)
        elif choice == "6":
            with open("results.txt", "w") as file:
                file.write(f"DNA sequence: {dna_sequence}\n")
                file.write(f"Length of the DNA sequence: {count_nucleotides(dna_sequence)}\n")
                file.write(f"GC content of the DNA sequence: {gc_content(dna_sequence)}%\n")
                file.write(f"Reverse complement of the DNA sequence: {complement(dna_sequence)}\n")
                file.write(f"Transcribed mRNA sequence: {transcribe(dna_sequence)}\n")
                file.write(f"Translated protein sequence: {translate(transcribe(dna_sequence))}\n")
            print("Results saved to results.txt")
        elif choice == "7":
            print("Exiting the program.")
            return False
        else:
            print("Invalid choice.")
    except ValueError as exc:
        print(exc)

    return True


while True:
    dna_sequence = input("Enter a DNA sequence: ").strip().upper()
    print_menu()
    enter = input("Enter your choice: ")

    should_continue = run_analysis(dna_sequence, enter)
    if not should_continue:
        break

    again = input("enter DNA sequence(y/n): ").strip().lower()
    if again == "y":
        continue
    elif again == "n":
        print("thanks")
        break
    else:
        print("invalid input")
        print("thanks")
        break

with open("dna_sequence.txt", "a") as file:
    file.write(f"DNA Sequence: {dna_sequence}\n")
    file.write(f"Length: {count_nucleotides(dna_sequence)}\n")
    file.write(f"GC Content: {gc_content(dna_sequence)}%\n")
    file.write(f"AT Content: {at_content(dna_sequence)}%\n")
    file.write(f"Complementary Strand: {complement(dna_sequence)}\n")
    file.write(f"mRNA: {transcribe(dna_sequence)}\n")
    file.write(f"Protein Sequence: {translate(transcribe(dna_sequence))}\n")
    file.write("\n")










 
