---
aid: chips-alliance
name: CHIPS Alliance
x-type: opensource
description: CHIPS Alliance is a Linux Foundation project (founded in 2019) that develops open-source hardware (silicon) and tools, including CPUs, SoC subsystems, peripherals, IP blocks, and FPGA tooling. The Alliance fosters collaboration among 50+ member organizations across industry (AMD, Antmicro, Google, Microsoft, SiFive, Intel, Nvidia, Cisco, Synopsys, Microchip, SanDisk and others) and academia (Berkeley, Stanford, MIT, and more) to lower the cost of hardware design, accelerate innovation in silicon, and provide an open and accessible alternative to proprietary EDA flows. CHIPS Alliance hosts more than a dozen technical projects including Chisel (Hardware Construction Language), F4PGA, Caliptra (Root of Trust), VeeR (RISC-V cores), Surelog/UHDM (SystemVerilog parsing), and the FPGA Interchange format. The Alliance does not publish a centralized REST API; technical assets are distributed via GitHub repositories under github.com/chipsalliance and member-driven mailing lists.
type: Index
position: Consumer
access: Open
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/chips-alliance/refs/heads/main/apis.yml
tags:
  - Chisel
  - EDA
  - FPGA
  - Hardware
  - Linux Foundation
  - Open Hardware
  - Open Source
  - RISC-V
  - SiFive
  - Silicon
  - SoC
  - SystemVerilog
created: '2026-03-16'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: chips-alliance:chips-alliance-projects
    name: CHIPS Alliance Projects
    description: Catalog of open-source hardware and tooling projects hosted by CHIPS Alliance, including Chisel, F4PGA, Caliptra, VeeR, Surelog/UHDM, FPGA Interchange format, OpenPRoT, Intel Compiler for SystemC, FPGA tool perf, and SV tools. Project assets are distributed via GitHub repositories under the github.com/chipsalliance organization. There is no centralized HTTP API; integrations occur through Git, package managers, and per-project release artifacts.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://chipsalliance.org/projects/
    tags:
      - Hardware
      - Open Source
      - Silicon
    properties:
      - type: Documentation
        url: https://chipsalliance.org/projects/
      - type: GitHubOrg
        url: https://github.com/chipsalliance
common:
  - type: Website
    url: https://chipsalliance.org
  - type: Projects
    url: https://chipsalliance.org/projects/
  - type: GitHubOrg
    url: https://github.com/chipsalliance
  - type: ParentOrganization
    name: Linux Foundation
    url: https://www.linuxfoundation.org/
  - type: MemberPortal
    url: https://members.chipsalliance.org
  - type: MailingLists
    url: https://lists.chipsalliance.org/g/main/subgroups
  - type: Blog
    url: https://chipsalliance.org/news/
  - type: Events
    url: https://chipsalliance.org/events/
  - type: Twitter
    url: https://twitter.com/chipsalliance
  - type: LinkedIn
    url: https://www.linkedin.com/company/chips-alliance/
  - type: License
    name: Apache License 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: AntitrustPolicy
    url: https://chipsalliance.org/antitrust-policy/
  - name: Projects
    type: Projects
    data:
      - name: Caliptra (Root of Trust)
      - name: Chisel (Hardware Construction Language)
      - name: F4PGA (FPGA toolchain)
      - name: FPGA Interchange Format
      - name: FPGA tool perf
      - name: Intel Compiler for SystemC
      - name: OpenPRoT (Platform Root of Trust)
      - name: Surelog and UHDM
      - name: SV tools (SystemVerilog/UVM)
      - name: VeeR (RISC-V cores)
  - name: MemberTiers
    type: MemberTiers
    data:
      - name: Platinum (AMD, Antmicro, Google, Microsoft, SiFive, VeriSilicon)
      - name: Gold (ISCAS, Marvell)
      - name: Silver (Intel, Nvidia, Cisco, Synopsys, Microchip, SanDisk and others)
      - name: Academic / Associate (Berkeley, Stanford, MIT-affiliated, RISC-V Foundation, and more)
  - name: Workgroups
    type: Workgroups
    data:
      - name: Interconnect Workgroup
      - name: RISC-V Verification IP Workgroup
      - name: FPGA Workgroup
      - name: Caliptra Workgroup
      - name: Chisel Workgroup
      - name: SystemVerilog Tools Workgroup
  - name: Features
    type: Features
    data:
      - name: Open Source Silicon Design
      - name: Open Source FPGA Toolchains
      - name: Open Hardware Construction Languages (Chisel)
      - name: SystemVerilog Parsing and Tooling
      - name: Open RISC-V Cores
      - name: Hardware Root of Trust (Caliptra, OpenPRoT)
      - name: FPGA Interchange Format Standardization
      - name: Cross-Industry Collaboration
  - name: UseCases
    type: UseCases
    data:
      - name: Open Source CPU/SoC Design
      - name: FPGA Toolchain Development
      - name: SystemVerilog Linting and Compilation
      - name: Hardware Security Root of Trust
      - name: RISC-V IP Verification
      - name: EDA Tool Interoperability
      - name: Academic Hardware Research
      - name: Industry-Academia Hardware Collaboration
  - name: Standards
    type: Standards
    data:
      - name: SystemVerilog (IEEE 1800)
      - name: RISC-V ISA Specification
      - name: FPGA Interchange Format
      - name: UVM (Universal Verification Methodology)
      - name: Apache License 2.0
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
