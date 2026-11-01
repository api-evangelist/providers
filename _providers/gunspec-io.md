---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Gunspec Io Agentic Access
  operation_count: 162
  slug: gunspec-io-agentic-access
  summary_line: 162 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: 'The authenticated account surface: your favorites, data reports, support tickets, webhook endpoints, and API usage. Requires an API key belonging to a user account.'
  name: gunspec-io Account API
  slug: gunspec-io-account-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: Specific ammunition loads per caliber, with ballistics calculation and bullet diagrams
  name: gunspec-io Ammunition API
  slug: gunspec-io-ammunition-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: Ammunition calibers, cartridge specifications, comparison, and family relationships
  name: gunspec-io Calibers API
  slug: gunspec-io-calibers-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: Firearm categories (pistol, rifle, shotgun, etc.)
  name: gunspec-io Categories API
  slug: gunspec-io-categories-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: 'What changed in the catalogue: records added, updated, removed and merged, with the fields that moved, as a list to read forward from and as RSS'
  name: gunspec-io Changes API
  slug: gunspec-io-changes-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: Publicly shared user collections
  name: gunspec-io Collections API
  slug: gunspec-io-collections-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: 'Mount interfaces, the attachment catalog and what fits what: a firearm''s resolved interfaces, the attachments that fit it (direct, through a named adapter, or curated), the firearms an attachment fits'
  name: gunspec-io Compatibility API
  slug: gunspec-io-compatibility-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: Armed conflicts referenced by firearm service history
  name: gunspec-io Conflicts API
  slug: gunspec-io-conflicts-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: Changelog entries and blog posts
  name: gunspec-io Content API
  slug: gunspec-io-content-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: Countries of origin and national arsenals
  name: gunspec-io Countries API
  slug: gunspec-io-countries-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: Field coverage and confidence metrics for the dataset
  name: gunspec-io Data Quality API
  slug: gunspec-io-data-quality-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: 'Derived views over firearms: family tree, similar models, adoption map, dimensions, game profile, and the cost of marching with them'
  name: gunspec-io Firearm Analysis API
  slug: gunspec-io-firearm-analysis-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: 'Cross-catalog queries: random picks, top lists, head-to-head, and filters by feature, action, material, designer, or conflict'
  name: gunspec-io Firearm Discovery API
  slug: gunspec-io-firearm-discovery-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: Firearms specifications, search, comparison, and related data
  name: gunspec-io Firearms API
  slug: gunspec-io-firearms-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: 'Game-balance analysis: balance report, tier list, matchups, role roster, and stat distribution'
  name: gunspec-io Game API
  slug: gunspec-io-game-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: Versioned game stats snapshots. Pin your game to a specific dataset version (e.g., "2025.1") so rebalancing changes don't break your build mid-development. List available versions, then query firearms
  name: gunspec-io Game Stats API
  slug: gunspec-io-game-stats-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: Health and readiness checks
  name: gunspec-io Health API
  slug: gunspec-io-health-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: Firearm manufacturers, their products, timelines, and statistics
  name: gunspec-io Manufacturers API
  slug: gunspec-io-manufacturers-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: 'Research papers: technical reports on the catalogue, each with its authors, review status and the requests that reproduce its figures'
  name: gunspec-io Papers API
  slug: gunspec-io-papers-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: New firearm models, each with the dates it was announced and first read, its alternate names and the sources that name it
  name: gunspec-io Releases API
  slug: gunspec-io-releases-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: 'The seller layer: who stocks a catalogued part or firearm, and where to buy it. Public reads on any record, and a private surface for an Enterprise shop to keep its own listings from a server. GunSpec'
  name: gunspec-io Seller API
  slug: gunspec-io-seller-api
- baseURL: https://api.gunspec.io
  baseurl_source: declared
  description: 'Aggregate database statistics: coverage, distribution by category, era, country, material, and action type'
  name: gunspec-io Statistics API
  slug: gunspec-io-statistics-api
artifact_total: 39
common:
- group: agent
  href: https://artifacts.apis.io/gunspec-io/agentic-access/gunspec-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gunspec-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/gunspec-io/rate-limits/gunspec-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gunspec-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gunspec-io/plans/gunspec-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gunspec-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gunspec-io/rules/gunspec-io-rules.yml
  title: ''
  type: Spectral
  url: rules/gunspec-io-rules.yml
