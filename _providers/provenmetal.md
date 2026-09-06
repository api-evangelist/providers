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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/provenmetal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://provenmetal.com/security
- group: company
  title: ''
  type: Website
  url: https://provenmetal.com
- group: start
  title: ''
  type: Portal
  url: https://order.provenmetal.com
- group: start
  title: ''
  type: SignUp
  url: https://order.provenmetal.com/signup
- group: start
  title: ''
  type: Login
  url: https://order.provenmetal.com/login
- group: operate
  title: ''
  type: Support
  url: mailto:orders@provenmetal.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/provenmetal-domain-security.yml
created: '2026-07-17'
description: ProvenMetal is a Y Combinator (Summer 2026) startup building fast-turn, American-made printed circuit board (PCB) assembly. The company lets customers upload a Gerber file, automatically infers the board specification, and returns instant quoting for a 7-day standard turnaround with no expedite fees. ProvenMetal automates the traditional manufacturing bottlenecks — part procurement, design for manufacturability (DFM) review, and assembly — and performs 100% X-ray inspection of every board (AI-assisted, cited at 99.8% confidence) before shipment, including the inspection data with each order. It is a domestic B2B PCB manufacturing service aimed at reshoring electronics production, operated out of San Francisco. As of this profile ProvenMetal exposes a customer ordering portal at order.provenmetal.com but publishes no public developer API, SDKs, or technical documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/provenmetal.png
layout: provider
modified: '2026-07-20'
name: Provenmetal
nav: Providers
network: true
overview: 'Provenmetal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PCB, Printed Circuit Boards, Electronics Manufacturing, and Hardware.


  Provenmetal''s developer surface includes developer portal, signup flow, support, and 5 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/provenmetal/refs/heads/main/screenshots/provenmetal-2026-09-02T152236.png
security:
- kind: domain-security
  name: Provenmetal Domain Security
  slug: provenmetal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Provenmetal Vulnerability Disclosure
  slug: provenmetal-vulnerability-disclosure
  summary_line: disclosure policy published
slug: provenmetal
tags:
- Company
- PCB
- Printed Circuit Boards
- Electronics Manufacturing
- Hardware
- Contract Manufacturing
- Reshoring
- Y Combinator
website: https://provenmetal.com
---
