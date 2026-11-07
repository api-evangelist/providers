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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Density v3 Public API for real-time occupancy and presence, historical space metrics (occupancy, utilization, time used, sessions), spaces / doorways / sensors / labels management, sensor and space he
  name: Density Public API v3
  slug: density-public-api-v3
artifact_total: 7
asyncapis:
- description: ''
  name: Density Websockets Events
  slug: density-websockets-events
common:
- group: commercial
  href: https://artifacts.apis.io/density/plans/density-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/density-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://density.io/about-density/press
- group: auth
  href: https://artifacts.apis.io/density/security/density-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/density-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.density.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.density.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.density.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.density.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.density.io/quick_start/
- group: operate
  title: ''
  type: Support
  url: https://support.density.io/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://atlas.density.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.density.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.density.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.density.io/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DensityCo
- group: operate
  title: ''
  type: StatusPage
  url: https://status.density.io
- group: operate
  href: https://artifacts.apis.io/density/lifecycle/density-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/density-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/density/authentication/density-authentication.yml
  title: ''
  type: Authentication
  url: authentication/density-authentication.yml
- group: design
  href: https://artifacts.apis.io/density/conventions/density-conventions.yml
  title: ''
  type: Conventions
  url: conventions/density-conventions.yml
- group: design
  href: https://artifacts.apis.io/density/lifecycle/density-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/density-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/density/errors/density-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/density-problem-types.yml
- group: design
  href: https://artifacts.apis.io/density/conformance/density-conformance.yml
  title: ''
  type: Conformance
  url: conformance/density-conformance.yml
- group: build
  href: https://artifacts.apis.io/density/packages/density-packages.yml
  title: ''
  type: Packages
  url: packages/density-packages.yml
- group: design
  href: https://artifacts.apis.io/density/components/density-components.yml
  title: ''
  type: Components
  url: components/density-components.yml
- group: design
  href: https://artifacts.apis.io/density/asyncapi/density-websockets-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/density-websockets-events.yml
- group: design
  href: https://artifacts.apis.io/density/data-model/density-data-model.yml
  title: ''
  type: DataModel
  url: data-model/density-data-model.yml
- group: agent
  href: https://artifacts.apis.io/density/well-known/density-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/density-well-known.yml
- group: agent
  href: https://artifacts.apis.io/density/mcp/density-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/density-mcp.yml
- group: agent
  href: https://artifacts.apis.io/density/llms/density-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/density-llms.txt
created: '2026-07-17'
description: Density builds radar-based occupancy sensors and a workplace analytics platform that measures how people use physical space without cameras or personally identifiable information. Its v3 Public API (api.density.io) exposes real-time occupancy and presence, historical metrics (occupancy, utilization, time used, sessions, raw sessions), spaces / doorways / sensors / labels resources, sensor and space health, wayfinding display tokens, and WebSocket streams for live floor presence and space occupancy. Authentication is OAuth 2.0 client-credentials (Auth0-backed) or static Bearer API tokens. Originally surfaced as a portfolio company of kleiner-perkins and enriched from Density's public developer surface.
finops:
- has_sources: true
  method: derived
  name: Density Finops
  primary_unit: unit
  service_category: ''
  slug: density-finops
  template: false
image: https://cdn.prod.website-files.com/5f49c40736fbe713860f9203/681a28ab6cdef3f72543b7bd_density-favicon_256x256.png
layout: provider
modified: '2026-10-06'
name: Density
nav: Providers
network: true
overview: 'Density is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Occupancy Sensors, Workplace Analytics, and Real-Time.


  The Density catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Density''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, signup flow, pricing, and 21 more developer resources.'
plans:
- name: Density Plans Pricing
  plan_count: 4
  slug: density-plans-pricing
- name: Density Price Estimates
  plan_count: 0
  slug: density-price-estimates
random_paper: 0
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 57.1
    discoverability: 73.2
    operational_transparency: 34.2
  previous_composite: 49.1
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/density/density-2026-07-25T211718.png
security:
- kind: authentication
  name: Density Authentication
  slug: density-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Density Domain Security
  slug: density-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: density
tags:
- Company
- Enterprise
- Occupancy Sensors
- Workplace Analytics
- Real-Time
- Occupancy
- Sensors
- IoT
- Space Utilization
- PropTech
website: https://www.density.io
---
