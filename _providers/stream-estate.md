---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: unknown
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Stream Estate Agentic Access
  operation_count: 13
  slug: stream-estate-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.stream.estate
  baseurl_source: declared
  description: Market indicators, points of interest and location lookups.
  name: stream-estate Indicators API
  slug: stream-estate-indicators-api
- baseURL: https://api.stream.estate
  baseurl_source: declared
  description: Query aggregated real estate properties and their adverts.
  name: stream-estate Properties API
  slug: stream-estate-properties-api
- baseURL: https://api.stream.estate
  baseurl_source: declared
  description: Saved searches with webhook or email notifications.
  name: stream-estate Searches API
  slug: stream-estate-searches-api
- baseURL: https://api.stream.estate
  baseurl_source: declared
  description: Tools to test webhook integrations.
  name: stream-estate Webhooks API
  slug: stream-estate-webhooks-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/stream-estate/agentic-access/stream-estate-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stream-estate-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/stream-estate/rules/stream-estate-rules.yml
  title: ''
  type: Spectral
  url: rules/stream-estate-rules.yml
- group: design
  href: https://artifacts.apis.io/stream-estate/json-ld/stream-estate-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stream-estate-context.jsonld
- group: design
  href: https://artifacts.apis.io/stream-estate/vocabulary/stream-estate-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stream-estate-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/stream-estate/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/stream-estate/data-model/stream-estate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stream-estate-data-model.yml
- group: operate
  href: https://artifacts.apis.io/stream-estate/changelog/stream-estate-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/stream-estate-changelog.yml
- group: design
  href: https://artifacts.apis.io/stream-estate/conventions/stream-estate-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stream-estate-conventions.yml
- group: auth
  href: https://artifacts.apis.io/stream-estate/authentication/stream-estate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stream-estate-authentication.yml
- group: design
  href: https://artifacts.apis.io/stream-estate/errors/stream-estate-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stream-estate-problem-types.yml
- group: design
  href: https://artifacts.apis.io/stream-estate/conformance/stream-estate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stream-estate-conformance.yml
- group: agent
  href: https://artifacts.apis.io/stream-estate/llms/stream-estate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stream-estate-llms.txt
- group: other
  href: https://artifacts.apis.io/stream-estate/a2a/stream-estate-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/stream-estate-a2a.yml
- group: agent
  href: https://artifacts.apis.io/stream-estate/mcp/stream-estate-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stream-estate-mcp.yml
- group: agent
  href: https://artifacts.apis.io/stream-estate/well-known/stream-estate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stream-estate-well-known.yml
- group: other
  href: https://artifacts.apis.io/stream-estate/hosts/stream-estate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stream-estate-hosts.yml
- group: other
  href: https://artifacts.apis.io/stream-estate/vendors/stream-estate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stream-estate-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://stream.estate/legal/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.stream.estate/changelog
- group: start
  title: ''
  type: SignUp
  url: https://stream.estate/signup
- group: auth
  href: https://artifacts.apis.io/stream-estate/security/stream-estate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stream-estate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stream.estate/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stream.estate
- group: docs
  title: ''
  type: APIReference
  url: https://docs.stream.estate
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stream.estate/introduction
- group: operate
  title: ''
  type: Support
  url: https://stream.estate/contact
- group: company
  title: ''
  type: Blog
  url: https://stream.estate/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StreamEstate
- group: commercial
  title: ''
  type: Pricing
  url: https://stream.estate/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stream.estate/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stream.estate/privacy
created: '2026-10-31'
description: Stream.Estate provides a real-time real estate data API for PropTech companies, delivering over 50 million deduplicated property listings sourced from more than 1,500 data providers across France. The platform offers comprehensive market analytics, property insights, and live updates, enabling developers to build valuation tools, lead generation widgets, portfolio analysis, and market monitoring solutions. With robust API endpoints, webhook notifications, and flexible pricing plans, Stream.Estate empowers businesses to integrate accurate property data quickly and reliably.
image: https://stream.estate/img/logo-dark.png
json_schemas:
- name: PricePerMeterCollection
  property_count: 4
  slug: stream-estate-price-per-meter-collection
- name: PropertyCollection
  property_count: 4
  slug: stream-estate-property-collection
- name: PropertyDocument
  property_count: 30
  slug: stream-estate-property-document
- name: SearchCollection
  property_count: 4
  slug: stream-estate-search-collection
- name: SearchInput
  property_count: 40
  slug: stream-estate-search-input
- name: Search
  property_count: 42
  slug: stream-estate-search
jsonld:
- class_count: 25
  name: Stream Estate Context
  property_count: 128
  slug: stream-estate-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.stream.estate.
  name: stream-estate MCP Server
  slug: stream-estate-mcp-yml
modified: '2026-10-31'
name: stream-estate
nav: Providers
network: true
overview: 'stream-estate publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Indicators API, Properties API, Searches API, and 1 more. Tagged areas include RealEstate, PropTech, DataAPI, MarketAnalytics, and Valuation.


  The stream-estate catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  stream-estate''s developer surface includes changelog, authentication, signup flow, documentation, API reference, getting-started guide, support, and 24 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: stream-estate API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: stream-estate-rules
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 62.1
    developer_ergonomics: 54.0
    discoverability: 65.0
    operational_transparency: 31.6
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
  name: Stream Estate Authentication
  slug: stream-estate-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stream Estate Domain Security
  slug: stream-estate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: search-properties
  slug: stream-estate-search-properties
slug: stream-estate
tags:
- RealEstate
- PropTech
- DataAPI
- MarketAnalytics
- Valuation
website: https://stream.estate/
---
