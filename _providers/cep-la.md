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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Brazil RESTful API to find information about streets, zip codes, neighborhoods, cities and states
  name: Cep.la
  slug: cepla
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cep-la-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://cep.la/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Brazil RESTful API to find information about streets, zip codes, neighborhoods, cities and states
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cep-la.png
layout: provider
modified: '2026-05-28'
name: Cep.la
nav: Providers
network: true
overview: Cep.la publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.
random_paper: 9
score:
  band: minimal
  composite: 5.7
  delta: -1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cep-la/refs/heads/main/screenshots/cep-la-2026-06-20T174132.png
security:
- kind: domain-security
  name: Cep La Domain Security
  slug: cep-la-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cep-la
tags:
- Geocoding
- Public APIs
website: http://cep.la/
---
