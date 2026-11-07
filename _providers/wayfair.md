---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Wayfair Agentic Access
  operation_count: 2
  slug: wayfair-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.wayfair.com/v1/graphql
  baseurl_source: declared
  description: Token-based authentication for API access.
  name: Wayfair Authentication API
  slug: wayfair-authentication-api
- baseURL: https://api.wayfair.com/v1/graphql
  baseurl_source: declared
  description: GraphQL query and mutation operations for supplier management.
  name: Wayfair Graph QL API
  slug: wayfair-graph-ql-api
artifact_total: 45
collections:
- collection_type: open
  name: Wayfair Supplier Authentication API
  slug: open-wayfair-authentication-api
- collection_type: open
  name: Wayfair Supplier Authentication GraphQL API
  slug: open-wayfair-graphql-api
- collection_type: open
  name: Wayfair Supplier API
  slug: open-wayfair-supplier-api
common:
- group: commercial
  href: https://artifacts.apis.io/wayfair/plans/wayfair-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wayfair-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/wayfair/rate-limits/wayfair-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wayfair-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/wayfair/finops/wayfair-finops.yml
  title: ''
  type: FinOps
  url: finops/wayfair-finops.yml
- group: agent
  href: https://artifacts.apis.io/wayfair/agentic-access/wayfair-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wayfair-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/wayfair/security/wayfair-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/wayfair-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/wayfair/security/wayfair-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wayfair-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/wayfair/authentication/wayfair-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wayfair-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wayfair
- group: start
  title: Developer Portal
  type: Portal
  url: https://developer.wayfair.com/docs/
- group: start
  title: Developer Portal (Introduction)
  type: Portal
  url: https://developer.wayfair.io/posts/introduction
- group: docs
  title: GraphQL Documentation
  type: Documentation
  url: https://developer.wayfair.io/posts/graphQL
- group: docs
  title: Sandbox API Testing
  type: Documentation
  url: https://developer.wayfair.io/posts/api-testing
- group: company
  title: Wayfair Website
  type: Website
  url: https://www.wayfair.com/
- group: company
  title: About Wayfair
  type: About
  url: https://www.aboutwayfair.com/
- group: build
  title: Wayfair GitHub Organization
  type: GitHubOrganization
  url: https://github.com/wayfair
- group: design
  href: https://artifacts.apis.io/wayfair/rules/wayfair-spectral-rules.yml
  title: Wayfair Spectral Rules
  type: SpectralRules
  url: rules/wayfair-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/wayfair/vocabulary/wayfair-vocabulary.yml
  title: Wayfair Vocabulary
  type: Vocabulary
  url: vocabulary/wayfair-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/wayfair/json-ld/wayfair-context.jsonld
  title: Wayfair JSON-LD Context
  type: JSONLD
  url: json-ld/wayfair-context.jsonld
created: '2025-03-01'
description: Wayfair Inc. is one of the world's largest online destinations for home goods and furniture, serving over 20 million customers and 10,000+ suppliers. Wayfair's Developer Portal provides GraphQL-based APIs enabling suppliers to manage purchase orders, inventory updates, product catalog management, advanced shipment notifications, and returns. The platform is built on federated GraphQL architecture using domain-oriented microservices, allowing suppliers to request only the data they need.
examples:
- key_count: 3
  name: Wayfair Graph Ql Error Example
  slug: wayfair-graph-ql-error-example
- key_count: 3
  name: Wayfair Graph Ql Request Example
  slug: wayfair-graph-ql-request-example
- key_count: 2
  name: Wayfair Graph Ql Response Example
  slug: wayfair-graph-ql-response-example
- key_count: 2
  name: Wayfair Token Request Example
  slug: wayfair-token-request-example
- key_count: 3
  name: Wayfair Token Response Example
  slug: wayfair-token-response-example
features:
- description: Unified GraphQL endpoint enabling suppliers to query and mutate data across orders, inventory, catalog, and shipping with precise data fetching.
  name: GraphQL Supplier API
- description: Suppliers retrieve, acknowledge, and manage purchase orders from Wayfair buyers through the GraphQL API.
  name: Purchase Order Management
- description: Real-time inventory updates and stock level management for the Wayfair marketplace catalog.
  name: Inventory Management
