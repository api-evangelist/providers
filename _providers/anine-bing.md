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
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.aninebing.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anine-bing-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anine-bing-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/anine-bing-agents.md
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anine-bing-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anine-bing-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/anine-bing-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/anine-bing-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anine-bing-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aninebing.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aninebing.com/policies/terms-of-service
- group: company
  title: ''
  type: Blog
  url: https://www.aninebing.com/blogs/journal
- group: operate
  title: ''
  type: Support
  url: https://www.aninebing.com/pages/contact
created: '2026-07-17'
description: 'Anine Bing is a Los Angeles-based contemporary womenswear and fashion brand selling apparel, denim, footwear, and accessories direct to consumers through its online store at aninebing.com. The storefront runs on Shopify and exposes a modern agent-commerce surface: a published /llms.txt and /agents.md, a Universal Commerce Protocol (ucp.dev) merchant profile at /.well-known/ucp, and a live UCP shopping MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout. Customer authentication is provided by Shopify''s Customer Account API over OpenID Connect. Originally added to the API Evangelist network as a portfolio lead of Index Ventures, this profile has been enriched from the brand''s real public agent, auth, and discovery surfaces.'
image: https://www.aninebing.com/cdn/shop/files/Screen_Shot_2019-11-20_at_9.53.49_AM.png?v=1614725796
layout: provider
mcp_servers:
- description: Live Universal Commerce Protocol (UCP, ucp.dev) shopping MCP endpoint for the Anine Bing Shopify storefront. Enables agent-driven catalog search, cart, and buyer-approved checkout. This is Shopify's n
  name: Anine Bing UCP shopping MCP
  slug: anine-bing-ucp-shopping-mcp
modified: '2026-07-17'
name: Anine Bing
nav: Providers
network: true
overview: 'Anine Bing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Fashion, Apparel, and E-Commerce.


  Anine Bing''s developer surface includes authentication, engineering blog, support, and 10 more developer resources.'
random_paper: 18
scopes:
- name: Anine Bing Scopes
  scope_count: 4
  slug: anine-bing-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.2
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anine-bing/refs/heads/main/screenshots/anine-bing-2026-08-07T161415.png
security:
- kind: authentication
  name: Anine Bing Authentication
  slug: anine-bing-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Anine Bing Domain Security
  slug: anine-bing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anine-bing
tags:
- Company
- Retail
- Fashion
- Apparel
- E-Commerce
- Shopify
- Agent Commerce
- MCP
website: https://www.aninebing.com
---
