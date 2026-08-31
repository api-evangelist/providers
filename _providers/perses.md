---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Perses Agentic Access
  operation_count: 20
  slug: perses-agentic-access
  summary_line: 20 operations · 12 acting
api_count: 1
apis:
- description: The Perses REST API provides programmatic access to dashboards, datasources, ephemeral dashboards, projects, roles, role bindings, secrets, users, variables, plugins, validation, and migration resourc
  name: Perses API
  slug: perses
- description: Manage dashboards inside a project.
  name: Perses Dashboards API
  slug: perses-dashboards-api
- description: Manage project-scoped datasources.
  name: Perses Datasources API
  slug: perses-datasources-api
- description: Manage shared datasources across projects.
  name: Perses Global Datasources API
  slug: perses-global-datasources-api
- description: Manage Perses projects (workspaces).
  name: Perses Projects API
  slug: perses-projects-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Perses Dashboards API
  slug: open-perses-dashboards-api
- collection_type: open
  name: Perses Dashboards Datasources API
  slug: open-perses-datasources-api
- collection_type: open
  name: Perses Dashboards Global Datasources API
  slug: open-perses-global-datasources-api
- collection_type: open
  name: Perses Dashboards Projects API
  slug: open-perses-projects-api
- collection_type: open
  name: Perses API
  slug: open-perses
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/perses-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perses-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://perses.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://perses.dev/perses/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://perses.dev/perses/docs/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/perses
- group: build
  title: ''
  type: GitHub
  url: https://github.com/perses/perses
- group: operate
  title: ''
  type: Community
  url: https://perses.dev/community/
- group: company
  title: ''
  type: Blog
  url: https://perses.dev/blog/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/perses/mcp-server
created: '2026-03-16'
description: Perses is an open-source monitoring and dashboarding tool designed as a modern alternative for visualizing time-series data with a focus on performance, extensibility, and GitOps. Perses exposes a REST API for managing dashboards, datasources, ephemeral dashboards, projects, roles, role bindings, secrets, users, variables, plugins, validation, and migrations. It is a CNCF sandbox project.
finops:
- name: Perses Finops
  service_category: API
  slug: perses-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/perses.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Perses
nav: Providers
network: true
overview: 'Perses publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Dashboards API, Datasources API, Global Datasources API, and 1 more. Tagged areas include CNCF, Dashboards, Monitoring, Observability, and Open-Source.


  Perses'' developer surface includes documentation, API reference, GitHub presence, engineering blog, and 6 more developer resources.'
plans:
- name: Perses Plans Pricing
  plan_count: 3
  slug: perses-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Perses Rate Limits
  slug: perses-rate-limits
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 26.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/perses/refs/heads/main/screenshots/perses-2026-06-20T191616.png
security:
- kind: domain-security
  name: Perses Domain Security
  slug: perses-domain-security
  summary_line: TLSv1.3
slug: perses
tags:
- CNCF
- Dashboards
- Monitoring
- Observability
- Open-Source
- Time Series
- Visualization
website: https://perses.dev/
---
