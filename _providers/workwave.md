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
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Workwave Agentic Access
  operation_count: 41
  slug: workwave-agentic-access
  summary_line: 41 operations · 26 acting
api_count: 11
apis:
- description: Manage the webhook callback URL for asynchronous notifications.
  name: WorkWave Callback API
  slug: workwave-callback-api
- description: Manage companies.
  name: WorkWave Companies API
  slug: workwave-companies-api
- description: Manage depots within a territory.
  name: WorkWave Depots API
  slug: workwave-depots-api
- description: Manage the driver roster within a territory.
  name: WorkWave Drivers API
  slug: workwave-drivers-api
- description: Retrieve GPS tracking and location data.
  name: WorkWave GPS API
  slug: workwave-gps-api
- description: Manage orders within a territory.
  name: WorkWave Orders API
  slug: workwave-orders-api
- description: Manage regions within a territory.
  name: WorkWave Regions API
  slug: workwave-regions-api
- description: Retrieve optimized routes and Time of Arrival data.
  name: WorkWave Routes API
  slug: workwave-routes-api
- description: List and edit territories and their planning range.
  name: WorkWave Territories API
  slug: workwave-territories-api
- description: Validate contact emails and phone numbers.
  name: WorkWave Validation API
  slug: workwave-validation-api
- description: Manage the vehicle fleet within a territory.
  name: WorkWave Vehicles API
  slug: workwave-vehicles-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WorkWave Route Manager Callback API
  slug: open-workwave-callback-api
- collection_type: open
  name: WorkWave Route Manager Callback Companies API
  slug: open-workwave-companies-api
- collection_type: open
  name: WorkWave Route Manager Callback Depots API
  slug: open-workwave-depots-api
- collection_type: open
  name: WorkWave Route Manager Callback Drivers API
  slug: open-workwave-drivers-api
- collection_type: open
  name: WorkWave Route Manager Callback GPS API
  slug: open-workwave-gps-api
- collection_type: open
  name: WorkWave Route Manager Callback Orders API
  slug: open-workwave-orders-api
- collection_type: open
  name: WorkWave Route Manager Callback Regions API
  slug: open-workwave-regions-api
- collection_type: open
  name: WorkWave Route Manager Callback Routes API
  slug: open-workwave-routes-api
- collection_type: open
  name: WorkWave Route Manager Callback Territories API
  slug: open-workwave-territories-api
- collection_type: open
  name: WorkWave Route Manager Callback Validation API
  slug: open-workwave-validation-api
- collection_type: open
  name: WorkWave Route Manager Callback Vehicles API
  slug: open-workwave-vehicles-api
- collection_type: open
  name: WorkWave Route Manager API
  slug: open-workwave
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workwave-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workwave-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workwave-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.workwave.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WorkWave
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/workwave
- group: company
  title: ''
  type: Website
  url: https://www.workwave.com
- group: docs
  title: ''
  type: Documentation
  url: https://wwrm.workwave.com/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/workwave-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/workwave-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/workwave-finops.yml
created: '2026-06-21'
description: WorkWave builds field-service and last-mile delivery software for service professionals in pest control, lawn care, cleaning, security, and delivery. Its RouteManager product exposes the WorkWave Route Manager (WWRM) REST API for managing territories, depots, drivers, vehicles, orders, route optimization, time of arrival, and GPS tracking, with API-key authentication and webhook callbacks.
finops:
- name: Workwave Finops
  service_category: Field Service and Logistics Software
  slug: workwave-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workwave.png
layout: provider
modified: '2026-06-21'
name: WorkWave
nav: Providers
network: true
overview: 'WorkWave publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Callback API, Companies API, Depots API, and 8 more. Tagged areas include Field Service, Route Optimization, Last Mile Delivery, Fleet, and GPS Tracking.


  WorkWave''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Workwave Plans Pricing
  plan_count: 2
  slug: workwave-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Workwave Rate Limits
  slug: workwave-rate-limits
score:
  band: thin
  composite: 34.0
  delta: 0.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 51.9
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Workwave Authentication
  slug: workwave-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Workwave Domain Security
  slug: workwave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: workwave
tags:
- Field Service
- Route Optimization
- Last Mile Delivery
- Fleet
- GPS Tracking
- Logistics
website: https://www.workwave.com
---
