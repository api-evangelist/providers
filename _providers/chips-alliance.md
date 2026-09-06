---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chips-alliance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chipsalliance.org
- group: other
  title: ''
  type: Projects
  url: https://chipsalliance.org/projects/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/chipsalliance
- group: other
  title: ''
  type: ParentOrganization
  url: https://www.linuxfoundation.org/
- group: start
  title: ''
  type: MemberPortal
  url: https://members.chipsalliance.org
- group: other
  title: ''
  type: MailingLists
  url: https://lists.chipsalliance.org/g/main/subgroups
- group: company
  title: ''
  type: Blog
  url: https://chipsalliance.org/news/
- group: other
  title: ''
  type: Events
  url: https://chipsalliance.org/events/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/chipsalliance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chips-alliance/
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: auth
  title: ''
  type: AntitrustPolicy
  url: https://chipsalliance.org/antitrust-policy/
- group: other
  title: ''
  type: Projects
  url: ''
- group: other
  title: ''
  type: MemberTiers
  url: ''
- group: other
  title: ''
  type: Workgroups
  url: ''
- group: other
  title: ''
  type: Standards
  url: ''
created: '2026-03-16'
description: CHIPS Alliance is a Linux Foundation project (founded in 2019) that develops open-source hardware (silicon) and tools, including CPUs, SoC subsystems, peripherals, IP blocks, and FPGA tooling. The Alliance fosters collaboration among 50+ member organizations across industry (AMD, Antmicro, Google, Microsoft, SiFive, Intel, Nvidia, Cisco, Synopsys, Microchip, SanDisk and others) and academia (Berkeley, Stanford, MIT, and more) to lower the cost of hardware design, accelerate innovation in silicon, and provide an open and accessible alternative to proprietary EDA flows. CHIPS Alliance hosts more than a dozen technical projects including Chisel (Hardware Construction Language), F4PGA, Caliptra (Root of Trust), VeeR (RISC-V cores), Surelog/UHDM (SystemVerilog parsing), and the FPGA Interchange format. The Alliance does not publish a centralized REST API; technical assets are distributed via GitHub repositories under github.com/chipsalliance and member-driven mailing lists.
features:
- name: Open Source Silicon Design
- name: Open Source FPGA Toolchains
- name: Open Hardware Construction Languages (Chisel)
- name: SystemVerilog Parsing and Tooling
- name: Open RISC-V Cores
- name: Hardware Root of Trust (Caliptra, OpenPRoT)
- name: FPGA Interchange Format Standardization
- name: Cross-Industry Collaboration
finops:
- name: Chips Alliance Finops
  service_category: API
  slug: chips-alliance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chips-alliance.png
layout: provider
modified: '2026-07-25'
name: CHIPS Alliance
nav: Providers
network: true
overview: 'CHIPS Alliance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Chisel, EDA, FPGA, Hardware, and Linux Foundation.


  CHIPS Alliance''s developer surface includes engineering blog and 12 more developer resources.'
plans:
- name: Chips Alliance Plans Pricing
  plan_count: 3
  slug: chips-alliance-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Chips Alliance Rate Limits
  slug: chips-alliance-rate-limits
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 10.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chips-alliance/refs/heads/main/screenshots/chips-alliance-2026-06-20T174320.png
security:
- kind: domain-security
  name: Chips Alliance Domain Security
  slug: chips-alliance-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chips-alliance
tags:
- Chisel
- EDA
- FPGA
- Hardware
- Linux Foundation
- Open Hardware
- Open-Source
- RISC-V
- SiFive
- Silicon
- SOC
- SystemVerilog
use_cases:
- name: Open Source CPU/SoC Design
- name: FPGA Toolchain Development
- name: SystemVerilog Linting and Compilation
- name: Hardware Security Root of Trust
- name: RISC-V IP Verification
- name: EDA Tool Interoperability
- name: Academic Hardware Research
- name: Industry-Academia Hardware Collaboration
website: https://chipsalliance.org
---
