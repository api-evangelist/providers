---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-11'
api_count: 10
apis:
- description: D-1 investor data for authorized fintechs and custodians - investment positions, account transactions, listed-asset buy/sell activity, public offering participation, and provisioned corporate events -
  name: B3 Investor Area (Área do Investidor) APIs
  slug: b3-investor-area-apis
- description: Treasury Direct platform APIs - the Bonds API serves reference data for Brazilian public bonds (name, maturity, Selic code, platform identifiers), Positions serves investor position balances, and Orde
  name: B3 Tesouro Direto APIs
  slug: b3-tesouro-direto-apis
- description: Registration, custody, and consultation APIs for the OTC segment - bank funding instruments (CDB, RDB, LCA, LCI, LF, LIG), credit notes (CCB, CPR, NC), OTC derivatives (swaps, flexible options, term c
  name: B3 OTC (Balcão) APIs
  slug: b3-otc-balcao-apis
- description: Post-trade APIs for the listed segment - iMercado investment fund registration and equities fee details, CORE risk calculation and simulation, unified client registration, asset lending, reconciliatio
  name: B3 Listed Markets (Listados) APIs
  slug: b3-listed-markets-apis
- description: ISIN issuance and management for financial instruments - B3 is the Brazilian numbering agency - covering ISIN requests, updates, and consultation of instrument identifier records.
  name: B3 ISIN API
  slug: b3-isin-api
- description: Banco B3 Custody API for operation billing, position reports, and fund quote validation, plus the Settlement API for Pix statement consultation.
  name: Banco B3 APIs
  slug: b3-banco-b3-apis
- description: Insurance-segment registration APIs (V3) covering accepted co-insurance registration, claim registration, document registration, and batch processing return with data-quality feedback.
  name: B3 Insurance (Seguros) APIs
  slug: b3-insurance-apis
- description: OAuth 2.0 token issuance APIs used across the B3 API catalog - Client Credentials flows (plain, plus category_ID, key, or scope parameter variants) and Resource Owner Password Credentials flows.
  name: B3 Authentication APIs
  slug: b3-authentication-apis
- description: 'B3''s real-time market data distribution over the Unified Market Data Feed (UMDF) - event-based bid, ask, trade, and statistics data in L1 (top of book) or L2 (full book) depth, real-time or 15-minute '
  name: B3 Market Data Feed (UMDF)
  slug: b3-market-data-feed-umdf
- description: End-of-day and reference data service covering fixed income, equities, currencies, and debentures for mark-to-market, risk, and pricing workflows - standardized files in TXT, CSV, JSON, or XML deliver
  name: B3 UP2DATA
  slug: b3-up2data
artifact_total: 15
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/b3-exchange-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/b3-exchange-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.b3.com.br/en_us/
- group: start
  title: ''
  type: Portal
  url: https://developers.b3.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.b3.com.br/apis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/b3
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.b3.com.br/en_us/terms-of-use-and-data-protection/
- group: operate
  title: ''
  type: Support
  url: https://developers.b3.com.br/contato
- group: build
  title: ''
  type: Packages
  url: packages/b3-exchange-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/b3-exchange-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/b3-exchange-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/b3-exchange-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/b3-exchange-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/b3-exchange-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/b3-exchange-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/b3-exchange-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/b3-exchange-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/b3-exchange-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/b3-exchange-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/b3-exchange-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/b3-exchange-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/b3-exchange-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://developers.b3.com.br/seguranca
- group: docs
  title: ''
  type: APIReference
  url: https://developers.b3.com.br/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.b3.com.br/faq
- group: start
  title: ''
  type: Login
  url: https://developers.b3.com.br/sign-in
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.b3.com.br/en_us/terms-of-use-and-data-protection/
created: '2026-07-21'
description: B3 S.A. - Brasil, Bolsa, Balcão is the Brazilian exchange and financial market infrastructure operator formed by the 2017 merger of BM&FBOVESPA and Cetip, running trading, clearing, central depository, and OTC registration for equities, derivatives, fixed income, and FX. Its public B3 for Developers portal documents 114 B2B REST APIs (OAuth 2.0 client credentials and ROPC) across investor-area, OTC (Balcão), listed-markets, Tesouro Direto, Banco B3, and insurance domains. Real-time market data is distributed through the UMDF multicast feed (FIX/FAST and Binary SBE, L1/L2) via authorized distributors, and end-of-day plus reference data through the UP2DATA file service (TXT/CSV/JSON/XML via client software or cloud). All API and data access is contract-gated for institutions - B3 explicitly offers no self-serve access for individuals.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: b3-exchange-mcp.yml
  slug: b3-exchange-mcpyml
modified: '2026-07-22'
name: B3 (Brasil Bolsa Balcão)
nav: Providers
network: true
overview: 'B3 (Brasil Bolsa Balcão) publishes 8 APIs on the [APIs.io](https://apis.io/) network, including B3 Investor Area (Área do Investidor) APIs, B3 Tesouro Direto APIs, B3 OTC (Balcão) APIs, and 5 more. Tagged areas include Financial, Market Data, Stocks, Trading, and Exchange.


  B3 (Brasil Bolsa Balcão)''s developer surface includes developer portal, documentation, support, authentication, sandbox, changelog, API reference, and 21 more developer resources.'
random_paper: 101
scopes:
- name: B3 Exchange Scopes
  scope_count: 2
  slug: b3-exchange-scopes
  summary_line: 2 scopes · clientCredentials/password
score:
  band: developing
  composite: 44.3
  delta: -1.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 32.3
    developer_ergonomics: 60.3
    discoverability: 72.2
    governance: 20.8
    operational_transparency: 26.3
  previous_composite: 45.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/b3-exchange/refs/heads/main/screenshots/b3-exchange-2026-07-22T202200.png
security:
- kind: authentication
  name: B3 Exchange Authentication
  slug: b3-exchange-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: B3 Exchange Domain Security
  slug: b3-exchange-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: B3 Exchange Vulnerability Disclosure
  slug: b3-exchange-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: b3-exchange
tags:
- Financial
- Market Data
- Stocks
- Trading
- Exchange
- Derivatives
- Fixed Income
- Real-Time
- Reference Data
- Brazil
website: https://www.b3.com.br/en_us/
---
