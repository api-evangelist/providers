---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/amd/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xilinx-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Xilinx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xilinx
- group: company
  title: ''
  type: Website
  url: https://www.xilinx.com
- group: other
  title: ''
  type: Protobuf
  url: grpc/xilinx-pynq-remote-device.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/xilinx-pynq-mmio.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/xilinx-pynq-gpio.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/xilinx-pynq-buffer.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/xilinx-pynq-xrfdc.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/xilinx-pynq-xrfclk.proto
- group: build
  title: ''
  type: Packages
  url: packages/xilinx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/xilinx-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/xilinx-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/xilinx-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xilinx-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/xilinx-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/xilinx-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xilinx-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/xilinx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xilinx-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amd.com/
- group: start
  title: ''
  type: Portal
  url: https://www.amd.com/en/developer.html
- group: start
  title: ''
  type: GettingStarted
  url: https://pynq.readthedocs.io/en/latest/getting_started.html
- group: operate
  title: ''
  type: Support
  url: https://adaptivesupport.amd.com/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amd.com/en/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amd.com/en/legal/privacy.html
created: '2026-04-07'
description: 'Xilinx was an American semiconductor company that invented the FPGA and built the Zynq SoC, Versal adaptive SoC and Alveo accelerator lines together with the Vivado and Vitis design toolchains, before AMD closed its $50B all-stock acquisition in February 2022. The brand no longer runs its own web properties — every xilinx.com path now redirects into amd.com — but github.com/Xilinx remains an active, verified organization of 469 public repositories, and it is the only place Xilinx still publishes machine-readable contracts: the proto3 gRPC services behind the PYNQ remote-device protocol, plus first-party Python packages for PYNQ, Brevitas, FINN, RapidWright and the XRT runtime. There is no Xilinx HTTP or REST API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xilinx.png
layout: provider
modified: '2026-09-04'
name: Xilinx
nav: Providers
network: true
overview: 'Xilinx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Semiconductors, FPGA, Programmable Logic, and Adaptive Computing.


  Xilinx''s developer surface includes CLI, changelog, documentation, developer portal, getting-started guide, support, and 21 more developer resources.'
plans:
- name: Xilinx Plans Pricing
  plan_count: 0
  slug: xilinx-plans-pricing
press:
- date: '2026-05-25'
  title: An Edge Computing System with AMD Xilinx FPGA AI ... - PMC
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11125175/
- date: '2026-05-25'
  title: Xilinx Technology to Power Baidu Brain Edge AI Applications
  url: https://www.prnewswire.com/news-releases/xilinx-technology-to-power-baidu-brain-edge-ai-applications-300779615.html
- date: '2026-05-25'
  title: Unleashing Edge Intelligence on XILINX FPGA through ...
  url: https://www.iwavesystems.com/news/unleashing-edge-intelligence-on-xilinx-fpga-through-corazon-ai/
- date: '2026-05-25'
  title: AMD Completes $50B Acquisition of Xilinx
  url: https://www.engineering.com/amd-completes-50b-acquisition-of-xilinx/
- date: '2026-05-25'
  title: AI Engine Technology
  url: https://www.amd.com/en/products/adaptive-socs-and-fpgas/technologies/ai-engine.html
random_paper: 17
rate_limits:
- limit_count: 0
  name: Xilinx Rate Limits
  slug: xilinx-rate-limits
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 50.0
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 2.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/xilinx/refs/heads/main/screenshots/xilinx-2026-06-20T201706.png
security:
- kind: domain-security
  name: Xilinx Domain Security
  slug: xilinx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xilinx
tags:
- Fortune 1000
- Semiconductors
- FPGA
- Programmable Logic
- Adaptive Computing
- Hardware Acceleration
- Embedded Systems
- Machine Learning
- gRPC
- Open Source
website: https://www.xilinx.com
---
