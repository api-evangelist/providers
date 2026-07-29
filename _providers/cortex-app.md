---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cortex App Agentic Access
  operation_count: 7
  slug: cortex-app-agentic-access
  summary_line: 7 operations
api_count: 9
apis:
- description: REST endpoints to list and retrieve catalog entities (services, libraries, domains, resources, teams) and their descriptors. Supports filtering by tag, type, group, and ownership; returns the canonica
  name: Cortex Catalog API
  slug: catalog-api
- description: 'REST endpoints to list Scorecards, fetch scores for a Scorecard across entities, and surface recommended next steps for improving an entity''s score. Underpins production-readiness, security, and cost '
  name: Cortex Scorecards API
  slug: scorecards-api
- description: REST endpoints to list and inspect entity-to-entity dependencies (caller and callee) and the relationships used to build the service graph.
  name: Cortex Dependencies API
  slug: dependencies-api
- description: REST endpoints to list and retrieve Initiatives - time-boxed cross-team programs that track Scorecard progress, owners, and deadlines.
  name: Cortex Initiatives API
  slug: initiatives-api
- description: REST endpoints for managing and querying Workflow runs, used to drive developer self-service actions and scaffolding from the Cortex IDP.
  name: Cortex Workflow Runs API
  slug: workflows-api
- description: Model Context Protocol server exposing Cortex catalog, scorecards, dependencies, and on-call data to AI agents and copilots through MCP tools and resources.
  name: Cortex MCP Server
  slug: mcp
- description: Catalog entity operations
  name: Cortex Catalog API
  slug: cortex-app-catalog-api
- description: Initiative operations
  name: Cortex Initiatives API
  slug: cortex-app-initiatives-api
- description: Scorecard operations
  name: Cortex Scorecards API
  slug: cortex-app-scorecards-api
artifact_total: 16
collections:
- collection_type: open
  name: Cortex API
  slug: open-cortex-app
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cortex-app-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cortex-app-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cortex-app-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cortexapp
- group: company
  title: ''
  type: Website
  url: https://www.cortex.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cortex.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cortexapps
- group: commercial
  title: ''
  type: Plans
  url: plans/cortex-app-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cortex-app-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cortex-app-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cortex.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.cortex.io/blog
created: '2026-05-23'
description: Cortex is an Internal Developer Portal and service catalog used by platform and engineering teams to inventory services, libraries, domains, teams, on-call rotations, and resources; measure them against Scorecards (production readiness, security, SLO compliance, cost, AI usage); and drive developer-facing experiences through Initiatives, Workflows, and Scaffolder templates. Cortex pulls signals from GitHub, GitLab, AWS, Azure, GCP, Datadog, PagerDuty, Slack, Jira, Snyk, SonarQube, and many other integrations, and exposes a REST API and an MCP server so that humans and AI agents can query the catalog, scorecards, dependencies, and entity descriptors.
finops:
- name: Cortex App Finops
  service_category: API
  slug: cortex-app-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cortex-app.png
layout: provider
modified: '2026-05-23'
name: Cortex
nav: Providers
network: true
overview: 'Cortex publishes 3 APIs on the [APIs.io](https://apis.io/) network: Catalog API, Initiatives API, and Scorecards API. Tagged areas include Internal Developer Portal, Service Catalog, Scorecards, Platform Engineering, and Developer Experience.


  Cortex''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Cortex App Plans Pricing
  plan_count: 1
  slug: cortex-app-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Cortex App Rate Limits
  slug: cortex-app-rate-limits
score:
  band: thin
  composite: 34.3
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cortex-app/refs/heads/main/screenshots/cortex-app-2026-06-20T175111.png
security:
- kind: authentication
  name: Cortex App Authentication
  slug: cortex-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cortex App Domain Security
  slug: cortex-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cortex-app
tags:
- Internal Developer Portal
- Service Catalog
- Scorecards
- Platform Engineering
- Developer Experience
- SRE
website: https://www.cortex.io/
---
