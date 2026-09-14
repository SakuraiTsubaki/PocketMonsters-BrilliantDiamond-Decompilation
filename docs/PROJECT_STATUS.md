# Project Status

**Current stage:** Phase 0 — Target definition / exhaustive public-source census

This project has **no locally owned retail dump**. Work therefore proceeds by exhaustive public-source research, using the Japanese release as the comparison baseline and preserving Brilliant Diamond-specific, regional, language, update, distribution, HOME and technical differences.

## Version inventory

| Target | Region | Language | Revision / update | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| Brilliant Diamond physical/base state | JP baseline | 9 officially supported languages | 1.0.0 baseline | Reference only | Must remain separate from launch-day updated state. Exact hashes/build TBD. |
| Brilliant Diamond updates | JP baseline | multilingual identity TBD | 1.1.0 → 1.3.0 | Reference only | Official chronology recorded in `VERSIONS.md`. |
| HOME linked state | JP baseline + all regions | HOME localization separate | HOME Ver.2.0.0 onward | Reference only | Cross-title transfer/conversion rules are versioned. |

## Active exhaustive-source work

- Japanese BDSP official site currently exposes a 42-entry latest-information index; every entry must be individually resolved and classified.
- Off-index Pokémon official pages, Pokémon Center/retailer campaigns, updates, HOME and cross-title notices are separate workstreams.
- Brilliant Diamond is kept independent from Shining Pearl for version-exclusive data and branch behavior.
- `TeamLumi/opendpr`, `MewTracker/bdsp-research`, PKHeX `SAV8BS`/PB8, EvScript tooling, Unity/IL2CPP research and materially different forks are technical source families.
- Project Pokémon's current BDSP event-category anchor is 14 records; each requires individual review and official cross-checking.

## Technical progress

- [ ] Establish authoritative version/revision inventory — **in progress**
- [ ] Document executable/IL2CPP and section layout — **public research mapping started**
- [ ] Map symbols, classes, methods and major subsystems — **opendpr/bdsp-research mapping started**
- [ ] Document game-data formats/resources — **in progress**
- [ ] Reconstruct scripts/events — **EvScript source mapping started**
- [ ] Reconstruct Unity asset/resource pipeline
- [ ] Add reproducible extraction/repacking tooling
- [ ] Add automated verification where practical

## Active research material

- `docs/research/PUBLIC_SOURCE_INDEX.md`
- `docs/research/SOURCE_COVERAGE_TRACKER.md`
- `docs/VERSIONS.md`
- `manifests/source-coverage.json`

## Validation levels

- **Unverified** — proposed or external technical claim not independently target-checked.
- **Observed** — directly confirmed in a target build/extracted target data.
- **Reproduced** — reproducible with documented steps.
- **Matched** — exact-match criterion against intended target satisfied.
- **Reference only** — public evidence exists while retail identity/hashes remain unavailable.

## Immediate next milestones

1. Enumerate all 42 Japanese dedicated-site entries and all off-index official BDSP pages.
2. Build Brilliant Diamond-specific version-difference ledger against Shining Pearl.
3. Recursively inventory `opendpr` classes/resources and `bdsp-research` notes at pinned commits.
4. Recursively inventory PKHeX `SAV8BS`, PB8 and Gen8/BS save substructures.
5. Resolve and enumerate the 14 Project Pokémon BDSP archive records.
6. Build the full 1.0.0→1.3.0 feature/bug/data-difference chronology.
7. Enumerate every official regional/language surface, event, HOME rule, packaging revision, glitch, unused and pre-release source.

Update this file whenever a meaningful milestone changes.
