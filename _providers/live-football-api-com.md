---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Real-time football scores, lineups, standings and statistics via a simple REST API.
  name: Live Football API
  slug: live-football-api
- description: 'live-football-api-com API as documented publicly: 68 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: live-football-api-com API
  slug: live-football-api-com-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/live-football-api-com/rate-limits/live-football-api-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/live-football-api-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/live-football-api-com/plans/live-football-api-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/live-football-api-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/live-football-api-com/rules/live-football-api-com-rules.yml
  title: ''
  type: Spectral
  url: rules/live-football-api-com-rules.yml
- group: design
  href: https://artifacts.apis.io/live-football-api-com/json-ld/live-football-api-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/live-football-api-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/live-football-api-com/vocabulary/live-football-api-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/live-football-api-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/live-football-api-com/data-model/live-football-api-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/live-football-api-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/live-football-api-com/components/live-football-api-com-components.yml
  title: ''
  type: Components
  url: components/live-football-api-com-components.yml
- group: auth
  href: https://artifacts.apis.io/live-football-api-com/authentication/live-football-api-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/live-football-api-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/live-football-api-com/lifecycle/live-football-api-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/live-football-api-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/live-football-api-com/errors/live-football-api-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/live-football-api-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/live-football-api-com/conformance/live-football-api-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/live-football-api-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/live-football-api-com/llms/live-football-api-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/live-football-api-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/live-football-api-com/well-known/live-football-api-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/live-football-api-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/live-football-api-com/hosts/live-football-api-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/live-football-api-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/live-football-api-com/vendors/live-football-api-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/live-football-api-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/live-football-api-com/packages/live-football-api-com-packages.yml
  title: ''
  type: SDKs
  url: packages/live-football-api-com-packages.yml
- group: build
  href: https://artifacts.apis.io/live-football-api-com/packages/live-football-api-com-packages.yml
  title: ''
  type: Packages
  url: packages/live-football-api-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.live-football-api.com/
- group: start
  title: ''
  type: Login
  url: https://www.live-football-api.com/login
- group: auth
  href: https://artifacts.apis.io/live-football-api-com/security/live-football-api-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/live-football-api-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.live-football-api.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.live-football-api.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.live-football-api.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.live-football-api.com/docs#quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.live-football-api.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.live-football-api.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.live-football-api.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.live-football-api.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://live-football-api.com/
coverage:
  checked: '2026-10-31'
  detail: The provider's documentation is publicly readable but does not publish any machine‑readable OpenAPI, AsyncAPI, GraphQL SDL, or other contract.
  evidence:
  - status: 200
    url: https://www.live-football-api.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Live Football API provides real-time football scores, lineups, standings and statistics for over 1,400 leagues including Premier League, La Liga, and Champions League. Offered by FORCESCRIPTS LTD, a UK-registered software company delivering sports data. Developers can access up-to-date match information, player stats, and league tables, with a free trial and plans starting at $9.99.
image: https://www.live-football-api.com/assets/uploads/blog/2026/09/f1e93661f3f58e5cfc5d2fab.webp
json_schemas:
- name: GetApiV1TeamMatchesResponse
  property_count: 4
  slug: live-football-api-com-get-api-v1-team-matches-response
- name: GetH2HResponse
  property_count: 4
  slug: live-football-api-com-get-h2-hresponse
- name: GetInjuriesResponse
  property_count: 4
  slug: live-football-api-com-get-injuries-response
- name: GetPlayerDetailsResponse
  property_count: 4
  slug: live-football-api-com-get-player-details-response
- name: GetWidgetSessionPhpResponse
  property_count: 2
  slug: live-football-api-com-get-widget-session-php-response
- name: PostWebhookRegisterRequest
  property_count: 4
  slug: live-football-api-com-post-webhook-register-request
jsonld:
- class_count: 33
  name: Live Football Api Com Context
  property_count: 15
  slug: live-football-api-com-context
layout: provider
modified: '2026-10-30'
name: live-football-api-com
nav: Providers
network: true
overview: 'live-football-api-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API, Sports, Football, Real-time, and Data.


  The live-football-api-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  live-football-api-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Live Football Api Com Plans Pricing
  plan_count: 13
  slug: live-football-api-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Live Football Api Com Rate Limits
  slug: live-football-api-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: live-football-api-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: live-football-api-com-rules
scopes:
- name: Live Football Api Com Scopes
  scope_count: 0
  slug: live-football-api-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 94.3
    catalog_earned_first_party: 0.0
    catalog_gap: 20.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 45.6
    developer_ergonomics: 54.8
    discoverability: 57.1
    operational_transparency: 44.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Live Football Api Com Authentication
  slug: live-football-api-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Live Football Api Com Domain Security
  slug: live-football-api-com-domain-security
  summary_line: TLSv1.3
slug: live-football-api-com
tags:
- API
- Sports
- Football
- Real-time
- Data
website: https://www.live-football-api.com/
---
