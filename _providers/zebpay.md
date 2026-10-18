---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Zebpay Agentic Access
  operation_count: 34
  slug: zebpay-agentic-access
  summary_line: 34 operations · 8 acting
api_count: 2
apis:
- description: Spot trading API on sapi.zebpay.com (market data, orders, balances), documented in markdown in the zebpay-api-references GitHub repository. No machine-readable contract is published for it.
  name: ZebPay Spot API v2
  slug: zebpay-spot-api
- baseURL: https://futuresbe.zebpay.com
  baseurl_source: declared
  description: The Futures API from ZebPay — 1 operation(s) for futures.
  name: ZebPay Futures API
  slug: zebpay-futures-api
- baseURL: https://futuresbe.zebpay.com
  baseurl_source: declared
  description: The Futures > Exchange API from ZebPay — 2 operation(s) for futures > exchange.
  name: ZebPay Futures > Exchange API
  slug: zebpay-futures-exchange-api
- baseURL: https://futuresbe.zebpay.com
  baseurl_source: declared
  description: The Futures > Market API from ZebPay — 5 operation(s) for futures > market.
  name: ZebPay Futures > Market API
  slug: zebpay-futures-market-api
- baseURL: https://futuresbe.zebpay.com
  baseurl_source: declared
  description: The Futures > Trade API from ZebPay — 9 operation(s) for futures > trade.
  name: ZebPay Futures > Trade API
  slug: zebpay-futures-trade-api
- baseURL: https://futuresbe.zebpay.com
  baseurl_source: declared
  description: The Futures > User Leverage API from ZebPay — 2 operation(s) for futures > user leverage.
  name: ZebPay Futures > User Leverage API
  slug: zebpay-futures-user-leverage-api
- baseURL: https://futuresbe.zebpay.com
  baseurl_source: declared
  description: The Futures > Wallet API from ZebPay — 1 operation(s) for futures > wallet.
  name: ZebPay Futures > Wallet API
  slug: zebpay-futures-wallet-api
- baseURL: https://futuresbe.zebpay.com
  baseurl_source: declared
  description: <p>These APIs returns market details including ticker(s), book (pending orders), trades (executed orders) etc.</p>
  name: ZebPay Market API
  slug: zebpay-market-api
- baseURL: https://futuresbe.zebpay.com
  baseurl_source: declared
  description: <p>This endpoint allows users to read order data, create a new order, or cancel a previously placed order.</p> <h3 id="signature-generation-for-post-methods"><strong>Signature Generation for POST Meth
  name: ZebPay Trade API
  slug: zebpay-trade-api-api
artifact_total: 15
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/rate-limits/zebpay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zebpay-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/agentic-access/zebpay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zebpay-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/rules/zebpay-rules.yml
  title: ''
  type: Spectral
  url: rules/zebpay-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/vocabulary/zebpay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zebpay-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/conformance/zebpay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zebpay-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/llms/zebpay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zebpay-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/mcp/zebpay-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zebpay-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/well-known/zebpay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zebpay-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/hosts/zebpay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zebpay-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/vendors/zebpay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zebpay-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/packages/zebpay-packages.yml
  title: ''
  type: SDKs
  url: packages/zebpay-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/packages/zebpay-packages.yml
  title: ''
  type: Packages
  url: packages/zebpay-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://zebpay.com/features/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/authentication/zebpay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zebpay-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zebpay/refs/heads/main/security/zebpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zebpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zebpay.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zebpay.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.zebpay.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://zebpay.com/app/api-trading
- group: company
  title: ''
  type: Blog
  url: https://zebpay.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://zebpay.com/features/pricing
- group: start
  title: ''
  type: SignUp
  url: https://onboarding.zebpay.com/onboarding
- group: operate
  title: ''
  type: Support
  url: https://help.zebpay.com/support/home
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zebpay
- group: build
  title: ''
  type: Postman
  url: https://docs.zebpay.com/
created: '2026-10-13'
description: ZebPay is an Indian cryptocurrency exchange offering spot trading in INR and USDT pairs and crypto futures. It publishes REST APIs for spot (sapi.zebpay.com, documented on GitHub), a legacy spot API (www.zebapi.com) and futures (futuresbe.zebpay.com), public Postman documentation at docs.zebpay.com and apidocs.zebpay.com, WebSocket market streams, futures webhooks, and an MCP server for AI-assisted trading.
layout: provider
mcp_servers:
- description: 'ZebPay publishes an MCP server in its own GitHub organization (github.com/zebpay/zebpay-mcp-server, TypeScript, @modelcontextprotocol/sdk) exposing spot and futures market-data and trading tools over '
  name: ZebPay MCP Server
  slug: zebpay-mcp-yml
modified: '2026-10-13'
name: ZebPay
nav: Providers
network: true
overview: 'ZebPay publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Futures API, Futures > Exchange API, Futures > Market API, and 6 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Futures.


  The ZebPay catalog on APIs.io includes 1 Spectral governance ruleset.


  ZebPay''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 3
  name: Zebpay Rate Limits
  slug: zebpay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ZebPay API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: zebpay-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 52.8
    catalog_earned_first_party: 12.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 46.1
    developer_ergonomics: 59.5
    discoverability: 68.3
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Zebpay Authentication
  slug: zebpay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zebpay Domain Security
  slug: zebpay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: zebpay
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Futures
- India
- Market Data
- MCP
website: https://zebpay.com
---
