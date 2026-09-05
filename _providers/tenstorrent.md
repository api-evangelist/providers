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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tenstorrent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tenstorrent.com
- group: other
  title: ''
  type: Hardware
  url: https://tenstorrent.com/en/hardware/wormhole
- group: other
  title: ''
  type: Hardware
  url: https://tenstorrent.com/en/hardware/blackhole
- group: other
  title: ''
  type: Hardware
  url: https://tenstorrent.com/en/hardware/galaxy
- group: other
  title: ''
  type: Hardware
  url: https://tenstorrent.com/en/hardware/tt-quietbox
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tenstorrent.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tenstorrent.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tenstorrent
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tenstorrent/tt-metal
- group: other
  title: ''
  type: Compiler
  url: https://github.com/tenstorrent/tt-forge
- group: other
  title: ''
  type: Compiler
  url: https://github.com/tenstorrent/tt-mlir
- group: other
  title: ''
  type: Compiler
  url: https://github.com/tenstorrent/tt-xla
- group: other
  title: ''
  type: InferenceServer
  url: https://github.com/tenstorrent/tt-inference-server
- group: other
  title: ''
  type: Debugger
  url: https://github.com/tenstorrent/tt-exalens
- group: other
  title: ''
  type: Simulator
  url: https://github.com/tenstorrent/polaris
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/tenstorrent
- group: company
  title: ''
  type: Blog
  url: https://tenstorrent.com/en/news
- group: auth
  title: ''
  type: BountyProgram
  url: https://tenstorrent.com/en/bounties
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tenstorrent-inc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/tenstorrent
- group: other
  title: ''
  type: Email
  url: mailto:ospo@tenstorrent.com
created: '2026-05-23'
description: Tenstorrent is an AI hardware company designing Tensix and Tensix++ based AI accelerators on the open RISC-V architecture, including the Wormhole and Blackhole generations of cards, the TT-QuietBox workstation, and the Galaxy Blackhole 6U server housing 32 Blackhole chips. The company is unusual in the AI silicon space for shipping a fully open-source software stack including TT-Metal (the low-level kernel and operator library), TT-Forge (an MLIR-based compiler for PyTorch, JAX, and ONNX), TT-MLIR, TT-XLA, the TT-Inference-Server, and RISC-V cores and toolchains. Pricing is published from 999 dollars for an entry card up to 440,000 dollars for a base Galaxy supercluster. Tenstorrent does not currently offer a public hosted-inference API, so this profile catalogs hardware, SDKs, compilers, and open-source repositories rather than an HTTP API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tenstorrent.png
layout: provider
modified: '2026-05-23'
name: Tenstorrent
nav: Providers
network: true
overview: 'Tenstorrent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Hardware, RISC-V, Accelerator, Open-Source, and Compiler.


  Tenstorrent''s developer surface includes documentation, engineering blog, and 20 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tenstorrent/refs/heads/main/screenshots/tenstorrent-2026-06-20T195122.png
security:
- kind: domain-security
  name: Tenstorrent Domain Security
  slug: tenstorrent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tenstorrent
tags:
- AI Hardware
- RISC-V
- Accelerator
- Open-Source
- Compiler
- MLIR
- PyTorch
- JAX
- SDK
- Data-Center
website: https://tenstorrent.com
---
