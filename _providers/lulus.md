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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lulus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lulus.com
created: '2026-07-17'
description: 'Lulus (Lulus Fashion Lounge Holdings) is a direct-to-consumer online fashion retailer offering women''s apparel, dresses, shoes, and accessories, operating primarily through lulus.com and mobile apps. Surfaced as a portfolio company of IVP and added to the API Evangelist network. As of this enrichment pass Lulus publishes no public developer portal, API documentation, or machine-readable API surface: developer.lulus.com does not resolve and no /.well-known/ discovery documents are served. This profile therefore captures company identity plus a live domain-security posture probe rather than any API artifacts.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lulus.png
layout: provider
modified: '2026-07-20'
name: Lulus
nav: Providers
network: true
overview: Lulus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ecommerce, Fashion, Retail, and Apparel.
random_paper: 118
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lulus/refs/heads/main/screenshots/lulus-2026-07-25T225659.png
security:
- kind: domain-security
  name: Lulus Domain Security
  slug: lulus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lulus
tags:
- Company
- Ecommerce
- Fashion
- Retail
- Apparel
- Direct To Consumer
- Online Shopping
website: https://www.lulus.com
---
