---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-10-31'
api_count: 3
apis:
- description: Birdeye Data provides market data APIs for Solana blockchain assets.
  name: Birdeye Data API
  slug: birdeye-data-api
- baseURL: https://public-api.birdeye.so
  baseurl_source: declared
  description: 'Birdeye (Solana data) data API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Birdeye (Solana data) data API
  slug: data-api
- baseURL: https://public-api.birdeye.so
  baseurl_source: declared
  description: 'Birdeye (Solana data) resources API as documented publicly: 66 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Birdeye (Solana data) resources API
  slug: resources-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/birdeye-so/rules/birdeye-so-rules.yml
  title: ''
  type: Spectral
  url: rules/birdeye-so-rules.yml
- group: design
  href: https://artifacts.apis.io/birdeye-so/json-ld/birdeye-so-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/birdeye-so-context.jsonld
- group: design
  href: https://artifacts.apis.io/birdeye-so/vocabulary/birdeye-so-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/birdeye-so-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/birdeye-so/data-model/birdeye-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/birdeye-so-data-model.yml
- group: operate
  href: https://artifacts.apis.io/birdeye-so/changelog/birdeye-so-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/birdeye-so-changelog.yml
- group: auth
  href: https://artifacts.apis.io/birdeye-so/authentication/birdeye-so-authentication.yml
  title: ''
  type: Authentication
  url: authentication/birdeye-so-authentication.yml
- group: design
  href: https://artifacts.apis.io/birdeye-so/conformance/birdeye-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/birdeye-so-conformance.yml
- group: agent
  href: https://artifacts.apis.io/birdeye-so/llms/birdeye-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/birdeye-so-llms.txt
- group: other
  href: https://artifacts.apis.io/birdeye-so/a2a/birdeye-so-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/birdeye-so-a2a.yml
- group: other
  href: https://artifacts.apis.io/birdeye-so/hosts/birdeye-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/birdeye-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/birdeye-so/vendors/birdeye-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/birdeye-so-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.birdeye.so/docs/resources/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.birdeye.so/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://birdeye.so/data-api/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://data.birdeye.so/docs/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://data.birdeye.so/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.birdeye.so/
- group: auth
  href: https://artifacts.apis.io/birdeye-so/security/birdeye-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/birdeye-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://birdeye.so/
coverage:
  checked: '2026-10-27'
  detail: Documentation is available but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found.
  evidence:
  - status: 200
    url: https://data.birdeye.so/docs/getting-started
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Birdeye (Solana data) provides a comprehensive token tracking and analytics platform for Solana and other blockchain ecosystems. It offers live price data, charts, trade histories, and advanced metrics such as supercharts and perps. Users can explore trending tokens, discover market trends, and access detailed token information through an intuitive web interface and API. The service aims to empower traders, developers, and analysts with real-time on-chain data and insights across multiple chains including Solana, BNB Chain, Ethereum, and more.
image: https://birdeye.so/opengraph-image.png
json_schemas:
- name: GetDefiHistoryPriceResponse
  property_count: 2
  slug: birdeye-so-get-defi-history-price-response
- name: GetDefiMultiPriceResponse
  property_count: 2
  slug: birdeye-so-get-defi-multi-price-response
- name: GetDefiOhlcvPairResponse
  property_count: 2
  slug: birdeye-so-get-defi-ohlcv-pair-response
- name: GetDefiOhlcvResponse
  property_count: 2
  slug: birdeye-so-get-defi-ohlcv-response
- name: GetDefiPriceResponse
  property_count: 2
  slug: birdeye-so-get-defi-price-response
- name: PostDefiMultiPriceResponse
  property_count: 2
  slug: birdeye-so-post-defi-multi-price-response
jsonld:
- class_count: 10
  name: Birdeye So Context
  property_count: 4
  slug: birdeye-so-context
layout: provider
modified: '2026-10-27'
name: Birdeye (Solana data)
nav: Providers
network: true
overview: 'Birdeye (Solana data) is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including data API, resources API, and 1 more. Tagged areas include Company, Blockchain, Data, Analytics, and Token.


  The Birdeye (Solana data) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Birdeye (Solana data)''s developer surface includes changelog, authentication, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Birdeye (Solana data) API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: birdeye-so-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 24.1
    developer_ergonomics: 33.3
    discoverability: 71.4
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
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
  name: Birdeye So Authentication
  slug: birdeye-so-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Birdeye So Domain Security
  slug: birdeye-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: birdeye-so
tags:
- Company
- Blockchain
- Data
- Analytics
- Token
website: https://birdeye.so/
---
