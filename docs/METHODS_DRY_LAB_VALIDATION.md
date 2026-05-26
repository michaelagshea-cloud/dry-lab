# Methods: Dry-Lab Validation

## Reference genomes

- Primary design reference: *Saccharomyces cerevisiae* S288C / R64-1-1.
- Practical strain background: BY4741, checked against public NCBI assembly GCA_000766575.2 / ASM76657v2.

## Donor architecture

Each donor cassette is 2,299 bp:

```text
500 bp 5′ homology arm, including retained native anchor
+ 30 bp (GGGGS)2 linker
+ 1,269 bp diversified ISC1 payload with TAA stop
+ 500 bp 3′ homology arm
```

## Coding-region validation

The coding-region FASTA contains only the intended ORF segment:

```text
native anchor + (GGGGS)2 + ISC1α/β/γ + TAA
```

This is the region to translate. The full 2,299 bp donor cassettes should not be translated from base 1 because they include homology arms.

## Locus confirmation

The BY4741 genome assembly was searched for exact matches to the donor-arm and source-region sequences. Exact-match confirmation supports strain compatibility for the target loci, but does not prove experimental editing.

## Assembly confidence

Assembly metrics are computed from the BY4741 FASTA. BUSCO and optional SV analysis commands are provided but must be run in the user's local environment if final genome-wide confidence reporting is required.
