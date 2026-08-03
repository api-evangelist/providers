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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Staples Agentic Access
  operation_count: 11
  slug: staples-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 6
apis:
- description: The Staples Product Catalog API provides programmatic access to Staples' office supply catalog including product search, pricing, availability, and category browsing for integration with procurement a
  name: Staples Product Catalog API
  slug: staples-product-catalog-api
- description: Account and contract management operations
  name: Staples Account API
  slug: staples-account-api
- description: Product catalog search and browse operations
  name: Staples Catalog API
  slug: staples-catalog-api
- description: Delivery tracking and scheduling operations
  name: Staples Delivery API
  slug: staples-delivery-api
- description: Invoice and billing operations
  name: Staples Invoices API
  slug: staples-invoices-api
- description: Order management operations
  name: Staples Orders API
  slug: staples-orders-api
artifact_total: 21
collections:
- collection_type: open
  name: Staples Advantage eProcurement API
  slug: open-staples-advantage-eprocurement-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/staples-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/staples-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/staples-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Staples-Inc
- group: company
  title: ''
  type: Website
  url: https://www.staples.com
- group: start
  title: ''
  type: Portal
  url: https://www.staplesadvantage.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.staplesadvantage.com/learn/eprocurement-integrations
- group: company
  title: ''
  type: Blog
  url: https://news.staples.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.staples.com/sbd/cre/programs/privacy_policy/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.staples.com/sbd/cre/marketing/terms-and-conditions/
- group: other
  title: ''
  type: X
  url: https://x.com/Staples
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/staples
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Staples
created: '2024-01-01'
description: Staples is an American multinational office supply retail company that offers B2B procurement integration through Staples Business Advantage. The platform supports over 170 eProcurement system integrations including PunchOut catalogs, EDI, and REST-based procurement APIs for enterprise customers.
examples:
- key_count: 2
  name: Staples Create Order Example
  slug: staples-create-order-example
- key_count: 2
  name: Staples Search Products Example
  slug: staples-search-products-example
finops:
- name: Staples Finops
  service_category: B2B Procurement
  slug: staples-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/staples.png
json_schemas:
- name: Staples Advantage Order
  property_count: 10
  slug: staples-order
- name: Staples Product
  property_count: 15
  slug: staples-product
json_structures:
- name: Staples Product Structure
  property_count: 0
  slug: staples-product-structure
jsonld:
- class_count: 47
  name: Staples Context
  property_count: 0
  slug: staples-context
layout: provider
modified: '2026-05-19'
name: Staples
nav: Providers
network: true
overview: 'Staples publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Catalog API, Delivery API, and 2 more. Tagged areas include Office Supplies, Retail, Procurement, B2B, and eProcurement.


  The Staples catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Staples'' developer surface includes authentication, developer portal, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Staples Plans Pricing
  plan_count: 1
  slug: staples-plans-pricing
press:
- date: '2026-05-25'
  title: 'Staples Canada: Scaling AI-Driven Ecommerce Search ...'
  url: https://www.algolia.com/customers/staples
- date: '2026-05-25'
  title: Will Staples 'Business is Human' Campaign Connect With ...
  url: https://retailwire.com/discussion/will-staples-business-is-human-campaign-connect-with-customers/
- date: '2026-05-25'
  title: Staples Launches “Business is Human” Brand Campaign
  url: https://www.businesswire.com/news/home/20230518005153/en/Staples-Launches-Business-is-Human-Brand-Campaign
- date: '2026-05-25'
  title: Staples Canada rethinks its fulfillment model
  url: https://www.scmr.com/article/staples-canada-rethinks-its-fulfillment-model
- date: '2026-05-25'
  title: Staples Canada ULC Press Releases | Cision
  url: https://www.newswire.ca/news/staples-canada-ulc/
random_paper: 4
rate_limits:
- limit_count: 1
  name: Staples Rate Limits
  slug: staples-rate-limits
rules:
- name: Staples API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: staples-jsonschema-spectral-rules
- name: Staples API Rules
  rule_count: 21
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 10
  slug: staples-rules
score:
  band: developing
  composite: 49.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 71.3
    developer_ergonomics: 30.4
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/staples/refs/heads/main/screenshots/staples-2026-06-20T194507.png
security:
- kind: authentication
  name: Staples Authentication
  slug: staples-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Staples Domain Security
  slug: staples-domain-security
  summary_line: TLSv1.3 · DMARC
slug: staples
tags:
- Office Supplies
- Retail
- Procurement
- B2B
- eProcurement
- Fortune 500
website: https://www.staples.com
---
