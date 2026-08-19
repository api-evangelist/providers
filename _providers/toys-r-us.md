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
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Toys R Us Agentic Access
  operation_count: 10
  slug: toys-r-us-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 5
apis:
- description: Create and retrieve order acknowledgements (EDI 855) to accept, cancel, or backorder order items. Sent after order receipt and before shipment or invoice creation.
  name: Toys R Us Acknowledgements API
  slug: toys-r-us-acknowledgements-api
- description: Create and retrieve invoices (EDI 810) providing billing details and item pricing for fulfilled goods.
  name: Toys R Us Invoices API
  slug: toys-r-us-invoices-api
- description: Retrieve and manage purchase orders in the EDI 850 format. Orders initiate the order lifecycle and update until all items are fulfilled and invoiced.
  name: Toys R Us Orders API
  slug: toys-r-us-orders-api
- description: Manage product catalog items including item creation, updates, and availability synchronization.
  name: Toys R Us Products API
  slug: toys-r-us-products-api
- description: Create and retrieve shipment notifications (EDI 856) containing containerized data, tracking numbers, and fulfillment details for shipped order items.
  name: Toys R Us Shipments API
  slug: toys-r-us-shipments-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Toys R Us Commerce Acknowledgements API
  slug: open-toys-r-us-acknowledgements-api
- collection_type: open
  name: Toys R Us Commerce API
  slug: open-toys-r-us-commerce
- collection_type: open
  name: Toys R Us Commerce Acknowledgements Invoices API
  slug: open-toys-r-us-invoices-api
- collection_type: open
  name: Toys R Us Commerce Acknowledgements Orders API
  slug: open-toys-r-us-orders-api
- collection_type: open
  name: Toys R Us Commerce Acknowledgements Products API
  slug: open-toys-r-us-products-api
- collection_type: open
  name: Toys R Us Commerce Acknowledgements Shipments API
  slug: open-toys-r-us-shipments-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/toys-r-us-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toys-r-us-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/toys-r-us-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/toysrus1
- group: company
  title: ''
  type: Website
  url: https://www.toysrus.com
- group: start
  title: ''
  type: SupplierPortal
  url: https://toysrus.logicbroker.com
- group: docs
  title: ''
  type: Documentation
  url: https://toysrus.logicbroker.com/hc/en-us/articles/9357008230164-API-Documentation
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.logicbroker.com
- group: company
  title: ''
  type: Blog
  url: https://www.toysrus.com/blogs/diy-activities.atom
created: '2026-03-24'
description: Toys 'R' Us is a leading toys and juvenile-products retailer offering a vast selection of toys, games, baby products, and children's apparel through retail stores and e-commerce sites. The brand integrates with suppliers and dropship vendors via the LogicBroker commerce platform, providing APIs for order management, shipment processing, product catalog synchronization, and invoice workflows.
examples:
- key_count: 2
  name: Toys R Us Create Shipment Example
  slug: toys-r-us-create-shipment-example
- key_count: 2
  name: Toys R Us Get Orders Example
  slug: toys-r-us-get-orders-example
finops:
- name: Toys R Us Finops
  service_category: API
  slug: toys-r-us-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toys-r-us.png
json_schemas:
- name: Toys R Us Order
  property_count: 6
  slug: toys-r-us-order
json_structures:
- name: Toys R Us Order Structure
  property_count: 0
  slug: toys-r-us-order-structure
jsonld:
- class_count: 34
  name: Toys R Us Context
  property_count: 0
  slug: toys-r-us-context
layout: provider
modified: '2026-05-19'
name: Toys R Us
nav: Providers
network: true
overview: 'Toys R Us publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Acknowledgements API, Invoices API, Orders API, and 2 more. Tagged areas include Commerce, Dropship, E-Commerce, Retail, and Supply Chain.


  The Toys R Us catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Toys R Us'' developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Toys R Us Plans Pricing
  plan_count: 3
  slug: toys-r-us-plans-pricing
press:
- date: '2026-05-25'
  title: Is AI Video the Future of Advertising? Toys “R” Us ...
  url: https://x.com/linqtoinc/status/1809326405697552864?lang=ar
- date: '2026-05-25'
  title: Toys R Us creates first brand film to use OpenAI's text-to- ...
  url: https://www.marketingdive.com/news/toys-r-us-openai-sora-gen-ai-first-text-video/719797/
- date: '2026-05-25'
  title: Why Toys R Us created an AI ad | Jason Mitchell posted on ...
  url: https://www.linkedin.com/posts/jhmitchell_this-entire-ad-was-made-with-ai-and-its-activity-7212092135708196864--_uY
- date: '2026-05-25'
  title: Toys"R"Us Studios and Native Foreign Use OpenAI's Sora ...
  url: https://www.prnewswire.com/news-releases/toysrus-studios-and-native-foreign-use-openais-sora-to-narrate-the-origin-story-of-beloved-toyrus-brand-302180332.html
- date: '2026-05-25'
  title: Toys 'R' Us calls AI-made video successful despite criticism
  url: https://www.nbcnews.com/tech/internet/toys-r-us-ai-video-ad-controversy-explained-commercial-rcna159030
random_paper: 5
rate_limits:
- limit_count: 5
  name: Toys R Us Rate Limits
  slug: toys-r-us-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Toys R Us API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: toys-r-us-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Toys R Us API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 6
  slug: toys-r-us-rules
score:
  band: thin
  composite: 36.6
  delta: -6.3
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 68.5
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/toys-r-us/refs/heads/main/screenshots/toys-r-us-2026-06-20T195516.png
security:
- kind: authentication
  name: Toys R Us Authentication
  slug: toys-r-us-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Toys R Us Domain Security
  slug: toys-r-us-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: toys-r-us
tags:
- Commerce
- Dropship
- E-Commerce
- Retail
- Supply Chain
- Fortune 500
website: https://www.toysrus.com
---
