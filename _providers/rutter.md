---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Rutter Agentic Access
  operation_count: 26
  slug: rutter-agentic-access
  summary_line: 26 operations · 9 acting
api_count: 1
apis:
- description: The Rutter Commerce API enables reading and writing data to all major commerce platforms through a unified API, supporting platforms like Shopify, WooCommerce, Amazon, and more.
  name: Rutter Commerce API
  slug: commerce-api
- description: The Rutter Accounting API provides a unified interface to read and write data to all major accounting platforms including QuickBooks, Xero, Freshbooks, and Zoho Books.
  name: Rutter Accounting API
  slug: accounting-api
- description: The Rutter Payments API provides a unified interface to read and write data to all major payment platforms through a single REST API.
  name: Rutter Payments API
  slug: payments-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: Accounting data across platforms
  name: Rutter Accounting API
  slug: rutter-accounting-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: Advertising platform data
  name: Rutter Ads API
  slug: rutter-ads-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: Banking and financial account data
  name: Rutter Banking API
  slug: rutter-banking-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: Commerce and e-commerce data
  name: Rutter Commerce API
  slug: rutter-commerce-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: Manage platform connections and authentication
  name: Rutter Connections API
  slug: rutter-connections-api
- baseURL: https://production.rutterapi.com/versioned
  baseurl_source: declared
  description: Webhook configuration and management
  name: Rutter Webhooks API
  slug: rutter-webhooks-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rutter Unified Accounting API
  slug: open-rutter-accounting-api
- collection_type: open
  name: Rutter Unified Accounting Ads API
  slug: open-rutter-ads-api
- collection_type: open
  name: Rutter Unified Accounting Banking API
  slug: open-rutter-banking-api
- collection_type: open
  name: Rutter Unified Accounting Commerce API
  slug: open-rutter-commerce-api
- collection_type: open
  name: Rutter Unified Accounting Connections API
  slug: open-rutter-connections-api
- collection_type: open
  name: Rutter Unified API
  slug: open-rutter-unified-api
- collection_type: open
  name: Rutter Unified Accounting Webhooks API
  slug: open-rutter-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rutter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rutter-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rutter-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rutterapi
- group: company
  title: ''
  type: Website
  url: https://www.rutter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rutter.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rutter.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.rutter.com/blog
- group: other
  title: ''
  type: APIs
  url: https://www.rutter.com/our-features/apis
- group: start
  title: ''
  type: Signup
  url: https://dashboard.rutterapi.com/sign-up
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rutter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rutter/react-rutter-link
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/vocabulary/rutter-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/json-ld/rutter-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/rules/rutter-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/json-schema/rutter-connection-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/json-schema/rutter-invoice-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/json-schema/rutter-order-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://dashboard.rutterapi.com/llms.txt
created: '2026-03-16'
description: Rutter is the leading unified RESTful API for B2B financial products that connects to over 60 commerce, payments, accounting, and ads platforms through a single API. Trusted by companies like Airwallex, Mercury, and Ramp, Rutter enables developers to read, update, write, and remove data across major business platforms with a unified data model and idempotency guarantees for financial data. The API supports OAuth2 and Basic authentication, versioning via the X-Rutter-Version header, cursor-based pagination, and asynchronous request processing.
examples:
- key_count: 2
  name: Rutter List Connections Example
  slug: rutter-list-connections-example
- key_count: 2
  name: Rutter List Invoices Example
  slug: rutter-list-invoices-example
- key_count: 2
  name: Rutter List Orders Example
  slug: rutter-list-orders-example
finops:
- name: Rutter Finops
  service_category: Unified API / Commerce + Accounting Integration
  slug: rutter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rutter.png
json_schemas:
- name: Rutter Connection
  property_count: 5
  slug: rutter-connection
- name: Rutter Invoice
  property_count: 7
  slug: rutter-invoice
- name: Rutter Order
  property_count: 8
  slug: rutter-order
json_structures:
- name: Rutter Connection Structure
  property_count: 0
  slug: rutter-connection-structure
- name: Rutter Invoice Structure
  property_count: 0
  slug: rutter-invoice-structure
- name: Rutter Order Structure
  property_count: 0
  slug: rutter-order-structure
jsonld:
- class_count: 1
  name: Rutter Context
  property_count: 24
  slug: rutter-context
layout: provider
modified: '2026-05-19'
name: Rutter
nav: Providers
network: true
overview: 'Rutter publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Ads API, Banking API, and 3 more. Tagged areas include Accounting, B2B, Commerce, Financial Data, and Payments.


  The Rutter catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Rutter''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, GitHub presence, and 13 more developer resources.'
plans:
- name: Rutter Plans Pricing
  plan_count: 1
  slug: rutter-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Rutter Rate Limits
  slug: rutter-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Rutter API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: rutter-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Rutter API Rules
  rule_count: 15
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 10
  slug: rutter-spectral-rules
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 61.0
    developer_ergonomics: 31.0
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/screenshots/rutter-2026-06-20T193303.png
security:
- kind: authentication
  name: Rutter Authentication
  slug: rutter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rutter Domain Security
  slug: rutter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rutter
tags:
- Accounting
- B2B
- Commerce
- Financial Data
- Payments
- Unified-API
website: https://www.rutter.com/
---
