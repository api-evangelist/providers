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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Superlog Agentic Access
  operation_count: 17
  slug: superlog-agentic-access
  summary_line: 17 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The API keys API from Superlog — 1 operation(s) for api keys.
  name: Superlog API keys API
  slug: superlog-api-keys-api
- description: The GitHub integration API from Superlog — 6 operation(s) for github integration.
  name: Superlog GitHub integration API
  slug: superlog-github-integration-api
- description: The Projects API from Superlog — 3 operation(s) for projects.
  name: Superlog Projects API
  slug: superlog-projects-api
- description: The Telemetry read API from Superlog — 3 operation(s) for telemetry read.
  name: Superlog Telemetry read API
  slug: superlog-telemetry-read-api
arazzos:
- description: Create a new Superlog project, then mint a project-scoped OTLP ingest key so a service can start sending OpenTelemetry telemetry.
  name: Provision a Superlog project and mint an ingest key
  slug: superlog-provision-project
artifact_total: 17
asyncapis:
- description: ''
  name: Superlog Webhooks
  slug: superlog-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Superlog Management API keys API
  slug: open-superlog-api-keys-api
- collection_type: open
  name: Superlog Management API keys GitHub integration API
  slug: open-superlog-github-integration-api
- collection_type: open
  name: Superlog Management API keys Projects API
  slug: open-superlog-projects-api
- collection_type: open
  name: Superlog Management API keys Telemetry read API
  slug: open-superlog-telemetry-read-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/superlog-management-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/superlog-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.superlog.sh/
- group: design
  title: ''
  type: Arazzo
  url: arazzo/superlog-provision-project.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.superlog.sh
- group: docs
  title: ''
  type: Documentation
  url: https://docs.superlog.sh/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://api.superlog.sh/api/v1/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.superlog.sh/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superloglabs
- group: start
  title: ''
  type: SignUp
  url: https://app.superlog.sh
- group: auth
  title: ''
  type: Authentication
  url: authentication/superlog-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/superlog-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/superlog-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/superlog-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/superlog-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/superlog-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/superlog-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/superlog-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/superlog-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/superlog-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/superlog-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superlog-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/superlog-llms.txt
created: '2026-07-17'
description: Superlog is an AI-native, open-core observability platform (Y Combinator, Spring 2026) that ingests OpenTelemetry traces, logs, and metrics over OTLP, groups noisy signals into incidents, and dispatches AI agents to investigate root causes and open fix pull requests automatically. It offers a Management REST API for provisioning projects and ingest keys, OTLP ingest endpoints, a hosted Model Context Protocol (MCP) server so coding assistants like Claude and Cursor can query telemetry and incidents, signed incident webhooks, and GitHub/Slack/Linear/AWS integrations. The Community edition is Apache-2.0 licensed and self-hostable via Docker Compose; Superlog Cloud is the managed offering.
image: https://media.brand.dev/b517a2c9-12a7-4caa-9afc-34d21e942292.jpg
layout: provider
mcp_servers:
- description: ''
  name: Superlog MCP Server
  slug: superlog-mcp-server
modified: '2026-07-21'
name: Superlog
nav: Providers
network: true
overview: 'Superlog publishes 4 APIs on the [APIs.io](https://apis.io/) network, including API keys API, GitHub integration API, Projects API, and 1 more. Tagged areas include Company, Observability, OpenTelemetry, Monitoring, and Logging.


  The Superlog catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Superlog''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, CLI, and 18 more developer resources.'
random_paper: 20
scopes:
- name: Superlog Scopes
  scope_count: 3
  slug: superlog-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 14.5
    commercial_clarity: 14.5
    contract_governance: 18.2
    contract_quality: 58.5
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/superlog/refs/heads/main/screenshots/superlog-2026-08-17T082159.png
security:
- kind: authentication
  name: Superlog Authentication
  slug: superlog-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Superlog Domain Security
  slug: superlog-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Superlog Trust Center
  slug: superlog-trust-center
  summary_line: SOC 2
slug: superlog
tags:
- Company
- Observability
- OpenTelemetry
- Monitoring
- Logging
- Tracing
- Metrics
- Incident Management
- AI Agents
- MCP
- Developer Tools
website: https://docs.superlog.sh
---
