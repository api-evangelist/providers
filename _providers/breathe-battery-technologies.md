---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: API-delivered battery simulation service for predicting performance and degradation with validated physics-based cell models, and for retrieving and designing battery cell formats. Accessed through th
  name: Breathe Simulate API
  slug: breathe-simulate-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.breathebatteries.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.breathebatteries.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.breathebatteries.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.breathebatteries.com/breathe-simulate-documentation/api_breathe_design_model/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.breathebatteries.com/breathe-simulate-documentation/
- group: start
  title: ''
  type: SignUp
  url: https://breathebatteries.com/knowledge-hub/simulate-trial/
- group: company
  title: ''
  type: Blog
  url: https://www.breathebatteries.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.breathebatteries.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.breathebatteries.com/simulation-products-license-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://breathebatteries.com/privacy-policy
- group: build
  title: ''
  type: SDKs
  url: packages/breathe-battery-technologies-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/breathe-battery-technologies-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/breathe-battery-technologies-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/breathe-battery-technologies-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/breathe-battery-technologies-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/breathe-battery-technologies-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/breathe-battery-technologies-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/breathe-battery-technologies-domain-security.yml
created: '2026-07-17'
description: Breathe Battery Technologies is a UK battery software company, spun out of Imperial College London in 2019, that builds physics-based battery simulation, cell design, and adaptive charging software for OEM and cell engineering teams. Its API-delivered products — Breathe Design (cell design), Breathe Simulate (validated performance and degradation modelling), and Breathe Charge (embedded adaptive charging, shipped in Volvo EVs) — are consumed through first-party Python client libraries (breathe-simulate, breathe-design) and MATLAB/Simulink integration, backed by a token-authenticated cloud service. The company is venture-backed (Speedinvest among its investors) and profiled in the API Evangelist network for its developer-facing, programmatically accessible battery engineering platform.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/breathe-battery-technologies.png
layout: provider
modified: '2026-07-18'
name: Breathe Battery Technologies
nav: Providers
network: true
overview: 'Breathe Battery Technologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Battery, Battery Simulation, Electric Vehicles, and Energy Storage.


  Breathe Battery Technologies'' developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, support, authentication, and 11 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 18.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/breathe-battery-technologies/refs/heads/main/screenshots/breathe-battery-technologies-2026-07-25T203734.png
security:
- kind: authentication
  name: Breathe Battery Technologies Authentication
  slug: breathe-battery-technologies-authentication
  summary_line: bearer-token · 1 scheme
- kind: domain-security
  name: Breathe Battery Technologies Domain Security
  slug: breathe-battery-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: breathe-battery-technologies
tags:
- Company
- Battery
- Battery Simulation
- Electric Vehicles
- Energy Storage
- Cell Design
- Physics-Based Modeling
- Automotive
- Deep Tech
- Developer Tools
website: https://www.breathebatteries.com/
---
