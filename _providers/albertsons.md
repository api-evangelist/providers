---
access_model:
  confidence: high
  label: Request access
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probe
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Albertsons Agentic Access
  operation_count: 6
  slug: albertsons-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- baseURL: https://api.albertsons.com
  baseurl_source: declared
  description: Manage audience targeting segments for retail media campaigns.
  name: albertsons Audiences API
  slug: albertsons-audiences-api
- baseURL: https://api.albertsons.com
  baseurl_source: declared
  description: Manage advertising campaigns on the Albertsons Media Collective.
  name: albertsons Campaigns API
  slug: albertsons-campaigns-api
- baseURL: https://api.albertsons.com
  baseurl_source: declared
  description: Access campaign performance metrics and analytics.
  name: albertsons Performance API
  slug: albertsons-performance-api
- baseURL: https://api.albertsons.com
  baseurl_source: declared
  description: Generate and retrieve performance reports.
  name: albertsons Reporting API
  slug: albertsons-reporting-api
artifact_total: 63
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Albertsons Media Collective Audiences API
  slug: open-albertsons-audiences-api
- collection_type: open
  name: Albertsons Media Collective Audiences Campaigns API
  slug: open-albertsons-campaigns-api
- collection_type: open
  name: Albertsons Media Collective Audiences Performance API
  slug: open-albertsons-performance-api
- collection_type: open
  name: Albertsons Media Collective Audiences Reporting API
  slug: open-albertsons-reporting-api
- collection_type: open
  name: Albertsons Media Collective API
  slug: open-albertsons-retail-media-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/albertsons-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/albertsons-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/albertsons-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/albertsons
- group: company
  title: ''
  type: Website
  url: https://www.albertsons.com
- group: start
  title: ''
  type: Portal
  url: https://portal-prod.apim.azwestus.stratus.albertsons.com/
- group: auth
  title: ''
  type: Authentication
  url: https://portal-prod.apim.azwestus.stratus.albertsons.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.albertsons.com/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.albertsonscompanies.com/about-us/our-policies/privacy-policy.html
- group: operate
  title: ''
  type: Support
  url: https://www.albertsons.com/contact-us.html
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/albertsons-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/albertsons-llms.txt
- group: design
  title: ''
  type: SpectralRules
  url: rules/albertsons-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/albertsons-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/albertsons-retail-media-api-context.jsonld
coverage:
  checked: '2026-08-13'
  detail: The Albertsons Media Collective API announced 2025-01-07 is issued only inside an advertising agreement, and the Azure API Management developer portal that fronted it is gone — the entire stratus.albertsons.com DNS zone now returns SERVFAIL from every public resolver, and the recorded base host api.albertsons.com is a stale record pointing at a decommissioned MyWebGrocer address with TCP 80 and 443 filtered, so there is no public reference or spec left to read.
  evidence:
  - status: 0
    url: https://portal-prod.apim.azwestus.stratus.albertsons.com/
  - status: 0
    url: https://api.albertsons.com/openapi.json
  - status: 404
    url: https://www.albertsons.com/llms.txt
  - status: 404
    url: https://www.albertsonsmediacollective.com/openapi.json
  - status: 200
    url: https://www.albertsonsmediacollective.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-03-23'
description: Albertsons Companies is one of the largest food and drug retailers in the United States, operating supermarkets and pharmacies under banners including Albertsons, Safeway, Vons, Jewel-Osco, Acme, Shaw's, Star Market, and others. The company operates the Albertsons Media Collective, a retail media network that provides advertisers API access to near-real-time campaign performance data and audience targeting capabilities based on shopper purchase behavior across its banner network.
examples:
- key_count: 5
  name: Retail Media Api Audience Example
  slug: retail-media-api-audience-example
- key_count: 4
  name: Retail Media Api Audience List Response Example
  slug: retail-media-api-audience-list-response-example
- key_count: 8
  name: Retail Media Api Campaign Example
  slug: retail-media-api-campaign-example
- key_count: 4
  name: Retail Media Api Campaign List Response Example
  slug: retail-media-api-campaign-list-response-example
- key_count: 5
  name: Retail Media Api Create Campaign Request Example
  slug: retail-media-api-create-campaign-request-example
- key_count: 3
  name: Retail Media Api Error Response Example
  slug: retail-media-api-error-response-example
- key_count: 8
  name: Retail Media Api Performance Metric Example
  slug: retail-media-api-performance-metric-example
- key_count: 2
  name: Retail Media Api Performance Metrics Response Example
  slug: retail-media-api-performance-metrics-response-example
- key_count: 6
  name: Retail Media Api Report Request Example
  slug: retail-media-api-report-request-example
- key_count: 4
  name: Retail Media Api Report Response Example
  slug: retail-media-api-report-response-example
features:
- description: Access advertising campaign performance data in near-real-time to bring metrics into custom dashboards and measurement models.
  name: Near-Real-Time Campaign Performance
- description: Target campaigns using audience segments derived from Albertsons shopper purchase behavior across grocery and pharmacy banners.
  name: Audience Targeting
- description: Create, update, and manage advertising campaigns with budget controls, scheduling, and audience targeting configurations.
  name: Campaign Management
