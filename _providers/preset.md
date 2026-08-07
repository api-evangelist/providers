---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Preset Agentic Access
  operation_count: 21
  slug: preset-agentic-access
  summary_line: 21 operations · 11 acting
api_count: 8
apis:
- description: The Authentication API from Preset — 1 operation(s) for authentication.
  name: Preset Authentication API
  slug: preset-authentication-api
- description: The Charts API from Preset — 3 operation(s) for charts.
  name: Preset Charts API
  slug: preset-charts-api
- description: The Dashboards API from Preset — 2 operation(s) for dashboards.
  name: Preset Dashboards API
  slug: preset-dashboards-api
- description: The Databases API from Preset — 2 operation(s) for databases.
  name: Preset Databases API
  slug: preset-databases-api
- description: The Datasets API from Preset — 2 operation(s) for datasets.
  name: Preset Datasets API
  slug: preset-datasets-api
- description: The SQL Lab API from Preset — 1 operation(s) for sql lab.
  name: Preset SQL Lab API
  slug: preset-sql-lab-api
- description: The Teams API from Preset — 1 operation(s) for teams.
  name: Preset Teams API
  slug: preset-teams-api
- description: The Workspaces API from Preset — 2 operation(s) for workspaces.
  name: Preset Workspaces API
  slug: preset-workspaces-api
artifact_total: 15
collections:
- collection_type: open
  name: Preset API
  slug: open-preset
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/preset-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/preset-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/preset-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/preset-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/preset-data
- group: company
  title: ''
  type: Website
  url: https://www.preset.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.preset.io
- group: commercial
  title: ''
  type: Plans
  url: plans/preset-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/preset-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/preset-finops.yml
created: '2026-06-20'
description: Preset is a managed cloud BI and analytics platform powered by Apache Superset. Its REST API combines a Preset Manager surface (authentication, teams, workspaces, users, guest tokens) at https://api.app.preset.io with a per-workspace proxy to the underlying Superset REST API for charts, dashboards, datasets, databases, and SQL Lab.
finops:
- name: Preset Finops
  service_category: Analytics and Business Intelligence
  slug: preset-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/preset.png
layout: provider
modified: '2026-06-20'
name: Preset
nav: Providers
network: true
overview: 'Preset publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Charts API, Dashboards API, and 5 more. Tagged areas include BI, Analytics, Superset, Dashboards, and Data Visualization.


  Preset''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Preset Plans Pricing
  plan_count: 3
  slug: preset-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 5
  name: Preset Rate Limits
  slug: preset-rate-limits
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/preset/refs/heads/main/screenshots/preset-2026-06-20T192138.png
security:
- kind: authentication
  name: Preset Authentication
  slug: preset-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Preset Domain Security
  slug: preset-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: preset
tags:
- BI
- Analytics
- Superset
- Dashboards
- Data Visualization
website: https://www.preset.io
---
