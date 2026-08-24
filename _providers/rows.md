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
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Rows Agentic Access
  operation_count: 7
  slug: rows-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 5
apis:
- description: Read and write table cell and value ranges.
  name: Rows Data API
  slug: rows-data-api
- description: Discover folders that organize spreadsheets.
  name: Rows Folders API
  slug: rows-folders-api
- description: List and read spreadsheets and their tables.
  name: Rows Spreadsheets API
  slug: rows-spreadsheets-api
- description: Extract structured data from files using Rows AI Vision.
  name: Rows Vision API
  slug: rows-vision-api
- description: Discover the workspaces available to the authenticated key.
  name: Rows Workspaces API
  slug: rows-workspaces-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rows Data API
  slug: open-rows-data-api
- collection_type: open
  name: Rows Data Folders API
  slug: open-rows-folders-api
- collection_type: open
  name: Rows Data Spreadsheets API
  slug: open-rows-spreadsheets-api
- collection_type: open
  name: Rows Data Vision API
  slug: open-rows-vision-api
- collection_type: open
  name: Rows Data Workspaces API
  slug: open-rows-workspaces-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rows-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rows-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.rows.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.rows.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rows.com/docs/using-rows-api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.rows.com/
- group: company
  title: ''
  type: Blog
  url: https://rows.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://rows.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rows.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rows.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rows
- group: operate
  title: ''
  type: ChangeLog
  url: https://rows.com/docs/whats-new-changelog
- group: build
  title: ''
  type: SDKs
  url: packages/rows-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/rows-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rows-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rows-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rows-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/rows-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rows-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rows-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rows-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://rows.com/docs/how-do-you-manage-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/rows-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rows-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://rows.com/docs/how-do-you-manage-security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rows-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rows-agentic-access.yml
created: '2026-07-17'
description: 'Rows is an AI-powered spreadsheet that connects to live data from dozens of business tools and lets teams build reports, dashboards and lightweight data apps without leaving a familiar grid. Beyond the app, Rows ships a public REST API (base https://api.rows.com/v1) authenticated with a Bearer API key: it exposes workspaces, folders and spreadsheets for discovery, table cell and value read-write operations for moving data in and out of a sheet, and a Vision endpoint that uses AI to extract structured tabular data from image and document files. API access is included on every plan with monthly call quotas scaling from the Free tier (500 calls/month) to Enterprise. Rows is SOC 2 Type II certified and GDPR compliant with European data residency, and joined Superhuman in 2025. It was backed by Accel.'
image: https://rows.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Rows MCP Server
  slug: rows-mcp-server
modified: '2026-07-21'
name: Rows
nav: Providers
network: true
overview: 'Rows publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Data API, Folders API, Spreadsheets API, and 2 more. Tagged areas include Company, Productivity, Spreadsheets, Data, and No-Code.


  Rows'' developer surface includes documentation, API reference, engineering blog, pricing, changelog, authentication, and 22 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 47.0
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 16.7
    contract_quality: 57.3
    developer_ergonomics: 41.1
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rows/refs/heads/main/screenshots/rows-2026-08-17T081656.png
security:
- kind: authentication
  name: Rows Authentication
  slug: rows-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rows Domain Security
  slug: rows-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rows Vulnerability Disclosure
  slug: rows-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Rows Trust Center
  slug: rows-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: rows
tags:
- Company
- Productivity
- Spreadsheets
- Data
- No-Code
- Automation
- Artificial Intelligence
- Analytics
- Business Intelligence
website: https://www.rows.com
---
