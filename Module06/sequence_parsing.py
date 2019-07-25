from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

def print_header():
    print('---------------------------------')
    print('       Summarize Genbank File')
    print('---------------------------------')
    print()


def get_genbank_path():

    filename = None
    while filename is None:

        filename = input('What is the /path/to/the/genbank/file? ')

        # Check if the filename exists.
        if not os.path.exists(filename):
            print('That file could not be found. Try again.')
            filename = None

    return filename


def print_genbank_record(gb_record):
    print('Found Sequence:', gb_record.id)
    print(gb_record.description)

    print('It starts:', gb_record.seq[:10])
    print('It ends:', gb_record.seq[-10:])
    print('It has %i nucleotides' % len(gb_record.seq))

    print('It has %i features.' % len(gb_record.features))

    for feat in gb_record.features:
        print("Type:", feat.type)
        print("Location:", feat.location)


def find_orfs(seq_record):
    seq = seq_record.seq

    start = 0
    forward_orf_count = 0
    while start < len(seq):

        pos = seq.find('ATG', start)
        if pos == -1: #Found no more starts
            break

        orfs = seq_record[pos:].translate(to_stop = True)

        with open('ORF_Translated.fasta', 'a+') as filename:
            SeqIO.write(orfs, filename, 'fasta')

        start = pos + 1

        forward_orf_count += 1

    reverse_orf_count = 0
    start = 0
    nseq = seq.reverse_complement()
    while start < len(nseq):

        pos = nseq.find('ATG', start)
        if pos == -1: #Found no more starts
            break

        orfs = seq_record[pos:].translate(to_stop = True)

        with open('ORF_Translated.fasta', 'a+') as filename:
            SeqIO.write(orfs, filename, 'fasta')

        start = pos + 1
        reverse_orf_count += 1

    print('There are a total of %i forward ORFs and %i reverse ORFs' % (forward_orf_count, reverse_orf_count))


def main():

    print_header()

    gb_path = get_genbank_path()

    with open(gb_path) as handle:
        for seq_record in SeqIO.parse(handle, 'genbank'):
            print_genbank_record(seq_record)
            find_orfs(seq_record)



if __name__ == '__main__':

    main()

