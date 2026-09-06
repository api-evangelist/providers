---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
  - rate-limits
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
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: The ASCII API is the primary runtime integration surface for the Realtime Controller. A client opens a TCP socket to the controller and exchanges inline YAML 1.2 command strings (topic / type / id / d
  name: RapidPlan Realtime Controller ASCII API
  slug: rapidplan-ascii-api
- description: RapidSense 2.x exposes a REST interface on port 11235 of the Realtime Controller alongside equivalent ASCII commands. Documented resources are /volumes (GET, POST, PUT, DELETE - cuboid perception volu
  name: RapidSense API
  slug: rapidsense-api
- description: 'Resolver is Realtime Robotics'' cloud optimisation application, reached at app.resolver.rtr.ai (global) and app-eu.resolver.rtr.ai (Europe). Work is submitted as a .zip study containing a project.yaml '
  name: Resolver Cloud
  slug: resolver-cloud
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/realtime-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rtr.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://resolver.rtr.ai/docs/user_guide/overview
- group: docs
  title: ''
  type: APIReference
  url: https://resolver.rtr.ai/docs/api/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://resolver.rtr.ai/docs/category/getting-started
- group: operate
  title: ''
  type: Support
  url: https://rtr.ai/support/
- group: company
  title: ''
  type: Blog
  url: https://rtr.ai/resources/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RealtimeRobotics
- group: start
  title: ''
  type: SignUp
  url: https://rtr.ai/demo/
- group: start
  title: ''
  type: Login
  url: https://app.resolver.rtr.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rtr.ai/privacy-policy/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/realtime-robotics-operations-query.schema.json
- group: build
  title: ''
  type: Packages
  url: packages/realtime-robotics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/realtime-robotics-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/realtime-robotics-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/realtime-robotics-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/realtime-robotics-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/realtime-robotics-clerk-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/realtime-robotics-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/realtime-robotics-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/realtime-robotics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/realtime-robotics-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/realtime-robotics-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/realtime-robotics-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/realtime-robotics-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/realtime-robotics-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/realtime-robotics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/realtime-robotics-rate-limits.yml
created: '2026-08-26'
description: 'Realtime Robotics is a Boston-based industrial robotics software company that builds collision-free autonomous motion planning for multi-robot workcells. Its products are RapidPlan (the RapidPlan Create offline programming tool plus the on-premise Realtime Controller that plans and deconflicts robot motion at runtime), RapidSense (a sensor/perception layer that adds dynamic collision avoidance, volumes, markers and change detection), and Resolver (a cloud application that optimises cell layout and cycle time from simulation projects exported through Process Simulate, Visual Components and MELSOFT Gemini connectors). Its integration surface is machine-facing rather than web-facing: an inline-YAML ASCII command API over a TCP socket to the Realtime Controller, a REST interface for RapidSense, PROFINET and CC-Link IE Field Basic fieldbus interfaces for PLCs, and a published JSON Schema for the Resolver Operations Query. A public Resolver Cloud REST API is documented as under development
  and not yet publicly available.'
image: https://rtr.ai/wp-content/uploads/2025/03/realtime-logo.svg
json_schemas:
- name: Operations Query
  property_count: 4
  slug: realtime-robotics-operations-query.schema
layout: provider
modified: '2026-08-26'
name: Realtime Robotics
nav: Providers
network: true
overview: 'Realtime Robotics publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Motion Planning, Industrial Automation, and Manufacturing.


  Realtime Robotics'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
plans:
- name: Realtime Robotics Plans Pricing
  plan_count: 0
  slug: realtime-robotics-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Realtime Robotics Rate Limits
  slug: realtime-robotics-rate-limits
scopes:
- name: Realtime Robotics Scopes
  scope_count: 0
  slug: realtime-robotics-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 25.5
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/realtime-robotics/refs/heads/main/screenshots/realtime-robotics-2026-09-02T153007.png
security:
- kind: authentication
  name: Realtime Robotics Authentication
  slug: realtime-robotics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Realtime Robotics Domain Security
  slug: realtime-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: realtime-robotics
tags:
- Company
- Robotics
- Motion Planning
- Industrial Automation
- Manufacturing
- Simulation
- Collision Avoidance
- Robot Programming
- Machine Vision
- Digital Twin
website: https://rtr.ai/
---
