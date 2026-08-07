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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Zatanna's hosted, remote Model Context Protocol (MCP) server — the agent-facing surface of its reverse-engineered portal integrations. Live at https://api.zatanna.ai/mcp over Streamable HTTP (JSON-RPC
  name: Zatanna MCP Server
  slug: zatanna-mcp-server
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.zatanna.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zatanna.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zatanna.ai/privacy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zatanna-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zatanna-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zatanna-domain-security.yml
created: '2026-07-17'
description: Zatanna is a Y Combinator (W2026) startup based in San Francisco that creates APIs for software that doesn't have any. It reverse-engineers the back ends of web-based cloud and on-prem software — ERPs (SAP), PMS/POS systems, insurance portals, and marketplaces — by observing real workflows, reconstructing the underlying request sequences, and hosting them as clean, callable APIs. Rather than relying on slow browser automation or computer-use agents, Zatanna gives AI agents faster, cheaper, and more reliable integrations, with a reliability layer that handles session management, authentication, and change detection. The agent-facing surface is a hosted, OAuth-protected Model Context Protocol (MCP) server at api.zatanna.ai.
image: https://raw.githubusercontent.com/api-evangelist/zatanna/refs/heads/main/apis.yml
layout: provider
mcp_servers:
- description: ''
  name: zatanna-mcp.yml
  slug: zatanna-mcpyml
modified: '2026-07-21'
name: Zatanna
nav: Providers
network: true
overview: Zatanna publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, MCP, AI Agents, and Integration.
random_paper: 71
scopes:
- name: Zatanna Scopes
  scope_count: 4
  slug: zatanna-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 14.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 14.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Zatanna Authentication
  slug: zatanna-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Zatanna Domain Security
  slug: zatanna-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zatanna
tags:
- Company
- API
- MCP
- AI Agents
- Integration
- Reverse Engineering
- Automation
- OAuth
- Y Combinator
website: https://www.zatanna.ai/
---
