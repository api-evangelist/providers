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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: United Rentals Agentic Access
  operation_count: 13
  slug: united-rentals-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 5
apis:
- description: Equipment catalog and availability
  name: United Rentals Equipment API
  slug: united-rentals-equipment-api
- description: Fleet and worksite management
  name: United Rentals Fleet API
  slug: united-rentals-fleet-api
- description: Invoice and billing management
  name: United Rentals Invoices API
  slug: united-rentals-invoices-api
- description: Branch locations and service areas
  name: United Rentals Locations API
  slug: united-rentals-locations-api
- description: Rental reservations and orders
  name: United Rentals Rentals API
  slug: united-rentals-rentals-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: United Rentals Total Control Equipment API
  slug: open-united-rentals-equipment-api
- collection_type: open
  name: United Rentals Total Control Equipment Fleet API
  slug: open-united-rentals-fleet-api
- collection_type: open
  name: United Rentals Total Control Equipment Invoices API
  slug: open-united-rentals-invoices-api
- collection_type: open
  name: United Rentals Total Control Equipment Locations API
  slug: open-united-rentals-locations-api
- collection_type: open
  name: United Total Control Equipment Rentals API
  slug: open-united-rentals-rentals-api
- collection_type: open
  name: United Rentals Total Control API
  slug: open-united-rentals-total-control
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/united-rentals-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-rentals-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/united-rentals-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.unitedrentals.com
- group: other
  title: ''
  type: Total Control
  url: https://www.unitedrentals.com/services/online-services/total-control
- group: build
  title: ''
  type: System Integration
  url: https://www.unitedrentals.com/services/online-services/total-control/system-integration
- group: other
  title: ''
  type: Digital Solutions
  url: https://www.unitedrentals.com/solutions/digital-solutions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/united-rentals
- group: other
  title: ''
  type: X
  url: https://twitter.com/UnitedRentals
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.unitedrentals.com
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/united-rentals/main/openapi/united-rentals-total-control-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/united-rentals/main/rules/united-rentals-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/united-rentals/main/json-schema/united-rentals-rental-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/united-rentals/main/json-schema/united-rentals-invoice-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/united-rentals/main/json-ld/united-rentals-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/united-rentals/main/vocabulary/united-rentals-vocabulary.yml
created: '2026-03-21'
description: United Rentals is the world's largest equipment rental company, headquartered in Stamford, Connecticut. The company provides a broad selection of APIs to help customers simplify the procure-to-pay lifecycle for equipment rentals. United Rentals offers system integration through its Total Control platform, supporting EDI, cXML, JSON, and flat-file formats to connect with customer procurement and ERP systems.
examples:
- key_count: 2
  name: United Rentals Total Control Createrental Example
  slug: united-rentals-total-control-createRental-example
- key_count: 2
  name: United Rentals Total Control Listequipment Example
  slug: united-rentals-total-control-listEquipment-example
- key_count: 2
  name: United Rentals Total Control Listinvoices Example
  slug: united-rentals-total-control-listInvoices-example
finops:
- name: United Rentals Finops
  service_category: API
  slug: united-rentals-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-rentals.png
json_schemas:
- name: United Rentals Invoice
  property_count: 11
  slug: united-rentals-invoice
- name: United Rentals Rental Order
  property_count: 12
  slug: united-rentals-rental
json_structures:
- name: United Rentals Rental Structure
  property_count: 0
  slug: united-rentals-rental-structure
jsonld:
- class_count: 0
  name: United Rentals Context
  property_count: 32
  slug: united-rentals-context
layout: provider
modified: '2026-05-19'
name: United Rentals
nav: Providers
network: true
overview: 'United Rentals publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Equipment API, Fleet API, Invoices API, and 2 more. Tagged areas include Equipment Rental, Procurement, Supply Chain, Construction, and Fortune 500.


  The United Rentals catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  United Rentals'' developer surface includes authentication and 15 more developer resources.'
plans:
- name: United Rentals Plans Pricing
  plan_count: 3
  slug: united-rentals-plans-pricing
press:
- date: '2026-05-25'
  title: Financials - Quarterly results
  url: https://investors.unitedrentals.com/financials/quarterly-results/default.aspx
- date: '2026-05-25'
  title: United Rentals Scales AI Applications with AWS
  url: https://investors.unitedrentals.com/press-releases/press-releases-details/2025/United-Rentals-Scales-AI-Applications-with-AWS/default.aspx
- date: '2026-05-25'
  title: Artificial Intelligence Is Reinventing Construction Scheduling
  url: https://www.unitedrentals.com/project-uptime/data/artificial-intelligence-reinventing-construction-scheduling
- date: '2026-05-25'
  title: United Rentals Introduces AI-Powered Equipment Agent
  url: https://investors.unitedrentals.com/press-releases/press-releases-details/2026/United-Rentals-Introduces-AI-Powered-Equipment-Agent/default.aspx
- date: '2026-05-25'
  title: United Rentals Expands Digital Customer Experience with ...
  url: https://www.businesswire.com/news/home/20260519107330/en/United-Rentals-Expands-Digital-Customer-Experience-with-Equipment-Agent-Launch-in-ChatGPT
random_paper: 114
rate_limits:
- limit_count: 5
  name: United Rentals Rate Limits
  slug: united-rentals-rate-limits
rules:
- name: United Rentals API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: united-rentals-jsonschema-spectral-rules
- name: United Rentals API Rules
  rule_count: 15
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 9
  slug: united-rentals-rules
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 68.7
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 7.9
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/united-rentals/refs/heads/main/screenshots/united-rentals-2026-06-20T200042.png
security:
- kind: authentication
  name: United Rentals Authentication
  slug: united-rentals-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: United Rentals Domain Security
  slug: united-rentals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: united-rentals
tags:
- Equipment Rental
- Procurement
- Supply Chain
- Construction
- Fortune 500
website: https://www.unitedrentals.com
---
