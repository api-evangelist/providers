---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.0
  scored_at: '2026-11-06'
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
  description: Read connected smart meters.
  name: Enode Meters API
  slug: enode-meters-api
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
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: This product or endpoint is now feature complete and the implementation will not change. There may be bugs or stability issues but they are actively being worked on. We are still open to receiving fee
  name: Enode Beta API
  slug: enode-beta-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: This feature or endpoint is available to early adopters for initial feedback. The implementation is still evolving and may change or be removed. See [Versioning Labels](/api#labels).
  name: Enode Early Adopter API
  slug: enode-early-adopter-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Endpoints that return information about interventions. More information and examples are available in the [Interventions](/docs/interventions) guide.
  name: Enode Interventions API
  slug: enode-interventions-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Locations are used to assign devices to a geographical group. This is useful when running schedules, smart charging, or smart heating, as target behavior usually depends on a common locality of demand
  name: Enode Locations API
  slug: enode-locations-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Endpoints to manage schedules for Vehicles, Chargers and HVACs. More information and examples are available in the [Scheduling](/docs/scheduling/overview) guide.
  name: Enode Schedules API
  slug: enode-schedules-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Endpoints that return information about the health of Enode and our integrations.
  name: Enode Service Health API
  slug: enode-service-health-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Solar inverters can be queried for current production state
  name: Enode Solar inverters API
  slug: enode-solar-inverters-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Endpoints returning timeseries data collected from linked devices.
  name: Enode Statistics API
  slug: enode-statistics-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Use the Tariffs API to submit pricing information to Enode. These prices will be preferred over market prices in Enode's smart products, like [Smart Charging](/api#updateVehicleSmartChargingPolicy), a
  name: Enode Tariffs API
  slug: enode-tariffs-api
- baseURL: https://enode-api.production.enode.io
  baseurl_source: declared
  description: Endpoints used to link and unlink users or vendors.
  name: Enode User Management API
  slug: enode-user-management-api
artifact_total: 34
collections:
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
  href: https://artifacts.apis.io/enode/capabilities/enode-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/enode-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/enode/agentic-access/enode-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/enode-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/enode/security/enode-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/enode-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/enode/security/enode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enode-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/enode/authentication/enode-authentication.yml
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
  href: https://artifacts.apis.io/enode/plans/enode-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/enode-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/enode/rate-limits/enode-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/enode-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/enode/finops/enode-finops.yml
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
- has_sources: true
  method: generated
  name: Enode Finops
  primary_unit: ''
  service_category: Energy and IoT
  slug: enode-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enode.png
layout: provider
modified: '2026-06-21'
name: Enode
nav: Providers
network: true
overview: 'Enode publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batteries API, Chargers API, HVAC API, and 13 more. Tagged areas include Energy, Electric Vehicles, EV Charging, Smart Charging, and Energy Transition.


  The Enode catalog on APIs.io includes 1 Spectral governance ruleset.


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
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Enode API Rules
  rule_count: 65
  severity_counts:
    error: 50
    hint: 0
    info: 4
    warn: 11
  slug: enode-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 52.9
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 61.5
      total: 26
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/enode/enode-2026-07-25T213409.png
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
- Mobility
website: https://www.enode.com
---
