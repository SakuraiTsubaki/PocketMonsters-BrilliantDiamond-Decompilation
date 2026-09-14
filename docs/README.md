# Documentation Hub

This directory is the central documentation portal for the decompilation project. The current phase is a **ROM-less exhaustive public-source census**, using the Japanese release as the comparison baseline while preserving Brilliant Diamond-specific and all-region differences.

## Quick links

| Document | Purpose |
| --- | --- |
| [Project Status](PROJECT_STATUS.md) | Current stage and next milestones |
| [Version Coverage](VERSIONS.md) | 1.0.0 and update/revision inventory |
| [Public Source Index](research/PUBLIC_SOURCE_INDEX.md) | Living Brilliant Diamond source ledger |
| [Exhaustive Source Coverage](research/SOURCE_COVERAGE_TRACKER.md) | Per-source-family completion state |
| [Roadmap](ROADMAP.md) | Project phases |
| [Research Guide](RESEARCH_GUIDE.md) | Evidence practices |
| [Verification Guide](VERIFICATION.md) | Validation levels |
| [Repository Structure](REPOSITORY_STRUCTURE.md) | Intended layout |
| [Project Standards](PROJECT_STANDARDS.md) | Naming/provenance rules |
| [Asset Workflow](ASSET_WORKFLOW.md) | Asset handling rules |
| [Manifest Guide](../manifests/README.md) | Machine-readable inventories |
| [Contributing](../CONTRIBUTING.md) | Contribution guidance |

## Recommended research flow

1. Check `research/SOURCE_COVERAGE_TRACKER.md` before declaring any family complete.
2. Identify the exact 1.0.0/updated target state in `VERSIONS.md`.
3. Register primary and technical sources in `research/PUBLIC_SOURCE_INDEX.md`.
4. Keep Brilliant Diamond branches/data separate from Shining Pearl.
5. Keep Unity/IL2CPP evidence separate from assumptions imported from other Pokémon engines.
6. Apply `RESEARCH_GUIDE.md`, `PROJECT_STANDARDS.md` and `VERIFICATION.md` when reconstructing classes/data/scripts/assets.
7. Update `PROJECT_STATUS.md` when meaningful milestones change.

## Documentation rules

- Representative samples do not satisfy exhaustive survey requirements.
- Japanese material is the comparison baseline; regional differences are preserved independently.
- 1.0.0 and every update remain historical targets instead of being overwritten by final-patch behavior.
- Gen IV DP/Platinum data is comparison evidence, not replacement BDSP data.
- Use `TBD`, `unknown` or `null` rather than inventing internal information.
- Preserve provenance and distinguish public-source observation from direct target verification.
- Keep retail game images, decrypted game images and console keys out of the repository.
