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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 23
  human_in_the_loop: 2
  name: Ardent Agentic Access
  operation_count: 35
  slug: ardent-agentic-access
  summary_line: 35 operations · 23 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: The v1-api-keys API from Ardent — 2 operation(s) for v1-api-keys.
  name: Ardent v1-api-keys API
  slug: ardent-v1-api-keys-api
- description: The v1-branching API from Ardent — 2 operation(s) for v1-branching.
  name: Ardent v1-branching API
  slug: ardent-v1-branching-api
- description: The v1-connectors API from Ardent — 10 operation(s) for v1-connectors.
  name: Ardent v1-connectors API
  slug: ardent-v1-connectors-api
- description: The v1-operations API from Ardent — 1 operation(s) for v1-operations.
  name: Ardent v1-operations API
  slug: ardent-v1-operations-api
- description: The v1-orgs API from Ardent — 7 operation(s) for v1-orgs.
  name: Ardent v1-orgs API
  slug: ardent-v1-orgs-api
- description: The v1-projects API from Ardent — 2 operation(s) for v1-projects.
  name: Ardent v1-projects API
  slug: ardent-v1-projects-api
artifact_total: 10
common:
- group: build
  title: ''
  type: Packages
  url: packages/ardent-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ardent-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ardent-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ardent-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ardent-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ardent-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ardent-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ardent-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ardent-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ardent-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ardent-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ardent-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ardent-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ardent-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tryardent.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryardent.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tryardent.com/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tryardent.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.tryardent.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tryardent.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.tryardent.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.tryardent.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tryardent.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tryardent.com/legal/privacy-policy
- group: other
  title: ''
  type: X
  url: https://x.com/ArdentAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ardent-db
created: '2026-07-17'
description: Ardent is a database branching platform for Postgres that lets developers and AI coding agents clone any production or development database in seconds into fully isolated, disposable branches. Each branch is isolated at both the compute and storage layers using copy-on-write, autoscales to zero when idle, and never touches production, so agents and CI/CD pipelines can run migrations, backfills, destructive tests, and risky experiments against production-like data with zero blast radius. Ardent exposes a REST API (api.tryardent.com), a first-party npm CLI (ardent-cli), and connectors for Supabase, AWS RDS, PlanetScale, and self-hosted Postgres 13+.
image: https://tryardent.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: ardent-mcp.yml
  slug: ardent-mcpyml
modified: '2026-07-18'
name: Ardent
nav: Providers
network: true
overview: 'Ardent publishes 6 APIs on the [APIs.io](https://apis.io/) network, including v1-api-keys API, v1-branching API, v1-connectors API, and 3 more. Tagged areas include Company, Database, PostgreSQL, Database Branching, and Developer Tools.


  Ardent''s developer surface includes CLI, sandbox, authentication, documentation, API reference, getting-started guide, support, and 20 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 45.2
  delta: -2.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 53.4
    developer_ergonomics: 66.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ardent/refs/heads/main/screenshots/ardent-2026-07-25T201116.png
security:
- kind: authentication
  name: Ardent Authentication
  slug: ardent-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ardent Domain Security
  slug: ardent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ardent
tags:
- Company
- Database
- PostgreSQL
- Database Branching
- Developer Tools
- Sandbox
- AI Agents
- CI/CD
- Data Infrastructure
- Testing
website: https://docs.tryardent.com
---
