#!/usr/bin/env python3
"""Compute basic FASTA assembly metrics: total length, record count, GC%, N50, L50.
Usage: python scripts/compute_assembly_metrics.py data/reference/BY4741_NCBI_GCA_000766575_2/GCA_000766575.2_ASM76657v2_genomic.fna
"""
import sys, re, json
from pathlib import Path

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

def n50_l50(lengths):
    lengths=sorted(lengths, reverse=True); total=sum(lengths); cum=0
    for i,l in enumerate(lengths,1):
        cum += l
        if cum >= total/2: return l,i,total
    return 0,0,total

fasta=Path(sys.argv[1])
records=parse_fasta(fasta)
lengths=[len(s) for s in records.values()]
n50,l50,total=n50_l50(lengths)
gc=sum(s.count('G')+s.count('C') for s in records.values())/total*100
print(json.dumps({"file":str(fasta),"records":len(lengths),"total_bp":total,"N50_bp":n50,"L50":l50,"min_bp":min(lengths),"max_bp":max(lengths),"GC_percent":round(gc,3)}, indent=2))
