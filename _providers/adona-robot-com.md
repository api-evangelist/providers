---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Candle history and live market data for foreign exchange (FX) and precious metals, with one‑second OHLC candles and live quote streams.
  name: Adona Market Data API
  slug: adona-market-data-api
- description: 'adona-robot-com API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: adona-robot-com API
  slug: adona-robot-com-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/adona-robot-com/rules/adona-robot-com-rules.yml
  title: ''
  type: Spectral
  url: rules/adona-robot-com-rules.yml
- group: design
  href: https://artifacts.apis.io/adona-robot-com/json-ld/adona-robot-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adona-robot-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/adona-robot-com/vocabulary/adona-robot-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adona-robot-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/adona-robot-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/adona-robot-com/data-model/adona-robot-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adona-robot-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/adona-robot-com/authentication/adona-robot-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adona-robot-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/adona-robot-com/errors/adona-robot-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adona-robot-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adona-robot-com/conformance/adona-robot-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adona-robot-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adona-robot-com/llms/adona-robot-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adona-robot-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/adona-robot-com/mcp/adona-robot-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adona-robot-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/adona-robot-com/well-known/adona-robot-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adona-robot-com-security.txt
- group: agent
  href: https://artifacts.apis.io/adona-robot-com/well-known/adona-robot-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adona-robot-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adona-robot-com/hosts/adona-robot-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adona-robot-com-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://adona-robot.com/en/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://adona-robot.com/en/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.adona-robot.com&quot;
- group: auth
  href: https://artifacts.apis.io/adona-robot-com/security/adona-robot-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adona-robot-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/adona-robot-com/security/adona-robot-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adona-robot-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adona-robot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://adona-robot.com/en/reference
- group: docs
  title: ''
  type: APIReference
  url: https://api.adona-robot.com/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://adona-robot.com/en/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://adona-robot.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adona-robot.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adona-robot.com/en/privacy
- group: start
  title: ''
  type: SignUp
  url: https://adona-robot.com/en/signup
- group: start
  title: ''
  type: Login
  url: https://adona-robot.com/en/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adona-robot
created: '2026-10-30'
description: Adona Robot Sàrl provides a market data API delivering one‑second OHLC candles and a live quote stream for foreign exchange (FX) and precious metals. The service is sold by capacity, starting at CHF 500 per month, with redistribution allowed. It offers tiered plans (Starter, Growth, Scale, Enterprise) and is hosted at api.adona-robot.com. The company is based in Switzerland, emphasizing low‑latency data, easy integration via OpenAPI, and comprehensive documentation.
image: https://adona-robot.com/brand/adona-robot-logo-1024.png
json_schemas:
- name: GetV1CandlesResponse
  property_count: 4
  slug: adona-robot-com-get-v1-candles-response
- name: GetV1TokensResponse
  property_count: 1
  slug: adona-robot-com-get-v1-tokens-response
- name: PostV1TokensRequest
  property_count: 1
  slug: adona-robot-com-post-v1-tokens-request
- name: PostV1TokensResponse
  property_count: 4
  slug: adona-robot-com-post-v1-tokens-response
- name: PostV1WsTicketResponse
  property_count: 2
  slug: adona-robot-com-post-v1-ws-ticket-response
jsonld:
- class_count: 5
  name: Adona Robot Com Context
  property_count: 8
  slug: adona-robot-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.adona-robot.com.
  name: adona-robot-com MCP Server
  slug: adona-robot-com-mcp-yml
modified: '2026-10-30'
name: adona-robot-com
nav: Providers
network: true
overview: 'adona-robot-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Market-Data, Forex, Metals, and API.


  The adona-robot-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  adona-robot-com''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Adona Robot Com Plans Pricing
  plan_count: 0
  slug: adona-robot-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Adona Robot Com Rate Limits
  slug: adona-robot-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: adona-robot-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: adona-robot-com-rules
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 69.7
    catalog_earned_first_party: 0.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 52.6
    developer_ergonomics: 56.4
    discoverability: 56.7
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adona Robot Com Authentication
  slug: adona-robot-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Adona Robot Com Domain Security
  slug: adona-robot-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Adona Robot Com Vulnerability Disclosure
  slug: adona-robot-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: adona-robot-com
tags:
- Finance
- Market-Data
- Forex
- Metals
- API
- Swiss
website: https://adona-robot.com/
---
