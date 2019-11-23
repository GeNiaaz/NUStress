# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 10:01:39 2019

@author: geniaaz
"""

#paste the sequence u want to complement, below
seq = 'TTTTGCGTCTACTATATACTT'

def complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::1]])

def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])

def RNA(rna):
    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A',}
    return ''.join([complement[base] for base in rna[::1]])

def reverse_RNA(rna):
    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A',}
    return ''.join([complement[base] for base in rna[::-1]])

#----------------------------------------------------------------

# DNA codon table
protein = {"AAA": "Lys(K) ", "AAU": "Asn(N) ", "AAC": "Asn(N) ", 
           "AAG": "Lys(K) ", "AUA": "lle(I) ", "AUU": "Ile(I) ",
           "AUC": "Ile(I) ", "AUG": "Met(M) ", "ACA": "Thr(T) ",
           "ACU": "Thr(T) ", "ACC": "Thr(T) ", "ACG": "Thr(T) ",
           "AGA": "Arg(R) ", "AGU": "Ser(S) ", "AGC": "Ser(S) ",
           "AGG": "Arg(R) ", "UAA": "STOP "  , "UAU": "Tyr(Y) ",
           "UAC": "Tyr(Y) ", "UAG": "STOP "  , "UUA": "Leu(L) ",
           "UUU": "Phe(F) ", "UUC": "Phe(F) ", "UUG": "Leu(L) ",
           "UCA": "Ser(S) ", "UCU": "Ser(S) ", "UCC": "Ser(S) ",
           "UCG": "Ser(S) ", "UGA": "STOP "  , "UGU": "Cys(C) ",
           "UGC": "Cys(C) ", "UGG": "Trp(W) ", "CAA": "Gln(Q) ",
           "CAU": "His(H) ", "CAC": "His(H) ", "CAG": "Gln(Q) ",
           "CUA": "Leu(L) ", "CUU": "Leu(L) ", "CUC": "Leu(L) ",
           "CUG": "Leu(L) ", "CCA": "Pro(P) ", "CCU": "Pro(P) ",
           "CCC": "Pro(P) ", "CCG": "Pro(P) ", "CGA": "Arg(R) ",
           "CGU": "Arg(R) ", "CGC": "Arg(R) ", "CGG": "Arg(R) ",
           "GAA": "Glu(E) ", "GAU": "Asp(D) ", "GAC": "Asp(D) ",
           "GAG": "Glu(E) ", "GUA": "Val(V) ", "GUU": "Val(V) ",
           "GUC": "Val(V) ", "GUG": "Val(V) ", "GCA": "Ala(A) ",
           "GCU": "Ala(A) ", "GCC": "Ala(A) ", "GCG": "Ala(A) ",
           "GGA": "Gly(G) ", "GGU": "Gly(G) ", "GGC": "Gly(G) ",
           "GGG": "Gly(G) "    
           }



# Generate protein sequence
def amino_code(modified_RNA):
	protein_sequence = ""
	for i in range(0, len(modified_RNA)-(len(modified_RNA)%3), 3):
	    #if protein[dna[i:i+3]] == "STOP" :
	     #   break
	    protein_sequence += protein[modified_RNA[i:i+3]]
	return (protein_sequence)


print ('')
print ('DNA complement: ' + complement(seq))
print ('')
print ('DNA complement (reverse): ' + reverse_complement(seq))
print ('')
print ('-------------------------')
print ('')
print ('RNA complement: ' + RNA(seq))
print ('RNA complement (reverse): ' + reverse_RNA(seq))
print('---------------------------------')
print('')
print('amino acids coded:' + amino_code(str(RNA(seq))))
print('')
print('amino acids coded (reverse):' + amino_code(str(reverse_RNA(seq))))
