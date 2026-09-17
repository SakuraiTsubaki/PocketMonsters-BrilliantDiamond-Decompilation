# Bug Eradication Program

## Goal

Drive the repository toward **zero known reproducible unintended defects** for the selected Pokémon Brilliant Diamond target revision while preserving intended rules, content, version differences, and patch-era behavior.

Coverage includes crashes, hangs, softlocks, progression blockers, save/data corruption, battle logic, AI, invalid data, event/script errors, map/collision issues, graphics/UI, audio, localization/text, local/online communication, Grand Underground behavior, Super Contest Show behavior, Ramanas Park/event behavior, performance/resource defects, update regressions, and other reproducible unintended behavior.

## Target identity gate

No binary-specific fix is verified until `config/target.json` records the exact release/region/revision and hashes of the locally supplied legal dump or extracted target. Full game images/installable packages are never committed.

## Evidence and severity

Evidence: `reported`, `probable`, `confirmed`, `not-a-bug`.
Severity: S0 critical, S1 high, S2 medium, S3 low, S4 cosmetic.

## Required lifecycle

Discovery/source citation → target/revision assignment → reproduction → expected/actual result → root cause → minimal fix → non-ROM patch/diff → positive regression test → negative regression tests → version/network compatibility checks → `verified-fixed`.

## BDSP-specific version axes

Track separately when applicable:

- Brilliant Diamond versus Shining Pearl shared and version-specific behavior;
- original cartridge/base data versus each update revision;
- local versus online communication;
- Grand Underground and Hideaway behavior;
- overworld/NPC collision and movement;
- menu/storage/trade/battle transitions;
- story/event flags and post-game content;
- language/region-specific text and data behavior.

## Repository placement

- `manifests/bug-registry.json`: authoritative defect index.
- `analysis/bugs/`: reproduction and root-cause reports.
- `patches/bugs/`: diffs, patch material, address/symbol maps.
- `logs/bugs/`: execution and regression logs.
- `artifacts/bugs/`: retained non-ROM evidence.
- `tools/`: validators and automation.

## Completion rule

A target revision is clean only when every known registry item is `verified-fixed` or `not-a-bug`, validation passes, and no unresolved report or regression remains.
