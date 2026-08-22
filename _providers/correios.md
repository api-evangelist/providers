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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Integration to provide information and prepare shipments using Correio's services
  name: Correios
  slug: correios
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/correios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cws.correios.com.br/ajuda
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Integration to provide information and prepare shipments using Correio's services
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/correios.png
layout: provider
modified: '2026-05-28'
name: Correios
nav: Providers
network: true
overview: Correios publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Tracking and Public APIs.
random_paper: 9
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/correios/refs/heads/main/screenshots/correios-2026-06-20T175039.png
security:
- kind: domain-security
  name: Correios Domain Security
  slug: correios-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: correios
tags:
- Tracking
- Public APIs
website: https://cws.correios.com.br/ajuda
---
