---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 14.4
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://august.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.august.com/
- group: operate
  title: ''
  type: Support
  url: https://support.august.com/
- group: company
  title: ''
  type: Blog
  url: https://august.com/blogs/home
- group: commercial
  title: ''
  type: Pricing
  url: https://august.com/pages/shop-all-products
- group: start
  title: ''
  type: SignUp
  url: https://august.com/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://august.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://august.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/august-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/august-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/august-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/august-domain-security.yml
created: '2026-07-17'
description: 'August (August Home) makes Wi-Fi smart locks, keypads, doorbell cameras, and the August Connect bridge for keyless, app-controlled home entry. Founded in San Francisco and originally backed by Bessemer Venture Partners and Uncork Capital, August was acquired by Assa Abloy and its product line is now unified with Yale Home; the two brands share the August mobile app. August does not publish a public device-control API for consumers — third-party integrations rely on community-reverse-engineered endpoints or aggregators such as Seam, and Yale/August partners use the developer.august.com portal. Its august.com storefront (hosted on Shopify) does, however, expose an agent-native commerce surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp and a hosted shopping MCP server at /api/ucp/mcp for buy-for-me agents, alongside Shopify customer-account OpenID Connect discovery.'
image: https://cdn.shopify.com/s/files/1/1354/7835/files/logoPng_10b2d83e-77e1-430a-8017-b882b2502d80.png?width=1200
layout: provider
mcp_servers:
- description: ''
  name: August Home UCP shopping MCP
  slug: august-home-ucp-shopping-mcp
modified: '2026-07-18'
name: August
nav: Providers
network: true
overview: 'August is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Smart Home, Smart Lock, and IoT.


  August''s developer surface includes support, engineering blog, pricing, signup flow, and 8 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 20.6
  delta: 0.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.5
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/august/refs/heads/main/screenshots/august-2026-07-25T201715.png
security:
- kind: domain-security
  name: August Domain Security
  slug: august-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: august
tags:
- Company
- Consumer
- Smart Home
- Smart Lock
- IoT
- Home Security
- Access Control
- Agentic Commerce
- MCP
website: https://august.com
---
