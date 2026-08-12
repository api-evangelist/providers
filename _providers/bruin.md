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
    agent_skills: true
    agentic_access: false
    auth_clarity: false
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
  score: 15.3
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://getbruin.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bruin-data.github.io/bruin/
- group: docs
  title: ''
  type: Documentation
  url: https://bruin-data.github.io/bruin/
- group: docs
  title: ''
  type: APIReference
  url: https://bruin-data.github.io/bruin/commands/overview.html
- group: start
  title: ''
  type: GettingStarted
  url: https://bruin-data.github.io/bruin/getting-started/introduction/quickstart.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bruin-data
- group: company
  title: ''
  type: Blog
  url: https://getbruin.com/blog
- group: operate
  title: ''
  type: Support
  url: https://getbruin.com/support
- group: start
  title: ''
  type: SignUp
  url: https://cloud.getbruin.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getbruin.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getbruin.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://getbruin.com/vulnerability-disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://getbruin.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/bruin-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bruin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bruin-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/bruin-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bruin-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bruin-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bruin-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bruin-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/bruin-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bruin-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bruin-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/bruin-data/bruin/releases
created: '2026-07-17'
description: Bruin is an end-to-end, open-source AI data platform that consolidates data ingestion, SQL and Python transformation, orchestration, quality checks, column-level lineage, and natural-language analytics into a single Git-native tool - positioned as a replacement for a fragmented Fivetran + dbt + Airflow + BI stack. Its developer surface is the open-source Bruin CLI (Apache-2.0, Go), the ingestr data-copy tool (MIT), a Python SDK, a VS Code extension, a GitHub Action, and a built-in Model Context Protocol server (`bruin mcp`) plus a set of packaged agent skills. Bruin Cloud adds a hosted control plane with scheduling and dashboards. Bruin is SOC 2 Type 2 audited and GDPR-compliant, and was a Techstars portfolio company. There is no public REST API; the platform is operated through the CLI, SDK, and MCP server.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bruin.png
layout: provider
mcp_servers:
- description: ''
  name: bruin-mcp.yml
  slug: bruin-mcpyml
modified: '2026-07-18'
name: Bruin
nav: Providers
network: true
overview: 'Bruin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Data Engineering, Data Pipelines, and ETL.


  Bruin''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 19 more developer resources.'
random_paper: 80
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 69.6
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 35.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bruin/refs/heads/main/screenshots/bruin-2026-07-25T204000.png
security:
- kind: domain-security
  name: Bruin Domain Security
  slug: bruin-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bruin Vulnerability Disclosure
  slug: bruin-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Bruin Trust Center
  slug: bruin-trust-center
  summary_line: SOC 2, GDPR
slug: bruin
tags:
- Company
- Data
- Data Engineering
- Data Pipelines
- ETL
- ELT
- Analytics
- Data Quality
- CLI
- MCP
- Open Source
website: https://getbruin.com/
---
