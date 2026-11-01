---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Market-State Brief API providing stock, ETF, and crypto ticker summaries.
  name: Patternfetch API
  slug: patternfetch-api
- baseURL: https://patternfetch.com
  baseurl_source: declared
  description: 'Agent-first API + MCP: a stock, ETF, or crypto ticker + timeframe -> a token-compact market-state brief (compact candles, chart/candlestick patterns, support/resistance, regime, interpreted indicators'
  name: patternfetch Api API
  slug: patternfetch-api-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/patternfetch-com/rules/patternfetch-com-rules.yml
  title: ''
  type: Spectral
  url: rules/patternfetch-com-rules.yml
- group: design
  href: https://artifacts.apis.io/patternfetch-com/json-ld/patternfetch-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/patternfetch-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/patternfetch-com/vocabulary/patternfetch-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/patternfetch-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/patternfetch-com/conformance/patternfetch-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/patternfetch-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/patternfetch-com/plans/patternfetch-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/patternfetch-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/patternfetch-com/data-model/patternfetch-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/patternfetch-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/patternfetch-com/authentication/patternfetch-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/patternfetch-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/patternfetch-com/errors/patternfetch-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/patternfetch-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/patternfetch-com/llms/patternfetch-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/patternfetch-com-llms.txt
- group: other
  href: https://artifacts.apis.io/patternfetch-com/a2a/patternfetch-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/patternfetch-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/patternfetch-com/mcp/patternfetch-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/patternfetch-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/patternfetch-com/well-known/patternfetch-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/patternfetch-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/patternfetch-com/hosts/patternfetch-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/patternfetch-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/patternfetch-com/vendors/patternfetch-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/patternfetch-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://patternfetch.com/media/digest.mp4
- group: auth
  href: https://artifacts.apis.io/patternfetch-com/security/patternfetch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/patternfetch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://patternfetch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://patternfetch.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://patternfetch.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://patternfetch.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://patternfetch.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://patternfetch.com/status
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MarvinRey7879
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/workspace/patternfetch
created: '2026-10-30'
description: Patternfetch provides a Market-State Brief API and MCP for stocks, ETFs, and crypto. It delivers concise market state summaries, pattern frequencies, and indicator interpretations in a token-efficient format, enabling developers to integrate market insights without handling raw candle data. The service offers endpoints for ticker data across multiple timeframes, pricing details, and comprehensive documentation, targeting fintech applications, trading bots, and analytics platforms.
image: https://patternfetch.com/og.png
json_schemas:
- name: Brief
  property_count: 6
  slug: patternfetch-com-brief
- name: MultiQuery
  property_count: 4
  slug: patternfetch-com-multi-query
- name: MultiResponse
  property_count: 6
  slug: patternfetch-com-multi-response
- name: Query
  property_count: 4
  slug: patternfetch-com-query
- name: ScanRequest
  property_count: 7
  slug: patternfetch-com-scan-request
- name: WatchSubscription
  property_count: 13
  slug: patternfetch-com-watch-subscription
jsonld:
- class_count: 17
  name: Patternfetch Com Context
  property_count: 70
  slug: patternfetch-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at patternfetch.com.
  name: patternfetch-com MCP Server
  slug: patternfetch-com-mcp-yml
modified: '2026-10-30'
name: patternfetch-com
nav: Providers
network: true
overview: 'patternfetch-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including patternfetch Api API, and 1 more. Tagged areas include Fintech, MarketData, API, Stocks, and Crypto.


  The patternfetch-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  patternfetch-com''s developer surface includes authentication, documentation, pricing, support, and 20 more developer resources.'
plans:
- name: Patternfetch Com Plans Pricing
  plan_count: 2
  slug: patternfetch-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: patternfetch-com API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 2
  slug: patternfetch-com-rules
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 84.9
    catalog_earned_first_party: 0.0
    catalog_gap: 30.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.5
    contract_governance: 79.1
    contract_quality: 50.7
    developer_ergonomics: 31.0
    discoverability: 66.7
    operational_transparency: 5.3
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
  name: Patternfetch Com Authentication
  slug: patternfetch-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Patternfetch Com Domain Security
  slug: patternfetch-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: patternfetch-com
tags:
- Fintech
- MarketData
- API
- Stocks
- Crypto
website: https://patternfetch.com/
---
