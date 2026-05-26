#!/usr/bin/env python3
"""Translate chimeric ORFs and verify expected lengths/no internal stops.
Input: data/constructs/chimera_coding_regions_for_translation_check.fasta
"""
import re, sys
codon_table = {
'TTT':'F','TTC':'F','TTA':'L','TTG':'L','TCT':'S','TCC':'S','TCA':'S','TCG':'S','TAT':'Y','TAC':'Y','TAA':'*','TAG':'*','TGT':'C','TGC':'C','TGA':'*','TGG':'W',
'CTT':'L','CTC':'L','CTA':'L','CTG':'L','CCT':'P','CCC':'P','CCA':'P','CCG':'P','CAT':'H','CAC':'H','CAA':'Q','CAG':'Q','CGT':'R','CGC':'R','CGA':'R','CGG':'R',
'ATT':'I','ATC':'I','ATA':'I','ATG':'M','ACT':'T','ACC':'T','ACA':'T','ACG':'T','AAT':'N','AAC':'N','AAA':'K','AAG':'K','AGT':'S','AGC':'S','AGA':'R','AGG':'R',
'GTT':'V','GTC':'V','GTA':'V','GTG':'V','GCT':'A','GCC':'A','GCA':'A','GCG':'A','GAT':'D','GAC':'D','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGA':'G','GGG':'G'}

def parse_fasta(path):
    records={}; name=None; seq=[]
    for line in open(path):
        line=line.strip()
        if not line: continue
        if line.startswith('>'):
            if name: records[name]=''.join(seq).upper()
            name=line[1:].split()[0]; seq=[]
        else: seq.append(re.sub('[^A-Za-z]','',line))
    if name: records[name]=''.join(seq).upper()
    return records

def translate(seq):
    return ''.join(codon_table.get(seq[i:i+3],'X') for i in range(0,len(seq)-2,3))

records=parse_fasta(sys.argv[1])
for name,seq in records.items():
    prot=translate(seq)
    internal='*' in prot[:-1]
    print(f"{name}\tDNA_bp={len(seq)}\tprotein_symbols={len(prot)}\tterminal_stop={prot.endswith('*')}\tinternal_stop={internal}\tstarts_ATG={seq.startswith('ATG')}")
