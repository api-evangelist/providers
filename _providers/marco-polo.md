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
- description: Hosted, remote Model Context Protocol server that connects governed enterprise data sources into a sandboxed agent workspace. OAuth 2.0 (WorkOS AuthKit) protected; requires a bearer token.
  name: MarcoPolo MCP Server
  slug: marcopolo-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://marcopolo.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.marcopolo.dev
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.marcopolo.dev/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.marcopolo.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.marcopolo.dev/resources
- group: agent
  title: ''
  type: MCPServer
  url: mcp/marco-polo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/marco-polo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/marco-polo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marco-polo-authentication.yml
- group: build
  title: ''
  type: CLI
  url: cli/marco-polo-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/marco-polo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/marco-polo-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marco-polo-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/marco-polo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/marco-polo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/marco-polo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: security/marco-polo-trust-center.yml
created: '2026-07-17'
description: MarcoPolo is an MCP-first enterprise AI data platform operated by Immersa - "Scale AI across the enterprise. Without the leaks." It exposes a hosted, remote Model Context Protocol (MCP) server that lets any AI assistant (Claude, ChatGPT, Cursor, Codex, or a custom agent) connect governed enterprise data sources - PostgreSQL, Snowflake, BigQuery, S3, OneDrive, Salesforce, Jira and local DuckDB - into a sandboxed workspace, run queries, and cache results, with centralized credential management, attribute-based access controls, token cost visibility, and SOC 2 Type II governance. Originally added to the API Evangelist network as a venture-portfolio lead and enriched from its public site, docs, and live MCP probes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marco-polo.png
layout: provider
mcp_servers:
- description: ''
  name: marco-polo-mcp.yml
  slug: marco-polo-mcpyml
modified: '2026-07-20'
name: Marco Polo
nav: Providers
network: true
overview: 'Marco Polo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, Model Context Protocol, Enterprise AI, and Data Governance.


  Marco Polo''s developer surface includes documentation, getting-started guide, pricing, engineering blog, authentication, CLI, and 11 more developer resources.'
random_paper: 69
scopes:
- name: Marco Polo Scopes
  scope_count: 0
  slug: marco-polo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.4
  delta: 1.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 25.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marco-polo/refs/heads/main/screenshots/marco-polo-2026-07-25T230151.png
security:
- kind: authentication
  name: Marco Polo Authentication
  slug: marco-polo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Marco Polo Domain Security
  slug: marco-polo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Marco Polo Vulnerability Disclosure
  slug: marco-polo-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Marco Polo Trust Center
  slug: marco-polo-trust-center
  summary_line: SOC 2 Type II
slug: marco-polo
tags:
- Company
- MCP
- Model Context Protocol
- Enterprise AI
- Data Governance
- AI Agents
- Data Integration
- Security
- OAuth
website: https://marcopolo.dev
---
