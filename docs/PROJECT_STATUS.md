# Project Status

**Current stage:** Phase 0 — target intake and reproducibility baseline

Generation VIII decompilation is active across Sword, Shield, Brilliant Diamond, Shining Pearl, and Pokémon Legends: Arceus. This repository tracks Brilliant Diamond independently while preserving only verified relationships with Shining Pearl and the original Generation IV titles.

## Progress

- [x] Establish clean repository baseline
- [x] Begin exact-target intake workflow
- [ ] Record exact Brilliant Diamond revision/update hashes
- [ ] Document observed executable and data layout
- [ ] Compare BD/SP only with byte/hash-backed evidence
- [ ] Map symbols, functions, assemblies/modules, scripts, and major subsystems as observed
- [ ] Document game-data formats and resource containers
- [ ] Reconstruct the first bounded source subsystem
- [ ] Add reproducible extraction/repacking tooling as formats are verified
- [ ] Add automated reconstruction verification where practical

## Comparison boundaries

- Brilliant Diamond and Shining Pearl remain separate targets.
- Diamond/Pearl/Platinum are historical comparison sources, not assumed implementation templates.
- Any shared file, table, script, asset, or code claim must be verified against the actual BDSP targets.

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Reference only** — sourced externally and not yet matched to the local target.
- **Observed** — confirmed directly in the selected target build or extraction.
- **Reproduced** — recreated by documented tooling or steps.
- **Matched** — reconstructed output satisfies an explicit match criterion.

## Immediate next milestone

Inventory a locally verified Brilliant Diamond target, then build the first observed executable/data map before source reconstruction expands.
