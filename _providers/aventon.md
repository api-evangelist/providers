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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 25.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: The agent-driven commerce surface exposed on the aventon.com Shopify storefront via the Universal Commerce Protocol (ucp.dev). An MCP endpoint offers catalog search, cart, checkout, discount, fulfillm
  name: Aventon Agent Commerce (UCP / MCP)
  slug: aventon-agent-commerce-ucp-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://aventon.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aventon.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aventon.com/policies/terms-of-service
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aventon-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aventon-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aventon-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aventon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aventon-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aventon-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aventon-domain-security.yml
created: '2026-07-17'
description: 'Aventon is a consumer electric bicycle (e-bike) manufacturer headquartered in Brea, California. Founded in 2012 and originally known for fixed-gear and track bikes, the company pivoted to electric bikes and is now one of the larger direct-to-consumer e-bike brands in the United States, with a lineup that spans commuter, fat-tire, lightweight, folding, cargo, and mountain e-bikes sold online and through a dealer network. Aventon operates no traditional public developer API of its own, but its Shopify-powered storefront at aventon.com natively exposes agent-facing commerce surfaces: a published /llms.txt, Shopify Customer Account OpenID Connect discovery, and a live Universal Commerce Protocol (UCP) MCP endpoint for agent-driven catalog search, cart, and checkout.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aventon.png
layout: provider
mcp_servers:
- description: ''
  name: aventon-mcp.yml
  slug: aventon-mcpyml
modified: '2026-07-18'
name: Aventon
nav: Providers
network: true
overview: 'Aventon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Electric Bikes, E-Commerce, and Retail.


  Aventon''s developer surface includes authentication and 9 more developer resources.'
random_paper: 15
scopes:
- name: Aventon Scopes
  scope_count: 4
  slug: aventon-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 17.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Aventon Authentication
  slug: aventon-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Aventon Domain Security
  slug: aventon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aventon
tags:
- Company
- Consumer
- Electric Bikes
- E-Commerce
- Retail
- Agent Commerce
- Shopify
- Universal Commerce Protocol
website: https://aventon.com
---
