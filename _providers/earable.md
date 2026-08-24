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
  url: https://frenzband.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shopify.dev
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://frenzband.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://frenzband.com/policies/terms-of-service
- group: company
  title: ''
  type: Blog
  url: https://frenzband.com/pages/blogs
- group: start
  title: ''
  type: GettingStarted
  url: https://frenzband.com/pages/how-it-works
- group: start
  title: ''
  type: SignUp
  url: https://account.frenzband.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/earable-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/earable-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/earable-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/earable-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/earable-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/earable-domain-security.yml
created: '2026-07-17'
description: 'Earable Neuroscience is the maker of FRENZ Brainband, marketed as the world''s first AI sleep-tech wearable that tracks and stimulates brain activity through bone-conduction speakers to promote better sleep. The company''s public surface is the frenzband.com direct-to-consumer storefront, built on Shopify. It has no first-party developer API; its machine-readable surface is entirely Shopify-platform provided: an OIDC/OAuth2 Customer Account API advertised at /.well-known/openid-configuration (account.frenzband.com), a Universal Commerce Protocol (UCP) profile at /.well-known/ucp, published agent instructions at /llms.txt, and a hosted agent-commerce MCP endpoint for buyer-approved checkout. Added to the API Evangelist network as a 500 Global portfolio lead and enriched from its live public storefront surface.'
image: https://frenzband.com/cdn/shop/t/64/assets/webclip.png
layout: provider
mcp_servers:
- description: ''
  name: Earable MCP Server
  slug: earable-mcp-server
modified: '2026-07-18'
name: Earable
nav: Providers
network: true
overview: 'Earable is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wearables, Sleep Technology, Neuroscience, and Health.


  Earable''s developer surface includes engineering blog, getting-started guide, signup flow, authentication, and 9 more developer resources.'
random_paper: 2
scopes:
- name: Earable Scopes
  scope_count: 4
  slug: earable-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 25.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 46.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/earable/refs/heads/main/screenshots/earable-2026-07-25T212636.png
security:
- kind: authentication
  name: Earable Authentication
  slug: earable-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Earable Domain Security
  slug: earable-domain-security
  summary_line: TLSv1.3 · HSTS
slug: earable
tags:
- Company
- Wearables
- Sleep Technology
- Neuroscience
- Health
- Consumer Electronics
- Agentic Commerce
- Shopify
website: https://frenzband.com
---
