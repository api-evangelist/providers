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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Td Synnex Agentic Access
  operation_count: 34
  slug: td-synnex-agentic-access
  summary_line: 34 operations · 15 acting
api_count: 10
apis:
- description: OAuth 2.0 token management
  name: TD SYNNEX Authentication API
  slug: td-synnex-authentication-api
- description: Shopping cart item management
  name: TD SYNNEX Cart Items API
  slug: td-synnex-cart-items-api
- description: Shopping cart management
  name: TD SYNNEX Carts API
  slug: td-synnex-carts-api
- description: Customer cloud provider account linking
  name: TD SYNNEX Cloud Providers API
  slug: td-synnex-cloud-providers-api
- description: End customer account management
  name: TD SYNNEX Customers API
  slug: td-synnex-customers-api
- description: Order creation and management
  name: TD SYNNEX Orders API
  slug: td-synnex-orders-api
- description: Technology product catalog browsing
  name: TD SYNNEX Products API
  slug: td-synnex-products-api
- description: Vendor provisioning template management
  name: TD SYNNEX Provisioning API
  slug: td-synnex-provisioning-api
- description: Business intelligence and reporting
  name: TD SYNNEX Reports API
  slug: td-synnex-reports-api
- description: Cloud subscription management
  name: TD SYNNEX Subscriptions API
  slug: td-synnex-subscriptions-api
artifact_total: 26
collections:
- collection_type: open
  name: TD SYNNEX StreamOne Ion Partner API
  slug: open-td-synnex-streamone-ion
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/td-synnex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/td-synnex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/td-synnex-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/td-synnex-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tdsynnex
- group: company
  title: ''
  type: Website
  url: https://www.tdsynnex.com/na/us/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.streamone.cloud/
- group: start
  title: ''
  type: Portal
  url: https://www.tdsynnex.com/ion/api/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/openapi/td-synnex-streamone-ion-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/vocabulary/td-synnex-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/json-schema/td-synnex-customer-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/json-schema/td-synnex-order-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/json-ld/td-synnex-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/rules/td-synnex-rules.yml
created: '2026-03-24'
description: TD SYNNEX is one of the world's largest IT distributors and solutions aggregators, serving over 150,000 resellers, retailers, and other customers in more than 100 countries. The company provides technology distribution, integration, and solutions services. TD SYNNEX offers the StreamOne Ion platform with REST APIs that enable partners to manage cloud subscriptions, customers, orders, and billing through a unified interface supporting multiple cloud vendors. Named NVIDIA EMEA Distributor of the Year 2026.
examples:
- key_count: 2
  name: Td Synnex Create Customer Example
  slug: td-synnex-create-customer-example
- key_count: 2
  name: Td Synnex Create Order Example
  slug: td-synnex-create-order-example
finops:
- name: Td Synnex Finops
  service_category: Technology Distribution
  slug: td-synnex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/td-synnex.png
json_schemas:
- name: TD SYNNEX StreamOne Customer
  property_count: 9
  slug: td-synnex-customer
- name: TD SYNNEX StreamOne Order
  property_count: 9
  slug: td-synnex-order
json_structures:
- name: Td Synnex Customer Structure
  property_count: 0
  slug: td-synnex-customer-structure
jsonld:
- class_count: 34
  name: Td Synnex Context
  property_count: 1
  slug: td-synnex-context
layout: provider
modified: '2026-05-19'
name: TD SYNNEX
nav: Providers
network: true
overview: 'TD SYNNEX publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Cart Items API, Carts API, and 7 more. Tagged areas include Technology Distribution, IT Distribution, Cloud, Reseller, and StreamOne.


  The TD SYNNEX catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TD SYNNEX''s developer surface includes authentication, documentation, developer portal, and 11 more developer resources.'
plans:
- name: Td Synnex Plans Pricing
  plan_count: 1
  slug: td-synnex-plans-pricing
random_paper: 98
rate_limits:
- limit_count: 1
  name: Td Synnex Rate Limits
  slug: td-synnex-rate-limits
rules:
- name: TD SYNNEX API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: td-synnex-jsonschema-spectral-rules
- name: TD SYNNEX API Rules
  rule_count: 12
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 9
  slug: td-synnex-rules
scopes:
- name: Td Synnex Scopes
  scope_count: 2
  slug: td-synnex-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 41.5
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 67.2
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/td-synnex/refs/heads/main/screenshots/td-synnex-2026-06-20T194950.png
security:
- kind: authentication
  name: Td Synnex Authentication
  slug: td-synnex-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Td Synnex Domain Security
  slug: td-synnex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: td-synnex
tags:
- Technology Distribution
- IT Distribution
- Cloud
- Reseller
- StreamOne
- Fortune 100
- B2B
website: https://www.tdsynnex.com/na/us/
---
