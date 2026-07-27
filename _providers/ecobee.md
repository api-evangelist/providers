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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Ecobee Agentic Access
  operation_count: 16
  slug: ecobee-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 7
apis:
- description: OAuth 2.0 PIN and authorization-code flows and token refresh.
  name: ecobee Authorization API
  slug: ecobee-authorization-api
- description: Utility demand response events.
  name: ecobee Demand Response API
  slug: ecobee-demand-response-api
- description: Group registered thermostats.
  name: ecobee Group API
  slug: ecobee-group-api
- description: EMS/Utility management-set hierarchy of thermostats, sets, and users.
  name: ecobee Hierarchy API
  slug: ecobee-hierarchy-api
- description: Historical runtime and meter reports.
  name: ecobee Reports API
  slug: ecobee-reports-api
- description: Read thermostat state and poll for changes.
  name: ecobee Thermostat API
  slug: ecobee-thermostat-api
- description: Update writable properties and run thermostat functions.
  name: ecobee Thermostat Update API
  slug: ecobee-thermostat-update-api
artifact_total: 14
collections:
- collection_type: open
  name: ecobee API
  slug: open-ecobee
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ecobee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ecobee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ecobee-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ecobee
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ecobee
- group: company
  title: ''
  type: Website
  url: https://www.ecobee.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.ecobee.com/home/developer/api/introduction/index.shtml
- group: commercial
  title: ''
  type: Plans
  url: plans/ecobee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ecobee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ecobee-finops.yml
created: '2026-07-03'
description: ecobee makes smart Wi-Fi thermostats, room sensors, cameras, and other connected home devices. The ecobee API is a REST-like JSON interface, based at https://api.ecobee.com/1/, that lets authorized third-party applications read and control registered ecobee thermostats - retrieving live runtime state, settings, sensors, and equipment status, updating programs and comfort settings via thermostat functions, pulling historical runtime and meter reports, grouping thermostats, and (for EMS and Utility accounts) organizing thermostats in a management-set hierarchy and issuing demand response events. Authorization uses OAuth 2.0 with an ecobee PIN flow or the standard authorization-code flow, plus refresh tokens. NOTE - as of late 2024 ecobee closed its developer program to new API-key registrations; existing keys continue to function.
finops:
- name: Ecobee Finops
  service_category: IoT and Smart Home
  slug: ecobee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ecobee.png
layout: provider
modified: '2026-07-03'
name: ecobee
nav: Providers
network: true
overview: 'ecobee publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Demand Response API, Group API, and 4 more. Tagged areas include Smart Home, Thermostat, IoT, HVAC, and Energy.


  ecobee''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Ecobee Plans Pricing
  plan_count: 2
  slug: ecobee-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 4
  name: Ecobee Rate Limits
  slug: ecobee-rate-limits
score:
  band: thin
  composite: 39.1
  delta: 3.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.4
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ecobee/refs/heads/main/screenshots/ecobee-2026-07-25T212750.png
security:
- kind: authentication
  name: Ecobee Authentication
  slug: ecobee-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ecobee Domain Security
  slug: ecobee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ecobee
tags:
- Smart Home
- Thermostat
- IoT
- HVAC
- Energy
- Home Automation
- Demand Response
website: https://www.ecobee.com
---
