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
- acting_count: 0
  human_in_the_loop: 0
  name: Myshiptracking Agentic Access
  operation_count: 10
  slug: myshiptracking-agentic-access
  summary_line: 10 operations
api_count: 3
apis:
- description: Account details and credit balance.
  name: MyShipTracking Account API
  slug: myshiptracking-account-api
- description: Port details, port calls, and arrival estimates.
  name: MyShipTracking Ports API
  slug: myshiptracking-ports-api
- description: Vessel positions, particulars, history, and search.
  name: MyShipTracking Vessels API
  slug: myshiptracking-vessels-api
artifact_total: 10
collections:
- collection_type: open
  name: MyShipTracking API
  slug: open-myshiptracking
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/myshiptracking-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/myshiptracking-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/myshiptracking-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.myshiptracking.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.myshiptracking.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/myshiptracking-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/myshiptracking-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/myshiptracking-finops.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/myshiptracking
created: '2026-07-12'
description: MyShipTracking is a real-time terrestrial AIS vessel-tracking platform. Its REST API delivers live vessel positions, voyage and static particulars, vessels within a geographic zone or near a reference ship, historical tracks, port details, port calls, estimated arrivals, and fleet management - all returned in a standardized JSON or XML envelope. Access is credit-metered under monthly subscription plans or a pay-per-use coin model, authenticated with an API key over Bearer or x-api-key.
finops:
- name: Myshiptracking Finops
  service_category: Maritime and Location Data
  slug: myshiptracking-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/myshiptracking.png
layout: provider
modified: '2026-07-12'
name: MyShipTracking
nav: Providers
network: true
overview: 'MyShipTracking publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Ports API, and Vessels API. Tagged areas include Vessel Tracking, AIS, Maritime, Ship Tracking, and Real-Time Data.


  MyShipTracking''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Myshiptracking Plans Pricing
  plan_count: 5
  slug: myshiptracking-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Myshiptracking Rate Limits
  slug: myshiptracking-rate-limits
score:
  band: thin
  composite: 38.4
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Myshiptracking Authentication
  slug: myshiptracking-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Myshiptracking Domain Security
  slug: myshiptracking-domain-security
  summary_line: TLSv1.3 · DMARC
slug: myshiptracking
tags:
- Vessel Tracking
- AIS
- Maritime
- Ship Tracking
- Real-Time Data
- Ships
- Port Calls
- Maritime Data
- Location
- Fleet Tracking
website: https://www.myshiptracking.com
---
