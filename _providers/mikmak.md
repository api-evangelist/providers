---
access_model:
  confidence: high
  label: Contract Only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.mikmak.com/pricing (404)
  - https://docs.mikmak.ai/reference/mikmak-headless-commerce-api
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-30'
api_count: 4
apis:
- description: MikMak Aura provides real-time intelligence, fueled by AI, to connect marketing spend across channels to actual sales performance at retailers.
  name: MikMak Aura
  slug: mikmak-aura
- description: The MikMak Commerce MCP Server is a hosted Model Context Protocol surface in front of the Headless Commerce API (v1). It exposes three strictly-typed, read-only, non-destructive tools — search_product
  name: MikMak Commerce MCP Server
  slug: mikmak-commerce-mcp
- description: The MikMak where-to-buy tag is the client-side distribution of MikMak Commerce for brand-owned websites. A single async script loaded from wtb-tag.mikmak.ai renders buy-now buttons, in-page containers
  name: MikMak Commerce for Brand.com (WTB Tag)
  slug: mikmak-brand-com-tag
- description: The Authentication API from MikMak — 1 operation(s) for authentication.
  name: MikMak Authentication API
  slug: mikmak-authentication-api
- description: The Availabilities API from MikMak — 1 operation(s) for availabilities.
  name: MikMak Availabilities API
  slug: mikmak-availabilities-api
- description: The Cart API from MikMak — 1 operation(s) for cart.
  name: MikMak Cart API
  slug: mikmak-cart-api
- description: The Custom Reports API from MikMak — 6 operation(s) for custom reports.
  name: MikMak Custom Reports API
  slug: mikmak-custom-reports-api
- description: The Experiences API from MikMak — 2 operation(s) for experiences.
  name: MikMak Experiences API
  slug: mikmak-experiences-api
- description: The Facet API from MikMak — 1 operation(s) for facet.
  name: MikMak Facet API
  slug: mikmak-facet-api
- description: The Historical Pricing Reports API from MikMak — 4 operation(s) for historical pricing reports.
  name: MikMak Historical Pricing Reports API
  slug: mikmak-historical-pricing-reports-api
- description: The Offers API from MikMak — 1 operation(s) for offers.
  name: MikMak Offers API
  slug: mikmak-offers-api
- description: The Product API from MikMak — 1 operation(s) for product.
  name: MikMak Product API
  slug: mikmak-product-api
- description: The Product Search API from MikMak — 1 operation(s) for product search.
  name: MikMak Product Search API
  slug: mikmak-product-search-api
- description: The Shoppable Recipe Reports API from MikMak — 4 operation(s) for shoppable recipe reports.
  name: MikMak Shoppable Recipe Reports API
  slug: mikmak-shoppable-recipe-reports-api
artifact_total: 25
collections:
- collection_type: open
  name: Commerce API (v1)
  slug: open-mikmak-commerce-api
- collection_type: open
  name: MikMak Insights API
  slug: open-mikmak-insights-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mikmak.ai/docs/developer-portal
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mikmak.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mikmak.ai/reference/mikmak-headless-commerce-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mikmak.ai/docs/quick-start-1
- group: operate
  title: ''
  type: Support
  url: https://docs.mikmak.ai/page/support
- group: operate
  title: ''
  type: Help Center
  url: https://help.mikmak.ai/hc
- group: company
  title: ''
  type: Blog
  url: https://www.mikmak.com/blog
- group: company
  title: ''
  type: Website
  url: https://www.mikmak.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mikmak-tv
- group: operate
  title: ''
  type: Contact
  url: https://www.mikmak.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mikmak.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mikmak.com/legal/privacypolicy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mikmak.com/product-updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mikmak-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mikmak-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.mikmak.ai/llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mikmak-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mikmak-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mikmak-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mikmak-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mikmak-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mikmak-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/mikmak-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mikmak-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mikmak-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mikmak-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mikmak-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/mikmak-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/mikmak-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mikmak-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Login
  url: https://platform.mikmak.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Swaven
- group: operate
  title: ''
  type: SLA
  url: https://www.mikmak.com/legal/sla
- group: other
  title: ''
  type: Subprocessors
  url: https://www.mikmak.com/legal/subprocessors
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mikmak-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mikmak-commerce-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mikmak-insights-api-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/mikmak-commerce-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/mikmak-insights-api-openapi.yml
created: '2025-02-21'
description: MikMak is an eCommerce enablement and analytics platform for multichannel brands, converting shoppers across social media, retail media, brand-owned websites, search, CTV, display and QR codes. The platform pairs a Headless Commerce API — product lookup, retailer availability, offers, carts and experience configuration across a global retailer network — with the MikMak Insights reporting API that pushes purchase-intent and attributable-sales data into data lakes and BI tools, and a hosted Model Context Protocol server that exposes the same commerce surface to AI agents. MikMak acquired the French shoppable-media company Swaven in 2021, whose where-to-buy tag technology still powers the brand.com widget and whose name persists in the platform's asset hosts.
finops:
- name: Mikmak Finops
  service_category: API
  slug: mikmak-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mikmak.png
layout: provider
mcp_servers:
- description: ''
  name: MikMak Commerce MCP Server
  slug: mikmak-commerce-mcp-server
- description: ''
  name: MikMak MCP Server
  slug: mikmak-mcp-server
modified: '2026-08-12'
name: MikMak
nav: Providers
network: true
overview: 'MikMak publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Availabilities API, Cart API, and 8 more. Tagged areas include Analytics, Commerce, E-Commerce, Multichannel, and Retail Media.


  MikMak''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 33 more developer resources.'
plans:
- name: Mikmak Plans Pricing
  plan_count: 0
  slug: mikmak-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Mikmak Rate Limits
  slug: mikmak-rate-limits
scopes:
- name: Mikmak Scopes
  scope_count: 0
  slug: mikmak-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 23
    catalog_gap: 65.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 4.5
    contract_quality: 54.5
    developer_ergonomics: 41.1
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 46.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mikmak/refs/heads/main/screenshots/mikmak-2026-06-20T185553.png
security:
- kind: authentication
  name: Mikmak Authentication
  slug: mikmak-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Mikmak Domain Security
  slug: mikmak-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mikmak Trust Center
  slug: mikmak-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: mikmak
tags:
- Analytics
- Commerce
- E-Commerce
- Multichannel
- Retail Media
- Where to Buy
- Shoppable Media
- Product Availability
- MCP
- Agent Native
- Reporting
- CPG
website: https://www.mikmak.com
---
