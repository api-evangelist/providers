---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: 'Maisonette''s agent-facing commerce surface: a Universal Commerce Protocol (2026-04-08) MCP server exposing thirteen tools across catalog search and lookup, cart, checkout and order. tools/list answers'
  name: Maisonette UCP Commerce MCP
  slug: maisonette-ucp-commerce-mcp
- description: The lighter read-and-cart Shopify Storefront MCP surface on Maisonette's own host — five anonymous tools covering catalog search, product detail, cart read and update, and a grounded search over the s
  name: Maisonette Storefront MCP
  slug: maisonette-storefront-mcp
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.maisonette.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.maisonette.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/maisonette-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/maisonette-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/maisonette-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maisonette-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/maisonette-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/maisonette-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/maisonette-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/maisonette-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/maisonette-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/maisonette-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/maisonette-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/maisonette-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/maisonette-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/maisonette-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maisonette-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://www.maisonette.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.maisonette.com/pages/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.maisonette.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.maisonette.com/policies/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.maisonette.com/account/register
created: '2026-08-25'
description: 'Maisonette is a New York-based online marketplace for babies and children, founded in 2017 by Sylvana Ward Durrett and Luisana Mendoza de Roccia, selling clothing, toys, furniture and decor for ages 0-12 from a curated network of independent boutiques and 800+ brands. It is a marketplace rather than a single seller: each item ships directly from its brand and is returned separately. Maisonette publishes no OpenAPI and runs no developer program, but its Shopify-hosted storefront exposes a real, live, unauthenticated agent surface — a Universal Commerce Protocol MCP endpoint with thirteen catalog, cart, checkout and order tools, a five-tool storefront MCP endpoint, an llms.txt and agents.md with explicit agent instructions, an agent-discovery sitemap, and OAuth 2.0/OIDC and RFC 9728 discovery documents served from its own host.'
image: https://www.maisonette.com/cdn/shop/files/Favicon_Maisonette_ac4c0de7-1fd8-4114-b034-f15a8d57ac59.png?v=1776358749&width=512
layout: provider
mcp_servers:
- description: ''
  name: Maisonette MCP Server
  slug: maisonette-mcp-server
modified: '2026-08-25'
name: Maisonette
nav: Providers
network: true
overview: 'Maisonette publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Marketplace, and Shopping.


  Maisonette''s developer surface includes documentation, authentication, support, signup flow, and 19 more developer resources.'
plans:
- name: Maisonette Plans Pricing
  plan_count: 0
  slug: maisonette-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Maisonette Rate Limits
  slug: maisonette-rate-limits
scopes:
- name: Maisonette Scopes
  scope_count: 0
  slug: maisonette-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 22.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maisonette/refs/heads/main/screenshots/maisonette-2026-09-02T150417.png
security:
- kind: authentication
  name: Maisonette Authentication
  slug: maisonette-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Maisonette Domain Security
  slug: maisonette-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: maisonette
tags:
- Company
- Retail
- E-Commerce
- Marketplace
- Shopping
- Children
- Baby
- Apparel
- Homes
- Agentic Commerce
- MCP
- Universal Commerce Protocol
- Shopify
website: https://www.maisonette.com/
---
