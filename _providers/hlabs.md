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
  url: security/hlabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hlaboratories.com
created: '2026-07-17'
description: Hlabs (Harrison Laboratories, Inc., operating as hlaboratories.com) is a US-based, Y Combinator-backed (Winter 2026) manufacturer of plug-and-play robotics components. The company produces a domestically-manufactured, integrated hardware ecosystem for robot builders — including the RB1 main board (powered by Nvidia Jetson), wireless communication modules, field-oriented control (FOC) boards, pancake motors, and actuators. Its stated goal is to eliminate the complexity of sourcing mismatched components from overseas and integrating them, so roboticists can focus on design rather than electronics debugging. Hlabs targets teams building medium-to-large robots such as quadrupeds, humanoids, and robot arms, and serves customers across household robotics, defense, and other robotic platforms. This is a hardware manufacturer with no public developer/API surface at the time of profiling.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hlabs.png
layout: provider
modified: '2026-07-19'
name: Hlabs
nav: Providers
network: true
overview: Hlabs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Hardware, Robots, and Electronics.
random_paper: 18
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hlabs/refs/heads/main/screenshots/hlabs-2026-07-25T221308.png
security:
- kind: domain-security
  name: Hlabs Domain Security
  slug: hlabs-domain-security
  summary_line: TLSv1.3 · HSTS
slug: hlabs
tags:
- Company
- Robotics
- Hardware
- Robots
- Electronics
- Actuators
- Motors
- Manufacturing
- Y Combinator
website: https://www.hlaboratories.com
---
