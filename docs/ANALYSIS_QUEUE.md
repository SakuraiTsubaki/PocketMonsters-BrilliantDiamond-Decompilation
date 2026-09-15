# Active Analysis Queue

This queue defines the first evidence-backed work for the Pokémon Brilliant Diamond decompilation.

## 0. Target identity

- [ ] Hash the exact local base-game extraction.
- [ ] Hash the exact local update extraction, including Ver. 1.3.0 when available.
- [ ] Record observed executable build identifiers from the selected target.
- [ ] Keep external Application/Patch IDs as `reference_only` until matched to local project material.

## 1. ExeFS and runtime map

- [ ] Enumerate every observed ExeFS path and hash.
- [ ] Identify executable/container/runtime formats from direct evidence.
- [ ] Record executable sections, metadata, imports/relocations, build identifiers, and code/data boundaries where observable.
- [ ] Do not assume a runtime-specific decompilation workflow until the selected target confirms it.

## 2. RomFS and content map

- [ ] Enumerate the full RomFS tree.
- [ ] Classify observed resource/container formats by signature and structure.
- [ ] Record which content exists in the base application versus updates.
- [ ] Preserve the important distinction that Ver. 1.1.0 added/implemented substantial shipped game content and later versions modified it further.

## 3. Brilliant Diamond / Shining Pearl comparison

- [ ] Map Brilliant Diamond independently.
- [ ] Compare only against a verified Shining Pearl target with matching revision scope.
- [ ] Classify path/hash identity, version exclusives, data differences, text differences, encounter differences, and executable differences.
- [ ] Deduplicate project representations only after byte/hash identity is proven.

## 4. Original DP / Platinum comparison

Generation IV games are reference targets, not implementation templates.

- [ ] Compare game data and behavior only after the BD target structure is mapped.
- [ ] Record whether an element is retained, changed, newly implemented, absent, or sourced through update content.
- [ ] Never infer an internal field/layout solely from the Nintendo DS originals.

## 5. First bounded reconstruction candidates

Prioritize components with deterministic verification, for example:

1. a metadata or table parser;
2. a resource/container reader;
3. a version-exclusive data table shared structurally with Shining Pearl;
4. a script/event representation with a decode/encode round trip.

## Verification gates

`Unverified -> Observed -> Reproduced -> Matched`

Every `Matched` result must state the exact comparison criterion and target revision.
