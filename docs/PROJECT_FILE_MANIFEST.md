# Project File Manifest

This document records the contents observed inside the supplied `BCM_ECU.pdsprj` archive. These entries were read from the archive; the design itself has not been simulated.

| Archive entry | Size (bytes) | Observed purpose |
|---|---:|---|
| `ROOT.DSN` | 170,474 | Proteus schematic/design data file |
| `ROOT.CDB` | 4,434 | Proteus component/design database |
| `PROJECT.XML` | 249 | Project metadata and script reference |
| `FIRMWARE.XML` | 92 | Firmware metadata; its `PROJECTS` element is empty |
| `SCRIPTS/PWRRAILS.DAT` | 132 | Power-rail definitions, including GND, VCC/VDD and VEE |

## Publication note

Upload the original `BCM_ECU.pdsprj` file to the repository root. The project archive is a ZIP-based container, so preserve the original file rather than renaming or editing its internal members. Check local permissions before publishing any firmware or third-party content.

## Verification status

- Archive members listed above: inspected.
- Proteus circuit behavior: not verified.
- Firmware execution: not verified.
- Simulation output: not yet documented.
