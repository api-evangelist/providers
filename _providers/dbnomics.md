---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dbnomics Agentic Access
  operation_count: 9
  slug: dbnomics-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: Dataset metadata within a provider, plus the last-updates feed.
  name: DBnomics Datasets API
  slug: dbnomics-datasets-api
- description: Statistical agencies, central banks, and institutions aggregated by DBnomics.
  name: DBnomics Providers API
  slug: dbnomics-providers-api
- description: Full-text search across all datasets.
  name: DBnomics Search API
  slug: dbnomics-search-api
- description: Economic time series and their observations.
  name: DBnomics Series API
  slug: dbnomics-series-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DBnomics Datasets API
  slug: open-dbnomics-datasets-api
- collection_type: open
  name: DBnomics Datasets Providers API
  slug: open-dbnomics-providers-api
- collection_type: open
  name: DBnomics Datasets Search API
  slug: open-dbnomics-search-api
- collection_type: open
  name: DBnomics Datasets Series API
  slug: open-dbnomics-series-api
- collection_type: open
  name: DBnomics API
  slug: open-dbnomics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dbnomics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dbnomics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://db.nomics.world
- group: docs
  title: ''
  type: Documentation
  url: https://docs.db.nomics.world
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dbnomics
- group: commercial
  title: ''
  type: Plans
  url: plans/dbnomics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dbnomics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dbnomics-finops.yml
created: '2026-07-11'
description: DBnomics is the world's economic database - a free, open-source aggregator run by Cepremap that harvests macroeconomic time series from more than 90 national and international providers (IMF, ECB, Eurostat, World Bank, OECD, BLS, BEA, Banque de France, Federal Statistical Office Germany, and many more) into one standardized format. Hundreds of millions of series covering economic indicators, government statistics, prices, employment, trade, and finance are refreshed daily and served through a documented public REST API (api.db.nomics.world/v22) that requires no API key, plus official Python and R clients and community clients for Julia, Matlab, Stata, EViews, and Gretl.
finops:
- name: Dbnomics Finops
  service_category: Analytics and Open Data
  slug: dbnomics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dbnomics.png
layout: provider
modified: '2026-07-11'
name: DBnomics
nav: Providers
network: true
overview: 'DBnomics publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Providers API, Search API, and 1 more. Tagged areas include Economic Indicators, Macroeconomics, Open Data, Statistics, and Time Series.


  DBnomics'' developer surface includes documentation and 7 more developer resources.'
plans:
- name: Dbnomics Plans Pricing
  plan_count: 2
  slug: dbnomics-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Dbnomics Rate Limits
  slug: dbnomics-rate-limits
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 51.4
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dbnomics/refs/heads/main/screenshots/dbnomics-2026-07-25T211453.png
security:
- kind: domain-security
  name: Dbnomics Domain Security
  slug: dbnomics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dbnomics
tags:
- Economic Indicators
- Macroeconomics
- Open Data
- Statistics
- Time Series
- Government Data
website: https://db.nomics.world
---
