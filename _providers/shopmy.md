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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Shopmy Agentic Access
  operation_count: 10
  slug: shopmy-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- description: Search the ShopMy catalog and resolve/rate product URLs (OAuth).
  name: ShopMy Catalog API
  slug: shopmy-catalog-api
- description: Create, edit and fetch a user's ShopMy shelf collections (OAuth).
  name: ShopMy Collections API
  slug: shopmy-collections-api
- description: Create and fetch a user's ShopMy product links (OAuth).
  name: ShopMy Links API
  slug: shopmy-links-api
- description: OAuth token exchange for developer applications.
  name: ShopMy OAuth API
  slug: shopmy-oauth-api
- description: Brand Partner affiliate order reports (developer-key auth).
  name: ShopMy Order Reporting API
  slug: shopmy-order-reporting-api
- description: Read the authenticated user's public ShopMy profile (OAuth).
  name: ShopMy Profile API
  slug: shopmy-profile-api
- description: Server-to-server affiliate tracking routes a brand calls to report completed orders to ShopMy for creator commission attribution, and to keep those commissions accurate through returns, edits and canc
  name: ShopMy Tracking API
  slug: shopmy-tracking-api
artifact_total: 22
asyncapis:
- description: ''
  name: Shopmy Tracking Events
  slug: shopmy-tracking-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ShopMy Partners Catalog API
  slug: open-shopmy-catalog-api
- collection_type: open
  name: ShopMy Partners Catalog Collections API
  slug: open-shopmy-collections-api
- collection_type: open
  name: ShopMy Partners Catalog Links API
  slug: open-shopmy-links-api
- collection_type: open
  name: ShopMy Partners Catalog OAuth API
  slug: open-shopmy-oauth-api
- collection_type: open
  name: ShopMy Partners Catalog Order Reporting API
  slug: open-shopmy-order-reporting-api
- collection_type: open
  name: ShopMy Partners Catalog Profile API
  slug: open-shopmy-profile-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/shopmy-partners-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.shopmy.us/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shopmy.us/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shopmy.us/reference/getting-started-with-your-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shopmy.us/reference/getting-started-with-your-api
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopmy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shopmy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shopmy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shopmy-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/shopmy-outcome-codes.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/shopmy-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shopmy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/shopmy-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/shopmy-packages.yml
- group: other
  title: ''
  type: EventCatalog
  url: asyncapi/shopmy-tracking-events.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.shopmy.us/reference/privacy-and-data-handling
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shopmy-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shopmy-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shopmy-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shopmy-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shopmy-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shopmy-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shopmy-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopmy-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://shopmy.us/blog
- group: start
  title: ''
  type: SignUp
  url: https://shopmy.us/signup
- group: operate
  title: ''
  type: Support
  url: https://shopmy.us/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shopmy.us/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shopmy.us/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://shopmy.us/home
created: '2026-07-17'
description: ShopMy is a creator-commerce and influencer-marketing platform connecting top brands with content creators across beauty, fashion, and lifestyle. Creators build curated digital shops and earn performance commissions (typically 10-30%) plus paid brand partnerships, while brands run affiliate programs, product gifting (Lookbooks), and performance budgets (Opportunities). The ShopMy Partners API lets Brand Partners pull detailed affiliate order reports, and lets OAuth developer applications create and read product links, manage shelf collections, resolve and rate product URLs, search the catalog, and read public profile information on behalf of authenticated ShopMy users. Backed by Bain Capital Ventures, Bessemer Venture Partners, and Menlo Ventures.
image: https://shopmy.us/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: ShopMy MCP Server
  slug: shopmy-mcp-server
modified: '2026-08-13'
name: ShopMy
nav: Providers
network: true
overview: 'ShopMy publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Collections API, Links API, and 3 more. Tagged areas include Company, Commerce, Creator Economy, Creator Commerce, and Affiliate Marketing.


  The ShopMy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ShopMy''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, engineering blog, signup flow, and 24 more developer resources.'
plans:
- name: Shopmy Plans Pricing
  plan_count: 0
  slug: shopmy-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Shopmy Rate Limits
  slug: shopmy-rate-limits
scopes:
- name: Shopmy Scopes
  scope_count: 5
  slug: shopmy-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 24
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 65.3
    developer_ergonomics: 38.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shopmy/refs/heads/main/screenshots/shopmy-2026-08-17T081840.png
security:
- kind: authentication
  name: Shopmy Authentication
  slug: shopmy-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Shopmy Domain Security
  slug: shopmy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shopmy
tags:
- Company
- Commerce
- Creator Economy
- Creator Commerce
- Affiliate Marketing
- Influencer Marketing
- E-Commerce
- Retail
website: https://shopmy.us/home
---
