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
- acting_count: 0
  human_in_the_loop: 0
  name: Target Agentic Access
  operation_count: 9
  slug: target-agentic-access
  summary_line: 9 operations
api_count: 8
apis:
- description: Redsky is Target's internal aggregation API platform that converts GraphQL queries into client-managed REST APIs. It serves product data, pricing, promotions, and fulfillment information for Target.co
  name: Target Redsky API
  slug: target-redsky-api
- description: Target's partner API program enables technology vendors, affiliates, and supply chain partners to integrate with Target's retail operations including product catalog, inventory management, order fulfi
  name: Target Partner API
  slug: target-partner-api
- description: Store and online inventory availability
  name: target Inventory API
  slug: target-inventory-api
- description: Order management for partners
  name: target Orders API
  slug: target-orders-api
- description: Product catalog and detail operations
  name: target Products API
  slug: target-products-api
- description: Product search and discovery
  name: target Search API
  slug: target-search-api
- description: API health and status
  name: target Status API
  slug: target-status-api
- description: Store locator and store information
  name: target Stores API
  slug: target-stores-api
artifact_total: 27
collections:
- collection_type: open
  name: Target API
  slug: open-target-target-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/target-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/target-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/target-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/target-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/target
- group: company
  title: ''
  type: Website
  url: https://www.target.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.target.com/
- group: company
  title: ''
  type: Blog
  url: https://tech.target.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/target
- group: other
  title: ''
  type: Open Source
  url: https://tech.target.com/open-source
- group: operate
  title: ''
  type: StatusPage
  url: https://status.target.com
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/target-product-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/target-store-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/target-product-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/target-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/target-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.target.com/llms.txt
created: '2024-01-01'
description: Target Corporation is one of the largest retailers in the United States, offering a wide assortment of general merchandise and food through more than 1,900 stores and digital channels. Target's technology platform powers partner integrations, internal services, and open-source tooling across their retail operations.
examples:
- key_count: 2
  name: Target Get Product Example
  slug: target-get-product-example
- key_count: 2
  name: Target Get Product Fulfillment Example
  slug: target-get-product-fulfillment-example
- key_count: 2
  name: Target List Stores Example
  slug: target-list-stores-example
- key_count: 2
  name: Target Search Products Example
  slug: target-search-products-example
finops:
- name: Target Finops
  service_category: Retail
  slug: target-finops
graphqls:
- description: Redsky is Target's internal aggregation API platform that converts GraphQL queries into client-managed REST APIs. It serves product data, pricing, promotions, and fulfillment information for Target.co
  name: target GraphQL API
  slug: target-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/target.png
json_schemas:
- name: Target Product
  property_count: 10
  slug: target-product
- name: Target Store
  property_count: 8
  slug: target-store
json_structures:
- name: Target Product Structure
  property_count: 0
  slug: target-product-structure
jsonld:
- class_count: 32
  name: Target Context
  property_count: 0
  slug: target-context
layout: provider
modified: '2026-05-19'
name: target
nav: Providers
network: true
overview: 'target publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Inventory API, Orders API, Products API, and 3 more. Tagged areas include Fortune 100, E-Commerce, Retail, Products, and Inventory.


  The target catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  target''s developer surface includes authentication, engineering blog, and 15 more developer resources.'
plans:
- name: Target Plans Pricing
  plan_count: 1
  slug: target-plans-pricing
press:
- date: '2026-05-25'
  title: Target to Roll Out Transformative GenAI Technology to its ...
  url: https://corporate.target.com/press/release/2024/06/target-to-roll-out-transformative-genai-technology-to-its-store-team-members-chainwide
- date: '2026-05-25'
  title: A Partnership to Develop Generative AI Applications Helps ...
  url: https://www.bain.com/client-results/ai/target/
- date: '2026-05-25'
  title: A look at Target's approach to generative AI
  url: https://www.retaildive.com/news/target-generative-artificial-intelligence-technology-forecasting-marketplace/802801/
- date: '2026-05-25'
  title: Target Launches New AI-Powered Features to Make ...
  url: https://www.prnewswire.com/news-releases/target-launches-new-ai-powered-features-to-make-holiday-shopping-easier-smarter-and-more-fun-302612422.html
- date: '2026-05-25'
  title: Target's Using Artificial Intelligence to Make Your Shopping ...
  url: https://corporate.target.com/news-features/article/2023/12/artificial-intelligence
random_paper: 80
rate_limits:
- limit_count: 1
  name: Target Rate Limits
  slug: target-rate-limits
rules:
- name: target API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: target-jsonschema-spectral-rules
- name: target API Rules
  rule_count: 21
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 16
  slug: target-spectral-rules
score:
  band: developing
  composite: 48.3
  delta: -4.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 68.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Target Authentication
  slug: target-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Target Domain Security
  slug: target-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Target Vulnerability Disclosure
  slug: target-vulnerability-disclosure
  summary_line: disclosure policy published
slug: target
tags:
- Fortune 100
- E-Commerce
- Retail
- Products
- Inventory
- Fortune 100
- Stores
- Orders
website: https://www.target.com
---
