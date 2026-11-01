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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Mammoth Media API as documented publicly: 64 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Mammoth Media API
  slug: mammoth-la-api
artifact_total: 13
asyncapis:
- description: ''
  name: Mammoth La Webhooks
  slug: mammoth-la-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/mammoth-la/rate-limits/mammoth-la-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mammoth-la-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/mammoth-la/rules/mammoth-la-rules.yml
  title: ''
  type: Spectral
  url: rules/mammoth-la-rules.yml
- group: design
  href: https://artifacts.apis.io/mammoth-la/json-ld/mammoth-la-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mammoth-la-context.jsonld
- group: design
  href: https://artifacts.apis.io/mammoth-la/vocabulary/mammoth-la-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mammoth-la-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mammoth-la/asyncapi/mammoth-la-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mammoth-la-webhooks.yml
- group: design
  href: https://artifacts.apis.io/mammoth-la/data-model/mammoth-la-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mammoth-la-data-model.yml
- group: build
  href: https://artifacts.apis.io/mammoth-la/cli/mammoth-la-cli.yml
  title: ''
  type: CLI
  url: cli/mammoth-la-cli.yml
- group: auth
  href: https://artifacts.apis.io/mammoth-la/authentication/mammoth-la-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mammoth-la-authentication.yml
- group: design
  href: https://artifacts.apis.io/mammoth-la/conformance/mammoth-la-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mammoth-la-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mammoth-la/llms/mammoth-la-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mammoth-la-llms.txt
- group: agent
  href: https://artifacts.apis.io/mammoth-la/well-known/mammoth-la-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mammoth-la-well-known.yml
- group: other
  href: https://artifacts.apis.io/mammoth-la/hosts/mammoth-la-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mammoth-la-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tokenbot.com/home/api-docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://dev.tokenbot.com/
- group: auth
  href: https://artifacts.apis.io/mammoth-la/security/mammoth-la-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mammoth-la-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://mammoth.la
created: '2026-10-25'
description: TokenBot provides a platform that enables cryptocurrency traders to share and synchronize algorithmic and technical trades within Telegram and Discord groups. It allows users to connect exchange API keys to broadcast real‑time orders, receive alerts, and earn rewards through its TKB membership token. The service is aimed at crypto communities and traders seeking coordinated trading activity.
image: https://4266128855-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPazuVyhozCXsyQMYbQ%2Fuploads%2FNXEaplRH8atkjbUXrdNG%2FScreen_Shot_2023-01-18_at_9_51_26_PM.jpg?alt=media&token=c6deb894-d84f-4826-9887-499ce3c6d1dc
json_schemas:
- name: GetV1ExchangesResponse
  property_count: 2
  slug: mammoth-la-get-v1-exchanges-response
- name: GetV1HealthDetailedResponse
  property_count: 5
  slug: mammoth-la-get-v1-health-detailed-response
- name: GetV1SupportedExchangesResponse
  property_count: 2
  slug: mammoth-la-get-v1-supported-exchanges-response
- name: GetV1VersionResponse
  property_count: 6
  slug: mammoth-la-get-v1-version-response
- name: PostV1ExchangesTestRequest
  property_count: 4
  slug: mammoth-la-post-v1-exchanges-test-request
- name: PostV1TradesRequest
  property_count: 6
  slug: mammoth-la-post-v1-trades-request
jsonld:
- class_count: 17
  name: Mammoth La Context
  property_count: 30
  slug: mammoth-la-context
layout: provider
modified: '2026-10-25'
name: Mammoth Media
nav: Providers
network: true
overview: 'Mammoth Media is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Crypto Trading, Social Trading, Token Utility, and Community Platform.


  The Mammoth Media catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Mammoth Media''s developer surface includes CLI, authentication, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 2
  name: Mammoth La Rate Limits
  slug: mammoth-la-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Mammoth Media API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: mammoth-la-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 60.8
    catalog_earned_first_party: 8.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 35.0
    developer_ergonomics: 40.5
    discoverability: 48.2
    operational_transparency: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 18
      marker_coverage: 100.0
      total: 18
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mammoth La Authentication
  slug: mammoth-la-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Mammoth La Domain Security
  slug: mammoth-la-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mammoth-la
tags:
- Crypto Trading
- Social Trading
- Token Utility
- Community Platform
website: http://mammoth.la
---
