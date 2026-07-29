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
    agent_skills: derived
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
  score: 24.5
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://babymori.com
- group: company
  title: ''
  type: Blog
  url: https://babymori.com/blogs/journal
- group: operate
  title: ''
  type: Support
  url: https://babymori.com/pages/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://babymori.com/pages/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://babymori.com/pages/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mori-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mori-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mori-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mori-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/mori-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mori-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mori-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'MORI (Baby Mori) is a UK-based, online-first baby and children''s brand founded in 2015 by Akin Onal, known for soft essentials made from a proprietary bamboo and organic cotton fabric blend. Its direct-to-consumer range spans sleepwear, daywear, footwear, blankets and muslins, nursery and home goods, and a Sleep Club subscription, shipping across the UK, US, and Europe. MORI operates as a Shopify-hosted e-commerce business and does not publish a first-party developer API. Its machine-readable surface is provided natively by the Shopify platform: a live Storefront MCP server at /api/mcp (search_catalog, get_cart, update_cart, get_product_details, search_shop_policies_and_faqs), a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, an agent-instructions /llms.txt (mirrored at /agents.md), and the Shopify Customer Account API OIDC/OAuth discovery. This profile was surfaced as a 500 Global portfolio company and enriched by the API Evangelist pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mori.png
layout: provider
mcp_servers:
- description: ''
  name: mori-mcp.yml
  slug: mori-mcpyml
modified: '2026-07-20'
name: MORI
nav: Providers
network: true
overview: 'MORI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-commerce, Baby Products, and Consumer Goods.


  MORI''s developer surface includes engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 54
scopes:
- name: Mori Scopes
  scope_count: 0
  slug: mori-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.1
  delta: 0.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 27.7
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 17.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Mori Authentication
  slug: mori-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Mori Domain Security
  slug: mori-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mori
tags:
- Company
- Retail
- E-commerce
- Baby Products
- Consumer Goods
- Apparel
- Direct to Consumer
- Shopify
- MCP
- Agent Native
- Universal Commerce Protocol
website: https://babymori.com
---
