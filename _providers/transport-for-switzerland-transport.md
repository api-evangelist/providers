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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Swiss public transport API
  name: Transport for Switzerland
  slug: transport-for-switzerland
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transport-for-switzerland-transport-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://transport.opendata.ch/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Swiss public transport API
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transport-for-switzerland-transport.png
layout: provider
modified: '2026-05-28'
name: Transport for Switzerland
nav: Providers
network: true
overview: Transport for Switzerland publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Transportation and Public APIs.
random_paper: 4
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transport-for-switzerland-transport/refs/heads/main/screenshots/transport-for-switzerland-transport-2026-06-20T195618.png
security:
- kind: domain-security
  name: Transport For Switzerland Transport Domain Security
  slug: transport-for-switzerland-transport-domain-security
  summary_line: TLSv1.3 · DMARC
slug: transport-for-switzerland-transport
tags:
- Transportation
- Public APIs
website: https://transport.opendata.ch/
---
