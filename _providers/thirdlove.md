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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thirdlove-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thirdlove.com
created: '2026-07-17'
description: ThirdLove is a San Francisco-based direct-to-consumer women's intimate apparel brand best known for its online Fit Finder quiz and half-cup bra sizing, selling bras, underwear, and loungewear direct to consumers through its e-commerce site. It was surfaced in the API Evangelist network as a portfolio company of a16z and Felicis. An enrichment pass on 2026-07-21 found no public developer or API surface — no developer subdomain, no documented API, no /.well-known/ discovery documents, and no security.txt or trust-center program. Only a domain-security probe of thirdlove.com yielded real data (TLS 1.3, HSTS, SPF, DMARC).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thirdlove.png
layout: provider
modified: '2026-07-21'
name: ThirdLove
nav: Providers
network: true
overview: ThirdLove is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Apparel, and Direct to Consumer.
random_paper: 11
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Thirdlove Domain Security
  slug: thirdlove-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thirdlove
tags:
- Company
- Retail
- E-Commerce
- Apparel
- Direct to Consumer
- Consumer Brand
website: https://thirdlove.com
---
