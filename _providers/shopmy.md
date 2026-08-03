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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Shopmy Agentic Access
  operation_count: 10
  slug: shopmy-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 6
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
artifact_total: 11
common:
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
  name: shopmy-mcp.yml
  slug: shopmy-mcpyml
modified: '2026-07-21'
name: ShopMy
nav: Providers
network: true
overview: 'ShopMy publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Collections API, Links API, and 3 more. Tagged areas include Company, Commerce, Creator Economy, Creator Commerce, and Affiliate Marketing.


  ShopMy''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, engineering blog, signup flow, and 16 more developer resources.'
random_paper: 7
scopes:
- name: Shopmy Scopes
  scope_count: 5
  slug: shopmy-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 46.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 65.1
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
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
