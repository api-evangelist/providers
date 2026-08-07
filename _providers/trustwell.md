---
access_model:
  confidence: high
  label: Enterprise (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 5
  human_in_the_loop: 0
  name: Trustwell Agentic Access
  operation_count: 15
  slug: trustwell-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 8
apis:
- description: The Trustwell Genesis Foods GraphQL API provides programmatic access to food formulation, nutrition analysis, and label generation capabilities. The GraphQL endpoint at api.trustwell.com/genesis suppo
  name: Trustwell Genesis Foods GraphQL API
  slug: trustwell-genesis-foods-graphql-api
- description: The Trustwell Genesis Supplements API provides formulation and regulatory compliance capabilities for dietary supplement manufacturers. Built on the same Genesis Foods GraphQL endpoint, it supports Su
  name: Trustwell Genesis Supplements API
  slug: trustwell-genesis-supplements-api
- description: Compliance documentation and requirements
  name: Trustwell Compliance API
  slug: trustwell-compliance-api
- description: Product specification management
  name: Trustwell Products API
  slug: trustwell-products-api
- description: Quality incident management
  name: Trustwell Quality API
  slug: trustwell-quality-api
- description: Recall and withdrawal management
  name: Trustwell Recalls API
  slug: trustwell-recalls-api
- description: Supplier relationship management
  name: Trustwell Suppliers API
  slug: trustwell-suppliers-api
- description: Farm-to-fork traceability (FSMA 204)
  name: Trustwell Traceability API
  slug: trustwell-traceability-api
artifact_total: 29
collections:
- collection_type: open
  name: Trustwell FoodLogiQ API
  slug: open-trustwell-foodlogiq
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trustwell-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trustwell-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trustwell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trustwell-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.trustwell.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trustwell.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trustwell.com/genesis/api/
- group: start
  title: ''
  type: Portal
  url: https://www.trustwell.com/platform/
- group: other
  title: ''
  type: Products
  url: https://www.trustwell.com/products/
- group: company
  title: ''
  type: Blog
  url: https://blog.trustwell.com/
- group: company
  title: ''
  type: News
  url: https://www.trustwell.com/news-and-press/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trustwell.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trustwell.com/terms-of-service/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trustwell-llc
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/trustwell/refs/heads/main/rules/trustwell-rules.yml
created: '2026-03-16'
description: 'Trustwell is a food industry software company formed from the merger of ESHA Research and FoodLogiQ in 2023, providing the food and beverage industry with an integrated platform covering product formulation, nutrition labeling, regulatory compliance, supply chain management, traceability, quality assurance, and recall management. The Trustwell Connect Platform offers two primary APIs: the Genesis Foods GraphQL API for nutrition analysis, food formulation, and label generation (with support for US, Canadian, EU, Mexican, and Australian regulatory standards), and the FoodLogiQ API for supply chain visibility, compliance management, supplier relationships, and FSMA 204-compliant traceability. Both APIs require X-API-KEY authentication. The platform serves food manufacturers, retailers, restaurants, and distributors across the global food supply chain.'
examples:
- key_count: 2
  name: Trustwell Foodlogiq Create Recall Example
  slug: trustwell-foodlogiq-create-recall-example
- key_count: 2
  name: Trustwell Foodlogiq List Suppliers Example
  slug: trustwell-foodlogiq-list-suppliers-example
- key_count: 2
  name: Trustwell Genesis Foods Query Example
  slug: trustwell-genesis-foods-query-example
finops:
- name: Trustwell Finops
  service_category: Food Safety & Compliance SaaS
  slug: trustwell-finops
graphqls:
- description: The Trustwell Genesis Foods GraphQL API provides programmatic access to food formulation, nutrition analysis, and label generation capabilities. The GraphQL endpoint at api.trustwell.com/genesis suppo
  name: Trustwell GraphQL API
  slug: trustwell-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trustwell.png
json_schemas:
- name: FoodItem
  property_count: 13
  slug: trustwell-food-item
- name: QualityIncident
  property_count: 16
  slug: trustwell-quality-incident
- name: Recall
  property_count: 17
  slug: trustwell-recall
- name: Supplier
  property_count: 12
  slug: trustwell-supplier
json_structures:
- name: Trustwell Food Item Structure
  property_count: 0
  slug: trustwell-food-item-structure
- name: Trustwell Supplier Structure
  property_count: 0
  slug: trustwell-supplier-structure
jsonld:
- class_count: 46
  name: Trustwell Context
  property_count: 6
  slug: trustwell-context
layout: provider
modified: '2026-05-19'
name: Trustwell
nav: Providers
network: true
overview: 'Trustwell publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Compliance API, Products API, Quality API, and 3 more. Tagged areas include Food Industry, Food Safety, Nutrition, Supply Chain, and Food Labeling.


  The Trustwell catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trustwell''s developer surface includes authentication, documentation, developer portal, engineering blog, product news, and 10 more developer resources.'
plans:
- name: Trustwell Plans Pricing
  plan_count: 1
  slug: trustwell-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 1
  name: Trustwell Rate Limits
  slug: trustwell-rate-limits
rules:
- name: Trustwell API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: trustwell-jsonschema-spectral-rules
- name: Trustwell API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 3
    warn: 6
  slug: trustwell-rules
score:
  band: developing
  composite: 51.6
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 67.2
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trustwell/refs/heads/main/screenshots/trustwell-2026-06-20T195809.png
security:
- kind: authentication
  name: Trustwell Authentication
  slug: trustwell-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trustwell Domain Security
  slug: trustwell-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Trustwell Trust Center
  slug: trustwell-trust-center
  summary_line: SOC 2
slug: trustwell
tags:
- Food Industry
- Food Safety
- Nutrition
- Supply Chain
- Food Labeling
- Traceability
- Compliance
- Food Technology
website: https://www.trustwell.com/
---
