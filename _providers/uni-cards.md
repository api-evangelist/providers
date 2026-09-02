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
  scored_at: '2026-09-01'
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
random_paper: 20
score:
  band: minimal
  composite: 2.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 2.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
