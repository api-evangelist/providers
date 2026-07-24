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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 15.4
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Agentic-commerce surface for Brava's Shopify storefront. The store publishes a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp and a native Model Context Protocol (MCP) endpoint
  name: Brava Storefront Commerce (UCP / MCP)
  slug: brava-storefront-commerce-ucp-mcp
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.brava.com
- group: commercial
  title: ''
  type: Pricing
  url: https://shop.brava.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.brava.com/
- group: operate
  title: ''
  type: Support
  url: https://support.brava.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://shop.brava.com/account/register
- group: start
  title: ''
  type: Login
  url: https://shop.brava.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brava.com/welcome/TermsofService
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brava.com/welcome/Privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brava-home-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brava-home-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brava-home-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brava-home-domain-security.yml
created: '2026-07-17'
description: Brava Home, Inc. is a Redwood City, California consumer-hardware company that makes the Brava smart countertop oven — a connected cooking appliance that uses its patented Pure Light infrared-lamp technology to sear, bake, air-fry, dehydrate, toast, reheat, and slow-cook, controlled through the Brava Home mobile app and a guided recipe platform. Brava sells direct-to-consumer through a Shopify storefront at shop.brava.com. Brava does not publish a public developer/device API; its machine-facing surface is agentic commerce — the storefront exposes a Shopify-native Universal Commerce Protocol (UCP) profile at /.well-known/ucp and a Model Context Protocol (MCP) endpoint so shopping agents can search the catalog, build carts, and drive buyer-approved checkout. Originally added to the API Evangelist network as a cowboy-ventures portfolio lead, this profile has been enriched from Brava's real public surface.
image: https://shop.brava.com/cdn/shop/files/favicon180x180_180x180.png?v=1622467377
layout: provider
mcp_servers:
- description: ''
  name: brava-home-mcp.yml
  slug: brava-home-mcpyml
modified: '2026-07-18'
name: Brava Home
nav: Providers
network: true
overview: 'Brava Home publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Smart Home, Kitchen, and Cooking.


  Brava Home''s developer surface includes pricing, engineering blog, support, signup flow, and 8 more developer resources.'
random_paper: 25
score:
  band: emerging
  composite: 21.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Brava Home Domain Security
  slug: brava-home-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: brava-home
tags:
- Company
- Consumer
- Smart Home
- Kitchen
- Cooking
- Appliances
- Connected Devices
- IoT
- E-commerce
- Agentic Commerce
website: https://www.brava.com
---
