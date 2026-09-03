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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.5
  scored_at: '2026-09-03'
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
- baseURL: https://api.target.com
  baseurl_source: declared
  description: Store and online inventory availability
  name: target Inventory API
  slug: target-inventory-api
- baseURL: https://api.target.com
  baseurl_source: declared
  description: Order management for partners
  name: target Orders API
  slug: target-orders-api
- baseURL: https://api.target.com
  baseurl_source: declared
  description: Product catalog and detail operations
  name: target Products API
  slug: target-products-api
- baseURL: https://api.target.com
  baseurl_source: declared
  description: Product search and discovery
  name: target Search API
  slug: target-search-api
- baseURL: https://api.target.com
  baseurl_source: declared
  description: API health and status
  name: target Status API
  slug: target-status-api
- baseURL: https://api.target.com
  baseurl_source: declared
  description: Store locator and store information
  name: target Stores API
  slug: target-stores-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Target Inventory API
  slug: open-target-inventory-api
- collection_type: open
  name: Target Inventory Orders API
  slug: open-target-orders-api
- collection_type: open
  name: Target Inventory Products API
  slug: open-target-products-api
- collection_type: open
  name: Target Inventory Search API
  slug: open-target-search-api
- collection_type: open
  name: Target Inventory Status API
  slug: open-target-status-api
- collection_type: open
  name: Target Inventory Stores API
  slug: open-target-stores-api
- collection_type: open
  name: Target API
  slug: open-target-target-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/target-capability-edges.yml
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
  type: LLMsTxt
  url: https://www.target.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/target-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/target-well-known.yml
- group: auth
  title: ''
  type: Security
  url: security/target-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/target-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/target-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/target-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/target-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/target-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.target.com/c/terms-conditions/-/N-4sr7l
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.target.com/c/target-privacy-policy/-/N-4sr7p
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.target.com/
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
modified: '2026-08-27'
name: Target
nav: Providers
network: true
overview: 'Target publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Inventory API, Orders API, Products API, and 3 more. Tagged areas include Fortune 100, E-Commerce, Retail, Product, and Inventory.


  The Target catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Target''s developer surface includes authentication, engineering blog, and 26 more developer resources.'
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
random_paper: 17
rate_limits:
- limit_count: 1
  name: Target Rate Limits
  slug: target-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Target API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: target-jsonschema-spectral-rules
- effective_rule_count: 62
  extends:
  - spectral:oas
  name: Target API Rules
  rule_count: 21
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 16
  slug: target-spectral-rules
scopes:
- name: Target Scopes
  scope_count: 0
  slug: target-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 28
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 47.0
    contract_quality: 19.9
    developer_ergonomics: 14.3
    discoverability: 81.5
    governance: 47.0
    operational_transparency: 21.1
  previous_composite: 31.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/target/refs/heads/main/screenshots/target-2026-08-17T082249.png
security:
- kind: authentication
  name: Target Authentication
  slug: target-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Target Domain Security
  slug: target-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Target Vulnerability Disclosure
  slug: target-vulnerability-disclosure
  summary_line: Hackerone
slug: target
tags:
- Fortune 100
- E-Commerce
- Retail
- Product
- Inventory
- Stores
- Order
website: https://www.target.com
---
