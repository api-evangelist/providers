---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Price Lab Agentic Access
  operation_count: 35
  slug: price-lab-agentic-access
  summary_line: 35 operations · 20 acting
api_count: 9
apis:
- description: The Authentication API from Price Lab — 2 operation(s) for authentication.
  name: Price Lab Authentication API
  slug: price-lab-authentication-api
- description: The Categories API from Price Lab — 2 operation(s) for categories.
  name: Price Lab Categories API
  slug: price-lab-categories-api
- description: The Competitor Pricing API from Price Lab — 4 operation(s) for competitor pricing.
  name: Price Lab Competitor Pricing API
  slug: price-lab-competitor-pricing-api
- description: The Data Import API from Price Lab — 1 operation(s) for data import.
  name: Price Lab Data Import API
  slug: price-lab-data-import-api
- description: The Electronic Price Tags API from Price Lab — 6 operation(s) for electronic price tags.
  name: Price Lab Electronic Price Tags API
  slug: price-lab-electronic-price-tags-api
- description: The Price Management API from Price Lab — 5 operation(s) for price management.
  name: Price Lab Price Management API
  slug: price-lab-price-management-api
- description: The Products API from Price Lab — 6 operation(s) for products.
  name: Price Lab Products API
  slug: price-lab-products-api
- description: The Recommendations API from Price Lab — 3 operation(s) for recommendations.
  name: Price Lab Recommendations API
  slug: price-lab-recommendations-api
- description: The Users API from Price Lab — 1 operation(s) for users.
  name: Price Lab Users API
  slug: price-lab-users-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Price Lab Authentication API
  slug: open-price-lab-authentication-api
- collection_type: open
  name: Price Lab Authentication Categories API
  slug: open-price-lab-categories-api
- collection_type: open
  name: Price Lab Authentication Competitor Pricing API
  slug: open-price-lab-competitor-pricing-api
- collection_type: open
  name: Price Lab Authentication Data Import API
  slug: open-price-lab-data-import-api
- collection_type: open
  name: Price Lab Authentication Electronic Price Tags API
  slug: open-price-lab-electronic-price-tags-api
- collection_type: open
  name: Price Lab Authentication Price Management API
  slug: open-price-lab-price-management-api
- collection_type: open
  name: Price Lab Authentication Products API
  slug: open-price-lab-products-api
- collection_type: open
  name: Price Lab Authentication Recommendations API
  slug: open-price-lab-recommendations-api
- collection_type: open
  name: Price Lab Authentication Users API
  slug: open-price-lab-users-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/price-lab-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/price-lab-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/price-lab-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://pricelabsolutions.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://price-lab.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://price-lab.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://price-lab.readme.io/reference
- group: company
  title: ''
  type: Blog
  url: https://pricelabsolutions.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://pricelabsolutions.com/soporte-tecnico/
- group: start
  title: ''
  type: SignUp
  url: https://pricelabsolutions.com/#contactHome
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pricelabsolutions.com/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pricelabsolutions.com/politica-privacidad/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/price-lab-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/price-lab-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/price-lab-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/price-lab-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/price-lab-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/price-lab-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/price-lab-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/price-lab-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/price-lab-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Price Lab (Price Lab Solutions) is a Latin American retail pricing intelligence platform that helps retailers and e-commerce merchants monitor competitor prices, analyze pricing KPIs, and apply AI-driven price optimization across their catalog and store network. The platform pairs competitor price scraping and competitive pricing policies with a recommendation engine, bulk data ingestion (sales, stock, replenishment, offers, and competitor prices), and electronic shelf label (ESL) management with flash strategies. Its production REST API, documented at price-lab.readme.io and hosted at backend.pricelab.com.pe, exposes product and category master data, batch price and cost updates, competitor price exports, recommendation accept/reject flows, and store-level price management, all secured with JWT bearer authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/price-lab.png
layout: provider
mcp_servers:
- description: ''
  name: Price Lab MCP Server
  slug: price-lab-mcp-server
modified: '2026-07-20'
name: Price Lab
nav: Providers
network: true
overview: 'Price Lab publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Categories API, Competitor Pricing API, and 6 more. Tagged areas include Company, Pricing, Retail, E-Commerce, and Competitive Intelligence.


  Price Lab''s developer surface includes authentication, documentation, API reference, engineering blog, support, signup flow, and 16 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 37.0
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 53.1
    developer_ergonomics: 33.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Price Lab Authentication
  slug: price-lab-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Price Lab Domain Security
  slug: price-lab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: price-lab
tags:
- Company
- Pricing
- Retail
- E-Commerce
- Competitive Intelligence
- Price Optimization
- Artificial Intelligence
- Electronic Shelf Labels
- Latin America
website: https://pricelabsolutions.com
---
