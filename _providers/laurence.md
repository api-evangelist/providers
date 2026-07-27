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
- description: 'Laurence MCP is a hosted, remote Model Context Protocol server that exposes a read-only set of nine tools over a customer''s Amazon Advertising and Amazon Marketing Stream data — allowed ads profiles, '
  name: Laurence MCP
  slug: mcp
artifact_total: 5
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/laurence-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/laurence-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/laurence-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/laurence-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/laurence-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/laurence-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/laurence-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/laurence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.laurence.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.laurence.com/how-it-works
- group: company
  title: ''
  type: Blog
  url: https://www.laurence.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.laurence.com/blog/feed.xml
- group: start
  title: ''
  type: SignUp
  url: https://www.laurence.com/audit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.laurence.com/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.laurence.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.laurence.com/demo
- group: other
  title: ''
  type: Sitemap
  url: https://www.laurence.com/sitemap.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/laurence-ai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/trylaurence
created: '2026-07-17'
description: Laurence is a New York City based Y Combinator (Winter 2026) company that automates Amazon advertising and marketplace management for brands. The platform applies quantitative-trading methodology — hierarchical Bayesian bid optimization over Amazon Marketing Stream data landed in ClickHouse — to maximize contribution margin after margin and ad spend rather than optimizing to rules-of-thumb ACOS targets. Laurence ingests Amazon Advertising and Seller Central data, prices every keyword auction, and exposes the resulting data to customers through Ask Laurence and a hosted, OAuth-protected Model Context Protocol server that brings Amazon Ads data into Claude Code, Cursor, and Codex. The company raised a $5.8M seed round led by Susa Ventures and Box Group with participation from Y Combinator.
image: https://www.laurence.com/icon.png
layout: provider
mcp_servers:
- description: ''
  name: laurence-mcp.yml
  slug: laurence-mcpyml
modified: '2026-07-19'
name: Laurence
nav: Providers
network: true
overview: 'Laurence publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Amazon, E-Commerce, and Marketing.


  Laurence''s developer surface includes authentication, documentation, engineering blog, signup flow, support, and 14 more developer resources.'
random_paper: 31
scopes:
- name: Laurence Scopes
  scope_count: 0
  slug: laurence-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/laurence/refs/heads/main/screenshots/laurence-2026-07-25T224624.png
security:
- kind: authentication
  name: Laurence Authentication
  slug: laurence-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Laurence Domain Security
  slug: laurence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: laurence
tags:
- Company
- Advertising
- Amazon
- E-Commerce
- Marketing
- Machine Learning
- Retail Media
- MCP
website: https://www.laurence.com
---
