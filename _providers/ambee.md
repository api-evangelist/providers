---
access_model:
  confidence: high
  label: Enterprise (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
- acting_count: 0
  human_in_the_loop: 0
  name: Ambee Agentic Access
  operation_count: 19
  slug: ambee-agentic-access
  summary_line: 19 operations
api_count: 6
apis:
- description: The Air Quality API from Ambee — 5 operation(s) for air quality.
  name: Ambee Air Quality API
  slug: ambee-air-quality-api
- description: The Fire API from Ambee — 2 operation(s) for fire.
  name: Ambee Fire API
  slug: ambee-fire-api
- description: The NDVI API from Ambee — 2 operation(s) for ndvi.
  name: Ambee NDVI API
  slug: ambee-ndvi-api
- description: The Pollen API from Ambee — 5 operation(s) for pollen.
  name: Ambee Pollen API
  slug: ambee-pollen-api
- description: The Soil API from Ambee — 2 operation(s) for soil.
  name: Ambee Soil API
  slug: ambee-soil-api
- description: The Weather API from Ambee — 3 operation(s) for weather.
  name: Ambee Weather API
  slug: ambee-weather-api
artifact_total: 13
collections:
- collection_type: open
  name: Ambee API
  slug: open-ambee
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ambee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ambee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ambee-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.getambee.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ambeedata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getambee
- group: company
  title: ''
  type: Website
  url: https://www.getambee.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ambeedata.com
- group: commercial
  title: ''
  type: Plans
  url: plans/ambee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ambee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ambee-finops.yml
created: '2026-06-21'
description: Ambee is an environmental-intelligence company that aggregates satellite, sensor, and ground-station data into a unified REST API. The Ambee API delivers hyperlocal air quality, pollen, weather, wildfire, soil, and NDVI/vegetation data worldwide via simple lat/lng, postal-code, and place lookups secured with an x-api-key header.
finops:
- name: Ambee Finops
  service_category: Analytics and Data
  slug: ambee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ambee.png
layout: provider
modified: '2026-06-21'
name: Ambee
nav: Providers
network: true
overview: 'Ambee publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Air Quality API, Fire API, NDVI API, and 3 more. Tagged areas include Environmental Intelligence, Air Quality, Weather, Pollen, and Geospatial.


  Ambee''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Ambee Plans Pricing
  plan_count: 2
  slug: ambee-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Ambee Rate Limits
  slug: ambee-rate-limits
score:
  band: thin
  composite: 36.1
  delta: -3.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.1
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
screenshot: https://raw.githubusercontent.com/api-evangelist/ambee/refs/heads/main/screenshots/ambee-2026-07-25T200014.png
security:
- kind: authentication
  name: Ambee Authentication
  slug: ambee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ambee Domain Security
  slug: ambee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ambee
tags:
- Environmental Intelligence
- Air Quality
- Weather
- Pollen
- Geospatial
website: https://www.getambee.com
---
