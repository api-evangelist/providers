---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dbnomics Agentic Access
  operation_count: 9
  slug: dbnomics-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://api.db.nomics.world/v22
  baseurl_source: declared
  description: Dataset metadata within a provider, plus the last-updates feed.
  name: DBnomics Datasets API
  slug: dbnomics-datasets-api
- baseURL: https://api.db.nomics.world/v22
  baseurl_source: declared
  description: Statistical agencies, central banks, and institutions aggregated by DBnomics.
  name: DBnomics Providers API
  slug: dbnomics-providers-api
- baseURL: https://api.db.nomics.world/v22
  baseurl_source: declared
  description: Full-text search across all datasets.
  name: DBnomics Search API
  slug: dbnomics-search-api
- baseURL: https://api.db.nomics.world/v22
  baseurl_source: declared
  description: Economic time series and their observations.
  name: DBnomics Series API
  slug: dbnomics-series-api
artifact_total: 15
collections:
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
  href: https://artifacts.apis.io/dbnomics/agentic-access/dbnomics-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dbnomics-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/dbnomics/security/dbnomics-domain-security.yml
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
  href: https://artifacts.apis.io/dbnomics/plans/dbnomics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dbnomics-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dbnomics/rate-limits/dbnomics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dbnomics-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dbnomics/finops/dbnomics-finops.yml
  title: ''
  type: FinOps
  url: finops/dbnomics-finops.yml
created: '2026-07-11'
description: DBnomics is the world's economic database - a free, open-source aggregator run by Cepremap that harvests macroeconomic time series from more than 90 national and international providers (IMF, ECB, Eurostat, World Bank, OECD, BLS, BEA, Banque de France, Federal Statistical Office Germany, and many more) into one standardized format. Hundreds of millions of series covering economic indicators, government statistics, prices, employment, trade, and finance are refreshed daily and served through a documented public REST API (api.db.nomics.world/v22) that requires no API key, plus official Python and R clients and community clients for Julia, Matlab, Stata, EViews, and Gretl.
finops:
- has_sources: true
  method: generated
  name: Dbnomics Finops
  primary_unit: ''
  service_category: Analytics and Open Data
  slug: dbnomics-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dbnomics.png
layout: provider
modified: '2026-07-11'
name: DBnomics
nav: Providers
network: true
overview: 'DBnomics publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Datasets API, Providers API, Search API, and 1 more. Tagged areas include Economic Indicators, Macroeconomics, Open Data, Statistics, and Time Series.


  The DBnomics catalog on APIs.io includes 1 Spectral governance ruleset.


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
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: DBnomics API Rules
  rule_count: 55
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 1
  slug: dbnomics-rules
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 51.4
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 24.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/dbnomics/dbnomics-2026-07-25T211453.png
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
