# Public Source Index

This is the living source index for the ROM-less reconstruction of **Pocket Monsters Brilliant Diamond / Pokémon Brilliant Diamond**.

The project has no locally owned retail dump. Publicly accessible evidence is therefore surveyed exhaustively, with the **Japanese release used as the comparison baseline** and all regional, language, revision, update, distribution, storefront, save-link, HOME and technical differences preserved.

## Evidence policy

- Japanese official material is the baseline for chronology and Japanese terminology.
- Brilliant Diamond is tracked independently from Shining Pearl even when sources cover both games.
- BDSP is **Unity + IL2CPP** based; Sword/Shield Game Freak file-layout assumptions must not be imported into this repository.
- Public reverse-engineering projects are `Unverified / external evidence` for retail-target claims until corroborated.
- Official statements about features added by update are preserved by exact version; launch cartridge data and post-update state are not collapsed together.
- Unknown hashes, game-card revisions, content identities and regional binary relationships remain `TBD`.

## Official Japanese baseline sources

| ID | Source | Coverage |
| --- | --- | --- |
| `OFF-JP-BDSP-HOME` | https://www.pokemon.co.jp/ex/bdsp/ja/ | Japanese official site; currently exposes 42 indexed latest-information entries (8 news, 6 videos, 26 game-information, 2 campaign) |
| `OFF-JP-BDSP-LINEUP` | https://www.pokemon.co.jp/ex/bdsp/ja/lineup/210818_01/ | Release 2021-11-19, ILCA production, package/download forms, nine supported languages, double pack and product metadata |
| `OFF-JP-BDSP-DIFF` | https://www.pokemon.co.jp/ex/bdsp/ja/story/210818_06/ | Official Brilliant Diamond / Shining Pearl differences |
| `OFF-JP-BDSP-UPD-110` | https://www.pokemon.co.jp/info/2021/11/211110_at01.html | Ver.1.1.0; communications, postgame elements, movies/effects; explicit incompatibility with 1.0.0 local communication |
| `OFF-JP-BDSP-UPD-111` | https://www.pokemon.co.jp/info/2021/11/211118_at01.html | Ver.1.1.1 optimization |
| `OFF-JP-BDSP-UPD-112` | https://www.pokemon.co.jp/info/2021/12/211202_at01.html | Ver.1.1.2 fixes and future-update statement |
| `OFF-JP-BDSP-UPD-113` | https://www.pokemon.co.jp/info/2021/12/211222_at01.html | Ver.1.1.3 fixes and future-update statement |
| `OFF-JP-BDSP-UPD-120` | https://www.pokemon.co.jp/info/2022/02/220222_gm01.html | Ver.1.2.0 Union Room expansion and other changes |
| `OFF-JP-BDSP-UPD-130` | https://www.pokemon.co.jp/info/2022/03/220316_gm01.html | Ver.1.3.0; PLA save-link Arceus event, GMStation, fixes |
| `OFF-JP-HOME-200` | https://www.pokemon.co.jp/info/2022/05/220520_at01.html | Pokémon HOME Ver.2.0.0 adds BDSP support |

The official product page explicitly notes that some features/modes require update data. Therefore **1.0.0, launch-day 1.1.x states and later updates are separate research targets**.

## Brilliant Diamond-specific comparison axes

- Dialga-facing version content and Brilliant Diamond-exclusive wild Pokémon;
- fossil, Ramanas Park and other version-dependent encounter/reward content;
- Brilliant Diamond-specific assets, tables, flags and version branches in shared Unity/IL2CPP code/data;
- official packaging/art-book/retailer differences;
- events or gifts with Diamond/Pearl-dependent redemption or content;
- cross-save events and HOME conversion behavior;
- regional/localization differences against Japanese text and presentation.

## Public reverse-engineering and technical sources

| ID | Source | Relevant evidence |
| --- | --- | --- |
| `RE-OPENDPR` | https://github.com/TeamLumi/opendpr | Public BDSP source-reconstruction project; Unity project with Dpr classes, EvScript systems and large-scale recovered logic |
| `RE-BDSP-RESEARCH` | https://github.com/MewTracker/bdsp-research | IL2CPP/Ghidra/Il2CppDumper workflow and BDSP RNG/function research |
| `RE-PKHEX` | https://github.com/kwsch/PKHeX | `SAV8BS`, PB8/entity structures, save blocks, legality, encounters and HOME-related handling |
| `RE-PKHEX-SAV8BS` | https://github.com/kwsch/PKHeX/blob/master/PKHeX.Core/Saves/SAV8BS.cs | BDSP save root object; external source lead |
| `RE-UNITY-EV-AS` | https://github.com/AarCon/unity-ev-as | Public BDSP event-script assembler/parser lead; existence/content requires continued source review |
| `RE-HAX/IL2CPP` | https://github.com/Perfare/Il2CppDumper | Generic IL2CPP metadata tooling referenced by BDSP research; platform/tool context rather than BD-specific evidence by itself |
| `RE-HACTOOL` | https://github.com/SciresM/hactool | Switch container context |

`TeamLumi/opendpr` currently exposes recovered classes such as `Dpr.EvScript.EvDataManager`; this is high-value external evidence for event/script architecture, but it does not substitute for direct observation of the project's absent retail dump.

## Event / distribution / interoperability sources

| ID | Source | Coverage |
| --- | --- | --- |
| `DB-PP-GEN8` | https://projectpokemon.org/home/files/category/2-event-gallery/ | Generation VIII event archive; current census reports 14 BDSP records in its BDSP category |
| `OFF-JP-BIRTHDAY` | https://www.pokemon.co.jp/info/2021/10/211022_p01.html | Birthday Happiny serial campaign shared across BDSP/PLA timing; cross-title redemption constraints |
| `OFF-JP-PLA-ARCEUS-LINK` | https://www.pokemon.co.jp/ex/bdsp/ja/news/220314_02/ | PLA save-data linked Arceus event; requires BDSP Ver.1.3.0 and game-progress conditions |

## Source families requiring exhaustive enumeration

- all 42 dedicated Japanese BDSP latest-information entries, followed by off-index official pages;
- every patch from physical launch state through 1.3.0, including behaviors/features absent from 1.0.0;
- all Japanese/regional distributions, Mystery Gifts, Oak's Letter/Member Card and timed/network-delivered content;
- every official regional and language site;
- HOME compatibility, Strange Ball/conversion rules and transfer restrictions;
- opendpr classes/resources/history, bdsp-research, event-script tools, save/RNG projects and materially different forks;
- Unity version/packages, IL2CPP metadata research, asset bundles/addressables/resource tables, scene/field/event systems;
- save structure, PB8, flags, Pokétch, contest, seals, Underground and battle-related blocks;
- Grand Underground, Hideaways, Ramanas Park, Battle Tower, contests, follower systems and version differences;
- packaging, cartridge revisions, identifiers, ratings and region-facing metadata;
- glitches, patch-fixed behavior, unused/replaced data, pre-release footage and DP/Platinum comparison evidence;
- secondary databases/wikis/datamines only with provenance and upstream tracing.

## Completion rule

A representative sample is never enough. Each source family progresses through `Not started → Enumerating → Indexed → Reviewed → Cross-checked → Exhausted`.

_Last surveyed: 2026-09-14._
