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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Sinay Agentic Access
  operation_count: 14
  slug: sinay-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 6
apis:
- description: Per-voyage CO2 emission computation using vessel-model and GLEC tradelane methods.
  name: Sinay CO2 Emission API
  slug: sinay-co2-emission-api
- description: Estimated time of arrival prediction for a vessel to a destination port.
  name: Sinay ETA API
  slug: sinay-eta-api
- description: Meteorological and oceanographic conditions for an area and time.
  name: Sinay Metocean API
  slug: sinay-metocean-api
- description: Aggregated live port congestion data.
  name: Sinay Port Congestion API
  slug: sinay-port-congestion-api
- description: Vessel and port lookup from combined satellite and terrestrial AIS.
  name: Sinay Ports and Vessels API
  slug: sinay-ports-and-vessels-api
- description: Monthly API usage and credit-consumption reporting.
  name: Sinay Usage API
  slug: sinay-usage-api
artifact_total: 13
collections:
- collection_type: open
  name: Sinay Maritime APIs
  slug: open-sinay
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sinay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sinay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sinay-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sinay.ai
- group: docs
  title: ''
  type: Documentation
  url: https://help.sinay.ai/sinay-apis
- group: start
  title: ''
  type: SignUp
  url: https://developers.sinay.ai/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sinay
- group: commercial
  title: ''
  type: Plans
  url: plans/sinay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sinay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sinay-finops.yml
created: '2026-07-12'
description: Sinay is a maritime data and analytics company whose Developers Platform exposes a marketplace of REST APIs for the shipping and ocean-tech industry - vessel and port lookup from combined satellite and terrestrial AIS, metocean (weather and ocean) conditions, per-voyage CO2 emissions modeled on the GLEC Framework, ETA prediction, live port congestion, sailing schedules, and underwater noise. Every API is called over HTTPS at api.sinay.ai, authenticated with a single API_KEY header, and metered as monthly API units / credits with a free developer key to start.
finops:
- name: Sinay Finops
  service_category: Maritime Data and Analytics
  slug: sinay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sinay.png
layout: provider
modified: '2026-07-12'
name: Sinay
nav: Providers
network: true
overview: 'Sinay publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CO2 Emission API, ETA API, Metocean API, and 3 more. Tagged areas include Vessel Tracking, AIS, Maritime, Maritime Data, and Weather.


  Sinay''s developer surface includes authentication, documentation, signup flow, and 7 more developer resources.'
plans:
- name: Sinay Plans Pricing
  plan_count: 4
  slug: sinay-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 3
  name: Sinay Rate Limits
  slug: sinay-rate-limits
score:
  band: thin
  composite: 40.9
  delta: -2.3
  facets:
    commercial_clarity: 52.6
    contract_quality: 59.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 43.2
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
security:
- kind: authentication
  name: Sinay Authentication
  slug: sinay-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sinay Domain Security
  slug: sinay-domain-security
  summary_line: TLSv1.3 · HSTS
slug: sinay
tags:
- Vessel Tracking
- AIS
- Maritime
- Maritime Data
- Weather
- CO2 Emissions
- Port Congestion
- Ship Tracking
- ETA
- Ocean Data
website: https://sinay.ai
---
