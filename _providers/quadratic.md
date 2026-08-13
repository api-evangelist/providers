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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-08-12'
api_count: 14
apis:
- description: List and inspect team agent connections (third-party REST API bindings).
  name: Quadratic Agent Connections API
  slug: quadratic-agent-connections-api
- description: Identity for the calling token.
  name: Quadratic Auth API
  slug: quadratic-auth-api
- description: Read and write cell values, code, formulas, formats, borders, and merges.
  name: Quadratic Cells API
  slug: quadratic-cells-api
- description: Insert, delete, and resize columns and rows.
  name: Quadratic Columns and rows API
  slug: quadratic-columns-and-rows-api
- description: Manage conditional-format rules.
  name: Quadratic Conditional formats API
  slug: quadratic-conditional-formats-api
- description: Fetch schemas from registered DB connections.
  name: Quadratic Connections API
  slug: quadratic-connections-api
- description: Read-only exploration of file structure and contents.
  name: Quadratic Context, outline, search API
  slug: quadratic-context-outline-search-api
- description: OpenAPI spec and Scalar viewer.
  name: Quadratic Documentation API
  slug: quadratic-documentation-api
- description: Create, list, fetch, and import files.
  name: Quadratic Files API
  slug: quadratic-files-api
- description: Liveness probes.
  name: Quadratic Health API
  slug: quadratic-health-api
- description: Undo, redo, and atomic batches of actions.
  name: Quadratic History API
  slug: quadratic-history-api
- description: Add, rename, delete, reorder, and recolor sheets.
  name: Quadratic Sheets API
  slug: quadratic-sheets-api
- description: Create, configure, and manage data tables.
  name: Quadratic Tables API
  slug: quadratic-tables-api
- description: Manage cell validation rules.
  name: Quadratic Validations API
  slug: quadratic-validations-api
artifact_total: 18
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/quadratic-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.quadratichq.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.quadratichq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.quadratichq.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.quadratichq.com/spreadsheet-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.quadratichq.com/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.quadratichq.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quadratichq
- group: commercial
  title: ''
  type: Pricing
  url: https://www.quadratichq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.quadratichq.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quadratichq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quadratichq.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.quadratichq.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quadratic-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/quadratic-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quadratic-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/quadratic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/quadratic-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/quadratic-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/quadratic-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/quadratic-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quadratic-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quadratic-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/quadratic-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/quadratic-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/quadratic-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Quadratic is an AI-native infinite spreadsheet that combines Python, SQL, JavaScript, formulas, and AI agents on a single canvas, with live connections to databases like PostgreSQL, MySQL, BigQuery, and Snowflake. Its token-authenticated Developer (Spreadsheet) API and remote MCP server let agents and applications programmatically read and write cells, run code and SQL, build tables, and orchestrate spreadsheets.
image: https://www.quadratichq.com/images/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: quadratic-mcp.yml
  slug: quadratic-mcpyml
modified: '2026-07-20'
name: Quadratic
nav: Providers
network: true
overview: 'Quadratic publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Agent Connections API, Auth API, Cells API, and 11 more. Tagged areas include Company, AI, Spreadsheet, Analytics, and Data.


  Quadratic''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 118
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 64.7
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 50.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Quadratic Authentication
  slug: quadratic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Quadratic Domain Security
  slug: quadratic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Quadratic Trust Center
  slug: quadratic-trust-center
  summary_line: SOC 2, HIPAA
slug: quadratic
tags:
- Company
- AI
- Spreadsheet
- Analytics
- Data
- Developer Tools
- MCP
- Productivity
website: https://www.quadratichq.com
---