- description: Generate configurable performance reports with custom dimensions and metrics for export to external analytics tools.
  name: Custom Reporting
- description: Interactive developer portal built on Microsoft Azure API Management with documentation, code samples, and an API testing console.
  name: Azure API Management Portal
- description: Access to shopper audiences across Albertsons, Safeway, Vons, Jewel-Osco, Acme, and other banner networks.
  name: Multi-Banner Reach
finops:
- name: Albertsons Finops
  service_category: Retail Media
  slug: albertsons-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/albertsons.png
integrations:
- description: Partnership integration for enhanced audience measurement and identity resolution using TransUnion data.
  name: TransUnion
- description: Developer portal and API gateway infrastructure built on Microsoft Azure API Management.
  name: Microsoft Azure
- description: Export campaign data to third-party analytics dashboards and reporting tools via the Performance API.
  name: Analytics Platforms
json_schemas:
- name: Audience List Response
  property_count: 4
  slug: retail-media-api-audience-list-response
- name: Audience
  property_count: 5
  slug: retail-media-api-audience
- name: Campaign List Response
  property_count: 4
  slug: retail-media-api-campaign-list-response
- name: Campaign
  property_count: 8
  slug: retail-media-api-campaign
- name: Create Campaign Request
  property_count: 5
  slug: retail-media-api-create-campaign-request
- name: Error Response
  property_count: 3
  slug: retail-media-api-error-response
- name: Performance Metric
  property_count: 8
  slug: retail-media-api-performance-metric
- name: Performance Metrics Response
  property_count: 2
  slug: retail-media-api-performance-metrics-response
- name: Report Request
  property_count: 6
  slug: retail-media-api-report-request
- name: Report Response
  property_count: 4
  slug: retail-media-api-report-response
json_structures:
- name: Retail Media Api Audience List Response Structure
  property_count: 4
  slug: retail-media-api-audience-list-response-structure
- name: Retail Media Api Audience Structure
  property_count: 5
  slug: retail-media-api-audience-structure
- name: Retail Media Api Campaign List Response Structure
  property_count: 4
  slug: retail-media-api-campaign-list-response-structure
- name: Retail Media Api Campaign Structure
  property_count: 8
  slug: retail-media-api-campaign-structure
- name: Retail Media Api Create Campaign Request Structure
  property_count: 5
  slug: retail-media-api-create-campaign-request-structure
- name: Retail Media Api Error Response Structure
  property_count: 3
  slug: retail-media-api-error-response-structure
- name: Retail Media Api Performance Metric Structure
  property_count: 8
  slug: retail-media-api-performance-metric-structure
- name: Retail Media Api Performance Metrics Response Structure
  property_count: 2
  slug: retail-media-api-performance-metrics-response-structure
- name: Retail Media Api Report Request Structure
  property_count: 6
  slug: retail-media-api-report-request-structure
- name: Retail Media Api Report Response Structure
  property_count: 4
  slug: retail-media-api-report-response-structure
jsonld:
- class_count: 13
  name: Albertsons Retail Media Api Context
  property_count: 30
  slug: albertsons-retail-media-api-context
layout: provider
modified: '2026-08-13'
name: Albertsons
nav: Providers
network: true
overview: 'Albertsons publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Audiences API, Campaigns API, Performance API, and 1 more. Tagged areas include Grocery, Retail, Retail Media, Advertising, and Campaigns.


  The Albertsons catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Albertsons'' developer surface includes authentication, developer portal, support, and 12 more developer resources.'
plans:
- name: Albertsons Plans Pricing
  plan_count: 0
  slug: albertsons-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Albertsons Rate Limits
  slug: albertsons-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Albertsons API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: albertsons-jsonschema-spectral-rules
- effective_rule_count: 83
  extends:
  - spectral:oas
  name: Albertsons API Rules
  rule_count: 42
  severity_counts:
    error: 16
    hint: 0
    info: 6
    warn: 20
  slug: albertsons-spectral-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 73.5
    catalog_earned_first_party: 0.0
    catalog_gap: 41.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 29.3
    developer_ergonomics: 25.0
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 0.0
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Albertsons Authentication
  slug: albertsons-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Albertsons Domain Security
  slug: albertsons-domain-security
  summary_line: TLSv1.3 · DMARC
slug: albertsons
tags:
- Grocery
- Retail
- Retail Media
- Advertising
- Campaigns
- Analytics
- Consumer Goods
- Food
- Pharmacy
use_cases:
- description: Pull near-real-time campaign metrics into custom brand or agency dashboards for monitoring impressions, clicks, and ROAS.
  name: Campaign Performance Dashboards
- description: Integrate campaign performance data into automated bidding and budget allocation systems.
  name: Automated Budget Optimization
- description: Share campaign performance data with measurement partners like TransUnion for attribution and audience analysis.
  name: Third-Party Measurement Integration
- description: Incorporate Albertsons retail media performance data into multi-channel media mix models.
  name: Media Mix Modeling
- description: Analyze shopper audience segments to inform product marketing strategy and campaign targeting decisions.
  name: Audience Insights
website: https://www.albertsons.com
---
