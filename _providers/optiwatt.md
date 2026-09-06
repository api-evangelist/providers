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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optiwatt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://optiwatt.com/
- group: other
  title: ''
  type: ConsumerApp
  url: https://getoptiwatt.com/
- group: start
  title: ''
  type: SignUp
  url: https://optiwatt.com/login
- group: start
  title: ''
  type: Login
  url: https://optiwatt.com/login
- group: operate
  title: ''
  type: Support
  url: https://optiwatt.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optiwatt.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optiwatt.com/tos
created: '2026-07-17'
description: Optiwatt is a consumer-centric energy management platform that helps electric-vehicle drivers and homeowners lower their electricity bills by automatically scheduling EV charging and smart-thermostat use for off-peak, low-cost, and low-carbon hours. Its consumer app (getoptiwatt.com) connects to vehicles, chargers, and thermostats via direct OEM integrations such as the Tesla Fleet API and aggregators like Smartcar, while its utility platform (optiwatt.com) orchestrates these distributed energy resources as virtual power plants across demand-response and load-shaping programs for utility partners. Backed by GV. Optiwatt is primarily a consumer of third-party APIs rather than a public API producer; no public developer API or OpenAPI has been found.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optiwatt.png
layout: provider
modified: '2026-07-20'
name: Optiwatt
nav: Providers
network: true
overview: 'Optiwatt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Energy, Energy Management, and Electric Vehicles.


  Optiwatt''s developer surface includes signup flow, support, and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optiwatt/refs/heads/main/screenshots/optiwatt-2026-08-07T190814.png
security:
- kind: domain-security
  name: Optiwatt Domain Security
  slug: optiwatt-domain-security
  summary_line: TLSv1.3 · DMARC
slug: optiwatt
tags:
- Company
- Frontier Tech
- Energy
- Energy Management
- Electric Vehicles
- EV Charging
- Smart Home
- DERMS
- Demand Response
- Utilities
- Virtual Power Plant
website: https://optiwatt.com/
---
