---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Us Abilityone Commission Agentic Access
  operation_count: 6
  slug: us-abilityone-commission-agentic-access
  summary_line: 6 operations
api_count: 4
apis:
- description: Nonprofit agencies participating in the AbilityOne program
  name: US AbilityOne Commission Agencies API
  slug: us-abilityone-commission-agencies-api
- description: AbilityOne Procurement List products identified by NSN
  name: US AbilityOne Commission Products API
  slug: us-abilityone-commission-products-api
- description: Procurement list reports and data downloads
  name: US AbilityOne Commission Reports API
  slug: us-abilityone-commission-reports-api
- description: AbilityOne Procurement List services
  name: US AbilityOne Commission Services API
  slug: us-abilityone-commission-services-api
artifact_total: 48
collections:
- collection_type: open
  name: AbilityOne Procurement List API
  slug: open-abilityone-procurement-list-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-abilityone-commission-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-abilityone-commission-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-abilityone-commission
- group: company
  title: ''
  type: Website
  url: https://www.abilityone.gov
- group: start
  title: PLIMS - Procurement List Information Management System
  type: Portal
  url: https://plims.abilityone.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.abilityone.gov/procurement_list/
- group: other
  title: Procurement List Data Downloads
  type: DataAPI
  url: https://plims.abilityone.gov/reports/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/us-abilityone-commission-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/us-abilityone-commission-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/us-abilityone-commission-vocabulary.yaml
created: '2024-11-20'
description: The US AbilityOne Commission is an independent federal agency that administers the AbilityOne Program, which creates employment opportunities for individuals who are blind or have significant disabilities. Operating under the Javits-Wagner-O'Day (JWOD) Act, the Commission maintains the AbilityOne Procurement List — a catalog of products and services that federal agencies are required to purchase from qualified nonprofit agencies employing people who are blind or have significant disabilities. The PLIMS (Procurement List Information Management System) provides web-based search access to the products and services list. Two central nonprofit agencies, NIB (National Industries for the Blind) and SourceAmerica, manage the affiliated nonprofit network.
examples:
- key_count: 10
  name: Procurement List Api Agency Example
  slug: procurement-list-api-agency-example
- key_count: 2
  name: Procurement List Api Agencylistresponse Example
  slug: procurement-list-api-agencylistresponse-example
- key_count: 3
  name: Procurement List Api Apierror Example
  slug: procurement-list-api-apierror-example
- key_count: 11
  name: Procurement List Api Product Example
  slug: procurement-list-api-product-example
- key_count: 4
  name: Procurement List Api Productsearchresponse Example
  slug: procurement-list-api-productsearchresponse-example
- key_count: 9
  name: Procurement List Api Service Example
  slug: procurement-list-api-service-example
- key_count: 4
  name: Procurement List Api Servicesearchresponse Example
  slug: procurement-list-api-servicesearchresponse-example
features:
- description: Web-based search of the AbilityOne Procurement List by NSN, product description, agency, and nonprofit affiliate via PLIMS.
  name: Procurement List Search
- description: Searchable and downloadable catalog of products on the AbilityOne Procurement List, identified by National Stock Number (NSN).
  name: Products List
- description: Searchable catalog of services on the AbilityOne Procurement List, organized by service category and performing nonprofit agency.
  name: Services List
- description: Directory of NIB-affiliated and SourceAmerica-affiliated nonprofit agencies that employ people who are blind or have significant disabilities.
  name: Nonprofit Agency Directory
- description: Downloadable Excel reports of the Procurement List products and services, nonprofit agency rosters, and distributor lists.
  name: Reports and Data Downloads
finops:
- name: Us Abilityone Commission Finops
  service_category: API
  slug: us-abilityone-commission-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-abilityone-commission.png
integrations:
- description: Central nonprofit agency managing blind-employing organizations participating in the AbilityOne program.
  name: NIB (National Industries for the Blind)
- description: Central nonprofit agency managing organizations employing people with significant disabilities in the AbilityOne program.
  name: SourceAmerica
