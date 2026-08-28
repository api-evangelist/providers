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
  name: Sysco Agentic Access
  operation_count: 11
  slug: sysco-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 5
apis:
- description: Manage customer account information.
  name: Sysco Accounts API
  slug: sysco-accounts-api
- description: Track delivery status and scheduling.
  name: Sysco Deliveries API
  slug: sysco-deliveries-api
- description: Create and manage food distribution orders.
  name: Sysco Orders API
  slug: sysco-orders-api
- description: Retrieve product pricing and contract pricing.
  name: Sysco Pricing API
  slug: sysco-pricing-api
- description: Browse and search the Sysco product catalog.
  name: Sysco Products API
  slug: sysco-products-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sysco Food Distribution Accounts API
  slug: open-sysco-accounts-api
- collection_type: open
  name: Sysco Food Distribution Accounts Deliveries API
  slug: open-sysco-deliveries-api
- collection_type: open
  name: Sysco Food Distribution API
  slug: open-sysco-food-distribution-api
- collection_type: open
  name: Sysco Food Distribution Accounts Orders API
  slug: open-sysco-orders-api
- collection_type: open
  name: Sysco Food Distribution Accounts Pricing API
  slug: open-sysco-pricing-api
- collection_type: open
  name: Sysco Food Distribution Accounts Products API
  slug: open-sysco-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sysco-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sysco-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sysco-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sysco-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sysco
- group: company
  title: ''
  type: Website
  url: https://www.sysco.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apic-devportal.sysco.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/SyscoCorporation
- group: docs
  title: ''
  type: GraphQL
  url: https://www.apollographql.com/customers/sysco
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/sysco-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sysco-vocabulary.yml
created: '2026-05-03'
description: Sysco is the global leader in selling, marketing, and distributing food products to restaurants, healthcare and educational facilities, lodging establishments, and other foodservice customers. Sysco operates the Sysco Shop ecommerce platform (US, Canada, Bahamas) backed by an Apollo GraphQL supergraph composed of domain subgraphs for ordering, product, pricing, delivery, and accounts. Programmatic access is partner/customer-gated through the login-only APIC Developer Portal and through traditional EDI (X12) trading-partner integration; Sysco does not publish a self-serve public developer API, OpenAPI specification, or open GitHub presence.
examples:
- key_count: 2
  name: Sysco Food Distribution Api Createorder Example
  slug: sysco-food-distribution-api-createOrder-example
- key_count: 2
  name: Sysco Food Distribution Api Listproducts Example
  slug: sysco-food-distribution-api-listProducts-example
finops:
- name: Sysco Finops
  service_category: Foodservice Distribution
  slug: sysco-finops
graphqls:
- description: ''
  name: Sysco GraphQL API
  slug: sysco-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sysco.png
json_schemas:
- name: Product
  property_count: 12
  slug: sysco-product
json_structures:
- name: Sysco Product Structure
  property_count: 0
  slug: sysco-product-structure
jsonld:
- class_count: 24
  name: Sysco Context
  property_count: 4
  slug: sysco-context
layout: provider
modified: '2026-06-03'
name: Sysco
nav: Providers
network: true
overview: 'Sysco publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Deliveries API, Orders API, and 2 more. Tagged areas include Fortune 100, Food Distribution, Food Service, Supply Chain, and Wholesale.


  The Sysco catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sysco''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Sysco Plans Pricing
  plan_count: 1
  slug: sysco-plans-pricing
press:
- date: '2026-05-25'
  title: Incorporating generative AI into your company's technology ...
  url: https://mitsloan.mit.edu/ideas-made-to-matter/incorporating-generative-ai-your-companys-technology-strategy
- date: '2026-05-25'
  title: Sysco LABS' Nexus series spotlights AI-powered ...
  url: https://www.facebook.com/Dailymirroronline/posts/sysco-labs-nexus-series-spotlights-ai-powered-engineering/1090381859785819/
- date: '2026-05-25'
  title: Sysco puts AI at the center of its sales rebound in Q1
  url: https://www.digitalcommerce360.com/2025/10/31/sysco-puts-ai-at-the-center-of-its-sales-rebound-in-q1/
- date: '2026-05-25'
  title: 'The Restaurant Revolution: AI and Robotics'
  url: https://foodie.sysco.com/tips-and-trends/how-artificial-intelligence-and-robotics-are-revolutionizing-the-restaurant-industry/
- date: '2026-05-25'
  title: 2023 ANNUAL REPORT
  url: https://investors.sysco.com/~/media/Files/S/Sysco-IR/documents/annual-reports/Sysco_2023-Annual-Report_Web.pdf
random_paper: 15
rate_limits:
- limit_count: 1
  name: Sysco Rate Limits
  slug: sysco-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sysco API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sysco-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Sysco API Rules
  rule_count: 13
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 6
  slug: sysco-rules
score:
  band: thin
  composite: 36.6
  delta: 3.7
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 57.6
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Sysco Authentication
  slug: sysco-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sysco Domain Security
  slug: sysco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sysco Vulnerability Disclosure
  slug: sysco-vulnerability-disclosure
  summary_line: disclosure policy published
slug: sysco
tags:
- Fortune 100
- Food Distribution
- Food Service
- Supply Chain
- Wholesale
website: https://www.sysco.com
---
