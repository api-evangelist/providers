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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 2
  name: Sensibo Agentic Access
  operation_count: 19
  slug: sensibo-agentic-access
  summary_line: 19 operations · 9 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Read and command the air conditioner state.
  name: Sensibo AC States API
  slug: sensibo-ac-states-api
- description: Smart-mode automation driven by temperature and humidity thresholds.
  name: Sensibo Climate React API
  slug: sensibo-climate-react-api
- description: Individual device (pod) detail and status.
  name: Sensibo Devices API
  slug: sensibo-devices-api
- description: Time-series measurements and the device event log.
  name: Sensibo Historical Data API
  slug: sensibo-historical-data-api
- description: Latest temperature, humidity, and air quality readings.
  name: Sensibo Measurements API
  slug: sensibo-measurements-api
- description: Recurring day-and-time AC state schedules.
  name: Sensibo Schedules API
  slug: sensibo-schedules-api
- description: One-shot countdown timers that apply an AC state.
  name: Sensibo Timers API
  slug: sensibo-timers-api
- description: Account-level access to the devices enrolled on a Sensibo account.
  name: Sensibo Users API
  slug: sensibo-users-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sensibo AC States API
  slug: open-sensibo-ac-states-api
- collection_type: open
  name: Sensibo AC States Climate React API
  slug: open-sensibo-climate-react-api
- collection_type: open
  name: Sensibo AC States Devices API
  slug: open-sensibo-devices-api
- collection_type: open
  name: Sensibo AC States Historical Data API
  slug: open-sensibo-historical-data-api
- collection_type: open
  name: Sensibo AC States Measurements API
  slug: open-sensibo-measurements-api
- collection_type: open
  name: Sensibo AC States Schedules API
  slug: open-sensibo-schedules-api
- collection_type: open
  name: Sensibo AC States Timers API
  slug: open-sensibo-timers-api
- collection_type: open
  name: Sensibo AC States Users API
  slug: open-sensibo-users-api
- collection_type: open
  name: Sensibo API
  slug: open-sensibo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sensibo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sensibo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sensibo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sensibo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sensibo
- group: company
  title: ''
  type: Website
  url: https://sensibo.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.sensibo.com/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/sensibo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sensibo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sensibo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://sensibo.com/blogs/articles.atom
created: '2026-07-03'
description: Sensibo builds smart air conditioning controllers and indoor air quality monitors (Sensibo Sky, Air, Air Pro, and Elements) that add app, voice, and API control to existing mini-split, window, and portable AC and heat-pump units. The Sensibo REST API (base https://home.sensibo.com/api/v2) gives developers full control over enrolled devices ("pods") - reading temperature, humidity, and air quality measurements, getting and setting the AC state (power, mode, target temperature, fan, swing), configuring the Climate React smart automation, and managing schedules and timers. Authentication is a per-account API key passed as an apiKey query parameter, generated from home.sensibo.com/me/api. OAuth2 is available for commercial integrations.
finops:
- name: Sensibo Finops
  service_category: Smart Home and IoT
  slug: sensibo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sensibo.png
layout: provider
modified: '2026-07-03'
name: Sensibo
nav: Providers
network: true
overview: 'Sensibo publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AC States API, Climate React API, Devices API, and 5 more. Tagged areas include Smart Home, IoT, Air Conditioning, HVAC, and Air Quality.


  Sensibo''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sensibo Plans Pricing
  plan_count: 3
  slug: sensibo-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Sensibo Rate Limits
  slug: sensibo-rate-limits
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.5
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Sensibo Authentication
  slug: sensibo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sensibo Domain Security
  slug: sensibo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sensibo
tags:
- Smart Home
- IoT
- Air Conditioning
- HVAC
- Air Quality
- Climate Control
- Connected Devices
website: https://sensibo.com
---
