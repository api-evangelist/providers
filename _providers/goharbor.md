---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Goharbor Agentic Access
  operation_count: 38
  slug: goharbor-agentic-access
  summary_line: 38 operations · 14 acting
api_count: 14
apis:
- description: The artifacts API from GoHarbor — 2 operation(s) for artifacts.
  name: GoHarbor artifacts API
  slug: goharbor-artifacts-api
- description: The audit API from GoHarbor — 1 operation(s) for audit.
  name: GoHarbor audit API
  slug: goharbor-audit-api
- description: The health API from GoHarbor — 2 operation(s) for health.
  name: GoHarbor health API
  slug: goharbor-health-api
- description: The projects API from GoHarbor — 4 operation(s) for projects.
  name: GoHarbor projects API
  slug: goharbor-projects-api
- description: The quotas API from GoHarbor — 2 operation(s) for quotas.
  name: GoHarbor quotas API
  slug: goharbor-quotas-api
- description: The registries API from GoHarbor — 1 operation(s) for registries.
  name: GoHarbor registries API
  slug: goharbor-registries-api
- description: The replication API from GoHarbor — 2 operation(s) for replication.
  name: GoHarbor replication API
  slug: goharbor-replication-api
- description: The repositories API from GoHarbor — 3 operation(s) for repositories.
  name: GoHarbor repositories API
  slug: goharbor-repositories-api
- description: The robots API from GoHarbor — 2 operation(s) for robots.
  name: GoHarbor robots API
  slug: goharbor-robots-api
- description: The scan API from GoHarbor — 1 operation(s) for scan.
  name: GoHarbor scan API
  slug: goharbor-scan-api
- description: The search API from GoHarbor — 1 operation(s) for search.
  name: GoHarbor search API
  slug: goharbor-search-api
- description: The tags API from GoHarbor — 1 operation(s) for tags.
  name: GoHarbor tags API
  slug: goharbor-tags-api
- description: The usergroups API from GoHarbor — 2 operation(s) for usergroups.
  name: GoHarbor usergroups API
  slug: goharbor-usergroups-api
- description: The webhooks API from GoHarbor — 1 operation(s) for webhooks.
  name: GoHarbor webhooks API
  slug: goharbor-webhooks-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Harbor artifacts API
  slug: open-goharbor-artifacts-api
- collection_type: open
  name: Harbor artifacts audit API
  slug: open-goharbor-audit-api
- collection_type: open
  name: Harbor artifacts health API
  slug: open-goharbor-health-api
- collection_type: open
  name: Harbor artifacts projects API
  slug: open-goharbor-projects-api
- collection_type: open
  name: Harbor artifacts quotas API
  slug: open-goharbor-quotas-api
- collection_type: open
  name: Harbor artifacts registries API
  slug: open-goharbor-registries-api
- collection_type: open
  name: Harbor artifacts replication API
  slug: open-goharbor-replication-api
- collection_type: open
  name: Harbor artifacts repositories API
  slug: open-goharbor-repositories-api
- collection_type: open
  name: Harbor artifacts robots API
  slug: open-goharbor-robots-api
- collection_type: open
  name: Harbor artifacts scan API
  slug: open-goharbor-scan-api
- collection_type: open
  name: Harbor artifacts search API
  slug: open-goharbor-search-api
- collection_type: open
  name: Harbor artifacts tags API
  slug: open-goharbor-tags-api
- collection_type: open
  name: Harbor artifacts usergroups API
  slug: open-goharbor-usergroups-api
- collection_type: open
  name: Harbor artifacts webhooks API
  slug: open-goharbor-webhooks-api
- collection_type: open
  name: Harbor API
  slug: open-goharbor
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/goharbor/harbor/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/goharbor/harbor/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/goharbor/harbor/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/goharbor/harbor/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/goharbor/harbor/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/goharbor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goharbor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/goharbor-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://goharbor.io/
- group: docs
  title: ''
  type: Documentation
  url: https://goharbor.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goharbor
- group: company
  title: ''
  type: Blog
  url: https://goharbor.io/blog/index.xml
created: '2025-02-17'
description: You can view and test the Harbor REST API from your Harbor interface using the Swagger UI. This means that you can invoke all APIs through the Harbor interface. You can navigate to the REST API through the Harbor portal, or by navigate to the Swagger UI using your Harbor instance IP.
finops:
- name: Goharbor Finops
  service_category: API
  slug: goharbor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goharbor.png
layout: provider
modified: '2026-04-28'
name: GoHarbor
nav: Providers
network: true
overview: 'GoHarbor publishes 14 APIs on the [APIs.io](https://apis.io/) network, including artifacts API, audit API, health API, and 11 more. Tagged areas include Container Registry.


  GoHarbor''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Goharbor Plans Pricing
  plan_count: 3
  slug: goharbor-plans-pricing
random_paper: 107
rate_limits:
- limit_count: 5
  name: Goharbor Rate Limits
  slug: goharbor-rate-limits
score:
  band: thin
  composite: 30.8
  delta: -0.3
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 50.0
    developer_ergonomics: 23.8
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goharbor/refs/heads/main/screenshots/goharbor-2026-06-20T181946.png
security:
- kind: authentication
  name: Goharbor Authentication
  slug: goharbor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Goharbor Domain Security
  slug: goharbor-domain-security
  summary_line: TLSv1.3 · HSTS
slug: goharbor
tags:
- Container Registry
website: https://goharbor.io/
---
