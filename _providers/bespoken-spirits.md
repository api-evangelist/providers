---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Bespoken Spirits Agentic Access
  operation_count: 18
  slug: bespoken-spirits-agentic-access
  summary_line: 18 operations · 8 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: The Universal Commerce Protocol (UCP) shopping service for the Bespoken Spirits storefront, exposed over MCP as a JSON-RPC 2.0 endpoint. An anonymous tools/list returns 13 tools covering catalog searc
  name: Bespoken Spirits UCP Commerce MCP
  slug: bespoken-spirits-ucp-commerce-mcp
- description: The Shopify storefront-renderer MCP endpoint for bespokenspirits.com. An anonymous tools/list returns 5 tools — search_catalog, get_cart, update_cart, search_shop_policies_and_faqs and get_product_det
  name: Bespoken Spirits Storefront MCP
  slug: bespoken-spirits-storefront-mcp
- description: 'The public, unauthenticated Shopify storefront product JSON surface documented in the store''s own llms.txt and agents.md: /products.json for the catalog (30 by default, 47 with ?limit=250 at probe tim'
  name: Bespoken Spirits Storefront Catalog JSON
  slug: bespoken-spirits-storefront-catalog-json
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://bespokenspirits.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bespokenspirits.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bespoken-spirits-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bespoken-spirits-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bespoken-spirits-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bespoken-spirits-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bespoken-spirits-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bespoken-spirits-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bespoken-spirits-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bespoken-spirits-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bespoken-spirits-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bespoken-spirits-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bespoken-spirits-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bespoken-spirits-agentic-access.yml
- group: build
  title: ''
  type: Examples
  url: examples/bespoken-spirits-products-sample.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bespoken-spirits-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://bespokenspirits.com/blogs/news
- group: company
  title: ''
  type: BlogRSS
  url: https://bespokenspirits.com/blogs/news.atom
- group: operate
  title: ''
  type: Support
  url: https://bespokenspirits.com/pages/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://bespokenspirits.com/collections/all
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bespokenspirits.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bespokenspirits.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://bespokenspirits.com/policies/refund-policy
- group: other
  title: ''
  type: ShippingPolicy
  url: https://bespokenspirits.com/policies/shipping-policy
- group: other
  title: ''
  type: Sitemap
  url: https://bespokenspirits.com/sitemap.xml
- group: company
  title: ''
  type: About
  url: https://bespokenspirits.com/pages/our-story
- group: company
  title: ''
  type: Press
  url: https://bespokenspirits.com/pages/in-the-news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bespoken-spirits-inc
created: '2026-08-07'
description: 'Bespoken Spirits is a Lexington, Kentucky beverage-alcohol technology company that uses a patented, data-driven precision maturation process — micro staves plus machine learning over tasting-panel data — to finish whiskey, bourbon and other spirits in days rather than years, and to produce custom private-label and one-of-one barrel expressions for brands, distillers and retailers. Its public technical surface is not a developer program but an agentic-commerce one: the bespokenspirits.com storefront runs on Shopify and publishes an llms.txt, an agents.md, a Universal Commerce Protocol (UCP) discovery document at /.well-known/ucp, and two anonymous, live MCP endpoints that expose catalog search, cart, checkout and order tools to AI shopping agents.'
examples:
- key_count: 1
  name: Bespoken Spirits Products Sample
  slug: bespoken-spirits-products-sample
image: https://bespokenspirits.com/cdn/shop/files/HERO_IMAGE_0808cb9f-0b04-48f3-851a-6f6bd2307ad4.png?v=1749075439
layout: provider
mcp_servers:
- description: ''
  name: bespoken-spirits-mcp.yml
  slug: bespoken-spirits-mcpyml
modified: '2026-08-07'
name: Bespoken Spirits
nav: Providers
network: true
overview: 'Bespoken Spirits publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Spirits, Beverage Alcohol, Ecommerce, and Agentic Commerce.


  Bespoken Spirits'' developer surface includes documentation, authentication, code examples, engineering blog, support, pricing, and 23 more developer resources.'
random_paper: 2
scopes:
- name: Bespoken Spirits Scopes
  scope_count: 4
  slug: bespoken-spirits-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 24.1
  delta: -0.1
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 1.4
    developer_ergonomics: 35.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.2
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bespoken-spirits/refs/heads/main/screenshots/bespoken-spirits-2026-08-07T162314.png
security:
- kind: authentication
  name: Bespoken Spirits Authentication
  slug: bespoken-spirits-authentication
  summary_line: none/openIdConnect/oauth2 · 4 schemes
- kind: domain-security
  name: Bespoken Spirits Domain Security
  slug: bespoken-spirits-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bespoken-spirits
tags:
- Company
- Spirits
- Beverage Alcohol
- Ecommerce
- Agentic Commerce
- Universal Commerce Protocol
- Model Context Protocol
- Shopify
- Retail
- Manufacturing
website: https://bespokenspirits.com/
---
