---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Ryder System Agentic Access
  operation_count: 20
  slug: ryder-system-agentic-access
  summary_line: 20 operations · 8 acting
api_count: 13
apis:
- description: The Ryder Last Mile API handles last-mile delivery operations, enabling integration with Ryder's last-mile delivery network for e-commerce fulfillment and parcel delivery management.
  name: Ryder Last Mile API
  slug: last-mile-api
- description: The Ryder 3PA Load Tracking API provides third-party logistics load tracking functionality, enabling visibility into load status and location throughout the shipment lifecycle.
  name: Ryder 3PA Load Tracking API
  slug: 3pa-load-tracking-api
- description: Document upload to RyderShare
  name: Ryder System Documents API
  slug: ryder-system-documents-api
- description: Fleet vehicle information and specifications
  name: Ryder System Fleet API
  slug: ryder-system-fleet-api
- description: Invoice details and payment status
  name: Ryder System Invoices API
  slug: ryder-system-invoices-api
- description: Load tender and event management
  name: Ryder System Load Events API
  slug: ryder-system-load-events-api
- description: Load management within shipments
  name: Ryder System Loads API
  slug: ryder-system-loads-api
- description: Location information and service details
  name: Ryder System Locations API
  slug: ryder-system-locations-api
- description: Historical maintenance records
  name: Ryder System Service History API
  slug: ryder-system-service-history-api
- description: Shipment confirmation operations
  name: Ryder System Ship Confirmation API
  slug: ryder-system-ship-confirmation-api
- description: Shipment status and tracking
  name: Ryder System Ship Status API
  slug: ryder-system-ship-status-api
- description: Shipment management operations
  name: Ryder System Shipments API
  slug: ryder-system-shipments-api
- description: Vehicle and shipment location tracking
  name: Ryder System Tracking API
  slug: ryder-system-tracking-api
artifact_total: 49
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ryder Carrier API
  slug: open-ryder-carrier-api
- collection_type: open
  name: Ryder Fleet Management API
  slug: open-ryder-fleet-management-api
- collection_type: open
  name: Ryder Carrier Documents API
  slug: open-ryder-system-documents-api
- collection_type: open
  name: Ryder Carrier Documents Fleet API
  slug: open-ryder-system-fleet-api
- collection_type: open
  name: Ryder Carrier Documents Invoices API
  slug: open-ryder-system-invoices-api
- collection_type: open
  name: Ryder Carrier Documents Load Events API
  slug: open-ryder-system-load-events-api
- collection_type: open
  name: Ryder Carrier Documents Loads API
  slug: open-ryder-system-loads-api
- collection_type: open
  name: Ryder Carrier Documents Locations API
  slug: open-ryder-system-locations-api
- collection_type: open
  name: Ryder Carrier Documents Service History API
  slug: open-ryder-system-service-history-api
- collection_type: open
  name: Ryder Carrier Documents Ship Confirmation API
  slug: open-ryder-system-ship-confirmation-api
- collection_type: open
  name: Ryder Carrier Documents Ship Status API
  slug: open-ryder-system-ship-status-api
- collection_type: open
  name: Ryder Carrier Documents Shipments API
  slug: open-ryder-system-shipments-api
- collection_type: open
  name: Ryder Carrier Documents Tracking API
  slug: open-ryder-system-tracking-api
- collection_type: open
  name: Ryder TM Shipment Management API
  slug: open-ryder-tm-shipment-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ryder-system-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ryder-system-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ryder-system-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ryder-system-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://ryder.com/en-us/api/rssfeed/showrssfeed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ryder
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ryder-system-inc
- group: company
  title: ''
  type: Website
  url: https://www.ryder.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ryder.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ryder.com/fms/overview
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/vocabulary/ryder-system-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/json-ld/ryder-system-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/rules/ryder-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/json-schema/ryder-vehicle-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/json-schema/ryder-shipment-schema.json
created: '2026-03-21'
description: Ryder System, Inc. is a leading provider of supply chain, dedicated transportation, and fleet management solutions. Ryder operates a developer portal offering REST APIs for fleet management and supply chain operations, enabling customers to integrate Ryder services into their business systems. The Fleet Management APIs support customers who lease, rent, and maintain vehicles, while the Supply Chain Solutions APIs support carrier management, load tracking, shipment management, and last-mile delivery operations.
examples:
- key_count: 2
  name: Ryder Create Shipment Example
  slug: ryder-create-shipment-example
