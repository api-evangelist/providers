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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Plane So Agentic Access
  operation_count: 48
  slug: plane-so-agentic-access
  summary_line: 48 operations · 29 acting
api_count: 11
apis:
- description: The Cycle Work Items API from Plane — 3 operation(s) for cycle work items.
  name: Plane Cycle Work Items API
  slug: plane-so-cycle-work-items-api
- description: The Cycles API from Plane — 2 operation(s) for cycles.
  name: Plane Cycles API
  slug: plane-so-cycles-api
- description: The Labels API from Plane — 2 operation(s) for labels.
  name: Plane Labels API
  slug: plane-so-labels-api
- description: The Members API from Plane — 1 operation(s) for members.
  name: Plane Members API
  slug: plane-so-members-api
- description: The Module Work Items API from Plane — 2 operation(s) for module work items.
  name: Plane Module Work Items API
  slug: plane-so-module-work-items-api
- description: The Modules API from Plane — 2 operation(s) for modules.
  name: Plane Modules API
  slug: plane-so-modules-api
- description: The Projects API from Plane — 2 operation(s) for projects.
  name: Plane Projects API
  slug: plane-so-projects-api
- description: The States API from Plane — 2 operation(s) for states.
  name: Plane States API
  slug: plane-so-states-api
- description: The Work Item Comments API from Plane — 2 operation(s) for work item comments.
  name: Plane Work Item Comments API
  slug: plane-so-work-item-comments-api
- description: The Work Item Links API from Plane — 2 operation(s) for work item links.
  name: Plane Work Item Links API
  slug: plane-so-work-item-links-api
- description: The Work Items API from Plane — 2 operation(s) for work items.
  name: Plane Work Items API
  slug: plane-so-work-items-api
artifact_total: 19
collections:
- collection_type: open
  name: Plane API
  slug: open-plane-so
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plane-so-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/plane-so-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plane-so-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plane-so-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/makeplane
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/planepowers
- group: company
  title: ''
  type: Website
  url: https://plane.so
- group: docs
  title: ''
  type: Documentation
  url: https://developers.plane.so
- group: commercial
  title: ''
  type: Plans
  url: plans/plane-so-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/plane-so-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/plane-so-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://plane.so/blog
created: '2026-06-21'
description: Plane is an open-source project and product management tool for planning, tracking, and shipping work across workspaces, projects, cycles, and modules. It is available as a self-hosted Community Edition (AGPL v3.0) and as Plane Cloud, and exposes a REST API at https://api.plane.so/api/v1 secured with an X-API-Key header for managing projects, work items, cycles, modules, states, labels, and members.
finops:
- name: Plane So Finops
  service_category: Developer Tools and Productivity
  slug: plane-so-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plane-so.png
layout: provider
modified: '2026-06-21'
name: Plane
nav: Providers
network: true
overview: 'Plane publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Cycle Work Items API, Cycles API, Labels API, and 8 more. Tagged areas include Project Management, Issue Tracking, Work Management, Open Source, and Productivity.


  Plane''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Plane So Plans Pricing
  plan_count: 6
  slug: plane-so-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Plane So Rate Limits
  slug: plane-so-rate-limits
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Plane So Authentication
  slug: plane-so-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Plane So Domain Security
  slug: plane-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Plane So Trust Center
  slug: plane-so-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: plane-so
tags:
- Project Management
- Issue Tracking
- Work Management
- Open Source
- Productivity
website: https://plane.so
---
