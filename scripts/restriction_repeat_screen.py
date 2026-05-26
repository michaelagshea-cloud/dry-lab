#!/usr/bin/env python3
"""Basic restriction-site and repeat screen for donor cassettes.
Reports common assembly sites and longest pairwise exact shared substring.
"""
import sys, re, itertools
from pathlib import Path
enzymes = {
    'BsaI':'GGTCTC','BsmBI_Esp3I':'CGTCTC','BbsI':'GAAGAC','SapI':'GCTCTTC','AarI':'CACCTGC',
    'FokI':'GGATG','BtgZI':'GCGATG','EcoRI':'GAATTC','HindIII':'AAGCTT','XbaI':'TCTAGA','SpeI':'ACTAGT','NheI':'GCTAGC','BamHI':'GGATCC','KpnI':'GGTACC','SacI':'GAGCTC','SalI':'GTCGAC','PstI':'CTGCAG','NotI':'GCGGCCGC','XhoI':'CTCGAG'}
comp=str.maketrans('ACGT','TGCA')
def rc(seq): return seq.translate(comp)[::-1]
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

def longest_common_substring(a,b):
    # dynamic programming, fine for ~2kb donor strings
    prev=[0]*(len(b)+1); best=0
    for i,ca in enumerate(a,1):
        curr=[0]*(len(b)+1)
        for j,cb in enumerate(b,1):
            if ca==cb:
                curr[j]=prev[j-1]+1
                if curr[j]>best: best=curr[j]
        prev=curr
    return best
records=parse_fasta(sys.argv[1])
for name,seq in records.items():
    print(f"\n## {name} length={len(seq)}")
    for enz,site in enzymes.items():
        hits=[m.start()+1 for m in re.finditer(site,seq)] + [m.start()+1 for m in re.finditer(rc(site),seq)]
        if hits: print(f"{enz}\t{site}\tpositions={sorted(set(hits))}")
for (n1,s1),(n2,s2) in itertools.combinations(records.items(),2):
    matches=sum(1 for a,b in zip(s1,s2) if a==b)/min(len(s1),len(s2))*100
    print(f"PAIR\t{n1}\t{n2}\tpositional_identity={matches:.2f}%\tlongest_exact_shared_block={longest_common_substring(s1,s2)} bp")
