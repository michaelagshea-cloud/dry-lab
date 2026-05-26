#!/usr/bin/env python3
"""Search query FASTA records against a genome/scaffold FASTA in both orientations.
Useful for donor arms/locus confirmation.
Usage: python scripts/locus_exact_match.py genome.fna queries.fasta
"""
import sys, re
comp=str.maketrans('ACGTacgt','TGCAtgca')
def rc(seq): return seq.translate(comp)[::-1].upper()
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
genome=parse_fasta(sys.argv[1]); queries=parse_fasta(sys.argv[2])
for qn,qs in queries.items():
    found=False
    for gn,gs in genome.items():
        i=gs.find(qs)
        if i!=-1:
            print(f"{qn}\t{gn}\tplus\t{i+1}\t{i+len(qs)}\t100% exact")
            found=True; break
        j=gs.find(rc(qs))
        if j!=-1:
            print(f"{qn}\t{gn}\tminus\t{j+1}\t{j+len(qs)}\t100% exact")
            found=True; break
    if not found: print(f"{qn}\tNOT_FOUND")