- key_count: 2
  name: Ryder Get Service History Example
  slug: ryder-get-service-history-example
- key_count: 2
  name: Ryder List Fleet Vehicles Example
  slug: ryder-list-fleet-vehicles-example
features:
- 'Ryder System: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- Ryder fleet management and logistics APIs offered to commercial clients via Ryder Connect.
finops:
- name: Ryder System Finops
  service_category: Logistics / Fleet Management
  slug: ryder-system-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ryder-system.png
json_schemas:
- name: Ryder Shipment
  property_count: 12
  slug: ryder-shipment
- name: Ryder Vehicle
  property_count: 7
  slug: ryder-vehicle
json_structures:
- name: Ryder Shipment Structure
  property_count: 0
  slug: ryder-shipment-structure
- name: Ryder Vehicle Structure
  property_count: 0
  slug: ryder-vehicle-structure
jsonld:
- class_count: 0
  name: Ryder System Context
  property_count: 29
  slug: ryder-system-context
layout: provider
modified: '2026-05-19'
name: Ryder System
nav: Providers
network: true
overview: 'Ryder System publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Fleet API, Invoices API, and 8 more. Tagged areas include Fleet Management, Logistics, Supply Chain, Transportation, and Trucking.


  The Ryder System catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Ryder System''s developer surface includes authentication, engineering blog, documentation, and 12 more developer resources.'
plans:
- name: Ryder System Plans Pricing
  plan_count: 1
  slug: ryder-system-plans-pricing
press:
- date: '2026-05-25'
  title: Ryder Establishes Silicon Valley-Based Technology Lab ...
  url: https://newsroom.ryder.com/news/news-details/2023/Ryder-Establishes-Silicon-Valley-Based-Technology-Lab-Led-by-Founders-of-Start-Up-Baton/default.aspx
- date: '2026-05-25'
  title: Ryder Silicon Valley Lab Developing AI-Driven Logistics ...
  url: https://www.truckinginfo.com/news/ryder-establishes-silicon-valley-transportation-technology-lab
- date: '2026-05-25'
  title: Ryder names Richard Mohr as the new chief technology ...
  url: https://www.facebook.com/RyderSystemInc/posts/ryder-names-richard-mohr-as-the-new-chief-technology-officer-for-fleet-managemen/2530603403640485/
- date: '2026-05-25'
  title: Ryder System, Inc. - News
  url: https://newsroom.ryder.com/news/default.aspx
- date: '2026-05-25'
  title: Ryder and Terminal Digitize Yard; Achieve 99% Accuracy ...
  url: https://www.businesswire.com/news/home/20240821139395/en/Ryder-and-Terminal-Digitize-Yard-Achieve-99-Accuracy-with-AI-Computer-Vision
random_paper: 12
rate_limits:
- limit_count: 1
  name: Ryder System Rate Limits
  slug: ryder-system-rate-limits
rules:
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Ryder System API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: ryder-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Ryder System API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ryder-system-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Ryder System API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 6
  slug: ryder-system-spectral-rules
scopes:
- name: Ryder System Scopes
  scope_count: 1
  slug: ryder-system-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 41.0
  delta: 3.1
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 69.7
    contract_quality: 63.3
    developer_ergonomics: 33.3
    discoverability: 64.8
    governance: 69.7
    operational_transparency: 7.9
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/screenshots/ryder-system-2026-06-20T193310.png
security:
- kind: authentication
  name: Ryder System Authentication
  slug: ryder-system-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Ryder System Domain Security
  slug: ryder-system-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ryder-system
tags:
- Fleet Management
- Logistics
- Supply Chain
- Transportation
- Trucking
- Fortune 500
website: https://www.ryder.com
---
