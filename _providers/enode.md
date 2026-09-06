---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 9
  human_in_the_loop: 2
  name: Enode Agentic Access
  operation_count: 27
  slug: enode-agentic-access
  summary_line: 27 operations · 9 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Read and control connected home batteries.
  name: Enode Batteries API
  slug: enode-batteries-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Read and control connected EV chargers.
  name: Enode Chargers API
  slug: enode-chargers-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Read and control connected HVAC units.
  name: Enode HVAC API
  slug: enode-hvac-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Read connected solar inverters.
  name: Enode Inverters API
  slug: enode-inverters-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Read connected smart meters.
  name: Enode Meters API
  slug: enode-meters-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Configure smart-charging policies and overrides for vehicles.
  name: Enode Smart Charging API
  slug: enode-smart-charging-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Manage end users and Link sessions.
  name: Enode Users API
  slug: enode-users-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Read and control connected electric vehicles.
  name: Enode Vehicles API
  slug: enode-vehicles-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Manage event webhooks.
  name: Enode Webhooks API
  slug: enode-webhooks-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Enode Batteries API
  slug: open-enode-batteries-api
- collection_type: open
  name: Enode Batteries Chargers API
  slug: open-enode-chargers-api
- collection_type: open
  name: Enode Batteries HVAC API
  slug: open-enode-hvac-api
- collection_type: open
  name: Enode Batteries Inverters API
  slug: open-enode-inverters-api
- collection_type: open
  name: Enode Batteries Meters API
  slug: open-enode-meters-api
- collection_type: open
  name: Enode Batteries Smart Charging API
  slug: open-enode-smart-charging-api
- collection_type: open
  name: Enode Batteries Users API
  slug: open-enode-users-api
- collection_type: open
  name: Enode Batteries Vehicles API
  slug: open-enode-vehicles-api
- collection_type: open
  name: Enode Batteries Webhooks API
  slug: open-enode-webhooks-api
- collection_type: open
  name: Enode API
  slug: open-enode
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/enode-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/enode-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/enode-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enode-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/enode-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enode
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/enode-energy
- group: company
  title: ''
  type: Website
  url: https://www.enode.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.enode.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/enode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/enode-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.enode.com/blog
created: '2026-06-21'
description: Enode provides a single API to connect and control electric vehicles, chargers, HVAC systems, batteries, solar inverters, and smart meters across more than a thousand hardware brands. The energy-transition API links end-user devices via OAuth, normalizes telemetry, and exposes smart-charging and device-control endpoints for energy apps, VPPs, and home energy management.
finops:
- name: Enode Finops
  service_category: Energy and IoT
  slug: enode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enode.png
layout: provider
modified: '2026-06-21'
name: Enode
nav: Providers
network: true
overview: 'Enode publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Batteries API, Chargers API, HVAC API, and 6 more. Tagged areas include Energy, Electric Vehicles, EV Charging, Smart Charging, and Energy Transition.


  Enode''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Enode Plans Pricing
  plan_count: 2
  slug: enode-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Enode Rate Limits
  slug: enode-rate-limits
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 24.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enode/refs/heads/main/screenshots/enode-2026-07-25T213409.png
security:
- kind: authentication
  name: Enode Authentication
  slug: enode-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Enode Domain Security
  slug: enode-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Enode Vulnerability Disclosure
  slug: enode-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: enode
tags:
- Energy
- Electric Vehicles
- EV Charging
- Smart Charging
- Energy Transition
website: https://www.enode.com
---
