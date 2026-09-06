---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: HailoRT is Hailo's production runtime library for the Hailo-8, Hailo-10 and Hailo-15 device families. It is a host-side, user-space C/C++ library with a Python binding (pyHailoRT), a hailortcli comman
  name: HailoRT
  slug: hailo-hailort
- description: The Hailo Media Library is the C++ media and vision stack for the Hailo-15 AI vision processor. It exposes a real gRPC contract — service MediaLibraryService, 33 RPCs including five server-streaming s
  name: Hailo Media Library Service
  slug: hailo-media-library
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hailo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hailo.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hailo.ai/developer-zone/
- group: docs
  title: ''
  type: Documentation
  url: https://hailo.ai/developer-zone/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://hailo.ai/developer-zone/documentation/hailort/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hailo-ai
- group: operate
  title: ''
  type: Support
  url: https://community.hailo.ai/
- group: company
  title: ''
  type: Blog
  url: https://hailo.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hailo.ai/terms-and-conditions/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hailo.ai/terms-and-conditions/privacy-policy/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/hailo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hailo-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hailo-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hailo-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/hailo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hailo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hailo-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hailo-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hailo-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hailo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hailo-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hailo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hailo-rate-limits.yml
created: '2026-08-22'
description: 'Hailo Technologies Ltd. is an Israeli fabless semiconductor company, headquartered in Tel Aviv with offices in the United States, Germany, Japan, Taiwan, China and South Korea, that designs AI inference accelerators (the Hailo-8, Hailo-8L and Hailo-10 families) and AI vision processors (the Hailo-15 SoC family) for edge devices. Its developer surface is not a hosted web API: it is an on-device software stack published largely on GitHub under the hailo-ai organization — HailoRT, a C/C++/Python runtime library plus the hailortcli command line tool and a PCIe kernel driver; the Hailo Model Zoo of pre-compiled HEF models; TAPPAS and hailo-apps application pipelines; and the Hailo Media Library and Hailo Imaging stacks for the Hailo-15 vision processor. The machine-readable contracts Hailo publishes are Protocol Buffers — a 33-RPC gRPC MediaLibraryService, the HailoRT hRPC and GenAI message schemes, the HEF model-file format, and a WebSocket/ZMQ analytics metadata scheme. Hailo
  also publishes a first-party Agent Skills package (hailo15-agentic-coding) of twelve skills that drive board connection, pipeline editing, model swapping, cross-compilation and deployment on the Hailo-15 SBC.'
image: https://avatars.githubusercontent.com/u/83159046?v=4
layout: provider
modified: '2026-08-22'
name: Hailo
nav: Providers
network: true
overview: 'Hailo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Machine-Learning, Semiconductors, Edge Computing, and Computer-Vision.


  Hailo''s developer surface includes documentation, API reference, support, engineering blog, CLI, changelog, authentication, and 17 more developer resources.'
plans:
- name: Hailo Plans Pricing
  plan_count: 0
  slug: hailo-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Hailo Rate Limits
  slug: hailo-rate-limits
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 66.7
    discoverability: 59.3
    governance: 4.5
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 33.1
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Hailo Authentication
  slug: hailo-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hailo Domain Security
  slug: hailo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hailo
tags:
- Artificial Intelligence
- Machine-Learning
- Semiconductors
- Edge Computing
- Computer-Vision
- Inference
- Embedded Systems
- Video Analytics
- Hardware
- Generative AI
- Protocol Buffers
- gRPC
website: https://hailo.ai/
---
