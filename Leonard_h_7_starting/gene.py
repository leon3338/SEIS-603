# Andrew Leonard
#  gene.py -> H7-4
#

def is_valid_DNA(seq):
    validChar = 'ACGT'

    for ch in seq:
        if ch not in validChar:
            print("Not valid DNA")
            return False
    else:
            print("Is valid DNA")
            return True


def is_gene(seq):

#valid sequence length

       if len(seq)%3==0:
           if seq[0:3] in ['ATG']:
               if seq[-3:] in ['TAG', 'TAA', 'TGA']:
                   if seq[3:-3] in ['TAG', 'TAA', 'TGA']:
                       print("valid sequence length")
                       return True
       else:
           print("Invalid Sequence length")
           return False



'''
Determine if seq represents a potential gene, by checking it satisfies each of the following 4-part codon criteria:

1.	The number of bases in seq is a multiple of 3 (len(seq) is evenly divisible by 3). 
2.	seq begins with the start codon ATG, where a codon is a sequence of three consecutive bases starting at a seq index 
    evenly divisible by 3.
3.	seq ends with any one of the stop codons TAG, TAA, or TGA.
4.	seq has no intervening stop codons (one of the above) anywhere in the codon sequence between the first and last 
    codons. 

Remember that any 3-sequence of bases is a codon ONLY if it begins on an index of seq that’s evenly divisible by 3. 
'''

def main():

    sequenceEntered = input("Please enter as sequence to check if it is valid: ")
    is_valid_DNA(sequenceEntered)
    is_gene(sequenceEntered)

    # if seq is valid DNA, then check if potential gene;
    #   call is_gene(seq) and print 'Is potential gene' if it returns True,
    #   or print 'Is NOT potential gene' otherwise

main()