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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'eloedge-com API as documented publicly: 29 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: eloedge-com API
  slug: eloedge-com-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/eloedge-com/plans/eloedge-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eloedge-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/eloedge-com/rules/eloedge-com-rules.yml
  title: ''
  type: Spectral
  url: rules/eloedge-com-rules.yml
- group: design
  href: https://artifacts.apis.io/eloedge-com/json-ld/eloedge-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/eloedge-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/eloedge-com/vocabulary/eloedge-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eloedge-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/eloedge-com/data-model/eloedge-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eloedge-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/eloedge-com/changelog/eloedge-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/eloedge-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/eloedge-com/authentication/eloedge-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eloedge-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/eloedge-com/conformance/eloedge-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eloedge-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/eloedge-com/llms/eloedge-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eloedge-com-llms.txt
- group: other
  href: https://artifacts.apis.io/eloedge-com/hosts/eloedge-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eloedge-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/eloedge-com/vendors/eloedge-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eloedge-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://eloedge.com/status
- group: auth
  title: ''
  type: Security
  url: https://eloedge.com/security
- group: start
  title: ''
  type: Login
  url: https://eloedge.com/signin
- group: start
  title: ''
  type: GettingStarted
  url: https://eloedge.com/docs/agent
- group: auth
  href: https://artifacts.apis.io/eloedge-com/security/eloedge-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/eloedge-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/eloedge-com/security/eloedge-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eloedge-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eloedge.com/
- group: docs
  title: ''
  type: Documentation
  url: https://eloedge.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://eloedge.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eloedge.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eloedge.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://eloedge.com/support
coverage:
  checked: '2026-10-30'
  detail: Docs at https://eloedge.com/docs are rendered HTML with no machine‑readable OpenAPI/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://eloedge.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: EloEdge provides a platform for building AI-powered trading agents that operate in prediction markets. It offers live market data feeds, settled market outcomes, and integrates with large language models like Claude and Cursor via a simple MCP URL, a JSON API, and SQL access. Users can start for free, leveraging the service to create custom agents that analyze and trade on prediction market information.
image: https://eloedge.com/opengraph-image?fd21e3fefc087a76
json_schemas:
- name: GetApiV1Commodity15MWindowsResponse
  property_count: 5
  slug: eloedge-com-get-api-v1-commodity15-mwindows-response
- name: GetApiV1HistoryResponse
  property_count: 5
  slug: eloedge-com-get-api-v1-history-response
- name: GetApiV1ModelPAtResponse
  property_count: 5
  slug: eloedge-com-get-api-v1-model-pat-response
- name: GetApiV1PolymarketCryptoHourlyResponse
  property_count: 5
  slug: eloedge-com-get-api-v1-polymarket-crypto-hourly-response
- name: GetApiV1PolymarketCrypto5MWindowsResponse
  property_count: 11
  slug: eloedge-com-get-api-v1-polymarket-crypto5-mwindows-response
- name: GetApiV1WindowsResponse
  property_count: 5
  slug: eloedge-com-get-api-v1-windows-response
jsonld:
- class_count: 24
  name: Eloedge Com Context
  property_count: 53
  slug: eloedge-com-context
layout: provider
modified: '2026-10-30'
name: eloedge-com
nav: Providers
network: true
overview: 'eloedge-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Prediction-Market, Trading-Agent, MCP, and Data-Feeds.


  The eloedge-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  eloedge-com''s developer surface includes changelog, authentication, getting-started guide, documentation, pricing, support, and 17 more developer resources.'
plans:
- name: Eloedge Com Plans Pricing
  plan_count: 2
  slug: eloedge-com-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: eloedge-com API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: eloedge-com-rules
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 24.7
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 42.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 18
      marker_coverage: 100.0
      total: 18
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Eloedge Com Authentication
  slug: eloedge-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Eloedge Com Domain Security
  slug: eloedge-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Eloedge Com Vulnerability Disclosure
  slug: eloedge-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: eloedge-com
tags:
- AI
- Prediction-Market
- Trading-Agent
- MCP
- Data-Feeds
- Platform
website: https://eloedge.com/
---
