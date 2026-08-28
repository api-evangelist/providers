---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Windy Agentic Access
  operation_count: 3
  slug: windy-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 2
apis:
- description: The Point Forecast API from Windy — 1 operation(s) for point forecast.
  name: Windy Point Forecast API
  slug: windy-point-forecast-api
- description: The Webcams API from Windy — 2 operation(s) for webcams.
  name: Windy Webcams API
  slug: windy-webcams-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Windy Point Forecast API
  slug: open-windy-point-forecast-api
- collection_type: open
  name: Windy Point Forecast Webcams API
  slug: open-windy-webcams-api
- collection_type: open
  name: Windy API
  slug: open-windy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/windy-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/windy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/windy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/windy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/windycom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/windy-com
- group: company
  title: ''
  type: Website
  url: https://www.windy.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.windy.com
- group: commercial
  title: ''
  type: Plans
  url: plans/windy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/windy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/windy-finops.yml
created: '2026-06-21'
description: Windy.com is a weather visualization platform serving high-resolution forecast models, animated weather maps, and a global webcam network. The Windy API exposes three developer products - a Point Forecast API for multi-model numerical weather data at a coordinate, an embeddable Map Forecast API based on Leaflet, and a Webcams API for the world's largest webcam repository.
finops:
- name: Windy Finops
  service_category: Analytics
  slug: windy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/windy.png
layout: provider
modified: '2026-06-21'
name: Windy
nav: Providers
network: true
overview: 'Windy publishes 2 APIs on the [APIs.io](https://apis.io/) network: Point Forecast API and Webcams API. Tagged areas include Weather, Forecast, Maps, Webcams, and Visualization.


  Windy''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Windy Plans Pricing
  plan_count: 6
  slug: windy-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 8
  name: Windy Rate Limits
  slug: windy-rate-limits
score:
  band: thin
  composite: 38.1
  delta: 0.9
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Windy Authentication
  slug: windy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Windy Domain Security
  slug: windy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Windy Vulnerability Disclosure
  slug: windy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: windy
tags:
- Weather
- Forecast
- Maps
- Webcams
- Visualization
website: https://www.windy.com
---
