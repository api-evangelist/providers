---
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
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: An undocumented Model Context Protocol server operated by Copper at mcp.getcopper.com. The host publishes RFC 8414 OAuth 2.0 Authorization Server Metadata at /.well-known/oauth-authorization-server de
  name: Copper MCP Server
  slug: copper-mcp-server
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/copper-banking-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getcopper.com/
- group: company
  title: ''
  type: Blog
  url: https://www.getcopper.com/blog
- group: operate
  title: ''
  type: Support
  url: https://getcopper.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getcopper.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/61f9b891f832346a0a7b9f9a/65554dcca822725a736a8e84_da54d9e097d505e5874cac4bd7088ba6_Privacy%20Policy_11.20.2023.docx.pdf
- group: auth
  title: ''
  type: Compliance
  url: https://www.getcopper.com/legal/glba
- group: agent
  title: ''
  type: WellKnown
  url: well-known/copper-banking-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/copper-banking-mcp.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/copper-banking-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/copper-banking-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/copper-banking-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/copper-banking-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/copper-banking-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/copper-banking_stock/
created: '2026-08-04'
description: Copper (Copper Banking) is a Seattle-based consumer fintech founded in 2019 by Eddie Behringer and Stefan Berglund that began as a teen banking app and debit card built on the Synapse banking-as-a-service platform. After Synapse's collapse Copper abruptly discontinued its bank deposit accounts and debit cards in May 2024 and repositioned as a financial-empowerment and earning app, where members earn cash and gift-card rewards through cash back, surveys, receipt scanning, games and referrals, alongside financial-literacy content, guides and in-school workshops. Copper publishes no public developer portal, documentation or API specification; the only machine-readable surface reachable without credentials is an OAuth 2.0 authorization server for a Model Context Protocol endpoint at mcp.getcopper.com.
image: https://cdn.prod.website-files.com/61f9b891f832346a0a7b9f9a/673cf4a1dd4ac006b4602fab_OpenGraph_1200x627.jpg
layout: provider
mcp_servers:
- description: ''
  name: copper-banking-mcp.yml
  slug: copper-banking-mcpyml
modified: '2026-08-04'
name: Copper Banking
nav: Providers
network: true
overview: 'Copper Banking publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Fintech, Consumer Finance, and Financial Literacy.


  Copper Banking''s developer surface includes engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 83
scopes:
- name: Copper Banking Scopes
  scope_count: 2
  slug: copper-banking-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 26.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 26.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 59.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/copper-banking/refs/heads/main/screenshots/copper-banking-2026-08-07T163809.png
security:
- kind: authentication
  name: Copper Banking Authentication
  slug: copper-banking-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Copper Banking Domain Security
  slug: copper-banking-domain-security
  summary_line: TLSv1.3 · DMARC
slug: copper-banking
tags:
- Company
- Financial Services
- Fintech
- Consumer Finance
- Financial Literacy
- Rewards
- Neobank
- Mobile Banking
- Teen Banking
- Model Context Protocol
website: https://www.getcopper.com/
---
