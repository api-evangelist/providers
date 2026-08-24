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
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ecobee Authorization API
  slug: open-ecobee-authorization-api
- collection_type: open
  name: ecobee Authorization Demand Response API
  slug: open-ecobee-demand-response-api
- collection_type: open
  name: ecobee Authorization Group API
  slug: open-ecobee-group-api
- collection_type: open
  name: ecobee Authorization Hierarchy API
  slug: open-ecobee-hierarchy-api
- collection_type: open
  name: ecobee Authorization Reports API
  slug: open-ecobee-reports-api
- collection_type: open
  name: ecobee Authorization Thermostat API
  slug: open-ecobee-thermostat-api
- collection_type: open
  name: ecobee Authorization Thermostat Update API
  slug: open-ecobee-thermostat-update-api
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
random_paper: 2
rate_limits:
- limit_count: 4
  name: Ecobee Rate Limits
  slug: ecobee-rate-limits
score:
  band: thin
  composite: 36.1
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 58.5
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
