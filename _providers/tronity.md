---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 7
  human_in_the_loop: 4
  name: Tronity Agentic Access
  operation_count: 21
  slug: tronity-agentic-access
  summary_line: 21 operations · 7 acting · 4 human-in-the-loop
api_count: 6
apis:
- description: The Authentication API from TRONITY — 1 operation(s) for authentication.
  name: TRONITY Authentication API
  slug: tronity-authentication-api
- description: The Charging & Battery API from TRONITY — 3 operation(s) for charging & battery.
  name: TRONITY Charging & Battery API
  slug: tronity-charging-battery-api
- description: The Commands API from TRONITY — 3 operation(s) for commands.
  name: TRONITY Commands API
  slug: tronity-commands-api
- description: The Vehicle Data API from TRONITY — 7 operation(s) for vehicle data.
  name: TRONITY Vehicle Data API
  slug: tronity-vehicle-data-api
- description: The Vehicles API from TRONITY — 3 operation(s) for vehicles.
  name: TRONITY Vehicles API
  slug: tronity-vehicles-api
- description: The Webhooks API from TRONITY — 2 operation(s) for webhooks.
  name: TRONITY Webhooks API
  slug: tronity-webhooks-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TRONITY Platform Authentication API
  slug: open-tronity-authentication-api
- collection_type: open
  name: TRONITY Platform Authentication Charging & Battery API
  slug: open-tronity-charging-battery-api
- collection_type: open
  name: TRONITY Platform Authentication Commands API
  slug: open-tronity-commands-api
- collection_type: open
  name: TRONITY Platform Authentication Vehicle Data API
  slug: open-tronity-vehicle-data-api
- collection_type: open
  name: TRONITY Platform Authentication Vehicles API
  slug: open-tronity-vehicles-api
- collection_type: open
  name: TRONITY Platform Authentication Webhooks API
  slug: open-tronity-webhooks-api
- collection_type: open
  name: TRONITY Platform API
  slug: open-tronity
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tronity-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tronity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tronity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tronity-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tronity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tronity
- group: company
  title: ''
  type: Website
  url: https://www.tronity.tech
- group: docs
  title: ''
  type: Documentation
  url: https://app.tronity.tech/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/tronity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tronity-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tronity-finops.yml
created: '2026-06-21'
description: TRONITY is a connected-car platform that aggregates electric vehicle and fleet telematics across 20-plus OEM brands into one normalized REST API. The TRONITY Platform API exposes vehicle data - battery state of charge, range, odometer, location, charging sessions and trips - plus remote commands (start/stop charging, wake-up) and webhooks, secured with OAuth2.
finops:
- name: Tronity Finops
  service_category: Connected Vehicle and Telematics
  slug: tronity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tronity.png
layout: provider
modified: '2026-06-21'
name: TRONITY
nav: Providers
network: true
overview: 'TRONITY publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Charging & Battery API, Commands API, and 3 more. Tagged areas include Connected Car, EV, Telematics, Fleet, and Vehicle Data.


  TRONITY''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Tronity Plans Pricing
  plan_count: 5
  slug: tronity-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Tronity Rate Limits
  slug: tronity-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.2
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Tronity Authentication
  slug: tronity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tronity Domain Security
  slug: tronity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tronity Vulnerability Disclosure
  slug: tronity-vulnerability-disclosure
  summary_line: disclosure policy published
slug: tronity
tags:
- Connected Car
- EV
- Telematics
- Fleet
- Vehicle Data
website: https://www.tronity.tech
---
