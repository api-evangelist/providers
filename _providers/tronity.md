---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 4
  name: Tronity Agentic Access
  operation_count: 21
  slug: tronity-agentic-access
  summary_line: 21 operations · 7 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.tronity.tech
  baseurl_source: declared
  description: The Authentication API from TRONITY — 1 operation(s) for authentication.
  name: TRONITY Authentication API
  slug: tronity-authentication-api
- baseURL: https://api.tronity.tech
  baseurl_source: declared
  description: The Charging & Battery API from TRONITY — 3 operation(s) for charging & battery.
  name: TRONITY Charging & Battery API
  slug: tronity-charging-battery-api
- baseURL: https://api.tronity.tech
  baseurl_source: declared
  description: The Commands API from TRONITY — 3 operation(s) for commands.
  name: TRONITY Commands API
  slug: tronity-commands-api
- baseURL: https://api.tronity.tech
  baseurl_source: declared
  description: The Vehicle Data API from TRONITY — 7 operation(s) for vehicle data.
  name: TRONITY Vehicle Data API
  slug: tronity-vehicle-data-api
- baseURL: https://api.tronity.tech
  baseurl_source: declared
  description: The Vehicles API from TRONITY — 3 operation(s) for vehicles.
  name: TRONITY Vehicles API
  slug: tronity-vehicles-api
- baseURL: https://api.tronity.tech
  baseurl_source: declared
  description: The Webhooks API from TRONITY — 2 operation(s) for webhooks.
  name: TRONITY Webhooks API
  slug: tronity-webhooks-api
artifact_total: 21
collections:
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
- group: other
  href: https://artifacts.apis.io/tronity/capabilities/tronity-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tronity-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/tronity/agentic-access/tronity-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tronity-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/tronity/security/tronity-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tronity-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tronity/security/tronity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tronity-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tronity/authentication/tronity-authentication.yml
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
  href: https://artifacts.apis.io/tronity/plans/tronity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tronity-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tronity/rate-limits/tronity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tronity-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tronity/finops/tronity-finops.yml
  title: ''
  type: FinOps
  url: finops/tronity-finops.yml
created: '2026-06-21'
description: TRONITY is a connected-car platform that aggregates electric vehicle and fleet telematics across 20-plus OEM brands into one normalized REST API. The TRONITY Platform API exposes vehicle data - battery state of charge, range, odometer, location, charging sessions and trips - plus remote commands (start/stop charging, wake-up) and webhooks, secured with OAuth2.
finops:
- has_sources: true
  method: generated
  name: Tronity Finops
  primary_unit: ''
  service_category: Connected Vehicle and Telematics
  slug: tronity-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tronity.png
layout: provider
modified: '2026-06-21'
name: TRONITY
nav: Providers
network: true
overview: 'TRONITY publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Charging & Battery API, Commands API, and 3 more. Tagged areas include Connected Vehicles, Electric Vehicles, Telematics, Fleet Management, and Vehicle Data.


  The TRONITY catalog on APIs.io includes 1 Spectral governance ruleset.


  TRONITY''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Tronity Plans Pricing
  plan_count: 5
  slug: tronity-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Tronity Rate Limits
  slug: tronity-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: TRONITY API Rules
  rule_count: 59
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 4
  slug: tronity-rules
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 44.8
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 25.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tronity/tronity-2026-09-02T164310.png
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
  summary_line: no policy recorded
slug: tronity
tags:
- Connected Vehicles
- Electric Vehicles
- Telematics
- Fleet Management
- Vehicle Data
website: https://www.tronity.tech
---
