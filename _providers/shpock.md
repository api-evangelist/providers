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
  url: security/shpock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shpock.com/en-gb
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.shpock.com/
created: '2026-07-17'
description: Shpock is a mobile-first second-hand marketplace and classifieds platform that brings millions of private buyers and sellers together, primarily across the United Kingdom, Austria, and Germany. Users list, discover, and negotiate on pre-owned goods across categories including electronics, fashion, home and garden, vehicles, and property, alongside a Shpock+ for Professionals program for business sellers. Founded in Vienna and backed by Speedinvest, Shpock operates consumer iOS/Android apps and a web experience. As of this enrichment pass Shpock publishes no public developer API, developer portal, or SDKs; the api.shpock.com host exists but is private (returns 401 to unauthenticated requests). This profile therefore captures company identity and probed domain security rather than an API contract.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shpock.png
layout: provider
modified: '2026-07-21'
name: Shpock
nav: Providers
network: true
overview: Shpock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Classifieds, Marketplace, Second-hand, and E-commerce.
random_paper: 16
score:
  band: minimal
  composite: 5.9
  delta: -1.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Shpock Domain Security
  slug: shpock-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: shpock
tags:
- Company
- Classifieds
- Marketplace
- Second-hand
- E-commerce
- Consumer
- Mobile App
website: https://www.shpock.com/en-gb
---