- description: Suppliers manage product listings, pricing, descriptions, and attributes through the Product Catalog Update API.
  name: Product Catalog Management
- description: Suppliers submit ASN (Advanced Shipment Notification) data to notify Wayfair of pending shipments, carrier details, and tracking numbers.
  name: Advanced Shipment Notifications
- description: Full sandbox environment at sandbox.api.wayfair.com/v1/graphql for integration testing without affecting production orders.
  name: Sandbox Testing Environment
- description: Client credentials flow authentication issuing temporary access tokens for secure API access.
  name: OAuth2 Token Authentication
finops:
- has_sources: false
  method: generated
  name: Wayfair Finops
  primary_unit: request
  service_category: API
  slug: wayfair-finops
  template: true
graphqls:
- description: GraphQL-based API for Wayfair suppliers to manage orders, inventory, product catalogs, shipping notifications, and returns. Provides access to purchase orders, inventory updates, catalog management, a
  name: Wayfair GraphQL API
  slug: wayfair-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wayfair.png
integrations:
- description: Full sandbox environment for integration testing before deploying to the production Wayfair platform.
  name: Wayfair Sandbox
- description: Wayfair's federated GraphQL architecture enables domain-oriented microservices composition behind a unified supplier API.
  name: Apollo GraphQL Federation
- description: Standard OAuth2 client credentials flow for secure supplier application authentication.
  name: OAuth2 Authentication
json_schemas:
- name: GraphQLError
  property_count: 3
  slug: wayfair-graph-ql-error
- name: GraphQLRequest
  property_count: 3
  slug: wayfair-graph-ql-request
- name: GraphQLResponse
  property_count: 2
  slug: wayfair-graph-ql-response
- name: TokenRequest
  property_count: 2
  slug: wayfair-token-request
- name: TokenResponse
  property_count: 3
  slug: wayfair-token-response
json_structures:
- name: Wayfair Graph Ql Error Structure
  property_count: 3
  slug: wayfair-graph-ql-error-structure
- name: Wayfair Graph Ql Request Structure
  property_count: 3
  slug: wayfair-graph-ql-request-structure
- name: Wayfair Graph Ql Response Structure
  property_count: 2
  slug: wayfair-graph-ql-response-structure
- name: Wayfair Token Request Structure
  property_count: 2
  slug: wayfair-token-request-structure
- name: Wayfair Token Response Structure
  property_count: 3
  slug: wayfair-token-response-structure
jsonld:
- class_count: 5
  name: Wayfair Context
  property_count: 15
  slug: wayfair-context
layout: provider
modified: '2026-05-19'
name: Wayfair
nav: Providers
network: true
overview: 'Wayfair publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Authentication API and Graph QL API. Tagged areas include E-Commerce, Furniture, Home Goods, Retail, and Suppliers.


  The Wayfair catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Wayfair''s developer surface includes authentication, developer portal, documentation, and 15 more developer resources.'
plans:
- name: Wayfair Plans Pricing
  plan_count: 3
  slug: wayfair-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Wayfair Rate Limits
  slug: wayfair-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Wayfair — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wayfair-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Wayfair API Rules
  rule_count: 35
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 20
  slug: wayfair-spectral-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 72.0
    catalog_earned_first_party: 0.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 27.3
    contract_quality: 69.3
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/wayfair/wayfair-2026-06-20T201300.png
security:
- kind: authentication
  name: Wayfair Authentication
  slug: wayfair-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wayfair Domain Security
  slug: wayfair-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wayfair Vulnerability Disclosure
  slug: wayfair-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wayfair
tags:
- E-Commerce
- Furniture
- Home Goods
- Retail
- Suppliers
- GraphQL
use_cases:
- description: Suppliers automate purchase order retrieval, acknowledgment, and fulfillment workflows to reduce manual processing time.
  name: Order Fulfillment Automation
- description: Real-time synchronization of warehouse inventory levels with the Wayfair marketplace to prevent overselling.
  name: Inventory Synchronization
- description: Batch and real-time updates to product listings, pricing, and attributes in the Wayfair catalog.
  name: Product Catalog Updates
- description: Automated submission of ASN data and tracking information when orders are shipped from supplier warehouses.
  name: Shipping Notification Automation
website: https://www.wayfair.com/
---
