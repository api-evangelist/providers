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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.0
  scored_at: '2026-07-28'
api_count: 38
apis:
- description: AI-powered query generation
  name: Omni AI API
  slug: omni-ai-api
- description: Manage organization-level AI credit usage
  name: Omni AI Credit Controls API
  slug: omni-ai-credit-controls-api
- description: 'AI evaluation: manage prompt sets and runs used to score AI quality against curated prompt suites.'
  name: Omni AI Eval API
  slug: omni-ai-eval-api
- description: Manage AI-generated suggestions for shared models
  name: Omni AI Model Suggestions API
  slug: omni-ai-model-suggestions-api
- description: 'Manage AI Routines: schedule recurring AI-powered tasks to run automatically on your data.'
  name: Omni AI Routines API
  slug: omni-ai-routines-api
- description: Manage API tokens (Organization keys, Personal Access Tokens, MCP OAuth grants)
  name: Omni API Tokens API
  slug: omni-api-tokens-api
- description: Manage connection environments database connections
  name: Omni Connection environments API
  slug: omni-connection-environments-api
- description: Manage database connections
  name: Omni Connections API
  slug: omni-connections-api
- description: Unified content retrieval (documents and folders)
  name: Omni Content API
  slug: omni-content-api
- description: Export and import dashboards
  name: Omni Content migration API
  slug: omni-content-migration-api
- description: Validate content against models and perform find/replace operations
  name: Omni Content validator API
  slug: omni-content-validator-api
- description: Download dashboards and tiles as PDF, PNG, XLSX, CSV, or JSON files
  name: Omni Dashboard downloads API
  slug: omni-dashboard-downloads-api
- description: The Dashboard filters API from Omni — 1 operation(s) for dashboard filters.
  name: Omni Dashboard filters API
  slug: omni-dashboard-filters-api
- description: Manage dbt configuration for connections
  name: Omni dbt API
  slug: omni-dbt-api
- description: Favorite and unfavorite documents
  name: Omni Document favorites API
  slug: omni-document-favorites-api
- description: Apply and manage labels on documents
  name: Omni Document labels API
  slug: omni-document-labels-api
- description: Manage document-level access
  name: Omni Document permissions API
  slug: omni-document-permissions-api
- description: Create, retrieve, and manage documents
  name: Omni Documents API
  slug: omni-documents-api
- description: 'A draft-based workflow for creating and editing documents: create a document, patch a draft, then publish. Replaces the one-shot `PUT`/`PATCH` v1 document write endpoints.'
  name: Omni Documents v2 API
  slug: omni-documents-v2-api
- description: Manage folder-level access
  name: Omni Folder permissions API
  slug: omni-folder-permissions-api
- description: Create and organize content folders
  name: Omni Folders API
  slug: omni-folders-api
- description: Check status of asynchronous jobs
  name: Omni Jobs API
  slug: omni-jobs-api
- description: 'Manage labels in an organization. Labels can be applied to documents and folders to help organize and categorize content. **Label types:** - **Basic labels**: Can be created and managed by any user - '
  name: Omni Labels API
  slug: omni-labels-api
- description: Manage model branches and merge changes
  name: Omni Model branches API
  slug: omni-model-branches-api
- description: Manage git configuration for shared models
  name: Omni Model git configuration API
  slug: omni-model-git-configuration-api
- description: Create and manage data models
  name: Omni Models API
  slug: omni-models-api
- description: Execute workbook queries
  name: Omni Queries API
  slug: omni-queries-api
- description: Manage schedule recipients
  name: Omni Schedule recipients API
  slug: omni-schedule-recipients-api
- description: Create and manage scheduled tasks
  name: Omni Schedules API
  slug: omni-schedules-api
- description: Manage automated schema refresh schedules for connections
  name: Omni Schema refresh schedules API
  slug: omni-schema-refresh-schedules-api
- description: Retrieve topic information from models
  name: Omni Topics API
  slug: omni-topics-api
- description: Manage CSV and spreadsheet uploads
  name: Omni Uploads API
  slug: omni-uploads-api
- description: Manage user attribute definitions
  name: Omni User attributes API
  slug: omni-user-attributes-api
- description: Manage model and connection role assignments for user groups
  name: Omni User group model roles API
  slug: omni-user-group-model-roles-api
- description: Manage user groups
  name: Omni User groups API
  slug: omni-user-groups-api
- description: Manage model and connection role assignments for users
  name: Omni User model roles API
  slug: omni-user-model-roles-api
- description: Manage users
  name: Omni Users API
  slug: omni-users-api
- description: Inspect your own user permissions
  name: Omni Who Am I API
  slug: omni-who-am-i-api
artifact_total: 43
common:
- group: company
  title: ''
  type: Website
  url: https://omni.co
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
  url: https://docs.omni.co/api/api-explorer
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.omni.co/getting-started/developers
- group: company
  title: ''
  type: Blog
  url: https://omni.co/blog
- group: operate
  title: ''
  type: Support
  url: https://community.omni.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exploreomni
- group: start
  title: ''
  type: SignUp
  url: https://omni.co/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://omni.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://omni.co/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/omni-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/omni-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/omni-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/omni-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/omni-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/omni-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/omni-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/omni-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/omni-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.omniapp.co
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/omni-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/omni-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://omni.co/security
- group: design
  title: ''
  type: DataModel
  url: data-model/omni-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/omni-openapi-overlay.yaml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/omni-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/omni-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/omni-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/omni-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/omni-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://omni.co/security
created: '2026-07-17'
description: Omni is an AI-powered business intelligence and embedded analytics platform that turns a governed semantic model into a trusted source of truth for people and AI agents. It connects to warehouses like Snowflake, BigQuery, Databricks and Postgres, layers a git-versioned modeling layer (with dbt integration) on top, and exposes everything through a 187-operation REST API, a first-party CLI, an embed SDK, and a hosted MCP server for natural-language querying from Claude, ChatGPT, Cursor and more. Omni is backed by GV, ICONIQ Capital and Redpoint Ventures.
image: https://omni.co/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: omni-mcp.yml
  slug: omni-mcpyml
modified: '2026-07-20'
name: Omni
nav: Providers
network: true
overview: 'Omni publishes 38 APIs on the [APIs.io](https://apis.io/) network, including AI API, AI Credit Controls API, AI Eval API, and 35 more. Tagged areas include Company, Ai, Analytics, Business Intelligence, and Data.


  Omni''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 26 more developer resources.'
random_paper: 30
score:
  band: strong
  composite: 59.0
  delta: -0.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.0
    developer_ergonomics: 82.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 59.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 38
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Omni Authentication
  slug: omni-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Omni Domain Security
  slug: omni-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Omni Vulnerability Disclosure
  slug: omni-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Omni Trust Center
  slug: omni-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: omni
tags:
- Company
- Ai
- Analytics
- Business Intelligence
- Data
- Embedded Analytics
- Semantic Layer
- MCP
website: https://omni.co
---