- group: design
  href: https://artifacts.apis.io/gunspec-io/json-ld/gunspec-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gunspec-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/gunspec-io/vocabulary/gunspec-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gunspec-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gunspec-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gunspec-io/data-model/gunspec-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gunspec-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/gunspec-io/changelog/gunspec-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gunspec-io-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://gunspec.io/en/vulnerability-disclosure
- group: auth
  href: https://artifacts.apis.io/gunspec-io/authentication/gunspec-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gunspec-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/gunspec-io/lifecycle/gunspec-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gunspec-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gunspec-io/errors/gunspec-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gunspec-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gunspec-io/conformance/gunspec-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gunspec-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gunspec-io/llms/gunspec-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gunspec-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/gunspec-io/well-known/gunspec-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gunspec-io-security.txt
- group: agent
  href: https://artifacts.apis.io/gunspec-io/well-known/gunspec-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gunspec-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/gunspec-io/hosts/gunspec-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gunspec-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/gunspec-io/vendors/gunspec-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gunspec-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/gunspec-io/packages/gunspec-io-packages.yml
  title: ''
  type: SDKs
  url: packages/gunspec-io-packages.yml
- group: build
  href: https://artifacts.apis.io/gunspec-io/packages/gunspec-io-packages.yml
  title: ''
  type: Packages
  url: packages/gunspec-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gunspec.io/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gunspec.io/en/privacy
- group: start
  title: ''
  type: Login
  url: https://app.gunspec.io/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gunspec
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.gunspec.io/en/changelog
- group: company
  title: ''
  type: Blog
  url: https://blog.gunspec.io/en/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gunspec.io/en/sdk/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gunspec.io/llms.txt
- group: auth
  href: https://artifacts.apis.io/gunspec-io/security/gunspec-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gunspec-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gunspec-io/security/gunspec-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gunspec-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gunspec.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gunspec.io
- group: commercial
  title: ''
  type: Pricing
  url: https://gunspec.io/en/pricing
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/QbN5GhwtgU
created: '2026-10-30'
description: 'A firearm database API for developers: specifications for over 8,500 guns, every figure sourced. The REST API offers endpoints for firearms, ammunition, manufacturers, and accessories, plus SDKs for popular languages and an MCP server. A free plan is available, with paid tiers for higher rate limits.'
image: https://gunspec.io/logo/logo.svg
json_schemas:
- name: AmmunitionLoad
  property_count: 25
  slug: gunspec-io-ammunition-load
- name: ApiContractRun
  property_count: 14
  slug: gunspec-io-api-contract-run
- name: Caliber
  property_count: 39
  slug: gunspec-io-caliber
- name: FirearmListItem
  property_count: 17
  slug: gunspec-io-firearm-list-item
- name: FirearmSearchResult
  property_count: 20
  slug: gunspec-io-firearm-search-result
- name: SdkVerificationRun
  property_count: 12
  slug: gunspec-io-sdk-verification-run
jsonld:
- class_count: 88
  name: Gunspec Io Context
  property_count: 316
  slug: gunspec-io-context
layout: provider
modified: '2026-10-30'
name: gunspec-io
nav: Providers
network: true
overview: 'gunspec-io publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Ammunition API, Calibers API, and 19 more. Tagged areas include Firearms, API, Database, Specifications, and SDK.


  The gunspec-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  gunspec-io''s developer surface includes changelog, authentication, engineering blog, getting-started guide, API reference, documentation, pricing, and 28 more developer resources.'
plans:
- name: Gunspec Io Plans Pricing
  plan_count: 4
  slug: gunspec-io-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 12
  name: Gunspec Io Rate Limits
  slug: gunspec-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: gunspec-io API Rules
  rule_count: 18
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 6
  slug: gunspec-io-rules
scopes:
- name: Gunspec Io Scopes
  scope_count: 0
  slug: gunspec-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 70.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 65.2
    developer_ergonomics: 61.2
    discoverability: 66.1
    operational_transparency: 60.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gunspec Io Authentication
  slug: gunspec-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Gunspec Io Domain Security
  slug: gunspec-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gunspec Io Vulnerability Disclosure
  slug: gunspec-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: list-firearms
  slug: gunspec-io-list-firearms
- name: search-firearms
  slug: gunspec-io-search-firearms
slug: gunspec-io
tags:
- Firearms
- API
- Database
- Specifications
- SDK
- MCP
website: https://gunspec.io/
---
