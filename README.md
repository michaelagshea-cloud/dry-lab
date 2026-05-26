# Three-Lock HDR Donor Package v1.0 — Dry-Lab Genome Biology Repository

This repository contains the dry-lab files needed to reproduce and audit the computational candidate genome design:

- **OCH1/YGL038C** catalytic-domain replacement donor: 5′ arm ending at codon 45 + `(GGGGS)2` + **ISC1α** + `TAA` + 3′ arm after native stop.
- **MNN2/YBR015C** catalytic-domain replacement donor: 5′ arm ending at codon 41 + `(GGGGS)2` + **ISC1β** + `TAA` + 3′ arm after native stop.
- **MNN5/YJL186W** catalytic-domain replacement donor: 5′ arm ending at codon 45 + `(GGGGS)2` + **ISC1γ** + `TAA` + 3′ arm after native stop.

## Validation status

These records are **computationally validated donor candidates**, not experimentally validated strains or EVs.

Completed dry-lab layers included here:

1. Donor cassette sequence records in FASTA and GenBank.
2. Benchling visual import PDFs.
3. Feature table and R64-1-1 genome mapping table.
4. Chimeric ORF translation inputs and expected proteins.
5. BY4741 target-locus exact-match confirmation outputs.
6. BY4741 assembly metadata and computed assembly metrics.
7. Scripts for repeat/restriction screening, exact-match locus confirmation, N50/L50 assembly metrics, BUSCO, and optional SV analysis.

Pending validation layers:

- BUSCO completeness scoring has not been run in this package.
- Genome-wide structural variant analysis is optional and not yet completed.
- Wet-lab or ex-vivo EV validation is not included.

## Reproducibility quick start

```bash
python scripts/compute_assembly_metrics.py data/reference/BY4741_NCBI_GCA_000766575_2/GCA_000766575.2_ASM76657v2_genomic.fna
python scripts/validate_chimeric_orfs.py data/constructs/chimera_coding_regions_for_translation_check.fasta
python scripts/restriction_repeat_screen.py data/constructs/final_three_lock_full_donor_cassettes_500bpHDR_transcript_orientation.fasta
python scripts/locus_exact_match.py data/reference/BY4741_NCBI_GCA_000766575_2/GCA_000766575.2_ASM76657v2_genomic.fna data/constructs/catalytic_domain_replacement_500bp_arms_transcript_orientation.fasta
```

## Repository interpretation

The current dry-lab claim is narrow:

> The v1.0 donor cassettes are internally consistent, translate in-frame, map to the intended target architecture, and match the practical BY4741 background at the required target-locus sequences.

Do **not** claim that the triple-lock strain exists, that editing has succeeded, or that EV behavior has been experimentally validated.
