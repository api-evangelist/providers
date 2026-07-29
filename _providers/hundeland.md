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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hundeland-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.hundeland.de
created: '2026-07-17'
description: Hundeland was a German direct-to-consumer online shop for dog supplies — dog food, treats, accessories, and pet-care products — and a portfolio company of the Point Nine venture capital firm. The hundeland.de storefront has been permanently closed ("dauerhaft geschlossen") and now 302-redirects to Pets Premium (petspremium.de), operated by the same company, which carries the same brands and product range; former customers must re-register there. Hundeland publishes no public API, developer portal, documentation, or SDKs, so the enrichment pipeline found no API surface to harvest. This record is retained as a Point Nine portfolio lead with the real closure status captured; the only machine-verifiable artifact is the domain-security probe of the still-resolving hundeland.de host that serves the redirect.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hundeland.png
layout: provider
modified: '2026-07-19'
name: Hundeland
nav: Providers
network: true
overview: Hundeland is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pets, Dogs, Pet Supplies, and Ecommerce.
random_paper: 78
score:
  band: minimal
  composite: 5.0
  delta: -1.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hundeland/refs/heads/main/screenshots/hundeland-2026-07-25T221729.png
security:
- kind: domain-security
  name: Hundeland Domain Security
  slug: hundeland-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hundeland
tags:
- Company
- Pets
- Dogs
- Pet Supplies
- Ecommerce
- Retail
- Germany
- Closed
website: http://www.hundeland.de
---
