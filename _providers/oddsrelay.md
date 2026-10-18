---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Oddsrelay Agentic Access
  operation_count: 14
  slug: oddsrelay-agentic-access
  summary_line: 14 operations
api_count: 2
apis:
- baseURL: https://api.oddsrelay.io
  baseurl_source: declared
  description: Usage and prices. Free.
  name: OddsRelay Account API
  slug: oddsrelay-account-api
- baseURL: https://api.oddsrelay.io
  baseurl_source: declared
  description: Sports, events, venues, regions. Free.
  name: OddsRelay Discovery API
  slug: oddsrelay-discovery-api
- baseURL: https://api.oddsrelay.io
  baseurl_source: declared
  description: Matched boards, raw, one event.
  name: OddsRelay Odds API
  slug: oddsrelay-odds-api
- baseURL: https://api.oddsrelay.io
  baseurl_source: declared
  description: Coverage, status, health, liveness and this document.
  name: OddsRelay Service API
  slug: oddsrelay-service-api
artifact_total: 18
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/agentic-access/oddsrelay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/oddsrelay-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/rate-limits/oddsrelay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/oddsrelay-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/plans/oddsrelay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/oddsrelay-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/rules/oddsrelay-rules.yml
  title: ''
  type: Spectral
  url: rules/oddsrelay-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/json-ld/oddsrelay-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oddsrelay-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/vocabulary/oddsrelay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/oddsrelay-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/data-model/oddsrelay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/oddsrelay-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/changelog/oddsrelay-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/oddsrelay-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/conventions/oddsrelay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/oddsrelay-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/security/oddsrelay-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/oddsrelay-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/lifecycle/oddsrelay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/oddsrelay-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/errors/oddsrelay-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/oddsrelay-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/errors/oddsrelay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/oddsrelay-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/conformance/oddsrelay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/oddsrelay-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/llms/oddsrelay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oddsrelay-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/well-known/oddsrelay-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/oddsrelay-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/well-known/oddsrelay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/oddsrelay-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/hosts/oddsrelay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oddsrelay-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/vendors/oddsrelay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oddsrelay-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/packages/oddsrelay-packages.yml
  title: ''
  type: SDKs
  url: packages/oddsrelay-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/packages/oddsrelay-packages.yml
  title: ''
  type: Packages
  url: packages/oddsrelay-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://oddsrelay.io/status
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.oddsrelay.io</span
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/authentication/oddsrelay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/oddsrelay-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/security/oddsrelay-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/oddsrelay-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/security/oddsrelay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oddsrelay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oddsrelay.io
- group: docs
  title: ''
  type: Documentation
  url: https://oddsrelay.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://oddsrelay.io/docs/reference
- group: company
  title: ''
  type: Blog
  url: https://oddsrelay.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://oddsrelay.io/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://oddsrelay.io/docs/guides/quickstart
- group: start
  title: ''
  type: Login
  url: https://app.oddsrelay.io/login
- group: build
  title: ''
  type: Postman
  url: https://oddsrelay.io/docs/oddsrelay.postman_collection.json
- group: commercial
  title: ''
  type: Pricing
  url: https://oddsrelay.io/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oddsrelay.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.oddsrelay.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oddsrelay.io/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oddsrelay
created: '2026-10-09'
description: 'OddsRelay is a UK-based odds-data API for businesses, serving prices from 140+ bookmakers (60+ live in the UK & Ireland) through one keyed REST API: each bookmaker''s raw prices, and matched feeds pairing every bookmaker back price with the best exchange lay price on Betfair, Smarkets, Matchbook and BETDAQ plus the liquidity at that lay. It is a data supplier, not an operator, and takes no bets.'
image: https://oddsrelay.io/og.png
json_schemas:
- name: CoverageKeyed
  property_count: 3
  slug: oddsrelay-coverage-keyed
- name: CoverageSummary
  property_count: 4
  slug: oddsrelay-coverage-summary
- name: MatchedEvent
  property_count: 9
  slug: oddsrelay-matched-event
- name: RawEvent
  property_count: 8
  slug: oddsrelay-raw-event
- name: Regions
  property_count: 3
  slug: oddsrelay-regions
- name: Usage
  property_count: 9
  slug: oddsrelay-usage
jsonld:
- class_count: 22
  name: Oddsrelay Context
  property_count: 62
  slug: oddsrelay-context
layout: provider
modified: '2026-10-09'
name: OddsRelay
nav: Providers
network: true
overview: 'OddsRelay publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Discovery API, Odds API, and 1 more. Tagged areas include Company, Sports Betting, Odds, Sports Data, and Matched Betting.


  The OddsRelay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OddsRelay''s developer surface includes changelog, authentication, documentation, API reference, engineering blog, getting-started guide, pricing, and 33 more developer resources.'
plans:
- name: Oddsrelay Plans Pricing
  plan_count: 5
  slug: oddsrelay-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Oddsrelay Rate Limits
  slug: oddsrelay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: OddsRelay API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: oddsrelay-rules
score:
  band: exemplar
  composite: 67.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 66.7
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 78.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 66.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/oddsrelay/refs/heads/main/screenshots/oddsrelay-2026-10-11T111808.png
security:
- kind: authentication
  name: Oddsrelay Authentication
  slug: oddsrelay-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Oddsrelay Domain Security
  slug: oddsrelay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oddsrelay Vulnerability Disclosure
  slug: oddsrelay-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: oddsrelay
tags:
- Company
- Sports Betting
- Odds
- Sports Data
- Matched Betting
- Data Feed
website: https://oddsrelay.io
---
