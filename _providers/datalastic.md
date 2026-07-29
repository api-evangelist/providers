---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Datalastic Agentic Access
  operation_count: 12
  slug: datalastic-agentic-access
  summary_line: 12 operations · 1 acting
api_count: 6
apis:
- description: Past AIS positions for vessels and zones.
  name: Datalastic Historical API
  slug: datalastic-historical-api
- description: Real-time AIS vessel position and voyage data.
  name: Datalastic Live Tracking API
  slug: datalastic-live-tracking-api
- description: Global maritime port search.
  name: Datalastic Ports API
  slug: datalastic-ports-api
- description: Asynchronous bulk report jobs and account usage statistics.
  name: Datalastic Reports and Usage API
  slug: datalastic-reports-and-usage-api
- description: Static ship specifications and vessel search.
  name: Datalastic Vessel Data API
  slug: datalastic-vessel-data-api
- description: Vessels within a radius of a point, port, or moving vessel.
  name: Datalastic Zone Traffic API
  slug: datalastic-zone-traffic-api
artifact_total: 13
collections:
- collection_type: open
  name: Datalastic Maritime API
  slug: open-datalastic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/datalastic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datalastic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datalastic-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datalastic/
- group: company
  title: ''
  type: Website
  url: https://datalastic.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datalastic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://datalastic.com/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://datalastic.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/datalastic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datalastic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datalastic-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://datalastic.com/blog/
created: '2026-07-11'
description: Datalastic is a maritime data API providing real-time AIS vessel tracking, historical ship movements, vessel specifications, and global port data over a simple REST interface. A database of 750,000+ ships is queryable by MMSI, IMO, or UUID for live position, speed, course, heading, destination, and ETA, plus zone traffic monitoring around any coordinate or port, up to 31 days of historical track per request, vessel and port finder search, and asynchronous bulk reports. Access is subscription-based with a monthly credit model and api-key authentication.
finops:
- name: Datalastic Finops
  service_category: Maritime Data and Vessel Tracking
  slug: datalastic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datalastic.png
layout: provider
modified: '2026-07-11'
name: Datalastic
nav: Providers
network: true
overview: 'Datalastic publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Historical API, Live Tracking API, Ports API, and 3 more. Tagged areas include Vessel Tracking, Maritime, AIS, Ships, and Ports.


  Datalastic''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Datalastic Plans Pricing
  plan_count: 6
  slug: datalastic-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 7
  name: Datalastic Rate Limits
  slug: datalastic-rate-limits
score:
  band: developing
  composite: 42.2
  delta: -2.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.2
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datalastic/refs/heads/main/screenshots/datalastic-2026-07-25T211330.png
security:
- kind: authentication
  name: Datalastic Authentication
  slug: datalastic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Datalastic Domain Security
  slug: datalastic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datalastic
tags:
- Vessel Tracking
- Maritime
- AIS
- Ships
- Ports
- Shipping
website: https://datalastic.com
---
