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
    agent_skills: false
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
  score: 20.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Shopify-served Universal Commerce Protocol MCP endpoint for the JOLYN store, enabling buyer-approved agent-driven catalog search, cart, and checkout. Advertised in /.well-known/ucp and documented in /
  name: JOLYN UCP Agent Commerce (Shopify)
  slug: jolyn-ucp-agent-commerce-shopify
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jolynclothing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jolyn.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jolynclothing-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jolynclothing-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jolynclothing-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jolynclothing-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jolynclothing-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jolynclothing-conventions.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jolyn.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jolyn.com/policies/privacy-policy
created: '2026-07-17'
description: 'JOLYN is an athletic swimwear and apparel brand for competitive and team swimming, water polo, and aquatics, known for durable, functional practice and racing suits, team uniforms, and active lifestyle apparel. Surfaced as a portfolio company of Norwest Venture Partners and added to the API Evangelist network, JOLYN publishes no first-party developer API — its direct-to-consumer storefront at jolyn.com (jolynclothing.com redirects here) is Shopify-hosted. That platform exposes a genuine agent-native commerce surface: a published /llms.txt with agent instructions, OpenID Connect discovery for the Shopify Customer Account API, and a live Universal Commerce Protocol (UCP) MCP endpoint for buyer-approved, agent-driven shopping and checkout.'
image: https://cdn.shopify.com/s/files/1/0703/0099/files/JOLYN-LOGO-Black.png?height=628&pad_color=ffffff&v=1708450946&width=1200
layout: provider
mcp_servers:
- description: ''
  name: JOLYN MCP Server
  slug: jolyn-mcp-server
modified: '2026-07-19'
name: JOLYN
nav: Providers
network: true
overview: 'JOLYN publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Apparel, and Swimwear.


  JOLYN''s developer surface includes authentication and 9 more developer resources.'
random_paper: 5
scopes:
- name: Jolynclothing Scopes
  scope_count: 4
  slug: jolynclothing-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.2
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jolynclothing/refs/heads/main/screenshots/jolynclothing-2026-08-07T171017.png
security:
- kind: authentication
  name: Jolynclothing Authentication
  slug: jolynclothing-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Jolynclothing Domain Security
  slug: jolynclothing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jolynclothing
tags:
- Company
- Retail
- E-Commerce
- Apparel
- Swimwear
- Direct to Consumer
- Shopify
- Agentic Commerce
website: https://jolyn.com
---
