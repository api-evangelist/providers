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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Remote Model Context Protocol (MCP) server that lets AI assistants (Claude Code, Claude Desktop, Cursor, Windsurf, Gemini Enterprise) run natural-language analyses, list and execute metrics, trigger w
  name: Orion MCP Server
  slug: orion-mcp-server
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.bygravity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.runorion.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runorion.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.runorion.com/mcp/tools.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.runorion.com/quickstart.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/orion-by-gravity-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orion-by-gravity-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://bygravity.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/orion-by-gravity-changelog.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bygravity.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bygravity.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.runorion.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/orion-by-gravity-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.bygravity.com
- group: auth
  title: ''
  type: Security
  url: https://bygravity.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orion-by-gravity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/orion-by-gravity-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/orion-by-gravity-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orion-by-gravity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orion-by-gravity-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/orion-by-gravity-conformance.yml
created: '2026-07-17'
description: Orion by Gravity is a collaborative, AI-native analytics platform built by Gravity (bygravity.com) that connects directly to your data warehouse — Snowflake, BigQuery, Databricks, Redshift, Athena, Fabric, PostgreSQL, and MySQL — and lets teams ask questions in natural language to get shared analyses, dashboards, reports, scheduled workflows, and slide decks. Orion functions as an autonomous AI analyst that learns business context from a wiki-style Knowledge Base, integrates with Slack, Notion, Confluence, Looker, and Google Slides, and can be embedded as a white-label surface. Its primary programmatic surface is a remote Model Context Protocol (MCP) server at https://g.runorion.com/mcp that exposes twenty tools for AI assistants like Claude and Gemini Enterprise to run analyses, monitor KPIs, trigger workflows, and search the knowledge base. The platform is SOC 2 Type 2 audited.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orion-by-gravity.png
layout: provider
mcp_servers:
- description: ''
  name: orion-by-gravity-mcp.yml
  slug: orion-by-gravity-mcpyml
modified: '2026-07-20'
name: Orion by Gravity
nav: Providers
network: true
overview: 'Orion by Gravity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Business Intelligence, Artificial Intelligence, and Data.


  Orion by Gravity''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, signup flow, authentication, and 14 more developer resources.'
random_paper: 52
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 34.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Orion By Gravity Authentication
  slug: orion-by-gravity-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Orion By Gravity Domain Security
  slug: orion-by-gravity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Orion By Gravity Vulnerability Disclosure
  slug: orion-by-gravity-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Orion By Gravity Trust Center
  slug: orion-by-gravity-trust-center
  summary_line: SOC 2 Type 2
slug: orion-by-gravity
tags:
- Company
- Analytics
- Business Intelligence
- Artificial Intelligence
- Data
- MCP
- Data Warehouse
- SaaS
website: https://www.bygravity.com
---
