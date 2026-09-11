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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-protective-service-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fpsdhs
- group: company
  title: ''
  type: Website
  url: https://www.dhs.gov/federal-protective-service
coverage:
  checked: '2026-09-09'
  detail: The Federal Protective Service publishes no host of its own (fps.dhs.gov does not resolve) and is absent from the Department of Homeland Security developer program at https://www.dhs.gov/developer, which lists only NTAS, MyTSA and FEMA APIs; the GSA federal API inventory carries no FPS row and the DHS Project Open Data catalog (1,168 datasets) has no FPS-published dataset or API distribution.
  evidence:
  - status: 200
    url: https://www.dhs.gov/developer
  - status: 200
    url: https://www.dhs.gov/data.json
  - status: 404
    url: https://www.dhs.gov/.well-known/api-catalog
  - status: 404
    url: https://www.dhs.gov/openapi.json
  - status: 200
    url: https://raw.githubusercontent.com/GSA/federal-apis/master/inventory/federal-API-list.csv
  reason: no-developer-program
  state: none
created: '2024-12-03'
description: The Federal Protective Service uses its security expertise and law enforcement authority to protect federal government facilities and safeguard the millions of employees and visitors who pass through them every day.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-protective-service.png
layout: provider
modified: '2026-09-09'
name: Federal Protective Service
nav: Providers
network: true
overview: Federal Protective Service is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Security, Law Enforcement, Public Safety, and Physical Security.
random_paper: 13
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-protective-service/refs/heads/main/screenshots/federal-protective-service-2026-06-20T181124.png
security:
- kind: domain-security
  name: Federal Protective Service Domain Security
  slug: federal-protective-service-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-protective-service
tags:
- Federal-Government
- Security
- Law Enforcement
- Public Safety
- Physical Security
- Homeland Security
website: https://www.dhs.gov/federal-protective-service
---
