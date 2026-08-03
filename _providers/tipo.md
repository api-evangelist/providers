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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Taiwan patent search system api
  name: TIPO
  slug: tipo
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tipo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tiponet.tipo.gov.tw/Gazette/OpenData/OD/OD05.aspx?QryDS=API00
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Taiwan patent search system api
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tipo.png
layout: provider
modified: '2026-05-28'
name: TIPO
nav: Providers
network: true
overview: TIPO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Patent and Public APIs.
random_paper: 64
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tipo/refs/heads/main/screenshots/tipo-2026-06-20T195417.png
security:
- kind: domain-security
  name: Tipo Domain Security
  slug: tipo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tipo
tags:
- Patent
- Public APIs
website: https://tiponet.tipo.gov.tw/Gazette/OpenData/OD/OD05.aspx?QryDS=API00
---
