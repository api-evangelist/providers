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
  url: https://beeline.co
- group: company
  title: ''
  type: Blog
  url: https://beeline.co/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://beeline.co/pages/contact
- group: start
  title: ''
  type: Login
  url: https://beeline.co/account
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beeline.co/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beeline.co/policies/terms-of-service
- group: agent
  title: ''
  type: MCPServer
  url: mcp/beeline-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beeline-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beeline-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/beeline-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/beeline-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beeline-domain-security.yml
created: '2026-07-17'
description: Beeline makes smart navigation devices and a companion mobile app for cyclists and motorcyclists. Its compact handlebar-mounted devices — Beeline Velo for bicycles and Beeline Moto for motorcycles — use a simple directional and turn-by-turn interface to help riders find their way around towns and cities, discover better routes, and record their journeys. The London-based company is backed by Seedcamp. Beeline sells direct to consumers through a Shopify-hosted storefront at beeline.co, which exposes an agent-facing commerce surface — a Universal Commerce Protocol (UCP) MCP endpoint, Shopify customer-account OIDC, and an llms.txt agent policy — rather than a first-party developer product API.
image: https://beeline.co/cdn/shop/files/Beeline_logo_favicon.png?v=1748928074&width=180
layout: provider
mcp_servers:
- description: ''
  name: Beeline UCP shopping MCP (Shopify storefront)
  slug: beeline-ucp-shopping-mcp-shopify-storefront
modified: '2026-07-18'
name: Beeline
nav: Providers
network: true
overview: 'Beeline is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Navigation, Cycling, Motorcycle, and Hardware.


  Beeline''s developer surface includes engineering blog, support, authentication, and 9 more developer resources.'
random_paper: 4
scopes:
- name: Beeline Scopes
  scope_count: 4
  slug: beeline-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.9
  delta: 0.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.8
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Beeline Authentication
  slug: beeline-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Beeline Domain Security
  slug: beeline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beeline
tags:
- Company
- Navigation
- Cycling
- Motorcycle
- Hardware
- GPS
- Location
- Maps
- Mobile App
- Consumer Electronics
- Ecommerce
website: https://beeline.co
---
