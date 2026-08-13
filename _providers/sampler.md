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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sampler-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sampler.io
coverage:
  checked: '2026-08-12'
  detail: Sampler (The Sampler App Inc., Toronto) filed for bankruptcy on 2024-06-27 and ceased operations, and its estate is now fully decommissioned — sampler.io and www.sampler.io terminate the TLS handshake with an internal-error alert before any HTTP request is sent (reproduced from three independent SSL stacks), api.sampler.io still resolves to three stale AWS EC2 addresses that refuse every connection on tcp/80 and tcp/443, and docs./developers./app.sampler.io are NXDOMAIN, so there is no surface left to profile.
  evidence:
  - status: 0
    url: https://sampler.io/
  - status: 0
    url: https://www.sampler.io/
  - status: 0
    url: https://api.sampler.io/openapi.json
  - status: 301
    url: http://sampler.io/
  - status: 404
    url: https://www.sampler.io/.well-known/security.txt
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Sampler (The Sampler App Inc., Toronto) was a digital product-sampling platform used by consumer packaged goods (CPG) and retail brands to run targeted sample-distribution campaigns, collect first-party consumer data and reviews, and measure the impact of sampling on purchase behavior. Founded in 2013, it acquired Abeo and AdMass in 2023 and served brands including Procter & Gamble, Unilever, L''Oreal, Nestle and PepsiCo. THE COMPANY IS DEFUNCT: it filed for bankruptcy on 2024-06-27 with CAD 12.9M in liabilities against roughly CAD 300K in assets, and ceased operations. As of 2026-08-12 the entire estate is decommissioned — sampler.io and www.sampler.io fail the TLS handshake outright, api.sampler.io retains stale DNS records whose hosts refuse all connections, and every documentation or developer subdomain is NXDOMAIN. Sampler never published a public developer API, developer portal, documentation host, OpenAPI, or machine discovery surface; the api.sampler.io/v1/ endpoints
  visible in archived crawls were the private backend of its consumer claim widget and admin console, not a documented developer product.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sampler.png
layout: provider
modified: '2026-08-12'
name: Sampler
nav: Providers
network: true
overview: Sampler is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Product Sampling, Consumer Packaged Goods, and Advertising.
random_paper: 36
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
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Sampler Domain Security
  slug: sampler-domain-security
  summary_line: DMARC
slug: sampler
tags:
- Company
- Marketing
- Product Sampling
- Consumer Packaged Goods
- Advertising
- SaaS
- Defunct
- Retail
website: https://sampler.io
---
