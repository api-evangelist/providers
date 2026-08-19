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
  url: security/tsm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tsm.gg/
- group: other
  title: ''
  type: Store
  url: https://tsmshop.com/
created: '2026-07-17'
description: 'TSM (Team SoloMid) is a North American esports and gaming lifestyle organization, surfaced as a portfolio company of Bessemer Venture Partners in the consumer sector. Its public web presence at tsm.gg redirects to the official TSM Store (tsmshop.com), a Shopify-hosted storefront selling TSM apparel and accessories. An enrichment pass on 2026-07-21 found no first-party developer API surface: no developer portal, no API documentation, no OpenAPI, no resolving developer/api/docs subdomains, and no real /.well-known/ discovery documents (every probed path returned the storefront catch-all page). This profile is retained as a consumer-brand lead with only domain-security signals captured.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tsm.png
layout: provider
modified: '2026-07-21'
name: TSM
nav: Providers
network: true
overview: TSM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Esports, Gaming, and Ecommerce.
random_paper: 42
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
security:
- kind: domain-security
  name: Tsm Domain Security
  slug: tsm-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tsm
tags:
- Company
- Consumer
- Esports
- Gaming
- Ecommerce
- Merchandise
- Retail
website: https://www.tsm.gg/
---
