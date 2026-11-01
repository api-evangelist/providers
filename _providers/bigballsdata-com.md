---
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
    error_semantics: derived
    event_surface_described: unknown
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Unified sports data API aggregating multiple sources.
  name: Big Ball Sports API
  slug: big-ball-sports-api
- baseURL: https://api.bigballsdata.com
  baseurl_source: declared
  description: Unified sports data API (REST + GraphQL + WebSocket) aggregating 19+
  name: Big Ball Sports API API
  slug: big-ball-sports-api-api
artifact_total: 14
asyncapis:
- description: ''
  name: Bigballsdata Com Webhooks
  slug: bigballsdata-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/bigballsdata-com/rules/bigballsdata-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bigballsdata-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bigballsdata-com/json-ld/bigballsdata-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bigballsdata-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bigballsdata-com/vocabulary/bigballsdata-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bigballsdata-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bigballsdata-com/conformance/bigballsdata-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bigballsdata-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/bigballsdata-com/plans/bigballsdata-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bigballsdata-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bigballsdata-com/asyncapi/bigballsdata-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bigballsdata-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/bigballsdata-com/data-model/bigballsdata-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bigballsdata-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/bigballsdata-com/conventions/bigballsdata-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bigballsdata-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/bigballsdata-com/conventions/bigballsdata-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bigballsdata-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/bigballsdata-com/authentication/bigballsdata-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bigballsdata-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/bigballsdata-com/errors/bigballsdata-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bigballsdata-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/bigballsdata-com/llms/bigballsdata-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bigballsdata-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bigballsdata-com/well-known/bigballsdata-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bigballsdata-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bigballsdata-com/hosts/bigballsdata-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bigballsdata-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bigballsdata-com/vendors/bigballsdata-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bigballsdata-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bigballsdata.com/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://bigballsdata.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bigballsdata.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bigballsdata.com/pricing
- group: start
  title: ''
  type: Login
  url: https://bigballsdata.com/signin
- group: operate
  title: ''
  type: ChangeLog
  url: https://bigballsdata.com/whats-new
- group: company
  title: ''
  type: Blog
  url: https://bigballsdata.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://bigballsdata.com/docs/introduction
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.bigballsdata.com&quot;
- group: docs
  title: ''
  type: APIReference
  url: https://bigballsdata.com/docs/endpoints
- group: auth
  href: https://artifacts.apis.io/bigballsdata-com/security/bigballsdata-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigballsdata-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bigballsdata.com/
created: '2026-10-30'
description: bigballsdata-com provides a platform for aggregating and delivering large-scale data sets related to sports analytics, betting trends, and player performance metrics. The service offers APIs for accessing real-time and historical data, enabling developers to build applications in fantasy sports, betting platforms, and data-driven insights. This company aims to simplify data integration for sports tech solutions, delivering reliable, high‑volume datasets with comprehensive documentation and support.
image: https://bigballsdata.com/opengraph-image.png?62b0caddafddc9b0
json_schemas:
- name: Event
  property_count: 35
  slug: bigballsdata-com-event
- name: Match
  property_count: 16
  slug: bigballsdata-com-match
- name: NbaBoxScoreEntry
  property_count: 24
  slug: bigballsdata-com-nba-box-score-entry
- name: NbaPlayerAdvancedSeason
  property_count: 32
  slug: bigballsdata-com-nba-player-advanced-season
- name: NbaPlayerSeasonAverage
  property_count: 22
  slug: bigballsdata-com-nba-player-season-average
- name: NflPlayerWeekStat
  property_count: 64
  slug: bigballsdata-com-nfl-player-week-stat
jsonld:
- class_count: 56
  name: Bigballsdata Com Context
  property_count: 376
  slug: bigballsdata-com-context
layout: provider
modified: '2026-10-30'
name: bigballsdata-com
nav: Providers
network: true
overview: 'bigballsdata-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Big Ball Sports API API, and 1 more. Tagged areas include Company, Sports, Data, Analytics, and Betting.


  The bigballsdata-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  bigballsdata-com''s developer surface includes authentication, pricing, changelog, engineering blog, getting-started guide, API reference, and 21 more developer resources.'
plans:
- name: Bigballsdata Com Plans Pricing
  plan_count: 6
  slug: bigballsdata-com-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: bigballsdata-com API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 3
  slug: bigballsdata-com-rules
score:
  band: strong
  composite: 62.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 64.9
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 39.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bigballsdata Com Authentication
  slug: bigballsdata-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bigballsdata Com Domain Security
  slug: bigballsdata-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bigballsdata-com
tags:
- Company
- Sports
- Data
- Analytics
- Betting
website: https://bigballsdata.com/
---
