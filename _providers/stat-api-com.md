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
  score: 50.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Stat Api Com Agentic Access
  operation_count: 341
  slug: stat-api-com-agentic-access
  summary_line: 341 operations
api_count: 1
apis:
- baseURL: https://api.stat-api.com
  baseurl_source: declared
  description: Read-only catalog of DFS tables.
  name: stat-api-com DFS API
  slug: stat-api-com-dfs-api
- baseURL: https://api.stat-api.com
  baseurl_source: declared
  description: Read-only catalog of MLB tables.
  name: stat-api-com MLB API
  slug: stat-api-com-mlb-api
- baseURL: https://api.stat-api.com
  baseurl_source: declared
  description: Read-only catalog of NBA tables.
  name: stat-api-com NBA API
  slug: stat-api-com-nba-api
- baseURL: https://api.stat-api.com
  baseurl_source: declared
  description: Read-only catalog of NFL tables.
  name: stat-api-com NFL API
  slug: stat-api-com-nfl-api
- baseURL: https://api.stat-api.com
  baseurl_source: declared
  description: NHL — schema is published but handlers return 503 until data is loaded.
  name: stat-api-com NHL API
  slug: stat-api-com-nhl-api
- baseURL: https://api.stat-api.com
  baseurl_source: declared
  description: Read-only catalog of PGA tables.
  name: stat-api-com PGA API
  slug: stat-api-com-pga-api
- baseURL: https://api.stat-api.com
  baseurl_source: declared
  description: Read-only catalog of Reference tables.
  name: stat-api-com Reference API
  slug: stat-api-com-reference-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/stat-api-com/agentic-access/stat-api-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stat-api-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/stat-api-com/plans/stat-api-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stat-api-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/stat-api-com/rules/stat-api-com-rules.yml
  title: ''
  type: Spectral
  url: rules/stat-api-com-rules.yml
- group: design
  href: https://artifacts.apis.io/stat-api-com/json-ld/stat-api-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stat-api-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/stat-api-com/vocabulary/stat-api-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stat-api-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/stat-api-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/stat-api-com/data-model/stat-api-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stat-api-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/stat-api-com/errors/stat-api-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stat-api-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/stat-api-com/conformance/stat-api-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stat-api-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/stat-api-com/llms/stat-api-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stat-api-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/stat-api-com/well-known/stat-api-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stat-api-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/stat-api-com/hosts/stat-api-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stat-api-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/stat-api-com/vendors/stat-api-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stat-api-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/stat-api-com/packages/stat-api-com-packages.yml
  title: ''
  type: SDKs
  url: packages/stat-api-com-packages.yml
- group: build
  href: https://artifacts.apis.io/stat-api-com/packages/stat-api-com-packages.yml
  title: ''
  type: Packages
  url: packages/stat-api-com-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://stat-api.com/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://stat-api.com/docs/examples/quickstart/
- group: auth
  href: https://artifacts.apis.io/stat-api-com/authentication/stat-api-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stat-api-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/stat-api-com/security/stat-api-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stat-api-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stat-api.com/
- group: docs
  title: ''
  type: Documentation
  url: https://stat-api.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://stat-api.com/docs/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://stat-api.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://stat-api.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://stat-api.com/insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stat-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stat-api.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stat-api.com/privacy/
created: '2026-10-31'
description: STAT-API provides a comprehensive sports data API delivering play-by-play data for major leagues (NFL, NBA, MLB, NHL, PGA Tour) and daily fantasy contest results from DraftKings and FanDuel, with tiered pricing starting at $49 per month and a free preview of sample data. The service offers real-time updates, historical archives, and extensive data dictionaries, supporting developers with SDKs, GraphQL, and detailed documentation.
image: https://stat-api.com/og/home-2026-10-18.png
json_schemas:
- name: DFSContestsProjections_DfsContestProjectionsResponse
  property_count: 10
  slug: stat-api-com-dfscontests-projections-dfs-contest-projections-response
- name: DFSContestsUserLineups_DfsContestUserLineupsResponse
  property_count: 9
  slug: stat-api-com-dfscontests-user-lineups-dfs-contest-user-lineups-response
- name: DFSSlatesContestOwnership_DfsSlateContestOwnershipResponse
  property_count: 16
  slug: stat-api-com-dfsslates-contest-ownership-dfs-slate-contest-ownership-response
- name: DFSSlatesProjections_DfsSlateProjectionsResponse
  property_count: 8
  slug: stat-api-com-dfsslates-projections-dfs-slate-projections-response
- name: NFLPlayByPlays
  property_count: 371
  slug: stat-api-com-nflplay-by-plays
- name: NFLSeasonsContext_NflContextResponse
  property_count: 21
  slug: stat-api-com-nflseasons-context-nfl-context-response
jsonld:
- class_count: 120
  name: Stat Api Com Context
  property_count: 758
  slug: stat-api-com-context
layout: provider
modified: '2026-10-31'
name: stat-api-com
nav: Providers
network: true
overview: 'stat-api-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including DFS API, MLB API, NBA API, and 4 more. Tagged areas include Sports, Data, DFS, and Fantasy.


  The stat-api-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  stat-api-com''s developer surface includes changelog, getting-started guide, authentication, documentation, API reference, pricing, support, and 21 more developer resources.'
plans:
- name: Stat Api Com Plans Pricing
  plan_count: 3
  slug: stat-api-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Stat Api Com Rate Limits
  slug: stat-api-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: stat-api-com API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: stat-api-com-rules
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 59.2
    developer_ergonomics: 43.3
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/stat-api-com/stat-api-com-2026-11-03T143746.png
security:
- kind: authentication
  name: Stat Api Com Authentication
  slug: stat-api-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stat Api Com Domain Security
  slug: stat-api-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stat-api-com
tags:
- Sports
- Data
- DFS
- Fantasy
website: https://stat-api.com/
---
