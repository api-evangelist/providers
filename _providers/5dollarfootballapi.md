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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: 5Dollarfootballapi Agentic Access
  operation_count: 15
  slug: 5dollarfootballapi-agentic-access
  summary_line: 15 operations
api_count: 1
apis:
- baseURL: https://api.5dollarfootballapi.com/v1
  baseurl_source: declared
  description: The bookmakers quoted by the odds endpoints.
  name: 5DollarFootballAPI Bookmakers API
  slug: 5dollarfootballapi-bookmakers-api
- baseURL: https://api.5dollarfootballapi.com/v1
  baseurl_source: declared
  description: The country master referenced by league and team records.
  name: 5DollarFootballAPI Countries API
  slug: 5dollarfootballapi-countries-api
- baseURL: https://api.5dollarfootballapi.com/v1
  baseurl_source: declared
  description: 'Matches: the daily window and per-fixture detail — events, statistics, odds and odds history.'
  name: 5DollarFootballAPI Fixtures API
  slug: 5dollarfootballapi-fixtures-api
- baseURL: https://api.5dollarfootballapi.com/v1
  baseurl_source: declared
  description: Competitions and their seasons, plus a whole season of fixtures.
  name: 5DollarFootballAPI Leagues API
  slug: 5dollarfootballapi-leagues-api
- baseURL: https://api.5dollarfootballapi.com/v1
  baseurl_source: declared
  description: League tables — points, and the corner and card tables.
  name: 5DollarFootballAPI Standings API
  slug: 5dollarfootballapi-standings-api
- baseURL: https://api.5dollarfootballapi.com/v1
  baseurl_source: declared
  description: Your plan, limits and usage.
  name: 5DollarFootballAPI Status API
  slug: 5dollarfootballapi-status-api
- baseURL: https://api.5dollarfootballapi.com/v1
  baseurl_source: declared
  description: Clubs and national teams, plus their fixture history.
  name: 5DollarFootballAPI Teams API
  slug: 5dollarfootballapi-teams-api
- baseURL: https://api.5dollarfootballapi.com/v1
  baseurl_source: declared
  description: The bookmakers quoted by the odds endpoints.
  name: 5DollarFootballAPI Bookmakers API
  slug: 5dollarfootballapi-bookmakers-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/5dollarfootballapi/agentic-access/5dollarfootballapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/5dollarfootballapi-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/5dollarfootballapi/plans/5dollarfootballapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/5dollarfootballapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/5dollarfootballapi/rules/5dollarfootballapi-rules.yml
  title: ''
  type: Spectral
  url: rules/5dollarfootballapi-rules.yml
- group: design
  href: https://artifacts.apis.io/5dollarfootballapi/json-ld/5dollarfootballapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/5dollarfootballapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/5dollarfootballapi/vocabulary/5dollarfootballapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/5dollarfootballapi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/5dollarfootballapi/data-model/5dollarfootballapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/5dollarfootballapi-data-model.yml
- group: operate
  href: https://artifacts.apis.io/5dollarfootballapi/changelog/5dollarfootballapi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/5dollarfootballapi-changelog.yml
- group: auth
  href: https://artifacts.apis.io/5dollarfootballapi/security/5dollarfootballapi-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/5dollarfootballapi-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/5dollarfootballapi/errors/5dollarfootballapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/5dollarfootballapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/5dollarfootballapi/conformance/5dollarfootballapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/5dollarfootballapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/5dollarfootballapi/llms/5dollarfootballapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/5dollarfootballapi-llms.txt
- group: auth
  href: https://artifacts.apis.io/5dollarfootballapi/well-known/5dollarfootballapi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/5dollarfootballapi-security.txt
- group: agent
  href: https://artifacts.apis.io/5dollarfootballapi/well-known/5dollarfootballapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/5dollarfootballapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/5dollarfootballapi/hosts/5dollarfootballapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/5dollarfootballapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/5dollarfootballapi/vendors/5dollarfootballapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/5dollarfootballapi-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://5dollarfootballapi.com/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://5dollarfootballapi.com/status
