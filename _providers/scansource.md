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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Scansource Agentic Access
  operation_count: 18
  slug: scansource-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 7
apis:
- description: Real-time inventory availability checks
  name: ScanSource Availability API
  slug: scansource-availability-api
- description: Invoice retrieval and management operations
  name: ScanSource Invoices API
  slug: scansource-invoices-api
- description: Sales order creation and management
  name: ScanSource Orders API
  slug: scansource-orders-api
- description: Real-time pricing lookups for partner customers
  name: ScanSource Pricing API
  slug: scansource-pricing-api
- description: Product information, search, and catalog operations
  name: ScanSource Products API
  slug: scansource-products-api
- description: Shipping quotes and logistics
  name: ScanSource Shipping API
  slug: scansource-shipping-api
- description: Order tracking and delivery information
  name: ScanSource Tracking API
  slug: scansource-tracking-api
artifact_total: 24
collections:
- collection_type: open
  name: ScanSource Invoice API
  slug: open-scansource-invoice
- collection_type: open
  name: ScanSource Product API
  slug: open-scansource-product
- collection_type: open
  name: ScanSource Sales Order API
  slug: open-scansource-sales-order
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scansource-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scansource-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scansource-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scansource
- group: company
  title: ''
  type: Website
  url: https://www.scansource.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partnerportal.scansource.com
- group: docs
  title: ''
  type: Documentation
  url: https://services.scansource.com/api/Help
- group: start
  title: ''
  type: GettingStarted
  url: https://partnerportal.scansource.com/getstarted
- group: start
  title: ''
  type: PartnerPortal
  url: https://partnerdevportal.scansource.com
- group: design
  title: ''
  type: SpectralRules
  url: rules/scansource-rules.yml
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/scansource-product-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/scansource-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/scansource-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/partner-commerce.yaml
created: '2026-05-02'
description: ScanSource is an international technology distributor specializing in point-of-sale (POS), payments, barcode, physical security, unified communications, collaboration, telecom, and cloud services. Founded in 1992 in Greenville, South Carolina, ScanSource provides APIs that give partners real-time access to inventory, pricing, order management, and product information to automate the sales cycle and integrate with backend ERP systems and customer portals.
examples:
- key_count: 4
  name: Scansource Create Order Example
  slug: scansource-create-order-example
- key_count: 4
  name: Scansource Product Availability Example
  slug: scansource-product-availability-example
finops:
- name: Scansource Finops
  service_category: B2B Distribution
  slug: scansource-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scansource.png
json_schemas:
- name: ScanSource Sales Order
  property_count: 12
  slug: scansource-order
- name: ScanSource Product
  property_count: 12
  slug: scansource-product
json_structures:
- name: Scansource Product Structure
  property_count: 0
  slug: scansource-product-structure
jsonld:
- class_count: 7
  name: Scansource Context
  property_count: 27
  slug: scansource-context
layout: provider
modified: '2026-05-02'
name: ScanSource
nav: Providers
network: true
overview: 'ScanSource publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Invoices API, Orders API, and 4 more. Tagged areas include ScanSource, Distribution, Barcode, Point Of Sale, and AIDC.


  The ScanSource catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ScanSource''s developer surface includes authentication, documentation, getting-started guide, and 11 more developer resources.'
plans:
- name: Scansource Plans Pricing
  plan_count: 1
  slug: scansource-plans-pricing
press:
- date: '2026-05-25'
  title: ScanSource, Inc. (SCSC) Q3 2026 Earnings Call Transcript
  url: https://seekingalpha.com/article/4901024-scansource-inc-scsc-q3-2026-earnings-call-transcript
- date: '2026-05-25'
  title: ScanSource's Post
  url: https://www.linkedin.com/posts/scansource_executiveleadership-companygrowth-pressrelease-activity-6959867268562399232-vTqf?trk=public_profile_like_view
- date: '2026-05-25'
  title: Retail
  url: https://www.scansource.com/resource-center/market-resource-center/retail
- date: '2026-05-25'
  title: Blog
  url: https://intelisys.com/blog/
- date: '2026-05-25'
  title: ScanSource Q3 Earnings Call Highlights
  url: https://www.theglobeandmail.com/investing/markets/stocks/SCSC/pressreleases/1832981/scansource-q3-earnings-call-highlights/
random_paper: 38
rate_limits:
- limit_count: 1
  name: Scansource Rate Limits
  slug: scansource-rate-limits
rules:
- name: ScanSource API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: scansource-jsonschema-spectral-rules
- name: ScanSource API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: scansource-rules
score:
  band: developing
  composite: 51.5
  delta: -4.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 78.0
    developer_ergonomics: 39.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scansource/refs/heads/main/screenshots/scansource-2026-06-20T193517.png
security:
- kind: authentication
  name: Scansource Authentication
  slug: scansource-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Scansource Domain Security
  slug: scansource-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scansource
tags:
- ScanSource
- Distribution
- Barcode
- Point Of Sale
- AIDC
- Inventory
- Order Management
- E-Commerce
- Fortune 1000
website: https://www.scansource.com
---