- description: GSA procurement platform where AbilityOne products are listed and available for federal purchase.
  name: GSA Advantage
- description: System for Award Management integration for federal contract and acquisition data linked to AbilityOne awards.
  name: SAM.gov
- description: Federal Procurement Data System tracking AbilityOne program spending and contract awards across federal agencies.
  name: FPDS
json_schemas:
- name: Agency
  property_count: 10
  slug: procurement-list-api-agency
- name: AgencyListResponse
  property_count: 2
  slug: procurement-list-api-agencylistresponse
- name: APIError
  property_count: 3
  slug: procurement-list-api-apierror
- name: Product
  property_count: 11
  slug: procurement-list-api-product
- name: ProductSearchResponse
  property_count: 4
  slug: procurement-list-api-productsearchresponse
- name: Service
  property_count: 9
  slug: procurement-list-api-service
- name: ServiceSearchResponse
  property_count: 4
  slug: procurement-list-api-servicesearchresponse
json_structures:
- name: Procurement List Api Agency Structure
  property_count: 0
  slug: procurement-list-api-agency-structure
- name: Procurement List Api Agencylistresponse Structure
  property_count: 0
  slug: procurement-list-api-agencylistresponse-structure
- name: Procurement List Api Apierror Structure
  property_count: 0
  slug: procurement-list-api-apierror-structure
- name: Procurement List Api Product Structure
  property_count: 0
  slug: procurement-list-api-product-structure
- name: Procurement List Api Productsearchresponse Structure
  property_count: 0
  slug: procurement-list-api-productsearchresponse-structure
- name: Procurement List Api Service Structure
  property_count: 0
  slug: procurement-list-api-service-structure
- name: Procurement List Api Servicesearchresponse Structure
  property_count: 0
  slug: procurement-list-api-servicesearchresponse-structure
jsonld:
- class_count: 23
  name: Us Abilityone Commission Context
  property_count: 16
  slug: us-abilityone-commission-context
layout: provider
modified: '2026-05-19'
name: US AbilityOne Commission
nav: Providers
network: true
overview: 'US AbilityOne Commission publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Agencies API, Products API, Reports API, and 1 more. Tagged areas include Federal Government, Disability Employment, Procurement, Nonprofit, and Accessibility.


  The US AbilityOne Commission catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US AbilityOne Commission''s developer surface includes developer portal, documentation, and 8 more developer resources.'
plans:
- name: Us Abilityone Commission Plans Pricing
  plan_count: 3
  slug: us-abilityone-commission-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Us Abilityone Commission Rate Limits
  slug: us-abilityone-commission-rate-limits
rules:
- name: US AbilityOne Commission API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-abilityone-commission-jsonschema-spectral-rules
- name: US AbilityOne Commission API Rules
  rule_count: 33
  severity_counts:
    error: 7
    hint: 7
    info: 1
    warn: 18
  slug: us-abilityone-commission-spectral-rules
score:
  band: developing
  composite: 54.5
  delta: 5.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 74.3
    developer_ergonomics: 17.4
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 31.6
  previous_composite: 49.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/us-abilityone-commission/refs/heads/main/screenshots/us-abilityone-commission-2026-06-20T200541.png
security:
- kind: domain-security
  name: Us Abilityone Commission Domain Security
  slug: us-abilityone-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: us-abilityone-commission
tags:
- Federal Government
- Disability Employment
- Procurement
- Nonprofit
- Accessibility
use_cases:
- description: Federal contracting officers verifying mandatory source requirements for AbilityOne products and services before placing orders.
  name: Federal Acquisition Compliance
- description: Defense and civilian agencies searching by NSN to determine if a product must be procured through the AbilityOne program.
  name: Procurement List Lookup
- description: Federal buyers identifying which nonprofit agency supplies a specific product or service in their geographic region.
  name: Nonprofit Agency Discovery
- description: Authorized distributors accessing the Procurement List to maintain current product catalogs and pricing.
  name: Distributor Integration
website: https://www.abilityone.gov
---
