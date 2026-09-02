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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Best Buy Agentic Access
  operation_count: 8
  slug: best-buy-agentic-access
  summary_line: 8 operations
api_count: 6
apis:
- description: Navigate Best Buy's product taxonomy with access to 4,328+ product categories. Browse hierarchical category paths from root to specific categories and integrate with product searches for category-spec
  name: Best Buy Categories API
  slug: categories-api
- description: Access discounted open box and Geek Squad certified refurbished merchandise with ship-from-store fulfillment. Supports single SKU, batch queries up to 100 SKUs, and category-based discovery with condi
  name: Best Buy Buying Options (Open Box) API
  slug: buying-options-api
- description: Enable integrated shopping experiences for authorized partners with product availability lookups, shipping cost calculations, and order creation supporting store pickup, ship-to-home, and home deliver
  name: Best Buy Commerce API
  slug: commerce-api
- description: Product catalog queries and retrieval
  name: Best Buy Products API
  slug: best-buy-products-api
- description: Customer behavior-based product recommendations
  name: Best Buy Recommendations API
  slug: best-buy-recommendations-api
- description: Best Buy store location and information queries
  name: Best Buy Stores API
  slug: best-buy-stores-api
artifact_total: 69
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Best Buy Products API
  slug: open-best-buy-products-api
- collection_type: open
  name: Best Buy Products Recommendations API
  slug: open-best-buy-recommendations-api
- collection_type: open
  name: Best Buy Products Stores API
  slug: open-best-buy-stores-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/BestBuyAPIs/api-documentation/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/BestBuyAPIs/api-documentation/blob/master/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/best-buy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/best-buy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/best-buy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/best-buy
- group: company
  title: ''
  type: Website
  url: https://www.bestbuy.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bestbuy.com
- group: docs
  title: ''
  type: Documentation
  url: https://bestbuyapis.github.io/api-documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://bestbuyapis.github.io/api-documentation/#user-guide
- group: auth
  title: ''
  type: Authentication
  url: https://bestbuyapis.github.io/api-documentation/#authorization
- group: start
  title: ''
  type: Signup
  url: https://developer.bestbuy.com
- group: company
  title: ''
  type: Blog
  url: https://corporate.bestbuy.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BestBuyAPIs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/BestBuyAPIs/api-documentation
- group: operate
  title: ''
  type: RateLimits
  url: https://bestbuyapis.github.io/api-documentation/#rate-limiting
- group: design
  title: ''
  type: SpectralRules
  url: rules/best-buy-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/best-buy-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/best-buy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/best-buy-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/best-buy-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/best-buy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/best-buy-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/best-buy-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/best-buy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/best-buy-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/best-buy-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/best-buy-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/best-buy-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/best-buy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/best-buy-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/best-buy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/best-buy-plans-pricing.yml
- group: agent
  title: ''
  type: MCP
  url: mcp/best-buy-mcp.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/best-buy-well-known.yml
- group: docs
  title: ''
  type: APIReference
  url: https://bestbuyapis.github.io/api-documentation/#products-api
- group: operate
  title: ''
  type: Support
  url: https://developer.bestbuy.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.bestbuy.com/legal
- group: start
  title: ''
  type: Console
  url: https://bestbuyapis.github.io/bby-query-builder/
created: '2026-04-19'
description: Best Buy is a multinational consumer electronics retailer offering technology products, services, and solutions through stores, online, and in-home consultations. Best Buy provides a developer API giving access to product data, store locations, categories, recommendations, open box offers, and commerce capabilities for partners and developers building retail integrations and applications.
examples:
- key_count: 2
  name: Products Api Category Ref Example
  slug: products-api-category-ref-example
- key_count: 3
  name: Products Api Error Response Example
  slug: products-api-error-response-example
- key_count: 25
  name: Products Api Product Example
  slug: products-api-product-example
- key_count: 11
  name: Products Api Product List Response Example
  slug: products-api-product-list-response-example
- key_count: 3
  name: Recommendations Api Error Response Example
  slug: recommendations-api-error-response-example
- key_count: 2
  name: Recommendations Api Recommendations Response Example
  slug: recommendations-api-recommendations-response-example
- key_count: 6
  name: Recommendations Api Recommended Product Example
  slug: recommendations-api-recommended-product-example
- key_count: 3
  name: Stores Api Error Response Example
  slug: stores-api-error-response-example
- key_count: 16
  name: Stores Api Store Example
  slug: stores-api-store-example
- key_count: 8
  name: Stores Api Store List Response Example
  slug: stores-api-store-list-response-example
- key_count: 1
  name: Stores Api Store Service Example
  slug: stores-api-store-service-example
features:
- 'Best Buy: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- Best Buy APIs (Products, Stores) are accessible via developer key; commercial use requires partner agreement.
finops:
- name: Best Buy Finops
  service_category: Retail
  slug: best-buy-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Best Buy API. Best Buy provides a REST-based Open API covering products, stores, categories, recommendations, open box items, and commerce o
  name: Best Buy GraphQL Schema
  slug: best-buy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/best-buy.png
integrations:
- description: Pre-built Postman collection available for testing and exploring Best Buy APIs.
  name: Postman
- description: Affiliate commission integration using Impact Partner ID for revenue attribution.
  name: Impact Affiliate Network
json_schemas:
- name: CategoryRef
  property_count: 2
  slug: products-api-category-ref
- name: ErrorResponse
  property_count: 3
  slug: products-api-error-response
- name: ProductListResponse
  property_count: 11
  slug: products-api-product-list-response
- name: Product
  property_count: 25
  slug: products-api-product
- name: ErrorResponse
  property_count: 3
  slug: recommendations-api-error-response
