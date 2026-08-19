---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Lukka Agentic Access
  operation_count: 91
  slug: lukka-agentic-access
  summary_line: 91 operations · 3 acting
api_count: 22
apis:
- description: WebSocket streaming for executed trades, Level-1 order-book quotes, Lukka Prime pricing, Lukka Index valuations, Standard and Median Reference Rates, real-time MVWAP, derivative Greeks and prediction-
  name: Lukka Market Data Streaming API
  slug: lukka-market-data-streaming-api
- description: Seven first-party hosted Model Context Protocol servers exposing 69 read-only tools over Lukka pricing, reference data, AML risk scoring, on-chain data, analytics, news intelligence and prediction mar
  name: Lukka MCP Servers
  slug: lukka-mcp-servers
- description: The Analytics - Analytics API API from Lukka — 3 operation(s) for analytics - analytics api.
  name: Lukka Analytics - Analytics API API
  slug: lukka-analytics-analytics-api-api
- description: The Analytics - Derived Data API from Lukka — 3 operation(s) for analytics - derived data.
  name: Lukka Analytics - Derived Data API
  slug: lukka-analytics-derived-data-api
- description: The Analytics - Valuations API from Lukka — 2 operation(s) for analytics - valuations.
  name: Lukka Analytics - Valuations API
  slug: lukka-analytics-valuations-api
- description: The Market Data - Derivatives API from Lukka — 8 operation(s) for market data - derivatives.
  name: Lukka Market Data - Derivatives API
  slug: lukka-market-data-derivatives-api
- description: The Market Data - Downloadable Data (CSV) API from Lukka — 4 operation(s) for market data - downloadable data (csv).
  name: Lukka Market Data - Downloadable Data (CSV) API
  slug: lukka-market-data-downloadable-data-csv-api
- description: The Market Data - Prediction Markets API from Lukka — 5 operation(s) for market data - prediction markets.
  name: Lukka Market Data - Prediction Markets API
  slug: lukka-market-data-prediction-markets-api
- description: The Market Data - Spot API from Lukka — 9 operation(s) for market data - spot.
  name: Lukka Market Data - Spot API
  slug: lukka-market-data-spot-api
- description: The Pricing API from Lukka — 13 operation(s) for pricing.
  name: Lukka Pricing API
  slug: lukka-pricing-api
- description: The Pricing - Legacy Versions API from Lukka — 2 operation(s) for pricing - legacy versions.
  name: Lukka Pricing - Legacy Versions API
  slug: lukka-pricing-legacy-versions-api
- description: The Reference Data API from Lukka — 3 operation(s) for reference data.
  name: Lukka Reference Data API
  slug: lukka-reference-data-api
- description: The Reference Data - Asset Terms and Conditions API from Lukka — 3 operation(s) for reference data - asset terms and conditions.
  name: Lukka Reference Data - Asset Terms and Conditions API
  slug: lukka-reference-data-asset-terms-and-conditions-api
- description: The Reference Data - Crypto Actions API from Lukka — 2 operation(s) for reference data - crypto actions.
  name: Lukka Reference Data - Crypto Actions API
  slug: lukka-reference-data-crypto-actions-api
- description: The Reference Data - Custodian Terms and Conditions API from Lukka — 2 operation(s) for reference data - custodian terms and conditions.
  name: Lukka Reference Data - Custodian Terms and Conditions API
  slug: lukka-reference-data-custodian-terms-and-conditions-api
- description: The Reference Data (Deprecated) API from Lukka — 8 operation(s) for reference data (deprecated).
  name: Lukka Reference Data (Deprecated) API
  slug: lukka-reference-data-deprecated-api
- description: The Reference Data - Derivative Terms and Conditions API from Lukka — 2 operation(s) for reference data - derivative terms and conditions.
  name: Lukka Reference Data - Derivative Terms and Conditions API
  slug: lukka-reference-data-derivative-terms-and-conditions-api
- description: The Reference Data - Mapping and Normalization API from Lukka — 5 operation(s) for reference data - mapping and normalization.
  name: Lukka Reference Data - Mapping and Normalization API
  slug: lukka-reference-data-mapping-and-normalization-api
- description: The Reference Data - Marketplace Terms and Conditions API from Lukka — 2 operation(s) for reference data - marketplace terms and conditions.
  name: Lukka Reference Data - Marketplace Terms and Conditions API
  slug: lukka-reference-data-marketplace-terms-and-conditions-api
