---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 59.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Thinair Co Agentic Access
  operation_count: 34
  slug: thinair-co-agentic-access
  summary_line: 34 operations · 15 acting
api_count: 2
apis:
- baseURL: https://geo.thinair.co
  baseurl_source: declared
  description: The Account API from thinair-co — 1 operation(s) for account.
  name: thinair-co Account API
  slug: thinair-co-account-api
- baseURL: https://data.thinair.co
  baseurl_source: declared
  description: The billing API from thinair-co — 1 operation(s) for billing.
  name: thinair-co Billing API
  slug: thinair-co-billing-api
- baseURL: https://geo.thinair.co
  baseurl_source: declared
  description: The Conditions API from thinair-co — 2 operation(s) for conditions.
  name: thinair-co Conditions API
  slug: thinair-co-conditions-api
- baseURL: https://data.thinair.co
  baseurl_source: declared
  description: The connections API from thinair-co — 3 operation(s) for connections.
  name: thinair-co Connections API
  slug: thinair-co-connections-api
- baseURL: https://geo.thinair.co
  baseurl_source: declared
  description: The Geocoding API from thinair-co — 7 operation(s) for geocoding.
  name: thinair-co Geocoding API
  slug: thinair-co-geocoding-api
- baseURL: https://geo.thinair.co
  baseurl_source: declared
  description: The Geofences API from thinair-co — 2 operation(s) for geofences.
  name: thinair-co Geofences API
  slug: thinair-co-geofences-api
- baseURL: https://geo.thinair.co
  baseurl_source: declared
  description: The Intersections API from thinair-co — 2 operation(s) for intersections.
  name: thinair-co Intersections API
  slug: thinair-co-intersections-api
- baseURL: https://geo.thinair.co
  baseurl_source: declared
  description: The Learning API from thinair-co — 2 operation(s) for learning.
  name: thinair-co Learning API
  slug: thinair-co-learning-api
- baseURL: https://data.thinair.co
  baseurl_source: declared
  description: The migrations API from thinair-co — 1 operation(s) for migrations.
  name: thinair-co Migrations API
  slug: thinair-co-migrations-api
- baseURL: https://geo.thinair.co
  baseurl_source: declared
  description: The Places API from thinair-co — 2 operation(s) for places.
  name: thinair-co Places API
  slug: thinair-co-places-api
- baseURL: https://data.thinair.co
  baseurl_source: declared
  description: The query API from thinair-co — 3 operation(s) for query.
  name: thinair-co Query API
  slug: thinair-co-query-api
- baseURL: https://geo.thinair.co
  baseurl_source: declared
  description: The Routing API from thinair-co — 6 operation(s) for routing.
  name: thinair-co Routing API
  slug: thinair-co-routing-api
- baseURL: https://data.thinair.co
  baseurl_source: declared
  description: The tables API from thinair-co — 2 operation(s) for tables.
  name: thinair-co Tables API
  slug: thinair-co-tables-api
artifact_total: 33
common:
- group: agent
  href: https://artifacts.apis.io/thinair-co/agentic-access/thinair-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thinair-co-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/thinair-co/rules/thinair-co-rules.yml
  title: ''
  type: Spectral
  url: rules/thinair-co-rules.yml
- group: design
  href: https://artifacts.apis.io/thinair-co/json-ld/thinair-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/thinair-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/thinair-co/vocabulary/thinair-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thinair-co-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/thinair-co/data-model/thinair-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thinair-co-data-model.yml
- group: start
  href: https://artifacts.apis.io/thinair-co/sandbox/thinair-co-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/thinair-co-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/thinair-co/security/thinair-co-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/thinair-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/thinair-co/authentication/thinair-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thinair-co-authentication.yml
- group: design
  href: https://artifacts.apis.io/thinair-co/errors/thinair-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thinair-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/thinair-co/conformance/thinair-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thinair-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/thinair-co/llms/thinair-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thinair-co-llms.txt
- group: other
  href: https://artifacts.apis.io/thinair-co/a2a/thinair-co-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/thinair-co-a2a.yml
- group: auth
  href: https://artifacts.apis.io/thinair-co/well-known/thinair-co-geo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thinair-co-geo-security.txt
