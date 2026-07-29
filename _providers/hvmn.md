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
- description: 'Agent-native commerce surface for the Ketone-IQ (HVMN) Shopify store: a Universal Commerce Protocol (UCP) merchant profile and live MCP endpoint for catalog search, cart, and buyer-approved checkout, '
  name: Ketone-IQ Agent Commerce (UCP)
  slug: ketone-iq-agent-commerce-ucp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hvmn-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hvmn-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hvmn-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hvmn-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hvmn-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hvmn-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hvmn-conformance.yml
- group: docs
  title: ''
  type: Documentation
  url: https://ketone.com/agents.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ketone.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ketone.com/policies/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://account.ketone.com
- group: commercial
  title: ''
  type: Pricing
  url: https://ketone.com/collections/all
- group: company
  title: ''
  type: Website
  url: https://ketone.com
created: '2026-07-17'
description: 'HVMN (Health Via Modern Nutrition), now operating as Ketone-IQ, is an a16z-backed human-performance nutrition company founded by Geoffrey Woo and Michael Brandt. It pioneered exogenous ketone products, including the Ketone-IQ drinkable ketone shot and ketone ester, sold direct-to-consumer through its Shopify-powered online store at ketone.com (hvmn.com now redirects to ketone.com). The storefront is agent-native: it publishes /llms.txt and /agents.md agent instructions and implements the Universal Commerce Protocol (UCP) with a live MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout, backed by Shopify Customer Account OAuth 2.0 / OpenID Connect authentication.'
image: https://ketone.com/cdn/shop/files/OG_Home_Page_1200x1200.jpg?v=1781009088
layout: provider
mcp_servers:
- description: ''
  name: hvmn-mcp.yml
  slug: hvmn-mcpyml
modified: '2026-07-19'
name: HVMN
nav: Providers
network: true
overview: 'HVMN publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Nutrition, Ketones, and Supplements.


  HVMN''s developer surface includes authentication, documentation, pricing, and 10 more developer resources.'
random_paper: 41
scopes:
- name: Hvmn Scopes
  scope_count: 4
  slug: hvmn-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 28.0
  delta: -3.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 31.7
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Hvmn Authentication
  slug: hvmn-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Hvmn Domain Security
  slug: hvmn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hvmn
tags:
- Company
- Health
- Nutrition
- Ketones
- Supplements
- E-Commerce
- Shopify
- Agentic Commerce
- Consumer
- MCP
website: https://ketone.com
---
