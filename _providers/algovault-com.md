---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: AlgoVault Docs — API Reference, Knowledge Tools, Integrations & FAQ
  name: AlgoVault MCP API
  slug: algovault-mcp-api
- baseURL: https://api.algovault.com
  baseurl_source: declared
  description: 'AlgoVault API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AlgoVault API
  slug: algovault-com-api
artifact_total: 17
common:
- group: commercial
  href: https://artifacts.apis.io/algovault-com/plans/algovault-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/algovault-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/algovault-com/rules/algovault-com-rules.yml
  title: ''
  type: Spectral
  url: rules/algovault-com-rules.yml
- group: design
  href: https://artifacts.apis.io/algovault-com/json-ld/algovault-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/algovault-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/algovault-com/vocabulary/algovault-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/algovault-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/algovault-com/data-model/algovault-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/algovault-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/algovault-com/security/algovault-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/algovault-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/algovault-com/authentication/algovault-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/algovault-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/algovault-com/errors/algovault-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/algovault-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/algovault-com/conformance/algovault-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/algovault-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/algovault-com/llms/algovault-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algovault-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/algovault-com/mcp/algovault-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/algovault-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/algovault-com/well-known/algovault-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/algovault-com-security.txt
- group: agent
  href: https://artifacts.apis.io/algovault-com/well-known/algovault-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/algovault-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/algovault-com/hosts/algovault-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/algovault-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/algovault-com/vendors/algovault-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/algovault-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://algovault.com/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://algovault.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://api.algovault.com/signup?plan=starter
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://algovault.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://blog.algovault.com/
- group: auth
  href: https://artifacts.apis.io/algovault-com/security/algovault-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/algovault-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/algovault-com/security/algovault-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algovault-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://algovault.com/
- group: docs
  title: ''
  type: Documentation
  url: https://algovault.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://algovault.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://algovault.com/#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://algovault.com/#pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlgoVaultLabs
coverage:
  checked: '2026-11-01'
  detail: Documentation is publicly readable but provides no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://algovault.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AlgoVault provides a brain‑layer for AI trading agents, delivering composite trade verdicts across 15 leading crypto and traditional exchanges. Its Model Context Protocol server returns direction, confidence and market regime in a single MCP call, with a free tier offering 200 calls per month.
image: https://algovault.com/logo.png
json_schemas:
- name: PostMcpRequest
  property_count: 4
  slug: algovault-com-post-mcp-request
- name: PostX402GetMarketRegimeRequest
  property_count: 3
  slug: algovault-com-post-x402-get-market-regime-request
- name: PostX402GetMarketRegimeResponse
  property_count: 8
  slug: algovault-com-post-x402-get-market-regime-response
- name: PostX402GetTradeCallRequest
  property_count: 5
  slug: algovault-com-post-x402-get-trade-call-request
- name: PostX402GetTradeCallResponse
  property_count: 13
  slug: algovault-com-post-x402-get-trade-call-response
- name: PostX402ScanFundingArbResponse
  property_count: 4
  slug: algovault-com-post-x402-scan-funding-arb-response
jsonld:
- class_count: 13
  name: Algovault Com Context
  property_count: 39
  slug: algovault-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.algovault.com.
  name: AlgoVault MCP Server
  slug: algovault-com-mcp-yml
modified: '2026-11-01'
name: AlgoVault
nav: Providers
network: true
overview: 'AlgoVault is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Trading, Finance, MCP, and Cryptocurrency.


  The AlgoVault catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AlgoVault''s developer surface includes authentication, signup flow, engineering blog, documentation, API reference, getting-started guide, pricing, and 21 more developer resources.'
plans:
- name: Algovault Com Plans Pricing
  plan_count: 4
  slug: algovault-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Algovault Com Rate Limits
  slug: algovault-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AlgoVault API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: algovault-com-rules
scopes:
- name: Algovault Com Scopes
  scope_count: 0
  slug: algovault-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.8
    developer_ergonomics: 27.4
    discoverability: 65.0
    operational_transparency: 17.1
  previous_composite: 45.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 37.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Algovault Com Authentication
  slug: algovault-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Algovault Com Domain Security
  slug: algovault-com-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Algovault Com Vulnerability Disclosure
  slug: algovault-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: algovault-com
tags:
- Artificial Intelligence
- Trading
- Finance
- MCP
- Cryptocurrency
website: https://algovault.com/
---
