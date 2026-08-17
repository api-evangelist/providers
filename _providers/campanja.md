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
  url: security/campanja-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://campanja.com
coverage:
  checked: '2026-08-12'
  detail: Campanja was acquired by [24]7.ai in August 2015 and fully absorbed; campanja.com is now a mail-only registered domain with no A or AAAA record, so it does not resolve over HTTPS at all, and its one surviving subdomain (docs.campanja.com) is a dangling Google CNAME that 404s on every path.
  evidence:
  - note: 'curl (6) Could not resolve host: campanja.com — no A/AAAA record'
    status: 0
    url: https://campanja.com/
  - note: DNS resolution failure, no request sent
    status: 0
    url: https://campanja.com/.well-known/security.txt
  - note: dangling legacy CNAME to ghs.google.com; Google 404 page on every path
    status: 404
    url: http://docs.campanja.com/
  - status: 404
    url: http://docs.campanja.com/openapi.json
  - note: 0 results — no first-party packages on npm, PyPI, RubyGems, crates.io or Packagist
    status: 200
    url: https://registry.npmjs.org/-/v1/search?text=campanja
  reason: defunct
  state: none
created: '2026-07-17'
description: Campanja was a Stockholm-based advertising-technology company founded in 2010 that built a high-frequency paid-search bid-optimization engine. Its platform placed millions of automated bids per day across Google AdWords, Google Shopping, and Yahoo/Bing search campaigns, using real-time tracking and predictive big-data modeling to improve return on ad spend for large online advertisers while cutting media cost. Campanja raised a $5M Series A (Hoxton Ventures, DFJ Esprit) and was acquired by [24]7.ai in 2015, where its technology was folded into the [24]7 Customer Acquisition Cloud. The independent company is effectively defunct and campanja.com no longer resolves to a live site. This profile was surfaced as a 500 Global portfolio lead and processed by the API Evangelist enrichment pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/campanja.png
layout: provider
modified: '2026-08-12'
name: Campanja
nav: Providers
network: true
overview: Campanja is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Search Advertising, and Bid Management.
random_paper: 82
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Campanja Domain Security
  slug: campanja-domain-security
  summary_line: no transport/DNS hardening detected
slug: campanja
tags:
- Company
- Advertising
- AdTech
- Search Advertising
- Bid Management
- Marketing Technology
- PPC
website: https://campanja.com
---
