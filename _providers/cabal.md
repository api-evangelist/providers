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
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 17.1
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://getcabal.com
- group: company
  title: ''
  type: About
  url: https://getcabal.com/about
- group: company
  title: ''
  type: Blog
  url: https://getcabal.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://getcabal.com/pricing
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cabal-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cabal-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cabal-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cabal-security.txt
- group: auth
  title: ''
  type: Security
  url: well-known/cabal-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cabal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cabal-domain-security.yml
created: '2026-07-17'
description: Cabal is an AI-powered relationship-intelligence and warm-introduction platform that turns an organization's professional relationships into warm introductions. It infers connections across millions of professional records without CSV uploads or calendar syncs, letting teams "ask who's connected to anyone." Cabal serves VC platform / deal-sourcing teams, sales organizations, and investor-relations and partnerships teams, and ships Cabal Mail for bulk personalized outreach (company updates, LP communications, strategic asks). The relationship graph is queryable through in-app chat, Claude and ChatGPT via the Model Context Protocol (MCP), a Slack bot, or an API. Backed by Craft Ventures. This profile was enriched by the API Evangelist pipeline from Cabal's public surface; the company advertises API and MCP access but does not publish a public OpenAPI spec or open developer reference (both are account-gated).
image: https://getcabal.com/cabal-og-v6.png
layout: provider
mcp_servers:
- description: ''
  name: cabal-mcp.yml
  slug: cabal-mcpyml
modified: '2026-07-18'
name: Cabal
nav: Providers
network: true
overview: 'Cabal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Saas, Relationship Intelligence, Warm Introductions, and Venture Capital.


  Cabal''s developer surface includes engineering blog, pricing, and 9 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 12.5
  delta: 0.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.4
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cabal/refs/heads/main/screenshots/cabal-2026-07-25T204200.png
security:
- kind: domain-security
  name: Cabal Domain Security
  slug: cabal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cabal Vulnerability Disclosure
  slug: cabal-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cabal
tags:
- Company
- Saas
- Relationship Intelligence
- Warm Introductions
- Venture Capital
- Sales
- CRM
- MCP
- Artificial Intelligence
website: https://getcabal.com
---
