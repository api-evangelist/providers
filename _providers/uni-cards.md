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
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uni-cards-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uni-cards-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.uni.cards/
created: '2026-07-17'
description: Uni Cards (Uniorbit Technologies) is a Bangalore-based Indian consumer fintech backed by Accel that builds credit-card and pay-later products, best known for its Uni Pay 1/3rd Card and co-branded credit cards delivered through its consumer mobile app. Uni Cards publishes no public developer portal, API documentation, or SDKs; its api.uni.cards and docs.uni.cards hosts resolve but are closed behind a Cloudflare challenge, so its API surface is internal-only today.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uni-cards.png
layout: provider
modified: '2026-07-21'
name: Uni Cards
nav: Providers
network: true
overview: Uni Cards is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Credit Cards, Payments, and Consumer Finance.
random_paper: 8
score:
  band: minimal
  composite: 6.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Uni Cards Domain Security
  slug: uni-cards-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: uni-cards
tags:
- Company
- Fintech
- Credit Cards
- Payments
- Consumer Finance
- India
website: https://www.uni.cards/
---
