---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 60.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Lukka Agentic Access
  operation_count: 91
  slug: lukka-agentic-access
  summary_line: 91 operations · 3 acting
api_count: 7
apis:
- description: 'Institutional crypto pricing, valuation and market data: Lukka Prime fair-market-value prices, reference rates, index prices, MVWAP, OHLCV candles, market capitalisation, order-book liquidity and snap'
  name: Lukka Pricing & Market Data API
  slug: lukka-pricing-market-data-api
- description: 'The golden copy of crypto asset reference data: normalised assets, entities, marketplaces, custodians, VASPs, asset/pair/derivative cross-reference mappings, crypto actions, LDACS sector classificatio'
  name: Lukka Reference Data API
  slug: lukka-reference-data-api
- description: 'Derived analytics for digital assets: implied forward interest rate curves, OTC FX implied rates and options implied volatility surfaces.'
  name: Lukka Analytics API
  slug: lukka-analytics-api
- description: 'Bespoke pricing and valuation calculations for digital asset derivatives: submit an asynchronous calculation run, poll its status and retrieve results.'
  name: Lukka Valuation API
  slug: lukka-valuation-api
- description: 'The legacy Lukka Reference Data surface: the normalised asset master plus active, historical, newly added and newly deleted asset and pair cross-reference mappings per source entity.'
  name: Lukka Reference Data API (v1)
  slug: lukka-reference-data-api-v1
- description: WebSocket streaming for executed trades, Level-1 order-book quotes, Lukka Prime pricing, Lukka Index valuations, Standard and Median Reference Rates, real-time MVWAP, derivative Greeks and prediction-
  name: Lukka Market Data Streaming API
  slug: lukka-market-data-streaming-api
- description: Seven first-party hosted Model Context Protocol servers exposing 69 read-only tools over Lukka pricing, reference data, AML risk scoring, on-chain data, analytics, news intelligence and prediction mar
  name: Lukka MCP Servers
  slug: lukka-mcp-servers
artifact_total: 74
asyncapis:
- description: 'Lukka''s WebSocket streaming surface for institutional digital-asset market data: executed trades, Level-1 order-book quotes, Lukka Prime pricing, Lukka Index valuations, Standard and Median Reference '
  name: Lukka Market Data Streaming API
  slug: lukka-market-data-streaming-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://lukka.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.lukka.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.lukka.tech/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.lukka.tech/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/lukkatech/lukka-mcps/blob/main/docs/README.md
- group: build
  title: ''
  type: Postman
  url: https://apidocs.lukka.tech/
- group: operate
  title: ''
  type: Support
  url: https://lukka.tech/support/
- group: company
  title: ''
  type: Blog
  url: https://lukka.tech/insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lukkatech
- group: start
  title: ''
  type: Login
  url: https://app.lukka.tech/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lukka.tech/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lukka.tech/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://lukka.tech/trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://lukka.tech/trust-center/
- group: auth
  title: ''
  type: Security
  url: https://github.com/lukkatech/lukka-plugin-claude/blob/main/lukka/SECURITY.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lukka-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lukka-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lukka-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lukka-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lukka-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lukka-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lukka-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lukka-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lukka-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lukka-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lukka-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lukka-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/lukka-packages.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lukka-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lukka-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lukka-agentic-access.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/lukka-market-data-streaming-asyncapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lukka-llms.txt
- group: other
  title: ''
  type: X
  url: https://twitter.com/Lukka
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lukkaglobal/
created: '2026-08-04'
description: Lukka is an enterprise crypto data and financial software company that produces institutional-grade digital asset data for financial institutions, auditors, funds and corporates. Its products include Lukka Prime - the first fair-market-value pricing methodology for crypto assets, aligned to GAAP, IFRS and SEC guidance - plus reference rates and indices, Lukka Reference Data (a normalized 'golden copy' security master mapping thousands of crypto assets across hundreds of exchanges, custodians and VASPs), market data, derivatives analytics, AML risk scoring across 108+ blockchains, on-chain data, news intelligence and prediction markets. Data is delivered over REST, WebSocket streaming, FIX and SFTP, and - unusually for this sector - through seven first-party hosted Model Context Protocol (MCP) servers with an official Claude plugin, making Lukka one of the more agent-forward providers in the catalog. All access requires a Lukka account and per-product entitlement; there is no
  free tier or self-service signup.
examples:
- key_count: 5
  name: Lukka Analytics Api Implied Interest Rates
  slug: lukka-analytics-api-implied-interest-rates
- key_count: 7
  name: Lukka Analytics Api Implied Volatility
  slug: lukka-analytics-api-implied-volatility
- key_count: 19
  name: Lukka Asset Terms And Conditions A Lukka Asset And Its Details
  slug: lukka-asset-terms-and-conditions-a-lukka-asset-and-its-details
