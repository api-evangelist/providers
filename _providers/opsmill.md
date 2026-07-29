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
    agent_skills: true
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Opsmill Agentic Access
  operation_count: 34
  slug: opsmill-agentic-access
  summary_line: 34 operations · 10 acting
api_count: 16
apis:
- description: The GraphQL API is Infrahub's primary interface, auto-generated from core and user-defined schema models, supporting branch-aware queries, time-travel (global branch), mutations, and subscriptions. En
  name: Infrahub GraphQL API
  slug: infrahub-graphql-api
- description: The Artifact API from OpsMill — 2 operation(s) for artifact.
  name: OpsMill Artifact API
  slug: opsmill-artifact-api
- description: The Auth API from OpsMill — 4 operation(s) for auth.
  name: OpsMill Auth API
  slug: opsmill-auth-api
- description: The Config API from OpsMill — 1 operation(s) for config.
  name: OpsMill Config API
  slug: opsmill-config-api
- description: The Diff API from OpsMill — 2 operation(s) for diff.
  name: OpsMill Diff API
  slug: opsmill-diff-api
- description: The File API from OpsMill — 1 operation(s) for file.
  name: OpsMill File API
  slug: opsmill-file-api
- description: The Info API from OpsMill — 1 operation(s) for info.
  name: OpsMill Info API
  slug: opsmill-info-api
- description: The Menu API from OpsMill — 1 operation(s) for menu.
  name: OpsMill Menu API
  slug: opsmill-menu-api
- description: The Oauth2 API from OpsMill — 2 operation(s) for oauth2.
  name: OpsMill Oauth2 API
  slug: opsmill-oauth2-api
- description: The Oidc API from OpsMill — 2 operation(s) for oidc.
  name: OpsMill Oidc API
  slug: opsmill-oidc-api
- description: The Query API from OpsMill — 1 operation(s) for query.
  name: OpsMill Query API
  slug: opsmill-query-api
- description: The Schema API from OpsMill — 6 operation(s) for schema.
  name: OpsMill Schema API
  slug: opsmill-schema-api
- description: The Schema.graphql API from OpsMill — 1 operation(s) for schema.graphql.
  name: OpsMill Schema.graphql API
  slug: opsmill-schema-graphql-api
- description: The Storage API from OpsMill — 6 operation(s) for storage.
  name: OpsMill Storage API
  slug: opsmill-storage-api
- description: The Telemetry API from OpsMill — 1 operation(s) for telemetry.
  name: OpsMill Telemetry API
  slug: opsmill-telemetry-api
- description: The Transform API from OpsMill — 2 operation(s) for transform.
  name: OpsMill Transform API
  slug: opsmill-transform-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opsmill-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opsmill-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opsmill-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://opsmill.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.infrahub.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.infrahub.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.infrahub.app/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.infrahub.app/overview/quickstart
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.infrahub.app
- group: company
  title: ''
  type: Blog
  url: https://opsmill.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/opsmill
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opsmill
- group: commercial
  title: ''
  type: Pricing
  url: https://opsmill.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://opsmill.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opsmill.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opsmill.com/legal/
- group: build
  title: ''
  type: Packages
  url: packages/opsmill-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/opsmill-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/opsmill-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opsmill-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opsmill-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/opsmill-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opsmill-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opsmill-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opsmill-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/opsmill-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/opsmill-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/opsmill-infrahub-overlay.yaml
created: '2026-07-17'
description: OpsMill is the company behind Infrahub, an open-source, graph-based infrastructure data management platform that unifies a source of truth for network, data center, and cloud automation. Infrahub combines a flexible, extensible schema, native version control with branching and merging, and unified Git + graph-database storage, then exposes that data through a GraphQL API, a REST API, a Python SDK, the infrahubctl CLI, a web UI, and a Model Context Protocol (MCP) server so both automation pipelines and AI agents can query, propose, and review infrastructure changes with peer review and CI workflows built in.
image: https://avatars.githubusercontent.com/u/118297816?v=4
layout: provider
mcp_servers:
- description: ''
  name: opsmill-mcp.yml
  slug: opsmill-mcpyml
modified: '2026-07-20'
name: OpsMill
nav: Providers
network: true
overview: 'OpsMill publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Artifact API, Auth API, Config API, and 12 more. Tagged areas include Company, Infrastructure Saas, Network Automation, Source Of Truth, and Data Management.


  OpsMill''s developer surface includes authentication, documentation, API reference, getting-started guide, sandbox, engineering blog, support, and 22 more developer resources.'
random_paper: 75
score:
  band: developing
  composite: 50.1
  delta: -0.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 45.8
    developer_ergonomics: 87.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Opsmill Authentication
  slug: opsmill-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Opsmill Domain Security
  slug: opsmill-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opsmill
tags:
- Company
- Infrastructure Saas
- Network Automation
- Source Of Truth
- Data Management
- GraphQL
- DevOps
- Configuration Management
- AIOps
- Open Source
website: https://opsmill.com/
---
