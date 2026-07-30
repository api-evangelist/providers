---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
  score: 32.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Buywhere Agentic Access
  operation_count: 8
  slug: buywhere-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- description: Agent-native REST and MCP product catalog covering 1.5M+ products across Southeast Asian and US e-commerce platforms. Operations include keyword search, side-by-side comparison, deals discovery, price
  name: BuyWhere Product Catalog API
  slug: product-catalog-api
artifact_total: 26
collections:
- collection_type: open
  name: BuyWhere Product Catalog API
  slug: open-buywhere
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/buywhere-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/buywhere-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buywhere-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/buywhere-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://api.buywhere.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.buywhere.ai/
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://api.buywhere.ai/docs/guides/mcp
- group: agent
  title: ''
  type: MCPEndpoint
  url: https://api.buywhere.ai/mcp
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.buywhere.ai/openapi.json
- group: build
  title: ''
  type: PluginManifest
  url: https://api.buywhere.ai/.well-known/ai-plugin.json
- group: agent
  title: ''
  type: LlmsText
  url: https://api.buywhere.ai/llms.txt
- group: company
  title: ''
  type: Website
  url: https://api.buywhere.ai/us/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/BuyWhere
- group: build
  title: ''
  type: GitHub
  url: https://github.com/BuyWhere/buywhere
- group: commercial
  title: ''
  type: Plans
  url: plans/buywhere-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/buywhere-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/buywhere-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/buywhere-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/buywhere-context.jsonld
created: '2026-05-16'
description: Agent-native, MCP-native product catalog and price comparison API for Southeast Asia and US e-commerce. Search 1.5M+ products across Shopee, Lazada, Carousell, FairPrice, Best Denki, Amazon, Walmart, Best Buy, and 20+ retailers. AI agents and MCP clients discover and route purchases to local merchants through a hosted MCP HTTP endpoint at api.buywhere.ai/mcp or via the @buywhere/mcp-server STDIO package.
examples:
- key_count: 2
  name: Buywhere Compareproducts Example
  slug: buywhere-compareProducts-example
- key_count: 2
  name: Buywhere Getcategoryproducts Example
  slug: buywhere-getCategoryProducts-example
- key_count: 2
  name: Buywhere Getdeals Example
  slug: buywhere-getDeals-example
- key_count: 2
  name: Buywhere Getproduct Example
  slug: buywhere-getProduct-example
- key_count: 2
  name: Buywhere Getproductprices Example
  slug: buywhere-getProductPrices-example
- key_count: 2
  name: Buywhere Listcategories Example
  slug: buywhere-listCategories-example
- key_count: 3
  name: Buywhere Mcp Tools Call Example
  slug: buywhere-mcp-tools-call-example
- key_count: 2
  name: Buywhere Registeragent Example
  slug: buywhere-registerAgent-example
- key_count: 2
  name: Buywhere Searchproducts Example
  slug: buywhere-searchProducts-example
finops:
- name: Buywhere Finops
  service_category: Commerce / Product Catalog
  slug: buywhere-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: BuyWhere Category
  property_count: 4
  slug: buywhere-category
- name: BuyWhere Offer
  property_count: 14
  slug: buywhere-offer
- name: BuyWhere Price History
  property_count: 5
  slug: buywhere-price-history
- name: BuyWhere Product
  property_count: 20
  slug: buywhere-product
json_structures:
- name: Buywhere Offer Structure
  property_count: 0
  slug: buywhere-offer-structure
- name: Buywhere Product Structure
  property_count: 0
  slug: buywhere-product-structure
jsonld:
- class_count: 25
  name: Buywhere Context
  property_count: 4
  slug: buywhere-context
layout: provider
modified: '2026-05-19'
name: BuyWhere
nav: Providers
network: true
overview: 'BuyWhere publishes 1 API on the [APIs.io](https://apis.io/) network: Product Catalog API. Tagged areas include E-commerce, Shopping, Price Comparison, SEA, and Southeast Asia.


  The BuyWhere catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BuyWhere''s developer surface includes authentication, documentation, GitHub presence, and 16 more developer resources.'
plans:
- name: Buywhere Plans Pricing
  plan_count: 3
  slug: buywhere-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 4
  name: Buywhere Rate Limits
  slug: buywhere-rate-limits
rules:
- name: BuyWhere API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: buywhere-jsonschema-spectral-rules
- name: BuyWhere API Rules
  rule_count: 14
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 9
  slug: buywhere-rules
score:
  band: developing
  composite: 49.1
  delta: -7.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.4
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/buywhere/refs/heads/main/screenshots/buywhere-2026-06-20T173822.png
security:
- kind: authentication
  name: Buywhere Authentication
  slug: buywhere-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Buywhere Domain Security
  slug: buywhere-domain-security
  summary_line: TLSv1.3 · DMARC
slug: buywhere
tags:
- E-commerce
- Shopping
- Price Comparison
- SEA
- Southeast Asia
- AI Agents
- Product Catalog
website: https://api.buywhere.ai/
---
