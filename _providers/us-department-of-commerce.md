---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  name: Us Department Of Commerce Agentic Access
  operation_count: 5
  slug: us-department-of-commerce-agentic-access
  summary_line: 5 operations
api_count: 9
apis:
- description: The Census Bureau's Data API provides access to a broad range of demographic, economic, and geographic datasets including the American Community Survey, Decennial Census, Economic Census, and speciali
  name: US Census Bureau Data API
  slug: census-bureau-api
- description: The Bureau of Economic Analysis API provides access to national, regional, and international economic data including GDP, personal income, corporate profits, international trade and investment, and in
  name: Bureau of Economic Analysis API
  slug: bea-api
- description: The International Trade Administration Data Services Platform provides authoritative information on U.S. exporting and international trade, aggregating data from multiple federal agencies including th
  name: International Trade Administration Trade Data API
  slug: ita-trade-api
- description: The NOAA Climate Data Online Web Services API provides access to climate data including temperature, precipitation, wind, and weather observations from NOAA's National Centers for Environmental Inform
  name: NOAA Climate and Weather API
  slug: noaa-api
- description: The National Institute of Standards and Technology provides a Data Discovery API giving access to NIST's public data collections and research datasets covering materials science, chemistry, physics, e
  name: NIST Data Discovery API
  slug: nist-api
- description: The Commerce Data Hub Open Data Portal API (version 2.3) provides REST access to the Department of Commerce's open data catalog with rich search capabilities for discovering and accessing Commerce dat
  name: Commerce Data Hub Open Data Portal API
  slug: commerce-data-hub-api
- description: Blog posts published on Commerce.gov
  name: US Department of Commerce Blogs API
  slug: us-department-of-commerce-blogs-api
- description: Images published on Commerce.gov
  name: US Department of Commerce Images API
  slug: us-department-of-commerce-images-api
- description: News articles published on Commerce.gov
  name: US Department of Commerce News API
  slug: us-department-of-commerce-news-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Commerce.gov API
  slug: open-commerce-gov-api
- collection_type: open
  name: Commerce.gov Blogs API
  slug: open-us-department-of-commerce-blogs-api
- collection_type: open
  name: Commerce.gov Blogs Images API
  slug: open-us-department-of-commerce-images-api
- collection_type: open
  name: Commerce.gov Blogs News API
  slug: open-us-department-of-commerce-news-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-department-of-commerce-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-department-of-commerce-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/commercegov
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s-department-of-commerce
created: '2024-12-03'
description: The US Department of Commerce is responsible for promoting economic growth and job creation in the United States. It oversees various programs and initiatives aimed at supporting businesses, industries, and communities across the country. The department works to ensure fair trade practices, protect intellectual property, and promote innovation and entrepreneurship. It also collects and analyzes economic data to inform policy decisions and help businesses make informed decisions. The Commerce Department houses bureaus including the Census Bureau, Bureau of Economic Analysis, International Trade Administration, NOAA, and NIST, each offering public APIs for their respective data domains.
examples:
- key_count: 3
  name: Commerce Gov List News Example
  slug: commerce-gov-list-news-example
finops:
- name: Us Department Of Commerce Finops
  service_category: Government Open Data
  slug: us-department-of-commerce-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-department-of-commerce.png
json_schemas:
- name: Commerce.gov News Article
  property_count: 9
  slug: commerce-gov-news-article
json_structures:
- name: Commerce Gov News Article Structure
  property_count: 0
  slug: commerce-gov-news-article-structure
jsonld:
- class_count: 11
  name: Us Department Of Commerce Context
  property_count: 6
  slug: us-department-of-commerce-context
layout: provider
modified: '2026-05-19'
name: US Department of Commerce
nav: Providers
network: true
overview: 'US Department of Commerce publishes 3 APIs on the [APIs.io](https://apis.io/) network: Blogs API, Images API, and News API. Tagged areas include Commerce, Federal-Government, Open Data, Trade, and Economic Data.


  The US Department of Commerce catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Us Department Of Commerce Plans Pricing
  plan_count: 1
  slug: us-department-of-commerce-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Us Department Of Commerce Rate Limits
  slug: us-department-of-commerce-rate-limits
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: US Department of Commerce API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 7
  slug: commerce-gov-api-rules
- effective_rule_count: 5
  extends: []
  name: US Department of Commerce API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: us-department-of-commerce-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.2
  delta: 1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 54.5
    contract_quality: 56.5
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 54.5
    operational_transparency: 10.5
  previous_composite: 28.3
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
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-department-of-commerce/refs/heads/main/screenshots/us-department-of-commerce-2026-06-20T200620.png
security:
- kind: domain-security
  name: Us Department Of Commerce Domain Security
  slug: us-department-of-commerce-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: us-department-of-commerce
tags:
- Commerce
- Federal-Government
- Open Data
- Trade
- Economic Data
- Climate
- Standards
---
