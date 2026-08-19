---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bureau Of Transportation Statistics Agentic Access
  operation_count: 5
  slug: bureau-of-transportation-statistics-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: The BTS Open Data portal powered by Socrata provides programmatic access to transportation datasets via the Socrata Open Data API (SODA). Supports filtering, querying, and aggregation across aviation,
  name: BTS Open Data SODA API
  slug: bts-open-data-soda-api
- description: TranStats is BTS's aviation and transportation statistics database providing flight on-time performance data, carrier and airport snapshots, fuel consumption data, and comprehensive airline statistics
  name: TranStats - Airline On-Time Performance Data
  slug: transtats
- description: The Freight Analysis Framework integrates data from multiple sources to create a comprehensive picture of freight flows to, from, within, and through the United States. Includes volume, value, and mod
  name: BTS Freight Analysis Framework (FAF)
  slug: bts-freight-data
- description: Dataset and view metadata
  name: Bureau of Transportation Statistics Metadata API
  slug: bureau-of-transportation-statistics-metadata-api
- description: Dataset resource queries via SoQL
  name: Bureau of Transportation Statistics Resource API
  slug: bureau-of-transportation-statistics-resource-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BTS Open Data SODA Metadata API
  slug: open-bureau-of-transportation-statistics-metadata-api
- collection_type: open
  name: BTS Open Data SODA Metadata Resource API
  slug: open-bureau-of-transportation-statistics-resource-api
- collection_type: open
  name: BTS Open Data SODA API
  slug: open-bureau-of-transportation-statistics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bureau-of-transportation-statistics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-transportation-statistics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bureau-of-transportation-statistics-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dotbts
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-transportation-statistics-bts
- group: company
  title: ''
  type: Website
  url: https://www.bts.gov
- group: start
  title: ''
  type: Portal
  url: https://data.bts.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bts.gov/privacy-policy
- group: other
  title: ''
  type: TranStats
  url: https://www.transtats.bts.gov/
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=dot-gov&q=bts
created: '2024-11-30'
description: The Bureau of Transportation Statistics (BTS), part of the Department of Transportation (DOT) is the preeminent source of statistics on commercial aviation, multimodal freight activity, and transportation economics, and provides context to decision makers and the public for understanding statistics on transportation.
finops:
- name: Bureau Of Transportation Statistics Finops
  service_category: API
  slug: bureau-of-transportation-statistics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-transportation-statistics.png
layout: provider
modified: '2026-04-23'
name: Bureau of Transportation Statistics
nav: Providers
network: true
overview: 'Bureau of Transportation Statistics publishes 2 APIs on the [APIs.io](https://apis.io/) network: Metadata API and Resource API. Tagged areas include Federal Government, Statistics, Transportation, Aviation, and Freight.


  Bureau of Transportation Statistics'' developer surface includes authentication, developer portal, and 8 more developer resources.'
plans:
- name: Bureau Of Transportation Statistics Plans Pricing
  plan_count: 3
  slug: bureau-of-transportation-statistics-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 5
  name: Bureau Of Transportation Statistics Rate Limits
  slug: bureau-of-transportation-statistics-rate-limits
score:
  band: thin
  composite: 31.5
  delta: 0.6
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-transportation-statistics/refs/heads/main/screenshots/bureau-of-transportation-statistics-2026-06-20T173820.png
security:
- kind: authentication
  name: Bureau Of Transportation Statistics Authentication
  slug: bureau-of-transportation-statistics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bureau Of Transportation Statistics Domain Security
  slug: bureau-of-transportation-statistics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bureau-of-transportation-statistics
tags:
- Federal Government
- Statistics
- Transportation
- Aviation
- Freight
- Open Data
website: https://www.bts.gov
---
