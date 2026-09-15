# Decompilation Start

This repository is an independent Generation VIII reconstruction target for **Pokémon Brilliant Diamond**.

## Phase 0 — target intake

1. Keep retail game images, decrypted package archives, console keys, and complete redistributed game binaries outside Git.
2. Inventory the exact local extraction by relative path, size, and SHA-256.
3. Record revision/update identity before interpreting code or data.
4. Preserve Brilliant Diamond-specific files and behavior even when Shining Pearl appears similar.

## Phase 1 — executable and data map

Map only structures directly observed in the selected Brilliant Diamond target: executable files, metadata, assemblies/modules where present, asset/resource containers, filesystem paths, tables, scripts, and versioned data.

Do not import assumptions from Sword/Shield or from Generation IV Diamond/Pearl. Original DP is a comparison source, not a substitute for BDSP evidence.

## Phase 2 — bounded source reconstruction

Choose a subsystem with a stable evidence boundary and an explicit verification method. Add reconstructed source only when real work exists.

## Pair comparison

Brilliant Diamond and Shining Pearl may share large amounts of material, but shared-source or deduplication decisions require direct byte/hash/structure evidence. Version-exclusive data remains separate.

## Verification

Use `Unverified`, `Reference only`, `Observed`, `Reproduced`, and `Matched` consistently.
