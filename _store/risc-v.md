---
aid: risc-v
name: RISC-V International
description: RISC-V International advances the RISC-V open standard instruction set architecture (ISA), promoting open hardware development and reducing dependency on proprietary processor designs. The organization maintains the canonical RISC-V ISA specifications, profiles, non-ISA specifications, extensions, and a rich ecosystem of open-source tools including simulators, compilers, debuggers, and verification frameworks.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - C API
  - Compiler
  - Hardware
  - Instruction Set Architecture
  - Linux Foundation
  - Open Hardware
  - Open Source
  - Processor
  - RISC-V
  - Simulator
url: https://raw.githubusercontent.com/api-evangelist/risc-v/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: risc-v:isa-specifications
    name: RISC-V ISA Specifications
    description: The canonical RISC-V Instruction Set Architecture specifications including the Unprivileged ISA (RV32I/RV64I base integer instructions) and Privileged Architecture specification. Freely available as ratified standards with a machine-readable database in the riscv-unified-db repo.
    humanURL: https://riscv.org/technical/specifications/
    tags:
      - Instruction Set Architecture
      - Privileged Architecture
      - RISC-V
      - Specifications
    properties:
      - type: Documentation
        url: https://riscv.org/technical/specifications/
      - type: GithubRepository
        url: https://github.com/riscv/riscv-isa-manual
      - type: GithubRepository
        url: https://github.com/riscv/riscv-unified-db
  - aid: risc-v:c-api-documentation
    name: RISC-V C API Documentation
    description: Documentation of the RISC-V C API including calling conventions, ABI specifications, compiler intrinsics, and architectural extension interfaces for C/C++ development targeting RISC-V processors.
    humanURL: https://github.com/riscv-non-isa/riscv-c-api-doc
    tags:
      - ABI
      - C API
      - Compiler
      - RISC-V
    properties:
      - type: GithubRepository
        url: https://github.com/riscv-non-isa/riscv-c-api-doc
  - aid: risc-v:non-isa-specifications
    name: RISC-V Non-ISA Specifications
    description: Supporting technical standards that do not add new instructions or modify the RISC-V ISA but help develop the ecosystem, including platform specifications, debug specifications, trace specifications, and interface standards.
    humanURL: https://github.com/riscv-non-isa
    tags:
      - Debug
      - Non-ISA
      - Platform
      - RISC-V
      - Trace
    properties:
      - type: GithubOrg
        url: https://github.com/riscv-non-isa
  - aid: risc-v:spike-simulator
    name: RISC-V Spike ISA Simulator
    description: Spike is the official RISC-V ISA Simulator and the golden reference implementation for RISC-V. It simulates the execution of RISC-V programs and is used for architecture validation and software development.
    humanURL: https://github.com/riscv-software-src/riscv-isa-sim
    tags:
      - Reference Implementation
      - RISC-V
      - Simulator
      - Testing
    properties:
      - type: GithubRepository
        url: https://github.com/riscv-software-src/riscv-isa-sim
  - aid: risc-v:opensbi
    name: RISC-V OpenSBI
    description: OpenSBI is the official open-source implementation of the RISC-V Supervisor Binary Interface (SBI) specification. It provides a firmware execution environment for M-mode privileged operations and serves as the primary boot firmware for RISC-V Linux systems.
    humanURL: https://github.com/riscv-software-src/opensbi
    tags:
      - Firmware
      - Linux
      - RISC-V
      - SBI
    properties:
      - type: GithubRepository
        url: https://github.com/riscv-software-src/opensbi
common:
  - type: Website
    url: https://riscv.org/
  - type: Documentation
    url: https://riscv.org/technical/specifications/
  - type: GithubOrg
    url: https://github.com/riscv
  - type: GithubOrg
    url: https://github.com/riscv-non-isa
  - type: GithubOrg
    url: https://github.com/riscv-software-src
  - type: Wiki
    url: https://wiki.riscv.org/
  - type: MemberPortal
    url: https://members.riscv.org/
  - type: PrivacyPolicy
    url: https://riscv.org/privacy-policy/
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/risc-v/refs/heads/main/json-schema/risc-v-specification-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/risc-v/refs/heads/main/json-ld/risc-v-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/risc-v/refs/heads/main/vocabulary/risc-v-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
