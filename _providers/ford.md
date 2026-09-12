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
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
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
  score: 25.9
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 10
  human_in_the_loop: 2
  name: Ford Agentic Access
  operation_count: 18
  slug: ford-agentic-access
  summary_line: 18 operations · 10 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: FordConnect allows to send vehicle commands (e.g., lock, unlock, etc.) and request vehicle information (e.g., fuel range, tire pressure, etc.) to Ford and Lincoln vehicles.
  name: FordConnect
  slug: fordconnect
- description: With this API, authorized external parties can retrieve WLTP values based on a specific vehicle configuration.
  name: Ford WLTP Emissions
  slug: ford-wltp-emissions
- baseURL: https://api.mps.ford.com
  baseurl_source: declared
  description: The Charging API from Ford — 4 operation(s) for charging.
  name: Ford Charging API
  slug: ford-charging-api
- baseURL: https://api.mps.ford.com
  baseurl_source: declared
  description: The Commands API from Ford — 7 operation(s) for commands.
  name: Ford Commands API
  slug: ford-commands-api
- baseURL: https://api.mps.ford.com
  baseurl_source: declared
  description: The Images API from Ford — 2 operation(s) for images.
  name: Ford Images API
  slug: ford-images-api
- baseURL: https://api.mps.ford.com
  baseurl_source: declared
  description: The OAuth API from Ford — 1 operation(s) for oauth.
  name: Ford OAuth API
  slug: ford-oauth-api
- baseURL: https://api.mps.ford.com
  baseurl_source: declared
  description: The Status API from Ford — 2 operation(s) for status.
  name: Ford Status API
  slug: ford-status-api
- baseURL: https://api.mps.ford.com
  baseurl_source: declared
  description: The Vehicles API from Ford — 2 operation(s) for vehicles.
  name: Ford Vehicles API
  slug: ford-vehicles-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FordConnect Charging API
  slug: open-ford-charging-api
- collection_type: open
  name: FordConnect Charging Commands API
  slug: open-ford-commands-api
- collection_type: open
  name: FordConnect Charging Images API
  slug: open-ford-images-api
- collection_type: open
  name: FordConnect Charging OAuth API
  slug: open-ford-oauth-api
- collection_type: open
  name: FordConnect Charging Status API
  slug: open-ford-status-api
- collection_type: open
  name: FordConnect Charging Vehicles API
  slug: open-ford-vehicles-api
- collection_type: open
  name: FordConnect API
  slug: open-ford
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ford-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ford-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ford-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ford-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ford-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ford
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ford-motor-company
- group: start
  title: ''
  type: Portal
  url: https://developer.ford.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ford.com/help/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ford.com/help/privacy/
- group: company
  title: ''
  type: Website
  url: https://www.ford.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ford-well-known.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ford-data-dictionary.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ford-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ford-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ford-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/ford-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ford-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ford-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/ford-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ford-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ford-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ford-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ford.com/apis
- group: operate
  title: ''
  type: Support
  url: https://developer.ford.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://developer.ford.com/my-developer-account/my-dashboard
created: '2025-02-25'
description: 'Ford Motor Company is a multinational automotive manufacturer that designs, builds and sells cars, trucks, SUVs and commercial vehicles, and operates a partner-facing API program through the Ford Developer Marketplace at developer.ford.com. The flagship surface is FordConnect, which lets an approved application read connected-vehicle data and issue vehicle commands to enrolled Ford and Lincoln vehicles, with the vehicle owner''s consent captured as fourteen named data categories in the FordPass account-linking flow. Ford also publishes a WLTP emissions lookup for authorized parties. Access is partner-gated rather than self-serve: applications are registered in a Ford developer account and issued a client id plus two rotating secrets. Ford publishes no OpenAPI, pricing, rate limits, changelog or status page on any surface reachable without signing in.'
finops:
- name: Ford Finops
  service_category: Connected Vehicle / Mobility
  slug: ford-finops
graphqls:
- description: This conceptual GraphQL schema covers the Ford Motor Company connected vehicle and developer API surface, based on the Ford Developer Portal (https://developer.ford.com/). It models FordConnect capabi
  name: Ford Motor GraphQL Schema
  slug: ford-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ford.png
layout: provider
modified: '2026-09-10'
name: Ford
nav: Providers
network: true
overview: 'Ford publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Charging API, Commands API, Images API, and 3 more. Tagged areas include Automobiles, Cars, Vehicles, Connected Vehicle, and Automotive.


  Ford''s developer surface includes authentication, developer portal, documentation, support, and 22 more developer resources.'
plans:
- name: Ford Plans Pricing
  plan_count: 0
  slug: ford-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Ford Rate Limits
  slug: ford-rate-limits
scopes:
- name: Ford Scopes
  scope_count: 14
  slug: ford-scopes
  summary_line: 14 scopes
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 40.0
    catalog_earned_first_party: 5.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 33.3
    contract_quality: 19.6
    developer_ergonomics: 35.7
    discoverability: 59.3
    operational_transparency: 13.2
  previous_composite: 27.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/ford/refs/heads/main/screenshots/ford-2026-06-20T181414.png
security:
- kind: authentication
  name: Ford Authentication
  slug: ford-authentication
  summary_line: oauth2/openIdConnect/http · 3 schemes
- kind: domain-security
  name: Ford Domain Security
  slug: ford-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ford Vulnerability Disclosure
  slug: ford-vulnerability-disclosure
  summary_line: Hackerone
slug: ford
tags:
- Automobiles
- Cars
- Vehicles
- Connected Vehicle
- Automotive
- Telematics
- Electric Vehicles
- Fleet
website: https://www.ford.com/
---
