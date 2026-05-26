# Genome Assembly Confidence Addendum

## Current assembly evidence

The BY4741 public assembly included here is a scaffold-level Illumina assembly. It is adequate for target-locus exact-match confirmation because the required donor-arm and ISC1 source regions are found as exact matches.

## Current limitations

- Scaffold-level, not chromosome-complete.
- Long-read validation is not included in the current public dataset.
- BUSCO completeness scoring has not yet been run in this package.
- Genome-wide structural-variant analysis has not yet been run.

## Required high-confidence add-ons

1. Run BUSCO in genome mode using a Saccharomycetes lineage dataset.
2. Optionally align BY4741 to R64-1-1 with minimap2 for genome-wide synteny/SV review.
3. If possible, use raw reads to generate coverage plots across OCH1, MNN2, MNN5, and ISC1.
4. If available, add long-read validation data or a hybrid assembly.