- group: auth
  href: https://artifacts.apis.io/thinair-co/well-known/thinair-co-data-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thinair-co-data-security.txt
- group: agent
  href: https://artifacts.apis.io/thinair-co/well-known/thinair-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thinair-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/thinair-co/hosts/thinair-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thinair-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/thinair-co/vendors/thinair-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thinair-co-vendors.yml
- group: build
  href: https://artifacts.apis.io/thinair-co/packages/thinair-co-packages.yml
  title: ''
  type: SDKs
  url: packages/thinair-co-packages.yml
- group: build
  href: https://artifacts.apis.io/thinair-co/packages/thinair-co-packages.yml
  title: ''
  type: Packages
  url: packages/thinair-co-packages.yml
- group: auth
  href: https://artifacts.apis.io/thinair-co/security/thinair-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/thinair-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/thinair-co/security/thinair-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thinair-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thinair.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.thinair.co/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.thinair.co/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.thinair.co/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.thinair.co/discover
- group: operate
  title: ''
  type: Support
  url: https://www.thinair.co/contact
- group: company
  title: ''
  type: Blog
  url: https://www.thinair.co/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thinair.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.thinair.co/purchase
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thinair.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thinair.co/privacy-policy
created: '2026-10-30'
description: ThinAir provides a unified fleet management platform that combines real‑time vehicle tracking, driver safety, dispatch routing, ELD/HOS compliance, asset tracking, maintenance, and analytics. Their solutions include ThinAir Fleet, Thinair ELD, ThinAir Geo, and ThinAir Data, delivering live operational visibility for trucking, construction, oil & gas, field service, utilities, and waste‑recycling industries. The platform offers APIs and MCP servers for developers to integrate location intelligence, operational data, and compliance services into their own applications.
image: https://www.thinair.co/favicon.ico
json_schemas:
- name: AutocompleteResponse
  property_count: 3
  slug: thinair-co-autocomplete-response
- name: ConnectionHealthResponse
  property_count: 8
  slug: thinair-co-connection-health-response
- name: DirectionsRequest
  property_count: 24
  slug: thinair-co-directions-request
- name: DirectionsResponse
  property_count: 39
  slug: thinair-co-directions-response
- name: ExploreResponse
  property_count: 4
  slug: thinair-co-explore-response
- name: LocateResponse
  property_count: 16
  slug: thinair-co-locate-response
- name: MapMatchResponse
  property_count: 12
  slug: thinair-co-map-match-response
- name: MigrationsGenerateRequest
  property_count: 4
  slug: thinair-co-migrations-generate-request
- name: OptimizeRequest
  property_count: 3
  slug: thinair-co-optimize-request
- name: QueryRequest
  property_count: 3
  slug: thinair-co-query-request
- name: QuotaResponse
  property_count: 2
  slug: thinair-co-quota-response
- name: TablesProfileResponse
  property_count: 4
  slug: thinair-co-tables-profile-response
jsonld:
- class_count: 83
  name: Thinair Co Context
  property_count: 288
  slug: thinair-co-context
layout: provider
modified: '2026-10-30'
name: thinair-co
nav: Providers
network: true
overview: 'thinair-co publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Conditions API, and 10 more. Tagged areas include Company, Fleet Management, Telematics, Logistics, and Compliance.


  The thinair-co catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  thinair-co''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 25 more developer resources.'
random_paper: 22
rate_limits:
- limit_count: 0
  name: Thinair Co Rate Limits
  slug: thinair-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: thinair-co API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: thinair-co-rules
scopes:
- name: Thinair Co Scopes
  scope_count: 0
  slug: thinair-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 64.7
    developer_ergonomics: 48.8
    discoverability: 73.2
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/thinair-co/thinair-co-2026-11-03T144651.png
security:
- kind: authentication
  name: Thinair Co Authentication
  slug: thinair-co-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Thinair Co Domain Security
  slug: thinair-co-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Thinair Co Vulnerability Disclosure
  slug: thinair-co-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: thinair-co
tags:
- Company
- Fleet Management
- Telematics
- Logistics
- Compliance
website: https://thinair.co/
---
