---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.5
  scored_at: '2026-11-06'
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
- baseURL_template: http://{persesHost}
  baseurl_source: spec_template
  description: Manage dashboards inside a project.
  name: Perses Dashboards API
  slug: perses-dashboards-api
- baseURL_template: http://{persesHost}
  baseurl_source: spec_template
  description: Manage shared datasources across projects.
  name: Perses Global Datasources API
  slug: perses-global-datasources-api
- baseURL_template: http://{persesHost}
  baseurl_source: spec_template
  description: Manage Perses projects (workspaces).
  name: Perses Projects API
  slug: perses-projects-api
- baseURL_template: http://{persesHost}
  baseurl_source: spec_template
  description: Manage project-scoped datasources.
  name: Perses Data Sources API
  slug: perses-data-sources-api
artifact_total: 17
collections:
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
- group: commercial
  href: https://artifacts.apis.io/perses/plans/perses-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/perses-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/perses/rate-limits/perses-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/perses-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/perses/finops/perses-finops.yml
  title: ''
  type: FinOps
  url: finops/perses-finops.yml
- group: other
  href: https://artifacts.apis.io/perses/capabilities/perses-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/perses-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/perses/agentic-access/perses-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/perses-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/perses/security/perses-domain-security.yml
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
- has_sources: false
  method: generated
  name: Perses Finops
  primary_unit: request
  service_category: API
  slug: perses-finops
  template: true
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
overview: 'Perses publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dashboards API, Global Datasources API, Projects API, and 2 more. Tagged areas include CNCF, Dashboards, Monitoring, Observability, and Open Source.


  The Perses catalog on APIs.io includes 1 Spectral governance ruleset.


  Perses'' developer surface includes documentation, API reference, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Perses Plans Pricing
  plan_count: 3
  slug: perses-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Perses Rate Limits
  slug: perses-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Perses API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: perses-rules
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 41.4
    developer_ergonomics: 21.4
    discoverability: 56.7
    operational_transparency: 10.5
  previous_composite: 22.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/perses/perses-2026-06-20T191616.png
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
- Open Source
- Time Series
- Visualization
website: https://perses.dev/
---
