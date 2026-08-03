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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coravin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coravin.com/
- group: operate
  title: ''
  type: Support
  url: https://www.coravin.com/pages/support-product
- group: company
  title: ''
  type: Blog
  url: https://www.coravin.com/blogs/community
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coravin.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coravin.com/policies/terms-of-service
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coravin-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coravin-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coravin-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coravin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coravin-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coravin-conformance.yml
created: '2026-07-17'
description: Coravin is a consumer beverage-technology company best known for its wine preservation systems, which use a thin needle and inert argon gas to pour wine by the glass without pulling the cork, leaving the remaining wine unoxidized for weeks or months. Its product line spans the Timeless, Pivot, and Sparkling systems plus Pure argon capsules, sold direct-to-consumer and through retail and trade channels. Coravin does not operate a standalone public developer API; its direct storefront runs on Shopify, which exposes a real agent-native commerce surface — a Universal Commerce Protocol (UCP) merchant profile, a hosted shopping MCP endpoint, and OIDC / OAuth 2.0 authorization-server metadata for Shopify Customer Accounts. Backed by Battery Ventures.
image: https://www.coravin.com/cdn/shop/files/hero-sg-black.png?v=1746714317
layout: provider
mcp_servers:
- description: ''
  name: coravin-mcp.yml
  slug: coravin-mcpyml
modified: '2026-07-18'
name: Coravin
nav: Providers
network: true
overview: 'Coravin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wine, Beverage, Consumer Products, and Ecommerce.


  Coravin''s developer surface includes support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 89
scopes:
- name: Coravin Scopes
  scope_count: 4
  slug: coravin-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 17.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 17.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Coravin Authentication
  slug: coravin-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Coravin Domain Security
  slug: coravin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coravin
tags:
- Company
- Wine
- Beverage
- Consumer Products
- Ecommerce
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- Wine Preservation
website: https://www.coravin.com/
---
