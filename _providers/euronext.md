---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: On-demand real-time, delayed, and reference market data over HTTP in JSON (REST) covering equities, fixed income, ETFs and funds, warrants and certificates, derivatives, commodities, and indices, with
  name: Euronext Web Services Market Data API
  slug: euronext-web-services-market-data-api
- description: End-of-day summary time series (open, high, low, close, last, volumes, turnover, capitalization) for indices and cash markets by ISIN and MIC, requested as JSON over HTTPS using POST only (GET unsuppo
  name: Euronext Web Services Historical Data API
  slug: euronext-web-services-historical-data-api
- description: Index-level data for Euronext indices delivered through the Euronext Web Services JSON API, documented in a dedicated public client-specification PDF. Access is contracted through Euronext Market Data
  name: Euronext Web Services Indices API
  slug: euronext-web-services-indices-api
- description: REST web services for the Saturn global reporting solution covering MiFID II transaction reporting, trade submission (NEW, AMEND, CANCEL), and commodities positions reporting in JSON, XML, and CSV. HT
  name: Euronext Saturn Reporting API
  slug: euronext-saturn-reporting-api
- description: Low-latency real-time market data feed for Euronext cash and derivatives markets delivered as UDP multicast messages in Simple Binary Encoding (SBE) with LZ4-compressed snapshots, plus an MDG Lite var
  name: Euronext Optiq Market Data Gateway (MDG)
  slug: euronext-optiq-market-data-gateway
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/euronext-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/euronext-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/euronext-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/euronext-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/euronext-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/euronext-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/euronext-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/euronext-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/euronext-llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://www.euronext.com/en/data/how-access-market-data
- group: company
  title: ''
  type: Website
  url: https://www.euronext.com/
- group: start
  title: ''
  type: Portal
  url: https://connect.euronext.com/
- group: docs
  title: ''
  type: Documentation
  url: https://connect.euronext.com/en/it-documentation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/euronext
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/euronext
- group: company
  title: ''
  type: Blog
  url: https://www.euronext.com/en/news
- group: operate
  title: ''
  type: Support
  url: https://www.euronext.com/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.euronext.com/en/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.euronext.com/en/privacy-statement
created: '2026-07-21'
description: Euronext N.V. is the leading pan-European exchange operator, running regulated cash and derivatives markets in Amsterdam, Brussels, Dublin, Lisbon, Milan, Oslo, and Paris, and owning Borsa Italiana and power exchange Nord Pool. Its market data arm sells real-time, delayed, historical, index, and reference data through the low-latency Optiq Market Data Gateway (UDP multicast SBE feed, also cloud-delivered), Optiq flat files, and the Euronext Web Services JSON API, alongside the Saturn REST API for MiFID II regulatory reporting. All access is sales-gated and entitlement-managed - client specifications are published as public PDFs but base URLs and tokens are issued only at onboarding, with no self-serve developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/euronext.png
layout: provider
modified: '2026-07-22'
name: Euronext
nav: Providers
network: true
overview: 'Euronext publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Market Data, Stocks, Exchange, and Real-Time.


  Euronext''s developer surface includes authentication, changelog, sandbox, getting-started guide, developer portal, documentation, engineering blog, and 12 more developer resources.'
random_paper: 145
score:
  band: thin
  composite: 28.4
  delta: -0.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 28.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/euronext/refs/heads/main/screenshots/euronext-2026-07-22T202350.png
security:
- kind: authentication
  name: Euronext Authentication
  slug: euronext-authentication
  summary_line: apiKey/token/mutualTLS · 4 schemes
- kind: domain-security
  name: Euronext Domain Security
  slug: euronext-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: euronext
tags:
- Financial
- Market Data
- Stocks
- Exchange
- Real-Time
- Historical Data
- Indices
- Reference Data
- Derivatives
- Regulatory Reporting
website: https://www.euronext.com/
---