- name: RecommendationsResponse
  property_count: 2
  slug: recommendations-api-recommendations-response
- name: RecommendedProduct
  property_count: 6
  slug: recommendations-api-recommended-product
- name: ErrorResponse
  property_count: 3
  slug: stores-api-error-response
- name: StoreListResponse
  property_count: 8
  slug: stores-api-store-list-response
- name: Store
  property_count: 16
  slug: stores-api-store
- name: StoreService
  property_count: 1
  slug: stores-api-store-service
json_structures:
- name: Products Api Category Ref Structure
  property_count: 2
  slug: products-api-category-ref-structure
- name: Products Api Error Response Structure
  property_count: 3
  slug: products-api-error-response-structure
- name: Products Api Product List Response Structure
  property_count: 11
  slug: products-api-product-list-response-structure
- name: Products Api Product Structure
  property_count: 25
  slug: products-api-product-structure
- name: Recommendations Api Error Response Structure
  property_count: 3
  slug: recommendations-api-error-response-structure
- name: Recommendations Api Recommendations Response Structure
  property_count: 2
  slug: recommendations-api-recommendations-response-structure
- name: Recommendations Api Recommended Product Structure
  property_count: 6
  slug: recommendations-api-recommended-product-structure
- name: Stores Api Error Response Structure
  property_count: 3
  slug: stores-api-error-response-structure
- name: Stores Api Store List Response Structure
  property_count: 8
  slug: stores-api-store-list-response-structure
- name: Stores Api Store Service Structure
  property_count: 1
  slug: stores-api-store-service-structure
- name: Stores Api Store Structure
  property_count: 16
  slug: stores-api-store-structure
jsonld:
- class_count: 6
  name: Best Buy Products Api Context
  property_count: 38
  slug: best-buy-products-api-context
- class_count: 3
  name: Best Buy Recommendations Api Context
  property_count: 20
  slug: best-buy-recommendations-api-context
- class_count: 5
  name: Best Buy Stores Api Context
  property_count: 27
  slug: best-buy-stores-api-context
layout: provider
modified: '2026-08-27'
name: Best Buy
nav: Providers
network: true
overview: 'Best Buy publishes 3 APIs on the [APIs.io](https://apis.io/) network: Products API, Recommendations API, and Stores API. Tagged areas include Fortune 100, Retail, Consumer Electronics, E-Commerce, and Product.


  The Best Buy catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  Best Buy''s developer surface includes authentication, documentation, getting-started guide, signup flow, engineering blog, CLI, changelog, and 33 more developer resources.'
plans:
- name: Best Buy Plans Pricing
  plan_count: 2
  slug: best-buy-plans-pricing
press:
- date: '2026-05-25'
  title: Best Buy, Google Cloud, and Accenture Partner to Create a ...
  url: https://www.prnewswire.com/news-releases/best-buy-google-cloud-and-accenture-partner-to-create-a-better-customer-support-experience-with-generative-ai-302111387.html
- date: '2026-05-25'
  title: Artificial Intelligence Archives - Best Buy Corporate News ...
  url: https://corporate.bestbuy.com/tag/artificial-intelligence/
- date: '2026-05-25'
  title: Best Buy case study
  url: https://cloud.google.com/customers/bestbuy
- date: '2026-05-25'
  title: Best Buy launches AI-powered delivery tracking
  url: https://www.retaildive.com/news/best-buy-launches-artificial-intelligence-delivery-tracking/724541/
- date: '2026-05-25'
  title: How Best Buy Uses AI To Transform Customer Experience
  url: https://www.forbes.com/sites/maribellopez/2025/06/17/how-best-buy-uses-ai-to-transform-customer-experience/
random_paper: 13
rate_limits:
- limit_count: 2
  name: Best Buy Rate Limits
  slug: best-buy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Best Buy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: best-buy-jsonschema-spectral-rules
- effective_rule_count: 79
  extends:
  - spectral:oas
  name: Best Buy API Rules
  rule_count: 38
  severity_counts:
    error: 15
    hint: 0
    info: 6
    warn: 17
  slug: best-buy-spectral-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 32
    catalog_gap: 40.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 2.2
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 33.3
    contract_quality: 28.5
    developer_ergonomics: 80.4
    discoverability: 72.2
    governance: 33.3
    operational_transparency: 57.9
  open_source:
    applies: true
    score: 25.0
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/best-buy/refs/heads/main/screenshots/best-buy-2026-06-20T173159.png
security:
- kind: authentication
  name: Best Buy Authentication
  slug: best-buy-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Best Buy Domain Security
  slug: best-buy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Best Buy Vulnerability Disclosure
  slug: best-buy-vulnerability-disclosure
  summary_line: Hackerone
slug: best-buy
tags:
- Fortune 100
- Retail
- Consumer Electronics
- E-Commerce
- Product
- Stores
use_cases:
- description: Full-text search and filtering across product descriptions, specifications, and reviews.
  name: Product Discovery
- description: Real-time in-store availability checking by postal code or store ID.
  name: Inventory Management
- description: Display trending, most-viewed, and also-bought products on product detail pages.
  name: Recommendation Widgets
- description: Proximity-based store search with hours verification and service availability.
  name: Store Locator
- description: Identify discounted alternatives with transparent condition ratings.
  name: Open Box Sourcing
- description: Track product price changes and availability updates.
  name: Price Monitoring
- description: Build shopping experiences integrated with Best Buy's product catalog and fulfillment.
  name: Retail Integration
- description: Commission-based product recommendations with affiliate partner integration.
  name: Affiliate Commerce
website: https://www.bestbuy.com
---
