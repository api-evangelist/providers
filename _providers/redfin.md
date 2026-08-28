---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Redfin Agentic Access
  operation_count: 19
  slug: redfin-agentic-access
  summary_line: 19 operations
api_count: 7
apis:
- description: Endpoints for exporting property search results in CSV format.
  name: Redfin CSV Export API
  slug: redfin-csv-export-api
- description: Downloadable housing market tracker datasets segmented by region level.
  name: Redfin Market Tracker API
  slug: redfin-market-tracker-api
- description: Endpoints for regional aggregate and historical market trends.
  name: Redfin Market Trends API
  slug: redfin-market-trends-api
- description: Endpoints for neighborhood statistics, commute data, and area info.
  name: Redfin Neighborhood API
  slug: redfin-neighborhood-api
- description: Endpoints for retrieving detailed information about a specific property.
  name: Redfin Property Details API
  slug: redfin-property-details-api
- description: Endpoints for searching properties by location, region, and filters.
  name: Redfin Search API
  slug: redfin-search-api
- description: Endpoints for automated valuation model (AVM) data and estimates.
  name: Redfin Valuation API
  slug: redfin-valuation-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Redfin Data Center CSV Export API
  slug: open-redfin-csv-export-api
- collection_type: open
  name: Redfin Data Center
  slug: open-redfin-data-center
- collection_type: open
  name: Redfin GIS CSV Export API
  slug: open-redfin-gis-csv-api
- collection_type: open
  name: Redfin Data Center CSV Export Market Tracker API
  slug: open-redfin-market-tracker-api
- collection_type: open
  name: Redfin Data Center CSV Export Market Trends API
  slug: open-redfin-market-trends-api
- collection_type: open
  name: Redfin Data Center CSV Export Neighborhood API
  slug: open-redfin-neighborhood-api
- collection_type: open
  name: Redfin Data Center CSV Export Property Details API
  slug: open-redfin-property-details-api
- collection_type: open
  name: Redfin Data Center CSV Export Search API
  slug: open-redfin-search-api
- collection_type: open
  name: Redfin Stingray API
  slug: open-redfin-stingray-api
- collection_type: open
  name: Redfin Data Center CSV Export Valuation API
  slug: open-redfin-valuation-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/redfin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redfin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.redfin.com
- group: company
  title: ''
  type: Blog
  url: https://www.redfin.com/news/
- group: operate
  title: ''
  type: Support
  url: https://support.redfin.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redfin.com/about/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redfin.com/about/terms-of-use
- group: start
  title: ''
  type: Login
  url: https://www.redfin.com/login
- group: other
  title: ''
  type: DataCenter
  url: https://www.redfin.com/news/data-center/
- group: company
  title: ''
  type: News
  url: https://www.redfin.com/news/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/redfin
- group: other
  title: ''
  type: X
  url: https://twitter.com/redfin
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.redfin.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/redfin
created: '2026-03-20'
description: Redfin is a technology-powered real estate brokerage that provides property search, home value estimates, listing details, neighborhood statistics, commute data, and downloadable housing market data across the United States. Their platform exposes a Stingray REST API used by the Redfin website and mobile apps, a GIS CSV Export endpoint for bulk property downloads, and the Redfin Data Center for time-series housing market statistics at national, metro, state, county, city, ZIP code, and neighborhood levels.
examples:
- key_count: 2
  name: Redfin Gis Search Example
  slug: redfin-gis-search-example
- key_count: 3
  name: Redfin Market Tracker Example
  slug: redfin-market-tracker-example
- key_count: 2
  name: Redfin Property Details Example
  slug: redfin-property-details-example
finops:
- name: Redfin Finops
  service_category: Real Estate Data
  slug: redfin-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Redfin real estate platform. Redfin does not publish an official GraphQL API; this schema is derived from the publicly documented Redfin Sti
  name: Redfin GraphQL Schema
  slug: redfin-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/redfin.png
json_schemas:
- name: Redfin Market Tracker Record
  property_count: 38
  slug: redfin-market-tracker
- name: Redfin Property
  property_count: 25
  slug: redfin-property
json_structures:
- name: Redfin Market Tracker Structure
  property_count: 0
  slug: redfin-market-tracker-structure
- name: Redfin Property Structure
  property_count: 0
  slug: redfin-property-structure
jsonld:
- class_count: 0
  name: Redfin Context
  property_count: 4
  slug: redfin-context
layout: provider
modified: '2026-05-19'
name: Redfin
nav: Providers
network: true
overview: 'Redfin publishes 7 APIs on the [APIs.io](https://apis.io/) network, including CSV Export API, Market Tracker API, Market Trends API, and 4 more. Tagged areas include CSV Export, GIS, Home Values, Housing Market, and Listings.


  The Redfin catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Redfin''s developer surface includes engineering blog, support, product news, and 11 more developer resources.'
plans:
- name: Redfin Plans Pricing
  plan_count: 1
  slug: redfin-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Redfin Rate Limits
  slug: redfin-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Redfin API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: redfin-jsonschema-spectral-rules
- effective_rule_count: 10
  extends: []
  name: Redfin API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 6
  slug: redfin-rules
score:
  band: developing
  composite: 41.2
  delta: 3.8
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 25.0
    contract_quality: 62.3
    developer_ergonomics: 16.7
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/redfin/refs/heads/main/screenshots/redfin-2026-08-17T125152.png
security:
- kind: domain-security
  name: Redfin Domain Security
  slug: redfin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: redfin
tags:
- CSV Export
- GIS
- Home Values
- Housing Market
- Listings
- Property Data
- Real-Estate
website: https://www.redfin.com
---
