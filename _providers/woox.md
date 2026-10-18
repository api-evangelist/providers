---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Woox Agentic Access
  operation_count: 68
  slug: woox-agentic-access
  summary_line: 68 operations · 27 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Hosted documentation MCP server exposing search and read-only query over the WOO developer documentation.
  name: WOO Developer Docs MCP Server
  slug: woox-docs-mcp
- baseURL: https://api.woox.io
  baseurl_source: declared
  description: The Account API from WOO X — 9 operation(s) for account.
  name: WOO X Account API
  slug: woox-account-api
- baseURL: https://api.woox.io
  baseurl_source: declared
  description: The Asset API from WOO X — 9 operation(s) for asset.
  name: WOO X Asset API
  slug: woox-asset-api
- baseURL: https://api.woox.io
  baseurl_source: declared
  description: The Futures API from WOO X — 7 operation(s) for futures.
  name: WOO X Futures API
  slug: woox-futures-api
- baseURL: https://api.woox.io
  baseurl_source: declared
  description: The IsolatedMargin API from WOO X — 1 operation(s) for isolatedmargin.
  name: WOO X Isolated Margin API
  slug: woox-isolatedmargin-api
- baseURL: https://api.woox.io
  baseurl_source: declared
  description: The Public API from WOO X — 14 operation(s) for public.
  name: WOO X Public API
  slug: woox-public-api
- baseURL: https://api.woox.io
  baseurl_source: declared
  description: The SpotMargin API from WOO X — 5 operation(s) for spotmargin.
  name: WOO X Spot Margin API
  slug: woox-spotmargin-api
- baseURL: https://api.woox.io
  baseurl_source: declared
  description: The Trade API from WOO X — 9 operation(s) for trade.
  name: WOO X Trade API
  slug: woox-trade-api
artifact_total: 20
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.woox.io/hc/en-us/articles/4403851854233-Terms-of-service
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/agentic-access/woox-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/woox-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/rules/woox-rules.yml
  title: ''
  type: Spectral
  url: rules/woox-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/json-ld/woox-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/woox-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/vocabulary/woox-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/woox-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/data-model/woox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/woox-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/errors/woox-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/woox-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/conformance/woox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/woox-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/llms/woox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/woox-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/a2a/woox-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/woox-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/well-known/woox-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/woox-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/hosts/woox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/woox-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/vendors/woox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/woox-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/authentication/woox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/woox-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://woox.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.woox.io/home
- group: docs
  title: ''
  type: APIReference
  url: https://developer.woox.io/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://developer.woox.io/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.woox.io/api-reference/guide
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.woox.io/changelog/release_note_v3
- group: company
  title: ''
  type: Blog
  url: https://woox.io/blog
- group: other
  title: ''
  type: Leadership
  url: https://woox.io/team
- group: operate
  title: ''
  type: Support
  url: https://support.woox.io/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.woox.io/hc/en-us/articles/4404573651097--Privacy-Policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/mcp/woox-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/woox-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/woox/refs/heads/main/security/woox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/woox-domain-security.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://developer.woox.io/mcp
  - status: 401
    url: https://support.woox.io/mcp
  - status: 200
    url: https://woox.io
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: WOO X is a centralized cryptocurrency exchange offering spot, margin and perpetual futures trading. Its V3 REST API at api.woox.io exposes public market data (instruments, orderbook, klines, trades, funding rates) and authenticated trading, account, asset/wallet, spot-margin and futures endpoints, documented at developer.woox.io with a published OpenAPI definition and a documentation MCP server.
image: https://oss.woonetwork.org/static/woox/SEO_20240724.png
json_schemas:
- name: AccountInfoResponse
  property_count: 0
  slug: woox-account-info-response
- name: CreateOrder
  property_count: 14
  slug: woox-create-order
- name: GetAlgoOrderResponse
  property_count: 0
  slug: woox-get-algo-order-response
- name: GetBalancesResponse
  property_count: 0
  slug: woox-get-balances-response
- name: Stop bracket
  property_count: 0
  slug: woox-stop-bracket-stop-bracket
- name: WalletHistoryResponse
  property_count: 0
  slug: woox-wallet-history-response
jsonld:
- class_count: 21
  name: Woox Context
  property_count: 68
  slug: woox-context
layout: provider
mcp_servers:
- description: Remote MCP server at developer.woox.io over HTTP; 3 tools listed.
  name: WOO X MCP Server
  slug: woo-docs
modified: '2026-10-13'
name: WOO X
nav: Providers
network: true
overview: 'WOO X publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Asset API, Futures API, and 5 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Derivatives.


  The WOO X catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  WOO X''s developer surface includes authentication, API reference, documentation, getting-started guide, changelog, engineering blog, support, and 19 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: WOO X API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: woox-rules
score:
  band: developing
  composite: 43.6
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
    contract_quality: 63.7
    developer_ergonomics: 57.1
    discoverability: 76.7
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Woox Authentication
  slug: woox-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Woox Domain Security
  slug: woox-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: woox
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Derivatives
website: https://woox.io
---
