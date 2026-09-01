---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-01'
api_count: 7
apis:
- description: Per-dispensary POS surface exposing the functionality of an individual Treez retail instance - customer records and check-in queue, tickets/orders with a non-committing preview, product and stock read
  name: Treez Dispensary API v3
  slug: treez-dispensary-api-v3
- description: Organization-level central product catalog spanning every store an organization operates - products, SKUs/variants, brands, attributes and attribute categories, global and custom subcategories with pe
  name: Treez Catalog Service API
  slug: treez-catalog-service-api
- description: Treez central discount service - create, read, update and delete organization-level discounts that apply across the stores in an organization. 6 operations.
  name: Treez Discount Service API
  slug: treez-discount-service-api
- description: Organization-level product collections used to group products for merchandising, with product list retrieval per collection. 5 operations.
  name: Treez Collection Service API
  slug: treez-collection-service-api
- description: Organization-level tag groups and the tags within them - read all groups, read one group, create and update tags. 5 operations.
  name: Treez Tag Service API
  slug: treez-tag-service-api
- description: Validates a self-signed JWT and returns the organizations, dispensaries and endpoints the signing certificate has been granted access to. The onboarding self-check for the v3 auth scheme. 2 operations
  name: Treez JWT Validation Service
  slug: treez-jwt-validation-service
- description: Legacy v2.0 product surface - list products with rich filters, list products by last-updated, read a product by id, read product fields by category type, create and update products, and upload a produ
  name: Treez Legacy SellTreez v2.0 Product API
  slug: treez-legacy-selltreez-v20-product-api
- description: Live, anonymous, remote MCP endpoint served on Treez's own developer-documentation host. The ReadMe-generated documentation server - initialize returns serverInfo "Treez API Documentation" 3.1.0 and t
  name: Treez Documentation MCP Server
  slug: treez-documentation-mcp-server
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.treez.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://code.treez.io/
- group: docs
  title: ''
  type: Documentation
  url: https://code.treez.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://code.treez.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://code.treez.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.treez.io/
- group: company
  title: ''
  type: Blog
  url: https://www.treez.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.treez.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.treez.io/partner-application
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.treez.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.treez.io/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/treez-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://code.treez.io/llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/treez-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://code.treez.io/.well-known/api-catalog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/treez-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/treez-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/treez-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/treez-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/treez-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/treez-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/treez-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/treez-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/treez-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/treez-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/treez-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/treez-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/treez-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/treez-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-30'
description: 'Treez is an enterprise cloud commerce platform for US cannabis retail, providing dispensary point-of-sale, retail analytics, cashless payments, ecommerce and loyalty to high-volume operators across the largest legal state markets. Its public API surface is a partner-gated REST programme documented at code.treez.io and split into two families: per-dispensary Dispensary APIs at api-prod.treez.io/dispensary/v3 covering customers, tickets/orders, inventory packages, lab results, invoices, distributors and METRC state track-and-trace package sync; and organization-level Service APIs at api-prod.treez.io/service covering the central product catalog, collections, discounts, tags and JWT validation. A legacy SellTreez v2.0 Product API remains published at api.treez.io. Treez serves an RFC 9727 API Catalog naming all seven of its OpenAPI definitions, an llms.txt documentation index, and a live anonymous MCP endpoint over those definitions. Authentication is a self-signed RSA JWT with
  a 30-second TTL; access requires a partner application, an MNDA and API Usage Agreement, sandbox development and certification before a mutual customer can request a production key.'
image: https://images.prismic.io/treez/95e82f5a-f0d3-46e9-a4f0-a1fc774a1e79_Treez_Solful_DSC02615+1.jpg?auto=compress,format
layout: provider
mcp_servers:
- description: ''
  name: Treez API Documentation
  slug: treez-api-documentation
- description: ''
  name: Treez MCP Server
  slug: treez-mcp-server
modified: '2026-08-30'
name: Treez
nav: Providers
network: true
overview: 'Treez publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Dispensary API v3, Catalog Service API, Discount Service API, and 4 more. Tagged areas include Cannabis, Point-of-Sale, Retail, Dispensary, and Inventory Management.


  Treez''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Treez Plans Pricing
  plan_count: 0
  slug: treez-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Treez Rate Limits
  slug: treez-rate-limits
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 44.8
    developer_ergonomics: 57.1
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 46.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Treez Authentication
  slug: treez-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Treez Domain Security
  slug: treez-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: treez
tags:
- Cannabis
- Point-of-Sale
- Retail
- Dispensary
- Inventory Management
- E-Commerce
- Payments
- Compliance
- Track and Trace
- Metrc
- Product Catalog
- Customer Data
website: https://www.treez.io/
---
