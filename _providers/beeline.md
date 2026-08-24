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
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.8
  scored_at: '2026-08-24'
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
random_paper: 10
scopes:
- name: Beeline Scopes
  scope_count: 4
  slug: beeline-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 16.2
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.2
  provenance:
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beeline/refs/heads/main/screenshots/beeline-2026-08-07T162256.png
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
- E-Commerce
website: https://beeline.co
---
