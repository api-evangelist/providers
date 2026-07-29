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
  score: 23.4
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.baublebar.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/baublebar-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/baublebar-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/baublebar-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/baublebar-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/baublebar-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/baublebar-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://www.baublebar.com/pages/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.baublebar.com/account/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.baublebar.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.baublebar.com/policies/terms-of-service
created: '2026-07-17'
description: 'BaubleBar is a direct-to-consumer fashion jewelry and accessories brand founded in 2011 and headquartered in New York City, selling affordable, trend-driven earrings, necklaces, bracelets, rings, hair accessories, personalized "Design Your Own" pieces, and home and gift items through its own e-commerce storefront and wholesale partners. The baublebar.com storefront runs on Shopify: it exposes a live Shopify Storefront MCP server for agent-driven catalog search and cart operations, and authenticates shoppers through Shopify''s Customer Account API using OpenID Connect / OAuth 2.0 with PKCE. BaubleBar is backed by Accel and was added to the API Evangelist network from that portfolio.'
image: https://www.baublebar.com/cdn/shop/files/BB_Logo_stacked.jpg
layout: provider
mcp_servers:
- description: ''
  name: BaubleBar Storefront MCP
  slug: baublebar-storefront-mcp
modified: '2026-07-18'
name: BaubleBar
nav: Providers
network: true
overview: 'BaubleBar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Retail, E-commerce, and Jewelry.


  BaubleBar''s developer surface includes authentication, support, signup flow, and 8 more developer resources.'
random_paper: 48
scopes:
- name: Baublebar Scopes
  scope_count: 4
  slug: baublebar-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 19.2
  delta: 0.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 61.1
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 18.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Baublebar Authentication
  slug: baublebar-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Baublebar Domain Security
  slug: baublebar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: baublebar
tags:
- Company
- Consumer
- Retail
- E-commerce
- Jewelry
- Accessories
- Fashion
- Shopify
- MCP
website: https://www.baublebar.com
---
