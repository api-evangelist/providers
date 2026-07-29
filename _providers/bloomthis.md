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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Agent-facing commerce surface of the BloomThis Shopify store — a hosted UCP MCP endpoint for search-to-buyer-approved-checkout, the Shopify Customer Account OIDC/OAuth API, and the read-only storefron
  name: BloomThis Agent Commerce (UCP / Storefront)
  slug: bloomthis-agent-commerce-ucp-storefront
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://bloomthis.co
- group: company
  title: ''
  type: Blog
  url: https://bloomthis.co/blogs/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bloomthis.co/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bloomthis.co/policies/terms-of-service
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bloomthis-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bloomthis-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bloomthis-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bloomthis-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bloomthis-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bloomthis-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bloomthis-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomthis-domain-security.yml
created: '2026-07-17'
description: 'BloomThis is a Malaysian online florist and gifting brand (backed by 500 Global) offering fresh flower boxes, hand-tied bouquets, and weekly fresh-flower subscriptions, with a free personalised card and photo on every order and free same-day delivery across Kuala Lumpur, Selangor, Kedah, Penang, Negeri Sembilan, and Johor Bahru. Its Shopify storefront natively exposes an agent-commerce surface via the Universal Commerce Protocol (UCP): a hosted MCP endpoint at /api/ucp/mcp, an OpenID Connect / OAuth Customer Account API, and published /llms.txt and /agents.md instructions that let AI shopping agents search the catalog, build a cart, and run a buyer-approved checkout.'
image: https://bloomthis.co/cdn/shop/files/bloomthis-home-desktop_72fd684e-14fb-4cff-a9ac-c10a9e971094.jpg?v=1781515992&width=2048
layout: provider
mcp_servers:
- description: ''
  name: bloomthis-mcp.yml
  slug: bloomthis-mcpyml
modified: '2026-07-18'
name: BloomThis
nav: Providers
network: true
overview: 'BloomThis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Flowers, Gifting, Ecommerce, and Retail.


  BloomThis'' developer surface includes engineering blog, authentication, and 11 more developer resources.'
random_paper: 17
scopes:
- name: Bloomthis Scopes
  scope_count: 4
  slug: bloomthis-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 19.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 23.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 19.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Bloomthis Authentication
  slug: bloomthis-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Bloomthis Domain Security
  slug: bloomthis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomthis
tags:
- Company
- Flowers
- Gifting
- Ecommerce
- Retail
- Shopify
- Agent Commerce
- MCP
- Malaysia
website: https://bloomthis.co
---
