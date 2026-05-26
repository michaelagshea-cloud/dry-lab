#!/usr/bin/env bash
set -euo pipefail
# Optional genome-wide structural-variant / synteny confidence workflow.
# Requires minimap2 and paftools.js; use only as an addendum because the current design is already target-locus confirmed.
R64="data/reference/R64-1-1/GCA_000146045.2_R64_genomic.fna"
BY="data/reference/BY4741_NCBI_GCA_000766575_2/GCA_000766575.2_ASM76657v2_genomic.fna"
mkdir -p results/sv
minimap2 -x asm5 -t 4 "$R64" "$BY" > results/sv/BY4741_vs_R64.asm5.paf
# Optional visualization / variant calling depends on local installation:
# paftools.js call results/sv/BY4741_vs_R64.asm5.paf > results/sv/BY4741_vs_R64.sv.txt
