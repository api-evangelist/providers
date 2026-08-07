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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Rithum Agentic Access
  operation_count: 18
  slug: rithum-agentic-access
  summary_line: 18 operations · 14 acting
api_count: 8
apis:
- description: OAuth2 token management
  name: Rithum Authentication API
  slug: rithum-authentication-api
- description: Product catalog synchronization
  name: Rithum Catalog API
  slug: rithum-catalog-api
- description: Inventory level management
  name: Rithum Inventory API
  slug: rithum-inventory-api
- description: Invoice processing
  name: Rithum Invoices API
  slug: rithum-invoices-api
- description: Retailer and supplier order operations
  name: Rithum Orders API
  slug: rithum-orders-api
- description: Return and refund management
  name: Rithum Returns API
  slug: rithum-returns-api
- description: Shipment creation and tracking
  name: Rithum Shipments API
  slug: rithum-shipments-api
- description: Event stream management for real-time data
  name: Rithum Streams API
  slug: rithum-streams-api
artifact_total: 31
collections:
- collection_type: postman
  name: Dsco Platform Authentication API
  slug: postman-rithum-authentication-api
- collection_type: postman
  name: Dsco Platform Authentication Catalog API
  slug: postman-rithum-catalog-api
- collection_type: postman
  name: Dsco Platform Authentication Inventory API
  slug: postman-rithum-inventory-api
- collection_type: postman
  name: Dsco Platform Authentication Invoices API
  slug: postman-rithum-invoices-api
- collection_type: postman
  name: Dsco Platform Authentication Orders API
  slug: postman-rithum-orders-api
- collection_type: postman
  name: Dsco Platform Authentication Returns API
  slug: postman-rithum-returns-api
- collection_type: postman
  name: Dsco Platform Authentication Shipments API
  slug: postman-rithum-shipments-api
- collection_type: postman
  name: Dsco Platform Authentication Streams API
  slug: postman-rithum-streams-api
- collection_type: open
  name: Dsco Platform API
  slug: open-dsco-platform
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/rithum/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rithum-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rithum-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rithum-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rithumcommerce
- group: company
  title: ''
  type: Website
  url: https://www.rithum.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.dsco.io/doc/v3/reference/
- group: operate
  title: ''
  type: Support
  url: https://knowledge.rithum.com
- group: company
  title: ''
  type: Blog
  url: https://www.rithum.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rithum.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rithum.com/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rithum.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rithum
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rithum/refs/heads/main/json-ld/rithum-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rithum/refs/heads/main/vocabulary/rithum-vocabulary.yml
created: '2025-02-12'
description: Rithum is a commerce operations platform providing dropship, marketplace, and supply chain integration solutions for retailers, brands, and suppliers. Formerly known as CommerceHub and ChannelAdvisor, Rithum connects brands and retailers to manage product listings, inventory, order workflows, and performance across ecommerce channels. The platform powers the Dsco API for dropship and marketplace integrations. In 2025, Rithum launched RithumIQ, an AI engine for automated commerce recommendations and operational insights.
examples:
- key_count: 2
  name: Dsco Supplier Create Shipment Example
  slug: dsco-supplier-create-shipment-example
- key_count: 2
  name: Dsco Supplier List Orders Example
  slug: dsco-supplier-list-orders-example
finops:
- name: Rithum Finops
  service_category: API
  slug: rithum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rithum.png
json_schemas:
- name: Dsco Catalog Item
  property_count: 6
  slug: dsco-catalog-item
- name: Dsco Order
  property_count: 9
  slug: dsco-order
json_structures:
- name: Dsco Order Structure
  property_count: 0
  slug: dsco-order-structure
jsonld:
- class_count: 35
  name: Rithum Context
  property_count: 0
  slug: rithum-context
layout: provider
modified: '2026-05-19'
name: Rithum
nav: Providers
network: true
overview: 'Rithum publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Catalog API, Inventory API, and 5 more. Tagged areas include Commerce, Dropship, Marketplace, Ecommerce, and Supply Chain.


  The Rithum catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Rithum''s developer surface includes authentication, documentation, support, engineering blog, GitHub presence, and 10 more developer resources.'
plans:
- name: Rithum Plans Pricing
  plan_count: 3
  slug: rithum-plans-pricing
random_paper: 100
rate_limits:
- limit_count: 5
  name: Rithum Rate Limits
  slug: rithum-rate-limits
rules:
- name: Rithum API Rules
  rule_count: 11
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 7
  slug: dsco-platform-rules
- name: Rithum API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rithum-jsonschema-spectral-rules
score:
  band: strong
  composite: 58.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 77.2
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rithum/refs/heads/main/screenshots/rithum-2026-06-20T193131.png
security:
- kind: authentication
  name: Rithum Authentication
  slug: rithum-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rithum Domain Security
  slug: rithum-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rithum
tags:
- Commerce
- Dropship
- Marketplace
- Ecommerce
- Supply Chain
- Retail
website: https://www.rithum.com
---
