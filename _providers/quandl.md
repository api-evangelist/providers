---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Quandl Agentic Access
  operation_count: 6
  slug: quandl-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: Nasdaq Data Link Tables API provides access to tabular financial datasets including equity fundamentals, options data, and alternative data sets. Limited to 10,000 rows per call with pagination suppor
  name: Nasdaq Data Link Tables REST API
  slug: nasdaq-data-link-tables-api
- description: Nasdaq Cloud Data Service (NCDS) provides streaming and REST APIs for real-time and delayed market data delivery including equities, options, and fixed income from Nasdaq exchange feeds.
  name: Nasdaq Cloud Data Service (NCDS) Streaming API
  slug: nasdaq-cloud-data-service-api
- baseURL: https://data.nasdaq.com/api/v3
  baseurl_source: declared
  description: Database catalog and metadata
  name: Quandl (Nasdaq Data Link) Databases API
  slug: quandl-databases-api
- baseURL: https://data.nasdaq.com/api/v3
  baseurl_source: declared
  description: Time-series dataset retrieval
  name: Quandl (Nasdaq Data Link) Datasets API
  slug: quandl-datasets-api
- baseURL: https://data.nasdaq.com/api/v3
  baseurl_source: declared
  description: Tabular dataset retrieval
  name: Quandl (Nasdaq Data Link) Tables API
  slug: quandl-tables-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nasdaq Data Link Time-Series REST API
  slug: open-nasdaq-data-link-timeseries
- collection_type: open
  name: Nasdaq Data Link Time-Series REST Databases API
  slug: open-quandl-databases-api
- collection_type: open
  name: Nasdaq Data Link Time-Series REST Databases Datasets API
  slug: open-quandl-datasets-api
- collection_type: open
  name: Nasdaq Data Link Time-Series REST Databases Tables API
  slug: open-quandl-tables-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quandl-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quandl-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quandl-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quandl
- group: start
  title: ''
  type: Portal
  url: https://data.nasdaq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.data.nasdaq.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.data.nasdaq.com/docs/getting-started
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.data.nasdaq.com/docs/rate-limits
- group: company
  title: ''
  type: Website
  url: https://data.nasdaq.com/
- group: operate
  title: ''
  type: Support
  url: https://docs.data.nasdaq.com/docs/contact-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nasdaq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quandl
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nasdaq/data-link-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nasdaq/NasdaqCloudDataService-SDK-Python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Nasdaq/NasdaqCloudDataService-SDK-Java
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/nasdaq-data-link-timeseries-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/nasdaq-data-link-dataset-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/nasdaq-data-link-context.jsonld
created: '2026-03-18'
description: Nasdaq Data Link (formerly Quandl) provides REST and streaming APIs for financial and economic data including time-series datasets, tabular datasets, and real-time market data feeds. Datasets cover stock prices, economic indicators, interest rates, commodities, equity fundamentals, options data, and alternative data sets.
finops:
- name: Quandl Finops
  service_category: Market Data
  slug: quandl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quandl.png
json_schemas:
- name: Nasdaq Data Link Dataset
  property_count: 15
  slug: nasdaq-data-link-dataset
jsonld:
- class_count: 0
  name: Nasdaq Data Link Context
  property_count: 19
  slug: nasdaq-data-link-context
layout: provider
modified: '2026-05-19'
name: Quandl (Nasdaq Data Link)
nav: Providers
network: true
overview: 'Quandl (Nasdaq Data Link) publishes 3 APIs on the [APIs.io](https://apis.io/) network: Databases API, Datasets API, and Tables API. Tagged areas include Finance, Market Data, Economic Data, Time Series, and Streaming.


  The Quandl (Nasdaq Data Link) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Quandl (Nasdaq Data Link)''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, and 13 more developer resources.'
plans:
- name: Quandl Plans Pricing
  plan_count: 1
  slug: quandl-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Quandl Rate Limits
  slug: quandl-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Quandl (Nasdaq Data Link) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: quandl-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 50.3
    catalog_earned_first_party: 0.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 61.2
    developer_ergonomics: 60.7
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quandl/refs/heads/main/screenshots/quandl-2026-06-20T192403.png
security:
- kind: authentication
  name: Quandl Authentication
  slug: quandl-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Quandl Domain Security
  slug: quandl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quandl
tags:
- Finance
- Market Data
- Economic Data
- Time Series
- Streaming
website: https://data.nasdaq.com/
---
