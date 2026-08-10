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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Malware execution and analysis
  name: CAPEsandbox
  slug: capesandbox
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capesandbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capev2.readthedocs.io/en/latest/usage/api.html
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Malware execution and analysis
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/capesandbox.png
layout: provider
modified: '2026-05-28'
name: CAPEsandbox
nav: Providers
network: true
overview: CAPEsandbox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anti Malware and Public APIs.
random_paper: 0
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
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/capesandbox/refs/heads/main/screenshots/capesandbox-2026-06-20T173934.png
security:
- kind: domain-security
  name: Capesandbox Domain Security
  slug: capesandbox-domain-security
  summary_line: TLSv1.3 · HSTS
slug: capesandbox
tags:
- Anti Malware
- Public APIs
website: https://capev2.readthedocs.io/en/latest/usage/api.html
---
