---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Worldbank Agentic Access
  operation_count: 12
  slug: worldbank-agentic-access
  summary_line: 12 operations
api_count: 10
apis:
- description: Provides information about thousands of development-relevant datasets available through the World Bank Data Catalog. Supports searching, listing, viewing dataset metadata, and downloading resource fil
  name: World Bank Data Catalog API
  slug: worldbank-data-catalog
- description: Provides access to World Bank operations data including active, pipeline, and closed projects. Returns project details including financial commitments, status, country classification, themes, and team
  name: World Bank Projects API
  slug: worldbank-projects
- description: Provides programmatic access to World Bank financial data including loans, credits, trust funds, budget data, and financial statements. Delivered through the Finances One platform with support for JSO
  name: World Bank Finances API
  slug: worldbank-finances
- description: Provides access to World Bank development data in SDMX (Statistical Data and Metadata eXchange) format, the international standard for statistical data sharing. Supports World Development Indicators (
  name: World Bank SDMX API
  slug: worldbank-sdmx
- description: The Classifications API from World Bank — 2 operation(s) for classifications.
  name: World Bank Classifications API
  slug: worldbank-classifications-api
- description: The Countries API from World Bank — 2 operation(s) for countries.
  name: World Bank Countries API
  slug: worldbank-countries-api
- description: The Indicators API from World Bank — 5 operation(s) for indicators.
  name: World Bank Indicators API
  slug: worldbank-indicators-api
- description: The Regions API from World Bank — 1 operation(s) for regions.
  name: World Bank Regions API
  slug: worldbank-regions-api
- description: The Sources API from World Bank — 1 operation(s) for sources.
  name: World Bank Sources API
  slug: worldbank-sources-api
- description: The Topics API from World Bank — 2 operation(s) for topics.
  name: World Bank Topics API
  slug: worldbank-topics-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/worldbank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/worldbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.worldbank.org
- group: docs
  title: ''
  type: Documentation
  url: https://datahelpdesk.worldbank.org/knowledgebase/articles/889386-developer-information-overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/worldbank
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/showcase/world-bank-development-economics
- group: company
  title: ''
  type: Blog
  url: https://blogs.worldbank.org/opendata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets
- group: other
  title: ''
  type: X
  url: https://x.com/worldbankdata
- group: commercial
  title: ''
  type: Plans
  url: plans/worldbank-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/worldbank-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/worldbank-finops.yml
created: '2026-06-13'
description: World Bank open data platform providing REST APIs for accessing global development data including GDP, poverty indicators, health metrics, education statistics, country profiles, financial data, climate information, and project operations. All data is freely available under Creative Commons Attribution 4.0 licensing with no authentication required for most endpoints.
finops:
- name: Worldbank Finops
  service_category: ''
  slug: worldbank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/worldbank.png
json_schemas:
- name: Country
  property_count: 10
  slug: country
- name: IndicatorValue
  property_count: 8
  slug: indicator-value
- name: PaginationData
  property_count: 7
  slug: pagination
jsonld:
- class_count: 21
  name: Worldbank Context
  property_count: 22
  slug: worldbank-context
layout: provider
modified: '2026-06-13'
name: World Bank
nav: Providers
network: true
overview: 'World Bank publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Classifications API, Countries API, Indicators API, and 3 more. Tagged areas include Development Data, Global Economics, GDP, Poverty, and Health Metrics.


  The World Bank catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  World Bank''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
random_paper: 62
rate_limits:
- limit_count: 9
  name: Worldbank Rate Limits
  slug: worldbank-rate-limits
rules:
- name: World Bank API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: worldbank-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.1
  delta: -4.7
  facets:
    commercial_clarity: 18.4
    contract_quality: 60.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/worldbank/refs/heads/main/screenshots/worldbank-2026-06-20T201620.png
security:
- kind: domain-security
  name: Worldbank Domain Security
  slug: worldbank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: worldbank
tags:
- Development Data
- Global Economics
- GDP
- Poverty
- Health Metrics
- Education
- Climate
- Finance
- World Bank
- Open Data
- Country Data
- Indicators
website: https://data.worldbank.org
---
