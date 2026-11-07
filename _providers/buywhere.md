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
    agent_card: flavored
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
    mcp_server: verified
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Buywhere Agentic Access
  operation_count: 8
  slug: buywhere-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.buywhere.ai/v1
  baseurl_source: declared
  description: Product taxonomy and category browsing.
  name: BuyWhere Categories API
  slug: buywhere-categories-api
- baseURL: https://api.buywhere.ai/v1
  baseurl_source: declared
  description: Product search, lookup, comparison, deals, and price history.
  name: BuyWhere Products API
  slug: buywhere-products-api
- baseURL: https://api.buywhere.ai/v1
  baseurl_source: declared
  description: The Auth API from BuyWhere — 1 operation(s) for auth.
  name: BuyWhere Auth API
  slug: buywhere-auth-api
- baseURL: https://api.buywhere.ai/v1
  baseurl_source: declared
  description: The Featured API from BuyWhere — 1 operation(s) for featured.
  name: BuyWhere Featured API
  slug: buywhere-featured-api
- baseURL: https://api.buywhere.ai/v1
  baseurl_source: declared
  description: The Usage API from BuyWhere — 1 operation(s) for usage.
  name: BuyWhere Usage API
  slug: buywhere-usage-api
artifact_total: 34
collections:
- collection_type: open
  name: BuyWhere Product Catalog Authentication API
  slug: open-buywhere-authentication-api
- collection_type: open
  name: BuyWhere Product Catalog Authentication Categories API
  slug: open-buywhere-categories-api
- collection_type: open
  name: BuyWhere Product Catalog Authentication Products API
  slug: open-buywhere-products-api
- collection_type: open
  name: BuyWhere Product Catalog API
  slug: open-buywhere
common:
- group: other
  href: https://artifacts.apis.io/buywhere/capabilities/buywhere-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/buywhere-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/buywhere/a2a/buywhere-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/buywhere-a2a.yml
- group: agent
  href: https://artifacts.apis.io/buywhere/agentic-access/buywhere-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buywhere-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/buywhere/security/buywhere-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buywhere-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/buywhere/authentication/buywhere-authentication.yml
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
  href: https://artifacts.apis.io/buywhere/plans/buywhere-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buywhere-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/buywhere/rate-limits/buywhere-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/buywhere-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/buywhere/finops/buywhere-finops.yml
  title: ''
  type: FinOps
  url: finops/buywhere-finops.yml
- group: design
  href: https://artifacts.apis.io/buywhere/vocabulary/buywhere-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buywhere-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buywhere/json-ld/buywhere-context.jsonld
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
- has_sources: true
  method: generated
  name: Buywhere Finops
  primary_unit: ''
  service_category: Commerce / Product Catalog
  slug: buywhere-finops
  template: false
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
mcp_servers:
- description: Remote MCP server at mcp.buywhere.ai over HTTP; 13 tools listed.
  name: BuyWhere MCP Server
  slug: buywhere
modified: '2026-05-19'
name: BuyWhere
nav: Providers
network: true
overview: 'BuyWhere publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Categories API, Products API, Auth API, and 2 more. Tagged areas include E-Commerce, Shopping, Price Comparison, SEA, and Southeast Asia.


  The BuyWhere catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BuyWhere''s developer surface includes authentication, documentation, GitHub presence, and 17 more developer resources.'
plans:
- name: Buywhere Plans Pricing
  plan_count: 3
  slug: buywhere-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Buywhere Rate Limits
  slug: buywhere-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: BuyWhere — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: buywhere-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: BuyWhere API Rules
  rule_count: 14
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 9
  slug: buywhere-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 69.0
    catalog_earned_first_party: 0.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 7.9
    contract_governance: 27.3
    contract_quality: 61.6
    developer_ergonomics: 21.4
    discoverability: 75.0
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 55.6
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/buywhere/buywhere-2026-06-20T173822.png
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
- E-Commerce
- Shopping
- Price Comparison
- SEA
- Southeast Asia
- AI Agents
- Product Catalog
- A2A
website: https://api.buywhere.ai/
---
