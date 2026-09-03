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
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: The canonical RISC-V Instruction Set Architecture specifications including the Unprivileged ISA (RV32I/RV64I base integer instructions) and Privileged Architecture specification. Freely available as r
  name: RISC-V ISA Specifications
  slug: isa-specifications
- description: Documentation of the RISC-V C API including calling conventions, ABI specifications, compiler intrinsics, and architectural extension interfaces for C/C++ development targeting RISC-V processors.
  name: RISC-V C API Documentation
  slug: c-api-documentation
- description: 'Supporting technical standards that do not add new instructions or modify the RISC-V ISA but help develop the ecosystem, including platform specifications, debug specifications, trace specifications, '
  name: RISC-V Non-ISA Specifications
  slug: non-isa-specifications
- description: Spike is the official RISC-V ISA Simulator and the golden reference implementation for RISC-V. It simulates the execution of RISC-V programs and is used for architecture validation and software develo
  name: RISC-V Spike ISA Simulator
  slug: spike-simulator
- description: OpenSBI is the official open-source implementation of the RISC-V Supervisor Binary Interface (SBI) specification. It provides a firmware execution environment for M-mode privileged operations and serv
  name: RISC-V OpenSBI
  slug: opensbi
artifact_total: 13
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/riscv/riscv-isa-manual/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/riscv/riscv-isa-manual/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/riscv/riscv-isa-manual/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/riscv/riscv-isa-manual/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/risc-v-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://riscv.org/
- group: docs
  title: ''
  type: Documentation
  url: https://riscv.org/technical/specifications/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/riscv
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/riscv-non-isa
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/riscv-software-src
- group: other
  title: ''
  type: Wiki
  url: https://wiki.riscv.org/
- group: start
  title: ''
  type: MemberPortal
  url: https://members.riscv.org/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://riscv.org/privacy-policy/
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/risc-v/refs/heads/main/json-schema/risc-v-specification-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/risc-v/refs/heads/main/json-ld/risc-v-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/risc-v/refs/heads/main/vocabulary/risc-v-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://riscv.org/feed/
created: '2026-03-16'
description: RISC-V International advances the RISC-V open standard instruction set architecture (ISA), promoting open hardware development and reducing dependency on proprietary processor designs. The organization maintains the canonical RISC-V ISA specifications, profiles, non-ISA specifications, extensions, and a rich ecosystem of open-source tools including simulators, compilers, debuggers, and verification frameworks.
finops:
- name: Risc V Finops
  service_category: API
  slug: risc-v-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/risc-v.png
json_schemas:
- name: RISC-V Specification
  property_count: 11
  slug: risc-v-specification
json_structures:
- name: Risc V Specification Structure
  property_count: 0
  slug: risc-v-specification-structure
jsonld:
- class_count: 32
  name: Risc V Context
  property_count: 0
  slug: risc-v-context
layout: provider
modified: '2026-05-02'
name: RISC-V International
nav: Providers
network: true
overview: 'RISC-V International publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include C API, Compiler, Hardware, Instruction Set Architecture, and Linux Foundation.


  The RISC-V International catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RISC-V International''s developer surface includes documentation, engineering blog, and 15 more developer resources.'
plans:
- name: Risc V Plans Pricing
  plan_count: 3
  slug: risc-v-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Risc V Rate Limits
  slug: risc-v-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: RISC-V International API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: risc-v-jsonschema-spectral-rules
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 50.0
  previous_composite: 26.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/risc-v/refs/heads/main/screenshots/risc-v-2026-06-20T193125.png
security:
- kind: domain-security
  name: Risc V Domain Security
  slug: risc-v-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: risc-v
tags:
- C API
- Compiler
- Hardware
- Instruction Set Architecture
- Linux Foundation
- Open Hardware
- Open-Source
- Processor
- RISC-V
- Simulator
website: https://riscv.org/
---
