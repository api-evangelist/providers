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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agricultural Marketing Service Agentic Access
  operation_count: 3
  slug: agricultural-marketing-service-agentic-access
  summary_line: 3 operations
api_count: 4
apis:
- description: The USDA Local Food Directories API provides data sharing access to directory information for farmers markets, food hubs, on-farm markets, community supported agriculture (CSA) operations, and food co
  name: USDA Local Food Directories API
  slug: usda-local-food-directories-api
- baseURL: https://marsapi.ams.usda.gov/services/v1.2
  baseurl_source: declared
  description: USDA AMS market news offices
  name: Agricultural Marketing Service Offices API
  slug: agricultural-marketing-service-offices-api
- baseURL: https://marsapi.ams.usda.gov/services/v1.2
  baseurl_source: declared
  description: Agricultural market news reports across all commodity types
  name: Agricultural Marketing Service Reports API
  slug: agricultural-marketing-service-reports-api
- description: The Livestock Mandatory Price Reporting System (LMPRS) API provides programmatic access to federally mandated livestock price report data. The API requires no authentication for public access and retu
  name: USDA AMS LMPRS API (Livestock Mandatory Price Reporting)
  slug: usda-ams-lmprs-api-livestock-mandatory-price-reporting
artifact_total: 55
collections:
- collection_type: postman
  name: USDA AMS MARS API (MyMarketNews) Offices API
  slug: postman-agricultural-marketing-service-offices-api
- collection_type: postman
  name: USDA AMS MARS API (MyMarketNews) Offices Reports API
  slug: postman-agricultural-marketing-service-reports-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USDA AMS MARS API (MyMarketNews) Offices API
  slug: open-agricultural-marketing-service-offices-api
- collection_type: open
  name: USDA AMS MARS API (MyMarketNews) Offices Reports API
  slug: open-agricultural-marketing-service-reports-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/agricultural-marketing-service/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agricultural-marketing-service-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agricultural-marketing-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agricultural-marketing-service-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ams.usda.gov/rss.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amsusda
- group: company
  title: ''
  type: Website
  url: https://www.ams.usda.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.ams.usda.gov/resources/apis-open-data
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usda
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usda.gov/policies-and-links
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usda.gov/privacy-policy
- group: design
  title: ''
  type: SpectralRules
  url: rules/agricultural-marketing-service-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/agricultural-marketing-service-vocabulary.yaml
created: '2024-11-21'
description: 'The Agricultural Marketing Service (AMS), an agency of the United States Department of Agriculture (USDA), oversees programs in five commodity areas: cotton and tobacco, dairy, fruits and vegetables, livestock and seeds, and poultry. AMS provides testing, standardization, grading, and market news services. AMS operates several public APIs for agricultural market data including the Market Analysis Reporting System (MARS) API for real-time commodity market news and the Livestock Mandatory Price Reporting System (LMPRS) API for livestock price data.'
examples:
- key_count: 3
  name: Mars Api Error Response Example
  slug: mars-api-error-response-example
- key_count: 5
  name: Mars Api Office Example
  slug: mars-api-office-example
- key_count: 1
  name: Mars Api Offices List Response Example
  slug: mars-api-offices-list-response-example
- key_count: 2
  name: Mars Api Pagination Stats Example
  slug: mars-api-pagination-stats-example
- key_count: 11
  name: Mars Api Report Data Example
  slug: mars-api-report-data-example
- key_count: 2
  name: Mars Api Report Data Response Example
  slug: mars-api-report-data-response-example
- key_count: 8
  name: Mars Api Report Example
  slug: mars-api-report-example
- key_count: 2
  name: Mars Api Reports List Response Example
  slug: mars-api-reports-list-response-example
features:
- description: The MARS and LMPRS APIs are publicly accessible without authentication; registered users can obtain API keys for higher rate limits.
  name: No Authentication Required
- description: All API responses are returned in JSON format including errors and paginated results.
  name: JSON Data Format
- description: MARS API provides up-to-date commodity price and volume data as reports are released by AMS market reporters.
  name: Real-Time Market News
- description: Access up to 180 days of historical market data per request with up to 100,000 records returned per call.
  name: Historical Data Access
- description: Market data covers livestock, dairy, fruits, vegetables, grains, cotton, tobacco, poultry, and other agricultural commodities.
  name: Commodity Coverage
