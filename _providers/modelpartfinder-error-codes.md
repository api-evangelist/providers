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
api_count: 1
apis:
- description: Lookup appliance and equipment error codes by brand and code, with recommended replacement parts
  name: ModelPartFinder Error Codes
  slug: modelpartfinder-error-codes
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modelpartfinder-error-codes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://modelpartfinder.com/docs/api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Lookup appliance and equipment error codes by brand and code, with recommended replacement parts
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/modelpartfinder-error-codes.png
layout: provider
modified: '2026-05-28'
name: ModelPartFinder Error Codes
nav: Providers
network: true
overview: ModelPartFinder Error Codes publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.
random_paper: 19
score:
  band: minimal
  composite: 6.1
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
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modelpartfinder-error-codes/refs/heads/main/screenshots/modelpartfinder-error-codes-2026-06-20T185648.png
security:
- kind: domain-security
  name: Modelpartfinder Error Codes Domain Security
  slug: modelpartfinder-error-codes-domain-security
  summary_line: TLSv1.3 · DMARC
slug: modelpartfinder-error-codes
tags:
- Open Data
- Public APIs
website: https://modelpartfinder.com/docs/api
---
