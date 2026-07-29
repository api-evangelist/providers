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
api_count: 1
apis:
- description: 'Flaviar''s Shopify storefront exposes an agent-driven commerce surface built on the Universal Commerce Protocol (ucp.dev): a discovery document at /.well-known/ucp and a hosted MCP endpoint for catalog'
  name: Flaviar Agent Commerce (UCP + MCP)
  slug: flaviar-agent-commerce-ucp-mcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flaviar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flaviar.com
- group: docs
  title: ''
  type: Documentation
  url: https://flaviar.com/llms.txt
- group: start
  title: ''
  type: SignUp
  url: https://flaviar.com/account/login
- group: start
  title: ''
  type: Login
  url: https://flaviar.com/account/login
- group: commercial
  title: ''
  type: Pricing
  url: https://flaviar.com/pages/flaviar-black-membership
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flaviar.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flaviar.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://flaviar.com/policies/refund-policy
- group: other
  title: ''
  type: ShippingPolicy
  url: https://flaviar.com/policies/shipping-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flaviar-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flaviar-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flaviar-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flaviar-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flaviar-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flaviar-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flaviar-conformance.yml
created: '2026-07-17'
description: 'Flaviar is an online spirits retailer and members club for whiskey, tequila, rum, gin and other premium spirits, offering curated tasting boxes, full-size bottles, and a subscription membership. Its direct-to-consumer storefront runs on Shopify and exposes a modern agent-commerce surface: a Universal Commerce Protocol (UCP) merchant profile and hosted MCP shopping endpoint, an llms.txt / agents.md agent-instruction document, and Shopify Customer Account authentication via OAuth 2.0 + OpenID Connect. This profile was added to the API Evangelist network as a portfolio lead and enriched from Flaviar''s live public discovery documents.'
image: https://flaviar.com/cdn/shop/files/image_29.png?v=1694778656
layout: provider
mcp_servers:
- description: ''
  name: flaviar-mcp.yml
  slug: flaviar-mcpyml
modified: '2026-07-19'
name: Flaviar
nav: Providers
network: true
overview: 'Flaviar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Spirits, Whiskey, Ecommerce, and Retail.


  Flaviar''s developer surface includes documentation, signup flow, pricing, authentication, and 13 more developer resources.'
random_paper: 12
scopes:
- name: Flaviar Scopes
  scope_count: 4
  slug: flaviar-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 24.8
  delta: 0.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 23.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Flaviar Authentication
  slug: flaviar-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Flaviar Domain Security
  slug: flaviar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flaviar
tags:
- Company
- Spirits
- Whiskey
- Ecommerce
- Retail
- Beverages
- Subscription
- Agent Commerce
- Shopify
website: https://flaviar.com
---
