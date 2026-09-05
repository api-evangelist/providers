---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.getredcap.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.servicesuite.solera.com/ — a different registrable domain (getredcap.com -> solera.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/solera/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redcap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getredcap.com
- group: company
  title: ''
  type: Website
  url: https://www.servicesuite.solera.com/
created: '2026-07-17'
description: RedCap is an automotive dealer service software company that built an on-demand vehicle pickup-and-delivery, loaner, and shuttle platform for dealership fixed-operations (service) departments — offering live vehicle tracking, automated dispatching, at-home loaner contracting, on-demand parts fulfillment, and Uber-integrated shuttle coordination that plug into a dealership's existing DMS and service tools. Backed by Uncork Capital, RedCap was acquired by Solera and is now operated as Solera Service Suite; its former site (getredcap.com) redirects to the Solera Service Suite product. RedCap does not publish a public developer API, OpenAPI, or developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/redcap.png
layout: provider
modified: '2026-07-21'
name: RedCap
nav: Providers
network: true
overview: RedCap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Dealership, Service, and Fixed Operations.
random_paper: 14
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
screenshot: https://raw.githubusercontent.com/api-evangelist/redcap/refs/heads/main/screenshots/redcap-2026-09-02T153135.png
security:
- kind: domain-security
  name: Redcap Domain Security
  slug: redcap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: redcap
tags:
- Company
- Automotive
- Dealership
- Service
- Fixed Operations
- Pickup and Delivery
- Logistics
website: https://www.getredcap.com
---
