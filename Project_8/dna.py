# Parker Gabel, CSc 110, Autumn 2017, Section 1B
# Programming Assignment #8, 10/24/17
# This program takes a file containg information about dna and analizes it.
MIN_CODONS = 5
MASS_PERCENTAGE = 30
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
    outfile = open(outfile_name, "w+")
    lines = infile.readlines()
    for i in range(len(lines)):
        if i % 2 != 0:
            counts = process_sequence_counts(lines[i].strip())
            total = total_mass(lines[i].strip())
            percentages = process_percentages(counts, total)
            codons = process_codons(lines[i].strip())
            region_name = lines[i - 1].strip()
            write_to_file(region_name, lines[i].strip().upper(),
                          counts, total, percentages, codons, outfile)


def introduction():
    """A simple introduction."""
    print("This program reports information about DNA")
    print("nucleotide sequences that may encode proteins.")


def query_input_file():
    """Gets input file name"""
    return input("Input file name? ")


def query_output_file():
    """Gets output file name"""
    return input("Output file name? ")


def process_sequence_counts(seq):
    """Counts occurances of nucleotides.
       Param:  seq string
       Return: counts list(int)"""
    counts = [0] * 4
    for char in seq.upper():
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
    """Computes total mass of nucleotide.
       Param:  seq string
       Returns: total float"""
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
    """Computes percentages from counts.
       Params: counts list(int)
               total  int
       Returns: mass_percentages list(float)"""
    mass_percentages = [0] * NUCLEOTIDES
    for i in range(NUCLEOTIDES):
        mass = counts[i] * convert_to_mass(i)
        mass_percentages[i] = round(mass / total * 100, 1)
    return mass_percentages


def process_codons(seq):
    """Gets all codons from a sequence.
       Params: seq string
       Returns: codon_list list(str)"""
    codon_list = []
    new_seq = ""
    for char in seq.upper():
        if char != "-":
            new_seq += char
    i = 0
    while i != len(new_seq):
        codon_list.append(new_seq[i: i + 3])
        i += 3
    return codon_list


def is_valid_percentage(percentages):
    """checks if a sequence has valid mass percentages.
       Params: percentages list(float)
       Returns: boolean"""
    return percentages[CYTOSINE] + percentages[GUANINE] >= MASS_PERCENTAGE


def is_valid_start(codons):
    """Checks if a seqence has a valid start codon
        Params: codons list
        Returns: boolean"""
    return codons[0] == "ATG"


def is_valid_end(codons):
    """Checks if a seqence has a valid stop codon
        Params: codons list
        Returns: boolean"""
    return codons[-1] == "TAA" or codons[-1] == "TAG" or codons[-1] == "TGA"


def is_valid_start_and_end(codons):
    """Wraps aroung both is_valid_start and is_valid_end
        Params: codons list
        Returns: Boolean"""
    return is_valid_start(codons) and is_valid_end(codons)


def is_valid_length(codons):
    """Checks if a sequence is of valid length.
        Params: codons list
        Returns: boolean"""
    return len(codons) >= MIN_CODONS


def is_protein(codons, percentages):
    """Checks if something is a valid Protein
       Params: codons list
               percentages list
        Returns: string"""
    if is_valid_percentage(percentages) and is_valid_length(codons) and is_valid_start_and_end(codons):
        return "YES"
    return "NO"


def convert_to_mass(nucleotide):
    """Converts a nucleotide to its mass.
        Params: nucleotide int
        Returns: float"""
    if nucleotide == ADENINE:
        return MASS_ADENINE
    elif nucleotide == CYTOSINE:
        return MASS_CYTOSINE
    elif nucleotide == GUANINE:
        return MASS_GUANINE
    else:
        return MASS_THYMINE


def write_to_file(region, seq, counts, total, percentages, codons, outfile):
    """Writes data to file.
        Params: region string
                seq    string
                counts list
                total  float
                percentages list
                codons  list
                outfile file"""
    outfile.write("Region Name: " + region + "\n")
    outfile.write("Nucleotides: " + str(seq) + "\n")
    outfile.write("Nuc. Counts: " + str(counts) + "\n")
    outfile.write("Total Mass%: " + str(percentages) +
                  " of " + str(round(total, 1)) + "\n")
    outfile.write("Codons List: " + str(codons) + "\n")
    outfile.write("Is Protein?: " + is_protein(codons, percentages) + "\n")
    outfile.write("\n")


main()
