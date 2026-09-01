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
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.6
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The Omni REST API provides programmatic access to an Omni instance: models, topics, views and fields; documents, dashboards and folders; query execution and scheduling; users, groups and permissions; '
  name: Omni REST API
  slug: omni-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/omni-analytics-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/omni-analytics-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.omni.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.omni.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.omni.co/docs/API
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.omni.co/docs/API
- group: company
  title: ''
  type: Blog
  url: https://exploreomni.com/blog
- group: operate
  title: ''
  type: Support
  url: https://exploreomni.com/customer-support
- group: operate
  title: ''
  type: Community
  url: https://community.omni.co
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exploreomni
- group: start
  title: ''
  type: SignUp
  url: https://exploreomni.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://exploreomni.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://exploreomni.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.omni.co
- group: auth
  title: ''
  type: Compliance
  url: https://exploreomni.com/security
- group: auth
  title: ''
  type: Security
  url: https://exploreomni.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.omni.co/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/omni-analytics-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/omni-analytics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/omni-analytics-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/omni-analytics-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/omni-analytics-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/omni-analytics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/omni-analytics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/omni-analytics-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/omni-analytics-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/omni-analytics-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/omni-analytics-llms.txt
created: '2026-07-17'
description: Omni is a business intelligence and embedded analytics platform that turns raw warehouse data into trusted insights. It combines a central semantic layer with an AI chat interface, dashboards, spreadsheets, a point-and-click builder, and a SQL IDE, so data teams and business users can query data conversationally and then refine results with traditional analytics tools. Omni exposes a REST API, a hosted MCP server, a Go CLI, a Python SDK, and a library of published Agent Skills for programmatic and agent-driven access, plus white-label embedded analytics via SSO. It connects to Snowflake, BigQuery, Databricks, dbt and other warehouses, and is backed by GV (Google Ventures). Customers include Condé Nast, BuzzFeed, Perplexity, dbt Labs, and TripAdvisor.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/omni-analytics.png
layout: provider
mcp_servers:
- description: 'Official Omni MCP server for natural language querying across your datasets, scoped to specific models and respecting user permissions. Configured via AI Hub > MCP. Works with Claude, ChatGPT, Cursor '
  name: Omni Analytics MCP Server
  slug: omni-analytics-mcp-server
modified: '2026-07-20'
name: Omni Analytics
nav: Providers
network: true
overview: 'Omni Analytics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Analytics, Business Intelligence, and Embedded Analytics.


  Omni Analytics'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, changelog, and 22 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 41.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/omni-analytics/refs/heads/main/screenshots/omni-analytics-2026-08-07T190150.png
security:
- kind: authentication
  name: Omni Analytics Authentication
  slug: omni-analytics-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Omni Analytics Domain Security
  slug: omni-analytics-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Omni Analytics Trust Center
  slug: omni-analytics-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: omni-analytics
tags:
- Company
- Enterprise
- Analytics
- Business Intelligence
- Embedded Analytics
- Semantic Layer
- Artificial Intelligence
- Data
- MCP
website: https://docs.omni.co
---
