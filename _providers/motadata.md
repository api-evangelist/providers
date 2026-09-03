---
access_model:
  confidence: high
  label: Quote-based, sales-led; trial requested through a form
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans/motadata-plans-pricing.yml
  trial: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 17.8
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: ObserveOps (formerly Motadata AIOps) is a unified observability platform correlating metrics, logs, traces, flows and topology with anomaly detection that needs no training period. Its REST API is mou
  name: Motadata ObserveOps
  slug: observeops
- description: ServiceOps is Motadata's AI-powered, ITIL-aligned IT and enterprise service management suite. Its REST API lets third-party systems create, read, update and delete requests, problems, changes, release
  name: Motadata ServiceOps
  slug: serviceops
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.motadata.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.motadata.com
- group: company
  title: ''
  type: Blog
  url: https://www.motadata.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.motadata.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.motadata.com/support-portal
- group: start
  title: ''
  type: SignUp
  url: https://www.motadata.com/free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.motadata.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.motadata.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/motadata
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/motadata2025
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/motadata
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/motadata-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/motadata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/motadata-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/motadata-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: CLI
  url: cli/motadata-cli.yml
- group: design
  title: ''
  type: Components
  url: components/motadata-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/motadata-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/motadata-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/motadata-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/motadata-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/motadata-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/motadata-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/motadata-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/motadata-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/motadata-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/motadata-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/motadata-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/motadata-domain-security.yml
created: '2026-03-27'
description: 'Motadata (Mindarray Systems) is a global IT software company running two AI-native platforms on a shared deep-learning foundation: ObserveOps, a unified observability and AIOps platform that brings metrics, logs, traces, flows and topology into one backend, and ServiceOps, an ITIL-aligned IT and enterprise service management suite covering service desk, CMDB, asset management, patch management and workflow automation. Both products are deployed in the customer''s own environment, so every API host, credential and rate limit belongs to the customer rather than to Motadata. ObserveOps exposes a REST API at /api/v1 across 96 configuration resource types plus a Vert.x EventBus websocket for live streams, and ships an official agent-first CLI that doubles as an MCP server with 22 tools and five packaged Agent Skills. ServiceOps exposes a documented REST API over OAuth 2.0 or an API key across request, problem, change, release, CMDB, asset and service-catalog objects. Motadata publishes
  no OpenAPI for either product.'
finops:
- name: Motadata Finops
  service_category: API
  slug: motadata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/motadata.png
layout: provider
mcp_servers:
- description: Motadata ships an MCP server inside its official ObserveOps CLI. `observeops mcp` exposes the ObserveOps (AIOps) platform as typed MCP tools over stdio, holding one authenticated session for the whole
  name: Motadata MCP Server
  slug: motadata-mcp-server
modified: '2026-08-29'
name: Motadata
nav: Providers
network: true
overview: 'Motadata publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AIOps, Monitoring, Observability, ITSM, and Service Desk.


  Motadata''s developer surface includes documentation, engineering blog, getting-started guide, support, signup flow, CLI, authentication, and 23 more developer resources.'
plans:
- name: Motadata Plans Pricing
  plan_count: 0
  slug: motadata-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Motadata Rate Limits
  slug: motadata-rate-limits
scopes:
- name: Motadata Scopes
  scope_count: 0
  slug: motadata-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 36.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/motadata/refs/heads/main/screenshots/motadata-2026-06-20T185837.png
security:
- kind: authentication
  name: Motadata Authentication
  slug: motadata-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Motadata Domain Security
  slug: motadata-domain-security
  summary_line: TLSv1.3 · DMARC
slug: motadata
tags:
- AIOps
- Monitoring
- Observability
- ITSM
- Service Desk
- Network Monitoring
- Log Management
- IT Operations
- Application Performance Monitoring
- OpenTelemetry
website: https://www.motadata.com
---
