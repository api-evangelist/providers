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
  url: security/red-beacon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.redbeacon.com
created: '2026-07-17'
description: Redbeacon was a consumer home-services marketplace that connected homeowners with local service professionals — for home repair, cleaning, landscaping, handyman and similar jobs — letting people describe a job and receive quotes from vetted local pros. The company was an early venture-backed startup (with Mayfield among its investors) and was acquired by The Home Depot in 2012. The standalone Redbeacon consumer service was subsequently wound down. As of this enrichment pass the redbeacon.com domain still resolves (Cloudflare DNS, Google Workspace email) but serves no live website (origin returns HTTP 525 / 400) and publishes no developer portal, API documentation, or machine-readable API surface. This profile is retained as a historical/portfolio-graph node.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/red-beacon.png
layout: provider
modified: '2026-07-21'
name: Red Beacon
nav: Providers
network: true
overview: Red Beacon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Services, Marketplace, Local Services, and Consumer.
random_paper: 16
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
security:
- kind: domain-security
  name: Red Beacon Domain Security
  slug: red-beacon-domain-security
  summary_line: TLSv1.3
slug: red-beacon
tags:
- Company
- Home Services
- Marketplace
- Local Services
- Consumer
- Acquired
- Defunct
website: https://www.redbeacon.com
---
