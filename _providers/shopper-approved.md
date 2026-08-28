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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Shopper Approved Agentic Access
  operation_count: 6
  slug: shopper-approved-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- description: The Orders API from Shopper Approved — 1 operation(s) for orders.
  name: Shopper Approved Orders API
  slug: shopper-approved-orders-api
- description: The Product Reviews API from Shopper Approved — 1 operation(s) for product reviews.
  name: Shopper Approved Product Reviews API
  slug: shopper-approved-product-reviews-api
- description: The Reviews API from Shopper Approved — 3 operation(s) for reviews.
  name: Shopper Approved Reviews API
  slug: shopper-approved-reviews-api
- description: The Statistics API from Shopper Approved — 1 operation(s) for statistics.
  name: Shopper Approved Statistics API
  slug: shopper-approved-statistics-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shopper Approved Orders API
  slug: open-shopper-approved-orders-api
- collection_type: open
  name: Shopper Approved Orders Statistics API
  slug: open-shopper-approved-statistics-api
- collection_type: open
  name: Shopper Approved API
  slug: open-shopper-approved
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shopper-approved-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shopper-approved-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopper-approved-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopper-approved-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shopperapproved
created: '2026-05-02'
description: Shopper Approved is an e-commerce ratings and reviews platform that helps merchants collect, manage, and display verified customer reviews to improve conversion rates and build trust. The platform powers Google Seller Ratings, enabling reviews to appear in Google Shopping ads and organic search results. Shopper Approved offers a REST API for programmatic access to review data, order submission for review collection, product review management, and site statistics.
examples:
- key_count: 4
  name: Shopper Approved List Reviews Example
  slug: shopper-approved-list-reviews-example
- key_count: 4
  name: Shopper Approved Submit Order Example
  slug: shopper-approved-submit-order-example
finops:
- name: Shopper Approved Finops
  service_category: API
  slug: shopper-approved-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shopper-approved.png
json_schemas:
- name: Shopper Approved Product Review
  property_count: 9
  slug: shopper-approved-product-review
- name: Shopper Approved Review
  property_count: 10
  slug: shopper-approved-review
json_structures:
- name: Shopper Approved Review Structure
  property_count: 0
  slug: shopper-approved-review-structure
jsonld:
- class_count: 23
  name: Shopper Approved Context
  property_count: 2
  slug: shopper-approved-context
layout: provider
modified: '2026-05-19'
name: Shopper Approved
nav: Providers
network: true
overview: 'Shopper Approved publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Orders API, Product Reviews API, Reviews API, and 1 more. Tagged areas include Reviews, Ratings, E-Commerce, Customer Feedback, and Social Proof.


  The Shopper Approved catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Shopper Approved''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Shopper Approved Plans Pricing
  plan_count: 3
  slug: shopper-approved-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Shopper Approved Rate Limits
  slug: shopper-approved-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Shopper Approved API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: shopper-approved-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Shopper Approved API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: shopper-approved-rules
score:
  band: thin
  composite: 36.4
  delta: 4.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 64.6
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shopper-approved/refs/heads/main/screenshots/shopper-approved-2026-06-20T193837.png
security:
- kind: authentication
  name: Shopper Approved Authentication
  slug: shopper-approved-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shopper Approved Domain Security
  slug: shopper-approved-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Shopper Approved Vulnerability Disclosure
  slug: shopper-approved-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: shopper-approved
tags:
- Reviews
- Ratings
- E-Commerce
- Customer Feedback
- Social Proof
---
