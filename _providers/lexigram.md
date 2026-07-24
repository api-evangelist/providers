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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: NLP that extracts mentions of clinical concepts from text, gives access to clinical ontology
  name: Lexigram
  slug: lexigram
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lexigram-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.lexigram.io/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: NLP that extracts mentions of clinical concepts from text, gives access to clinical ontology
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lexigram.png
layout: provider
modified: '2026-05-28'
name: Lexigram
nav: Providers
network: true
overview: Lexigram publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 41
score:
  band: minimal
  composite: 7.7
  delta: 0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lexigram/refs/heads/main/screenshots/lexigram-2026-06-20T184442.png
security:
- kind: domain-security
  name: Lexigram Domain Security
  slug: lexigram-domain-security
  summary_line: TLSv1.3 · HSTS
slug: lexigram
tags:
- Health
- Public APIs
website: https://docs.lexigram.io/
---
