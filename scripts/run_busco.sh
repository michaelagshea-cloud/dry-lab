#!/usr/bin/env bash
set -euo pipefail
# BUSCO must be installed locally or run through Docker/Conda.
# Example Conda install:
#   conda create -n busco -c conda-forge -c bioconda busco
#   conda activate busco
# Recommended lineage can be checked with: busco --list-datasets | grep -i sacchar
ASSEMBLY="data/reference/BY4741_NCBI_GCA_000766575_2/GCA_000766575.2_ASM76657v2_genomic.fna"
OUT="results/busco_BY4741_ASM76657v2"
LINEAGE="saccharomycetes_odb10"
busco -i "$ASSEMBLY" -m genome -l "$LINEAGE" -o "$OUT" --cpu 4
# Copy the short_summary*.txt file into results/ and report:
# C:__%[S:__%,D:__%],F:__%,M:__%,n=__
