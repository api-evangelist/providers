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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-03'
api_count: 4
apis:
- description: Query reference data for the instruments, listings, and markets in the BMLL universe (equities, ETFs, futures, options), including availability by data type (LOB, listing/instrument/market-level metri
  name: BMLL Reference Data API
  slug: bmll-reference-data-api
- description: Daily time-series metrics and analytics derived from BMLL's harmonised Level 3 order book history, including classified trades, queried by instrument, listing, or market. Documented publicly through t
  name: BMLL Time-Series API
  slug: bmll-time-series-api
- description: 'Retrieve per-instrument market state and consolidated best bid and offer (CBBO) for listings on a given day, with an async poll-for-result request pattern. Documented publicly through the bmll Python '
  name: BMLL Market Data API
  slug: bmll-market-data-api
- description: 'Asynchronous dataset query API (initiate query, poll, download results as JSONL/Arrow into pandas or polars) over BMLL datasets, including a timeseries query endpoint. An OpenAPI definition exists at '
  name: BMLL APIv2 Query API
  slug: bmll-api-v2
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bmll-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bmlltech.com/
- group: start
  title: ''
  type: Portal
  url: https://data.bmlltech.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.bmlltech.com/products/bmll-data-feed/documentation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bmlltech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bmll
- group: company
  title: ''
  type: Blog
  url: https://www.bmlltech.com/knowledge-hub
- group: operate
  title: ''
  type: Support
  url: https://support.bmlltech.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bmlltech.com/support-pages/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bmlltech.com/support-pages/terms
- group: auth
  title: ''
  type: Compliance
  url: https://www.bmlltech.com/news/our-news/bmll-awarded-iso-27001-certification
- group: build
  title: ''
  type: Packages
  url: packages/bmll-technologies-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bmll-technologies-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bmll-technologies-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bmll-technologies-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bmll-technologies-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bmll-technologies-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bmll-technologies-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/bmll-technologies-cli.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bmll-technologies-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bmll-technologies-llms.txt
created: '2026-07-21'
description: BMLL is a London-based provider of harmonised historical Level 3, 2, and 1 order book data and analytics for capital markets, covering global equities, ETFs, futures, and options. Acquired by Nordic Capital in October 2025 (with Optiver as minority shareholder), BMLL sells its data through the BMLL Data Lab hosted Python environment, the BMLL Data Feed file product, and entitlement-gated REST APIs (Reference Data, Time-Series, Market Data, and an async query APIv2) documented publicly via the bmll Python SDK on PyPI, with delivery over API, S3, SFTP, and Snowflake. There is no self-serve signup - access is sales-led with key-pair credentials issued per account.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bmll-technologies.png
layout: provider
modified: '2026-07-22'
name: BMLL Technologies
nav: Providers
network: true
overview: 'BMLL Technologies publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Market Data, Order Book, Stocks, and Trading.


  BMLL Technologies'' developer surface includes developer portal, documentation, engineering blog, support, authentication, changelog, CLI, and 14 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 13
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 30.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bmll-technologies/refs/heads/main/screenshots/bmll-technologies-2026-07-22T202240.png
security:
- kind: authentication
  name: Bmll Technologies Authentication
  slug: bmll-technologies-authentication
  summary_line: key-pair-jwt/bearer/apiKey · 3 schemes
- kind: domain-security
  name: Bmll Technologies Domain Security
  slug: bmll-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bmll-technologies
tags:
- Financial
- Market Data
- Order Book
- Stocks
- Trading
- Reference Data
- Historical Data
- Analytics
- ETFs
- Futures
- Options
website: https://bmlltech.com/
---
