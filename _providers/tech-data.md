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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Tech Data Agentic Access
  operation_count: 36
  slug: tech-data-agentic-access
  summary_line: 36 operations · 14 acting
api_count: 11
apis:
- description: Digital Bridge is TD SYNNEX's integration platform providing enterprise-grade REST APIs and pre-built connectors. Engineering teams get direct access to APIs for products, pricing, orders, renewals, a
  name: TD SYNNEX Digital Bridge API
  slug: digital-bridge-api
- description: OAuth 2.0 token management
  name: Tech Data Authentication API
  slug: tech-data-authentication-api
- description: Cart line item management
  name: Tech Data Cart Items API
  slug: tech-data-cart-items-api
- description: Shopping cart management
  name: Tech Data Carts API
  slug: tech-data-carts-api
- description: Customer cloud provider account management
  name: Tech Data Cloud Providers API
  slug: tech-data-cloud-providers-api
- description: End customer account management
  name: Tech Data Customers API
  slug: tech-data-customers-api
- description: Order creation, management, and cancellation
  name: Tech Data Orders API
  slug: tech-data-orders-api
- description: Product catalog browsing and filtering
  name: Tech Data Products API
  slug: tech-data-products-api
- description: Vendor provisioning template retrieval
  name: Tech Data Provisioning Templates API
  slug: tech-data-provisioning-templates-api
- description: Billing and business intelligence reports
  name: Tech Data Reports API
  slug: tech-data-reports-api
- description: Customer subscription management
  name: Tech Data Subscriptions API
  slug: tech-data-subscriptions-api
artifact_total: 28
collections:
- collection_type: open
  name: TD SYNNEX StreamOne Ion API
  slug: open-streamone-ion
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tech-data-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tech-data-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tech-data-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tdsynnex.com
- group: company
  title: ''
  type: About
  url: https://www.tdsynnex.com/na/us/about-td-synnex/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tdsynnex.com/na/us/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tdsynnex.com/na/us/legal/privacy-notice/
- group: start
  title: ''
  type: Login
  url: https://ion.tdsynnex.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/td-synnex/
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/tech-data/refs/heads/main/vocabulary/tech-data-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/tech-data/refs/heads/main/json-ld/tech-data-context.jsonld
created: '2026-03-24'
description: Tech Data (now TD SYNNEX) is one of the world's largest IT distributors and solutions aggregators, serving as an intermediary between technology vendors and resellers. The company merged with SYNNEX in 2021 to form TD SYNNEX. TD SYNNEX exposes the StreamOne Ion API platform for reseller partners to manage customers, products, orders, subscriptions, and cloud services programmatically. The Digital Bridge platform provides pre-built connectors and enterprise-grade APIs for live pricing, inventory, and order workflows.
examples:
- key_count: 2
  name: Streamone Ion Create Order Example
  slug: streamone-ion-create-order-example
- key_count: 2
  name: Streamone Ion List Customers Example
  slug: streamone-ion-list-customers-example
finops:
- name: Tech Data Finops
  service_category: API
  slug: tech-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tech-data.png
json_schemas:
- name: StreamOne Ion Customer
  property_count: 8
  slug: streamone-ion-customer
- name: StreamOne Ion Order
  property_count: 10
  slug: streamone-ion-order
- name: StreamOne Ion Subscription
  property_count: 10
  slug: streamone-ion-subscription
json_structures:
- name: Streamone Ion Customer Structure
  property_count: 0
  slug: streamone-ion-customer-structure
- name: Streamone Ion Order Structure
  property_count: 0
  slug: streamone-ion-order-structure
jsonld:
- class_count: 55
  name: Tech Data Context
  property_count: 0
  slug: tech-data-context
layout: provider
modified: '2026-05-19'
name: Tech Data
nav: Providers
network: true
overview: 'Tech Data publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Cart Items API, Carts API, and 7 more. Tagged areas include Cloud, Distribution, Information Technology, Partner, and Fortune 500.


  The Tech Data catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tech Data''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Tech Data Plans Pricing
  plan_count: 3
  slug: tech-data-plans-pricing
press:
- date: '2026-05-25'
  title: Majority of Americans Oppose Fast-Tracking Data Centers ...
  url: https://techoversight.org/2025/01/09/data-center-poll/
- date: '2026-05-25'
  title: Tech Data Completes Acquisition of Innovix ...
  url: https://www.techdata.com/hk_tdcs/en/about-us/our-news/recent-news/tech-data-completes-acquisition-of-innovix-distributiontech-data.html
- date: '2026-05-25'
  title: A new report reveals that expanding AI data centers are ...
  url: https://www.facebook.com/TheDailyNote/posts/breaking-a-new-report-reveals-that-expanding-ai-data-centers-are-moving-into-wat/122289098210214858/
- date: '2026-05-25'
  title: Data Centers are Spreading the AI Boom Beyond Tech Hubs
  url: https://www.reveliolabs.com/news/tech/data-centers-are-spreading-the-ai-boom-beyond-tech-hubs/
- date: '2026-05-25'
  title: data & AI
  url: https://aholddelhaize.com/about/technology-innovation/data-ai/
random_paper: 8
rate_limits:
- limit_count: 5
  name: Tech Data Rate Limits
  slug: tech-data-rate-limits
rules:
- name: Tech Data API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 7
  slug: streamone-ion-rules
- name: Tech Data API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tech-data-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.4
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 67.6
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 39.5
    operational_transparency: 31.6
  previous_composite: 49.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tech-data/refs/heads/main/screenshots/tech-data-2026-06-20T195006.png
security:
- kind: authentication
  name: Tech Data Authentication
  slug: tech-data-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tech Data Domain Security
  slug: tech-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tech-data
tags:
- Cloud
- Distribution
- Information Technology
- Partner
- Fortune 500
website: https://www.tdsynnex.com
---
