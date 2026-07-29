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
  url: https://odeko.com/
- group: start
  title: ''
  type: Login
  url: https://portal.odeko.com/signin
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.odeko.com/knowledge
- group: company
  title: ''
  type: Blog
  url: https://odeko.com/blogs/resources
- group: operate
  title: ''
  type: Support
  url: https://odeko.com/pages/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://odeko.com/pages/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://odeko.com/pages/terms-of-use
- group: agent
  title: ''
  type: WellKnown
  url: well-known/odeko-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/odeko-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/odeko-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/odeko-domain-security.yml
created: '2026-07-17'
description: Odeko is a cafe operations platform that keeps independent coffee shops and cafes stocked by combining predictive ordering, overnight supply delivery, and mobile ordering plus rewards management through a single dashboard. It was surfaced as a portfolio company of GGV Capital and Y Combinator and added to the API Evangelist network. Odeko publishes no first-party developer API; its public odeko.com storefront runs on Shopify, which provisions agentic-commerce surfaces (llms.txt, UCP profile, and a UCP shopping MCP endpoint) on the domain. This profile captures those real domain artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/odeko.png
layout: provider
mcp_servers:
- description: ''
  name: odeko-mcp.yml
  slug: odeko-mcpyml
modified: '2026-07-20'
name: Odeko
nav: Providers
network: true
overview: 'Odeko is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Cafe, Coffee, and Supply Chain.


  Odeko''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 44
score:
  band: emerging
  composite: 16.7
  delta: 0.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.6
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Odeko Domain Security
  slug: odeko-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: odeko
tags:
- Company
- Food
- Cafe
- Coffee
- Supply Chain
- Logistics
- Commerce
- Shopify
website: https://odeko.com/
---
