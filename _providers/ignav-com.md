---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ignav Com Agentic Access
  operation_count: 7
  slug: ignav-com-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://ignav.com
  baseurl_source: declared
  description: The Airports API from ignav-com — 1 operation(s) for airports.
  name: ignav-com Airports API
  slug: ignav-com-airports-api
- baseURL: https://ignav.com
  baseurl_source: declared
  description: The Fares API from ignav-com — 5 operation(s) for fares.
  name: ignav-com Fares API
  slug: ignav-com-fares-api
- baseURL: https://ignav.com
  baseurl_source: declared
  description: The Health API from ignav-com — 1 operation(s) for health.
  name: ignav-com Health API
  slug: ignav-com-health-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/ignav-com/agentic-access/ignav-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ignav-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ignav-com/plans/ignav-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ignav-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ignav-com/rules/ignav-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ignav-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ignav-com/json-ld/ignav-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ignav-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ignav-com/vocabulary/ignav-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ignav-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ignav-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ignav-com/data-model/ignav-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ignav-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ignav-com/authentication/ignav-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ignav-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/ignav-com/lifecycle/ignav-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ignav-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ignav-com/errors/ignav-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ignav-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ignav-com/conformance/ignav-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ignav-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ignav-com/llms/ignav-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ignav-com-llms.txt
- group: build
  href: https://artifacts.apis.io/ignav-com/mcp/ignav-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ignav-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ignav-com/mcp/ignav-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ignav-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ignav-com/well-known/ignav-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ignav-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ignav-com/hosts/ignav-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ignav-com-hosts.yml
- group: start
  title: ''
  type: Sandbox
  url: https://ignav.com/playground
- group: start
  title: ''
  type: SignUp
  url: https://ignav.com/signup
- group: docs
  title: ''
  type: APIReference
  url: https://ignav.com/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/ignav-com/security/ignav-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ignav-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ignav.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ignav.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://ignav.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ignav.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ignav.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:gus@ignav.com
- group: start
  title: ''
  type: GettingStarted
  url: https://ignav.com/docs/quickstart
created: '2026-10-30'
description: Ignav provides a self‑serve API delivering real‑time flight price data and direct booking links. Developers can search one‑way, round‑trip, multi‑city, and open‑jaw fares, retrieve cheapest‑date options, and obtain affiliate booking URLs. The service offers a free tier with 1,000 requests and usage‑based pricing thereafter, with no monthly minimums or hard rate limits. Documentation includes quickstart guides, API reference, and example code.
image: https://ignav.com/og-image.png
json_schemas:
- name: BookingLinksRequest
  property_count: 14
  slug: ignav-com-booking-links-request
- name: CheapestDatesRequest
  property_count: 16
  slug: ignav-com-cheapest-dates-request
- name: FareSearchRequest
  property_count: 13
  slug: ignav-com-fare-search-request
- name: FareSearchResponseModel
  property_count: 6
  slug: ignav-com-fare-search-response-model
- name: OneWayRequest
  property_count: 17
  slug: ignav-com-one-way-request
- name: RoundTripRequest
  property_count: 19
  slug: ignav-com-round-trip-request
jsonld:
- class_count: 30
  name: Ignav Com Context
  property_count: 80
  slug: ignav-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at ignav.com requiring OAuth.
  name: ignav-com MCP Server
  slug: ignav-com-mcp-yml
modified: '2026-10-30'
name: ignav-com
nav: Providers
network: true
overview: 'ignav-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Airports API, Fares API, and Health API. Tagged areas include Company, Flights, Travel, Pricing, and Data.


  The ignav-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ignav-com''s developer surface includes authentication, sandbox, signup flow, API reference, documentation, pricing, support, and 20 more developer resources.'
plans:
- name: Ignav Com Plans Pricing
  plan_count: 1
  slug: ignav-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Ignav Com Rate Limits
  slug: ignav-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: ignav-com API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 1
  slug: ignav-com-rules
scopes:
- name: Ignav Com Scopes
  scope_count: 0
  slug: ignav-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 61.2
    developer_ergonomics: 41.0
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ignav-com/ignav-com-2026-11-03T133640.png
security:
- kind: authentication
  name: Ignav Com Authentication
  slug: ignav-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ignav Com Domain Security
  slug: ignav-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: search-airports
  slug: ignav-com-search_airports
- name: search-fares
  slug: ignav-com-search_fares
slug: ignav-com
tags:
- Company
- Flights
- Travel
- Pricing
- Data
website: https://ignav.com/
---
