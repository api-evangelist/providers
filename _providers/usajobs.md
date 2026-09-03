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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: US government job board
  name: USAJOBS
  slug: usajobs
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usajobs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.usajobs.gov/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: US government job board
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usajobs.png
layout: provider
modified: '2026-05-28'
name: USAJOBS
nav: Providers
network: true
overview: USAJOBS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Job and Public APIs.
random_paper: 3
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 7.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usajobs/refs/heads/main/screenshots/usajobs-2026-06-20T200640.png
security:
- kind: domain-security
  name: Usajobs Domain Security
  slug: usajobs-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: usajobs
tags:
- Job
- Public APIs
website: https://developer.usajobs.gov/
---