- description: LMPRS API provides federally mandated livestock price data under the Livestock Mandatory Reporting Act.
  name: Mandatory Price Reporting
finops:
- name: Agricultural Marketing Service Finops
  service_category: API
  slug: agricultural-marketing-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agricultural-marketing-service.png
integrations:
- description: USDA AMS provides guides for integrating MARS API data directly into Microsoft Excel for market analysis.
  name: Microsoft Excel
- description: AMS APIs are accessible through the federal api.data.gov gateway for consistent API key management.
  name: api.data.gov
json_schemas:
- name: Error Response
  property_count: 3
  slug: mars-api-error-response
- name: Office
  property_count: 5
  slug: mars-api-office
- name: Offices List Response
  property_count: 1
  slug: mars-api-offices-list-response
- name: Pagination Stats
  property_count: 2
  slug: mars-api-pagination-stats
- name: Report Data Response
  property_count: 2
  slug: mars-api-report-data-response
- name: Report Data
  property_count: 11
  slug: mars-api-report-data
- name: Report
  property_count: 8
  slug: mars-api-report
- name: Reports List Response
  property_count: 2
  slug: mars-api-reports-list-response
json_structures:
- name: Mars Api Error Response Structure
  property_count: 3
  slug: mars-api-error-response-structure
- name: Mars Api Office Structure
  property_count: 5
  slug: mars-api-office-structure
- name: Mars Api Offices List Response Structure
  property_count: 1
  slug: mars-api-offices-list-response-structure
- name: Mars Api Pagination Stats Structure
  property_count: 2
  slug: mars-api-pagination-stats-structure
- name: Mars Api Report Data Response Structure
  property_count: 2
  slug: mars-api-report-data-response-structure
- name: Mars Api Report Data Structure
  property_count: 11
  slug: mars-api-report-data-structure
- name: Mars Api Report Structure
  property_count: 8
  slug: mars-api-report-structure
- name: Mars Api Reports List Response Structure
  property_count: 2
  slug: mars-api-reports-list-response-structure
jsonld:
- class_count: 9
  name: Agricultural Marketing Service Mars Api Context
  property_count: 25
  slug: agricultural-marketing-service-mars-api-context
layout: provider
modified: '2026-07-25'
name: Agricultural Marketing Service
nav: Providers
network: true
overview: 'Agricultural Marketing Service publishes 2 APIs on the [APIs.io](https://apis.io/) network: Offices API and Reports API. Tagged areas include Agriculture, Federal-Government, Market News, Livestock, and Dairy.


  The Agricultural Marketing Service catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Agricultural Marketing Service''s developer surface includes authentication, engineering blog, developer portal, and 10 more developer resources.'
plans:
- name: Agricultural Marketing Service Plans Pricing
  plan_count: 3
  slug: agricultural-marketing-service-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Agricultural Marketing Service Rate Limits
  slug: agricultural-marketing-service-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Agricultural Marketing Service API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agricultural-marketing-service-jsonschema-spectral-rules
- effective_rule_count: 70
  extends:
  - spectral:oas
  name: Agricultural Marketing Service API Rules
  rule_count: 29
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 19
  slug: agricultural-marketing-service-spectral-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 35.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 28.7
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agricultural-marketing-service/refs/heads/main/screenshots/agricultural-marketing-service-2026-06-20T170415.png
security:
- kind: authentication
  name: Agricultural Marketing Service Authentication
  slug: agricultural-marketing-service-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agricultural Marketing Service Domain Security
  slug: agricultural-marketing-service-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: agricultural-marketing-service
tags:
- Agriculture
- Federal-Government
- Market News
- Livestock
- Dairy
- Fruits And Vegetables
- Cotton
- Tobacco
use_cases:
- description: Track commodity prices across livestock, dairy, fruits, and vegetables to support trading, purchasing, and production decisions.
  name: Agricultural Price Monitoring
- description: Pull historical and current market news data for academic research, economic analysis, and policy work.
  name: Market Analysis and Research
- description: Integrate USDA market news data into supply chain management and procurement systems for real-time pricing.
  name: Supply Chain Integration
- description: Use the Local Food Directories API to locate and integrate data about farmers markets, CSAs, and food hubs.
  name: Local Food System Mapping
- description: Build automated price monitoring systems using the MARS API to trigger alerts when prices cross defined thresholds.
  name: Commodity Price Alerts
website: https://www.ams.usda.gov/
---