- group: auth
  href: https://artifacts.apis.io/5dollarfootballapi/authentication/5dollarfootballapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/5dollarfootballapi-authentication.yml
- group: auth
  href: https://artifacts.apis.io/5dollarfootballapi/security/5dollarfootballapi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/5dollarfootballapi-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/5dollarfootballapi/security/5dollarfootballapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/5dollarfootballapi-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://5dollarfootballapi.com/blog
- group: company
  title: ''
  type: Website
  url: https://5dollarfootballapi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://5dollarfootballapi.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://5dollarfootballapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://5dollarfootballapi.com/docs
- group: docs
  title: ''
  type: OpenAPI
  url: https://5dollarfootballapi.com/openapi.json
- group: other
  title: ''
  type: APIsJSON
  url: https://5dollarfootballapi.com/apis.json
- group: agent
  title: ''
  type: LlmsText
  url: https://5dollarfootballapi.com/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://5dollarfootballapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://5dollarfootballapi.com/signup
- group: operate
  title: ''
  type: ChangeLog
  url: https://5dollarfootballapi.com/docs/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://5dollarfootballapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://5dollarfootballapi.com/privacy
created: '2026-08-19'
description: A read‑only REST football (soccer) data API offering comprehensive live scores, detailed fixtures, league standings, team and player statistics, match events, corner and card data, as well as bookmaker odds and a status endpoint. It provides fifteen operations across seven tags, hosted on a versioned API under bearer‑token or API‑key authentication, priced affordably at $5 per month for developers seeking reliable sports data.
finops:
- has_sources: true
  method: derived
  name: 5Dollarfootballapi Finops
  primary_unit: ''
  service_category: ''
  slug: 5dollarfootballapi-finops
  template: true
image: https://5dollarfootballapi.com/logo.png
json_schemas:
- name: SuccessEnvelope
  property_count: 3
  slug: 5dollarfootballapi-success-envelope
jsonld:
- class_count: 3
  name: 5Dollarfootballapi Context
  property_count: 8
  slug: 5dollarfootballapi-context
layout: provider
modified: '2026-10-06'
name: 5DollarFootballAPI
nav: Providers
network: true
overview: '5DollarFootballAPI publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bookmakers API, Countries API, Fixtures API, and 5 more. Tagged areas include Football, Soccer, Sports, Sports Data, and Live Scores.


  The 5DollarFootballAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  5DollarFootballAPI''s developer surface includes changelog, authentication, engineering blog, documentation, API reference, pricing, signup flow, and 26 more developer resources.'
plans:
- name: 5Dollarfootballapi Plans Pricing
  plan_count: 6
  slug: 5dollarfootballapi-plans-pricing
- name: 5Dollarfootballapi Price Estimates
  plan_count: 0
  slug: 5dollarfootballapi-price-estimates
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: 5DollarFootballAPI API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: 5dollarfootballapi-rules
score:
  band: strong
  composite: 57.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 65.2
    catalog_earned_first_party: 12.0
    catalog_gap: 49.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 80.3
    contract_governance: 22.0
    contract_quality: 64.2
    developer_ergonomics: 40.5
    discoverability: 73.2
    operational_transparency: 34.2
  previous_composite: 58.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/5dollarfootballapi/5dollarfootballapi-2026-09-02T144104.png
security:
- kind: authentication
  name: 5Dollarfootballapi Authentication
  slug: 5dollarfootballapi-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: 5Dollarfootballapi Domain Security
  slug: 5dollarfootballapi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: 5Dollarfootballapi Vulnerability Disclosure
  slug: 5dollarfootballapi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 5dollarfootballapi
tags:
- Football
- Soccer
- Sports
- Sports Data
- Live Scores
- Fixtures
- Standings
- Statistics
- Odds
- Bookmakers
website: https://5dollarfootballapi.com
---
