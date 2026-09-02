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
overview: Shpock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Classifieds, Marketplace, Secondhand, and E-Commerce.
random_paper: 18
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Secondhand
- E-Commerce
- Consumer
- Mobile App
website: https://www.shpock.com/en-gb
---