- key_count: 5
  name: Lukka Asset Terms And Conditions All Lukka Assets
  slug: lukka-asset-terms-and-conditions-all-lukka-assets
- key_count: 5
  name: Lukka Asset Terms And Conditions Asset Exposure
  slug: lukka-asset-terms-and-conditions-asset-exposure
- key_count: 5
  name: Lukka Crypto Actions All Crypto Actions
  slug: lukka-crypto-actions-all-crypto-actions
- key_count: 5
  name: Lukka Crypto Actions Asset Crypto Actions
  slug: lukka-crypto-actions-asset-crypto-actions
- key_count: 16
  name: Lukka Custodian Terms And Conditions A Custodian And Its Details
  slug: lukka-custodian-terms-and-conditions-a-custodian-and-its-details
- key_count: 5
  name: Lukka Custodian Terms And Conditions All Custodians
  slug: lukka-custodian-terms-and-conditions-all-custodians
- key_count: 13
  name: Lukka Derivative Terms And Conditions A Derivative And Its Details
  slug: lukka-derivative-terms-and-conditions-a-derivative-and-its-details
- key_count: 5
  name: Lukka Derivative Terms And Conditions All Derivatives
  slug: lukka-derivative-terms-and-conditions-all-derivatives
- key_count: 9
  name: Lukka Derivatives Get Candles By Exchange Source Derivative
  slug: lukka-derivatives-get-candles-by-exchange-source-derivative
- key_count: 4
  name: Lukka Derivatives Get Composite Funding Rates By Paircodes
  slug: lukka-derivatives-get-composite-funding-rates-by-paircodes
- key_count: 4
  name: Lukka Derivatives Get Composite Funding Rates By Underlying
  slug: lukka-derivatives-get-composite-funding-rates-by-underlying
- key_count: 7
  name: Lukka Derivatives Get Historical Derivative Trades
  slug: lukka-derivatives-get-historical-derivative-trades
- key_count: 1
  name: Lukka Derivatives Get Historical Mark Prices
  slug: lukka-derivatives-get-historical-mark-prices
- key_count: 5
  name: Lukka Derivatives Get Latest Derivative Trades
  slug: lukka-derivatives-get-latest-derivative-trades
- key_count: 1
  name: Lukka Derivatives Get Latest Mark Prices
  slug: lukka-derivatives-get-latest-mark-prices
- key_count: 4
  name: Lukka Derivatives Get Latest Markets Derivative
  slug: lukka-derivatives-get-latest-markets-derivative
- key_count: 4
  name: Lukka Derivatives Get Latest Markets Greeks
  slug: lukka-derivatives-get-latest-markets-greeks
- key_count: 1
  name: Lukka Downloadable Data Csv Create Historical Quotes Request
  slug: lukka-downloadable-data-csv-create-historical-quotes-request
- key_count: 1
  name: Lukka Downloadable Data Csv Create Historical Trades Request
  slug: lukka-downloadable-data-csv-create-historical-trades-request
- key_count: 1
  name: Lukka Downloadable Data Csv List Historical Quotes Requests
  slug: lukka-downloadable-data-csv-list-historical-quotes-requests
- key_count: 1
  name: Lukka Downloadable Data Csv List Historical Trades Requests
  slug: lukka-downloadable-data-csv-list-historical-trades-requests
- key_count: 3
  name: Lukka Legacy Versions Source Details
  slug: lukka-legacy-versions-source-details
- key_count: 5
  name: Lukka Mapping And Normalization All Entities
  slug: lukka-mapping-and-normalization-all-entities
- key_count: 5
  name: Lukka Mapping And Normalization All Legal Entity Mappings
  slug: lukka-mapping-and-normalization-all-legal-entity-mappings
- key_count: 5
  name: Lukka Mapping And Normalization Asset Mappings
  slug: lukka-mapping-and-normalization-asset-mappings
- key_count: 5
  name: Lukka Mapping And Normalization Derivative Mappings
  slug: lukka-mapping-and-normalization-derivative-mappings
- key_count: 5
  name: Lukka Marketplace Terms And Conditions All Marketplaces
  slug: lukka-marketplace-terms-and-conditions-all-marketplaces
- key_count: 4
  name: Lukka Prediction Markets Get Latest Markets Prediction
  slug: lukka-prediction-markets-get-latest-markets-prediction
- key_count: 8
  name: Lukka Prediction Markets Get Prediction History By Event Ticker
  slug: lukka-prediction-markets-get-prediction-history-by-event-ticker
- key_count: 8
  name: Lukka Prediction Markets Get Prediction History By Lukkasymbol
  slug: lukka-prediction-markets-get-prediction-history-by-lukkasymbol
- key_count: 8
  name: Lukka Prediction Markets Get Prediction Trade History By Event Tic
  slug: lukka-prediction-markets-get-prediction-trade-history-by-event-tic
