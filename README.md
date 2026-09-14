# Pocket Monsters Brilliant Diamond — Decompilation

![Status](https://img.shields.io/badge/status-public_source_census-blue)
![Project](https://img.shields.io/badge/project-decompilation-blue)
![Retail dump](https://img.shields.io/badge/local_retail_dump-not_available-orange)
![ROMs](https://img.shields.io/badge/ROM_binaries-not_included-success)

Decompilation and source-reconstruction project for **Pokémon Brilliant Diamond / ポケットモンスター ブリリアントダイヤモンド**.

## 🎯 Goals

- Reconstruct code, data and systems into readable, editable source form as public evidence permits.
- Exhaustively catalogue official, archival, reverse-engineering, Unity/IL2CPP, data-format, distribution, patch, HOME and regional sources.
- Use the **Japanese release as the comparison baseline** while preserving all regional/language/version/revision differences.
- Keep Brilliant Diamond independent from Shining Pearl wherever content, tables, branches, assets or behavior differ.
- Preserve 1.0.0 and every update state instead of flattening the game into its final patch.
- Compare Diamond/Pearl/Platinum only through identified evidence; Gen IV data never substitutes for BDSP data.

## 🚧 Current status

**Phase 0 — Target definition / exhaustive public-source census.**

There is currently **no locally owned retail game dump**. Research therefore begins from public evidence. Unknown hashes, cartridge revisions, content identities and internal fields remain unresolved instead of being guessed.

Current work includes:

- Japanese official 42-entry dedicated-site census plus off-index official material;
- 1.0.0 → 1.3.0 chronology and update-added functionality;
- Brilliant Diamond / Shining Pearl version differences;
- distributions, Mystery Gifts, HOME and save-data linkage;
- `TeamLumi/opendpr`, `MewTracker/bdsp-research`, PKHeX `SAV8BS`/PB8 and EvScript tooling;
- Unity/IL2CPP, field/event/resource/save research;
- packaging, bugs, unused/pre-release and archived material.

See [Project status](docs/PROJECT_STATUS.md) and [Exhaustive source coverage](docs/research/SOURCE_COVERAGE_TRACKER.md).

## 🗂️ Planned scope

- Unity/IL2CPP executable and class analysis
- Game data structures and master/resource tables
- EvScript, flags, events and field systems
- Pokémon / moves / items / abilities / evolution / encounters / trainers
- Grand Underground / Hideaways / Pokétch / contests / seals / followers
- Ramanas Park / Battle Tower / network features
- Graphics, models, animation, shaders, UI, fonts and audio
- Save data, PB8 and Pokémon HOME interoperability
- Region / language / patch / revision comparison
- DP/Platinum comparison with explicit source separation
- Tools, manifests, tests and verification data

## 📌 Repository policy

Retail ROM/game images, redistributed game binaries and console keys are **not included**. Research, reconstructed source, tooling, manifests, metadata and documentation are stored subject to provenance/license review.

## 🧭 Roadmap

- [ ] Exhaust public-source families and establish authoritative version/revision inventory
- [ ] Map Unity/IL2CPP classes, resources and data formats
- [ ] Reconstruct scripts/events and game systems from corroborated evidence
- [ ] Document assets, saves, network/HOME and version-specific behavior
- [ ] Add reproducible verification workflows when target evidence becomes available

## 📚 Documentation

| Document | Purpose |
| --- | --- |
| [Project status](docs/PROJECT_STATUS.md) | Current stage and next milestones |
| [Version coverage](docs/VERSIONS.md) | 1.0.0 and update chronology |
| [Public source index](docs/research/PUBLIC_SOURCE_INDEX.md) | Living Brilliant Diamond source ledger |
| [Exhaustive source coverage](docs/research/SOURCE_COVERAGE_TRACKER.md) | Per-source-family completion state |
| [Roadmap](docs/ROADMAP.md) | Long-term project phases |
| [Research guide](docs/RESEARCH_GUIDE.md) | Evidence workflow |
| [Verification guide](docs/VERIFICATION.md) | Validation standards |
| [Repository structure](docs/REPOSITORY_STRUCTURE.md) | Intended layout |
| [Documentation hub](docs/README.md) | Documentation entry point |

## 🧱 Repository structure

Existing project standards remain authoritative. New directories are created only when real material exists. BDSP's Unity/IL2CPP architecture is documented on its own terms rather than copied from Sword/Shield or another generation.

## 🔬 Research and verification

Every claim should identify version/region/language where relevant and distinguish public-source observation from direct retail-target verification. Shared BDSP sources must be reclassified for Brilliant Diamond applicability.

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
