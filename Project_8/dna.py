MIN_CODONS = 5
MASS_PRECENTAGE = 30
NUCLEOTIDES = 4
NUCLEOTIDES_PER_CODON = 3
MIN_SEQUENCE_LENGTH = NUCLEOTIDES_PER_CODON * 5
# These are for accessing the counting list.
ADENINE = 0
CYTOSINE = 1
GUANINE = 2
THYMINE = 3
# These are the moles for each nucleotides.
MASS_ADENINE = 135.128
MASS_CYTOSINE = 111.103
MASS_GUANINE = 151.128
MASS_THYMINE = 125.107
MASS_JUNK = 100.000


def main():
    introduction()
    infile_name = query_input_file()
    outfile_name = query_output_file()
    infile = open(infile_name)
    names = get_region_names(infile)
    seqs = get_sequences(infile)
    outfile = open(outfile_name, "w+")


def get_region_names(infile):
    names = []
    protein_name = ""
    for word in infile.read().split():
        if is_valid_start(word) and is_valid_end(word):
            names.append(protein_name[:-1])
        else:
            protein_name += word + " "
    return names


def get_sequences(infile):
    seqs = []
    for word in infile.read().split():
        if is_valid_start(word) and is_valid_end(word):
            seqs.append(word.upper())
    return seqs


def introduction():
    print("This program reports information about DNA")
    print("nucleotide sequences that may encode proteins.")


def query_input_file():
    return input("Input file name? ")


def query_output_file():
    return input("Output file name? ")


def is_valid_start(seq):
    return seq.upper().startswith("ATG")


def is_valid_end(seq):
    return seq.endswith("TAA") or seq.endswith("TAG") or seq.endswith("TGA")


def process_file(infile):
    protein_name = ""
    infile_split = infile.read().split()
    region = ""
    for word in infile_split:
        if is_valid_start(word) and is_valid_end(word):
            region = region[:-1]
            print("Region Name:", region)
            print("Nucleotides:", word.upper())
            counts = process_sequence_counts(word)
            region = ""
        else:
            region += word + " "


def process_sequence_counts(seqs):
    counts = [0] * 4
    for char in seq:
        if char == 'A':
            counts[ADENINE] += 1
        elif char == 'C':
            counts[CYTOSINE] += 1
        elif char == 'G':
            counts[GUANINE] += 1
        elif char == 'T':
            counts[THYMINE] += 1
    return counts


def total_mass(seq):
    total = 0
    for char in seq.upper():
        if char == 'A':
            total += MASS_ADENINE
        elif char == 'C':
            total += MASS_CYTOSINE
        elif char == 'G':
            total += MASS_GUANINE
        elif char == 'T':
            total += MASS_THYMINE
        else:
            total += MASS_JUNK
    return total


def process_percentages(counts, total):
    mass_percentages = [0] * 4
    for i in range(len(counts)):
        mass_percentages[i] = counts[i] / total
    return mass_percentages


main()
