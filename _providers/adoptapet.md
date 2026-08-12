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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Resource to help get pets adopted
  name: AdoptAPet
  slug: adoptapet
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adoptapet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adoptapet.com/public/apis/pet_list.html
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Resource to help get pets adopted
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adoptapet.png
layout: provider
modified: '2026-05-28'
name: AdoptAPet
nav: Providers
network: true
overview: AdoptAPet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Animals and Public APIs.
random_paper: 34
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
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Adoptapet Domain Security
  slug: adoptapet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adoptapet
tags:
- Animals
- Public APIs
website: https://www.adoptapet.com/public/apis/pet_list.html
---
