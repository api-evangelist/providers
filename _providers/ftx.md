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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Complete REST, websocket, and FTX APIs to suit your algorithmic trading needs
  name: FTX
  slug: ftx
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ftx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.ftx.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Complete REST, websocket, and FTX APIs to suit your algorithmic trading needs
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ftx.png
layout: provider
modified: '2026-05-28'
name: FTX
nav: Providers
network: true
overview: FTX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency and Public APIs.
random_paper: 2
score:
  band: minimal
  composite: 7.6
  delta: 1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ftx/refs/heads/main/screenshots/ftx-2026-06-20T181602.png
security:
- kind: domain-security
  name: Ftx Domain Security
  slug: ftx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ftx
tags:
- Cryptocurrency
- Public APIs
website: https://docs.ftx.com/
---
