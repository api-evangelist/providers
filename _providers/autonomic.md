---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://autonomic.ai'', ''status'': 302, ''note'': ''declared website redirects to https://www.ford.com/ — a different registrable domain (autonomic.ai -> ford.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
api_count: 1
apis:
- description: The Transportation Mobility Cloud (TMC) is Autonomic's API-driven connected-vehicle cloud platform, letting developers build applications that interact with vehicles across different models and connec
  name: Transportation Mobility Cloud
  slug: transportation-mobility-cloud
artifact_total: 2
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ford-motor/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autonomic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autonomic.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.autonomic.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ford.com/help/privacy/
created: '2026-07-17'
description: Autonomic is a connected-vehicle cloud company founded in 2016, acquired by Ford Motor Company in 2018 and fully integrated into Ford in 2023. Its flagship product, the Transportation Mobility Cloud (TMC), is one of the largest connected-vehicle cloud platforms in production, providing an API-driven platform for developers to build applications that interact with vehicles while abstracting the complexity of different vehicle models and connectivity devices. The public developer surface (the TMC Developer Portal) is gated behind partner authentication, so most technical artifacts are not publicly harvestable. This profile was surfaced as a portfolio company of Craft Ventures and added to the API Evangelist network for enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autonomic.png
layout: provider
modified: '2026-07-18'
name: Autonomic
nav: Providers
network: true
overview: Autonomic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Automotive, Connected Vehicles, and Mobility.
random_paper: 9
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autonomic/refs/heads/main/screenshots/autonomic-2026-07-25T201842.png
security:
- kind: domain-security
  name: Autonomic Domain Security
  slug: autonomic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: autonomic
tags:
- Company
- Infrastructure
- Automotive
- Connected Vehicles
- Mobility
- Cloud
- IoT
website: https://autonomic.ai
---