- description: The Reference Data - Prediction Markets API from Lukka — 2 operation(s) for reference data - prediction markets.
  name: Lukka Reference Data - Prediction Markets API
  slug: lukka-reference-data-prediction-markets-api
- description: The Reference Data v1 API from Lukka — 9 operation(s) for reference data v1.
  name: Lukka Reference Data v1 API
  slug: lukka-reference-data-v1-api
- description: The Reference Data - Virtual Asset Serivce Providers API from Lukka — 1 operation(s) for reference data - virtual asset serivce providers.
  name: Lukka Reference Data - Virtual Asset Serivce Providers API
  slug: lukka-reference-data-virtual-asset-serivce-providers-api
artifact_total: 110
asyncapis:
- description: 'Lukka''s WebSocket streaming surface for institutional digital-asset market data: executed trades, Level-1 order-book quotes, Lukka Prime pricing, Lukka Index valuations, Standard and Median Reference '
  name: Lukka Market Data Streaming API
  slug: lukka-market-data-streaming-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lukka Analytics Analytics - Analytics API API
  slug: open-lukka-analytics-analytics-api-api
- collection_type: open
  name: Lukka Reference Data Analytics - Derived Data API
  slug: open-lukka-analytics-derived-data-api
- collection_type: open
  name: Lukka Valuation (Data Calculation) Analytics - Valuations API
  slug: open-lukka-analytics-valuations-api
- collection_type: open
  name: Lukka Pricing & Market Data Market Data - Derivatives API
  slug: open-lukka-market-data-derivatives-api
- collection_type: open
  name: Lukka Pricing & Market Data Market Data - Downloadable Data (CSV) Market Data - Downloadable Data (CSV) API
  slug: open-lukka-market-data-downloadable-data-csv-api
- collection_type: open
  name: Lukka Pricing & Market Data Market Data - Prediction Markets API
  slug: open-lukka-market-data-prediction-markets-api
- collection_type: open
  name: Lukka Pricing & Market Data Market Data - Spot API
  slug: open-lukka-market-data-spot-api
- collection_type: open
  name: Lukka & Market Data Pricing API
  slug: open-lukka-pricing-api
- collection_type: open
  name: Lukka Pricing & Market Data Pricing - Legacy Versions API
  slug: open-lukka-pricing-legacy-versions-api
- collection_type: open
  name: Lukka Reference Data API
  slug: open-lukka-reference-data-api
- collection_type: open
  name: Lukka Reference Data Reference Data - Asset Terms and Conditions API
  slug: open-lukka-reference-data-asset-terms-and-conditions-api
- collection_type: open
  name: Lukka Reference Data Reference Data - Crypto Actions API
  slug: open-lukka-reference-data-crypto-actions-api
- collection_type: open
  name: Lukka Reference Data Reference Data - Custodian Terms and Conditions API
  slug: open-lukka-reference-data-custodian-terms-and-conditions-api
- collection_type: open
  name: Lukka Reference Data Reference Data (Deprecated) Reference Data (Deprecated) API
  slug: open-lukka-reference-data-deprecated-api
- collection_type: open
  name: Lukka Reference Data Reference Data - Derivative Terms and Conditions API
  slug: open-lukka-reference-data-derivative-terms-and-conditions-api
- collection_type: open
  name: Lukka Reference Data Reference Data - Mapping and Normalization API
  slug: open-lukka-reference-data-mapping-and-normalization-api
- collection_type: open
  name: Lukka Reference Data Reference Data - Marketplace Terms and Conditions API
  slug: open-lukka-reference-data-marketplace-terms-and-conditions-api
- collection_type: open
  name: Lukka Reference Data Reference Data - Prediction Markets API
  slug: open-lukka-reference-data-prediction-markets-api
- collection_type: open
  name: Lukka Reference Data API (v1) Reference Data v1 API
  slug: open-lukka-reference-data-v1-api
- collection_type: open
  name: Lukka Reference Data Reference Data - Virtual Asset Serivce Providers API
  slug: open-lukka-reference-data-virtual-asset-serivce-providers-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/lukka-analytics-overlay.yaml
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
overview: 'Lukka publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Market Data Streaming API, Analytics - Analytics API API, Analytics - Derived Data API, and 18 more. Tagged areas include Crypto, Digital Assets, Market Data, Reference Data, and Pricing.


  The Lukka catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lukka''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 31 more developer resources.'
random_paper: 89
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
  composite: 59.9
  delta: -1.5
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 30.3
    contract_quality: 63.8
    developer_ergonomics: 53.6
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 50.0
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lukka/refs/heads/main/screenshots/lukka-2026-08-07T171825.png
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
