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
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://tincan.kids/
- group: operate
  title: ''
  type: Support
  url: https://faq.tincan.com/
- group: company
  title: ''
  type: Blog
  url: https://tincan.kids/blogs/news
- group: start
  title: ''
  type: Login
  url: https://tincan.kids/account/login
- group: commercial
  title: ''
  type: Pricing
  url: https://tincan.kids/products/tin-can
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tincan.kids/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tincan.kids/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tin-can-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tin-can-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tin-can-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tin-can-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tin-can-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tin-can-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tin-can-domain-security.yml
created: '2026-07-17'
description: Tin Can is a Seattle-based consumer hardware company behind a screen-free, landline-style Wi-Fi phone for kids — no apps, texting, or games, just voice calls with contacts that parents approve through a companion mobile app, with free unlimited calling between Tin Can devices. Backed by Greylock (which led a $12M round in 2025, bringing total funding to roughly $15.5M). Tin Can publishes no first-party developer API; its agent-facing surface is the Shopify-hosted storefront, which exposes a live MCP server, a UCP merchant profile, an llms.txt, and Shopify Customer Accounts OIDC on the tincan.kids domain.
image: https://tincan.kids/cdn/shop/files/tinothy-icon.svg
layout: provider
mcp_servers:
- description: ''
  name: tin-can-mcp.yml
  slug: tin-can-mcpyml
modified: '2026-07-21'
name: Tin Can
nav: Providers
network: true
overview: 'Tin Can is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Hardware, Telecommunications, and Voice.


  Tin Can''s developer surface includes support, engineering blog, pricing, authentication, and 10 more developer resources.'
random_paper: 4
scopes:
- name: Tin Can Scopes
  scope_count: 4
  slug: tin-can-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 27.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 27.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Tin Can Authentication
  slug: tin-can-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Tin Can Domain Security
  slug: tin-can-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tin-can
tags:
- Company
- Consumer
- Hardware
- Telecommunications
- Voice
- Kids
- Phones
website: https://tincan.kids/
---
