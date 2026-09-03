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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.2
  scored_at: '2026-09-02'
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
  name: Orion by Gravity MCP Server
  slug: orion-by-gravity-mcp-server
modified: '2026-07-20'
name: Orion by Gravity
nav: Providers
network: true
overview: 'Orion by Gravity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Business Intelligence, Artificial Intelligence, and Data.


  Orion by Gravity''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, signup flow, authentication, and 14 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 33.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orion-by-gravity/refs/heads/main/screenshots/orion-by-gravity-2026-08-07T190940.png
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
- Software-as-a-Service
website: https://www.bygravity.com
---