- key_count: 8
  name: Lukka Prediction Markets Get Prediction Trade History By Lukkasymb
  slug: lukka-prediction-markets-get-prediction-trade-history-by-lukkasymb
- key_count: 5
  name: Lukka Pricing Get Historical Mvwap By Pair
  slug: lukka-pricing-get-historical-mvwap-by-pair
- key_count: 6
  name: Lukka Pricing Get Historical Prices
  slug: lukka-pricing-get-historical-prices
- key_count: 6
  name: Lukka Pricing Get Historical Reference Rate By Pair
  slug: lukka-pricing-get-historical-reference-rate-by-pair
- key_count: 1
  name: Lukka Pricing Get Latest Index Prices
  slug: lukka-pricing-get-latest-index-prices
- key_count: 5
  name: Lukka Pricing Get Multi Source Vwap By Pair
  slug: lukka-pricing-get-multi-source-vwap-by-pair
- key_count: 5
  name: Lukka Pricing Get Price Variances By Pair
  slug: lukka-pricing-get-price-variances-by-pair
- key_count: 3
  name: Lukka Pricing Get Source Details By Product
  slug: lukka-pricing-get-source-details-by-product
- key_count: 12
  name: Lukka Reference Data Deprecated A Lukka Asset
  slug: lukka-reference-data-deprecated-a-lukka-asset
- key_count: 5
  name: Lukka Reference Data Deprecated All Lukka Assets
  slug: lukka-reference-data-deprecated-all-lukka-assets
- key_count: 5
  name: Lukka Reference Data Deprecated All Lukka Entities
  slug: lukka-reference-data-deprecated-all-lukka-entities
- key_count: 10
  name: Lukka Reference Data Deprecated An Entity
  slug: lukka-reference-data-deprecated-an-entity
- key_count: 5
  name: Lukka Reference Data Deprecated Lukka Asset Mappings
  slug: lukka-reference-data-deprecated-lukka-asset-mappings
- key_count: 5
  name: Lukka Reference Data Deprecated Lukka Crypto Actions
  slug: lukka-reference-data-deprecated-lukka-crypto-actions
- key_count: 5
  name: Lukka Reference Data Deprecated Lukka Derivative Mappings
  slug: lukka-reference-data-deprecated-lukka-derivative-mappings
- key_count: 5
  name: Lukka Reference Data Deprecated Lukka Pair Mappings
  slug: lukka-reference-data-deprecated-lukka-pair-mappings
- key_count: 5
  name: Lukka Reference Data Ldacs
  slug: lukka-reference-data-ldacs
- key_count: 8
  name: Lukka Spot Get Candles By Exchange Source Spot
  slug: lukka-spot-get-candles-by-exchange-source-spot
- key_count: 9
  name: Lukka Spot Get Historical Spot Trades
  slug: lukka-spot-get-historical-spot-trades
- key_count: 1
  name: Lukka Spot Get Latest Market Caps
  slug: lukka-spot-get-latest-market-caps
- key_count: 4
  name: Lukka Spot Get Latest Markets Spot
  slug: lukka-spot-get-latest-markets-spot
- key_count: 10
  name: Lukka Spot Get Market Caps By Pair
  slug: lukka-spot-get-market-caps-by-pair
- key_count: 3
  name: Lukka Spot Get Order Book Liquidity Spot
  slug: lukka-spot-get-order-book-liquidity-spot
- key_count: 3
  name: Lukka Spot Get Order Book Snapshot Spot
  slug: lukka-spot-get-order-book-snapshot-spot
image: https://lukka.tech/wp-content/uploads/2023/06/lukka-tech.png
layout: provider
mcp_servers:
- description: ''
  name: lukka-mcp.yml
  slug: lukka-mcpyml
modified: '2026-08-04'
name: Lukka
nav: Providers
network: true
overview: 'Lukka publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Pricing & Market Data API, Reference Data API, Analytics API, and 3 more. Tagged areas include Crypto, Digital Assets, Market Data, Reference Data, and Pricing.


  The Lukka catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lukka''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 30 more developer resources.'
random_paper: 84
rate_limits:
- limit_count: 1
  name: Lukka Rate Limits
  slug: lukka-rate-limits
scopes:
- name: Lukka Scopes
  scope_count: 9
  slug: lukka-scopes
  summary_line: 9 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 62.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.1
    developer_ergonomics: 71.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 62.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Lukka Authentication
  slug: lukka-authentication
  summary_line: oauth2/http · 4 schemes
- kind: domain-security
  name: Lukka Domain Security
  slug: lukka-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Lukka Vulnerability Disclosure
  slug: lukka-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Lukka Trust Center
  slug: lukka-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, ISO/IEC 27001
slug: lukka
tags:
- Crypto
- Digital Assets
- Market Data
- Reference Data
- Pricing
- Blockchain
- AML
- Compliance
- Financial Services
- Analytics
- Prediction Markets
- MCP
website: https://lukka.tech/
---
