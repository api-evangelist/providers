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
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Hyperping Agentic Access
  operation_count: 35
  slug: hyperping-agentic-access
  summary_line: 35 operations · 22 acting
api_count: 7
apis:
- description: Cron-style monitors that expect periodic pings from scheduled tasks.
  name: Hyperping Healthchecks API
  slug: hyperping-healthchecks-api
- description: Status page incident lifecycle and updates.
  name: Hyperping Incidents API
  slug: hyperping-incidents-api
- description: Scheduled maintenance windows.
  name: Hyperping Maintenance API
  slug: hyperping-maintenance-api
- description: Create, retrieve, update, and delete uptime monitors.
  name: Hyperping Monitors API
  slug: hyperping-monitors-api
- description: On-call outage acknowledgement, resolution, and escalation.
  name: Hyperping Outages API
  slug: hyperping-outages-api
- description: Uptime, SLA, and MTTR reporting for monitors.
  name: Hyperping Reports API
  slug: hyperping-reports-api
- description: Public machine-readable status feed for a status page.
  name: Hyperping Status Pages API
  slug: hyperping-status-pages-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hyperping Healthchecks API
  slug: open-hyperping-healthchecks-api
- collection_type: open
  name: Hyperping Healthchecks Incidents API
  slug: open-hyperping-incidents-api
- collection_type: open
  name: Hyperping Healthchecks Maintenance API
  slug: open-hyperping-maintenance-api
- collection_type: open
  name: Hyperping Healthchecks Monitors API
  slug: open-hyperping-monitors-api
- collection_type: open
  name: Hyperping Healthchecks Outages API
  slug: open-hyperping-outages-api
- collection_type: open
  name: Hyperping Healthchecks Reports API
  slug: open-hyperping-reports-api
- collection_type: open
  name: Hyperping Healthchecks Status Pages API
  slug: open-hyperping-status-pages-api
- collection_type: open
  name: Hyperping API
  slug: open-hyperping
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperping-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperping-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hyperping-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hyperping
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyperping
- group: company
  title: ''
  type: Website
  url: https://hyperping.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hyperping.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/hyperping-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hyperping-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hyperping-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://hyperping.com/blog
created: '2026-06-21'
description: Hyperping is an uptime monitoring and status page platform. Its REST API lets teams programmatically manage HTTP, ping, port, keyword, DNS, and browser monitors, run scheduled-task healthchecks, operate public status pages through incidents and maintenance windows, manage on-call outages, and pull uptime and SLA reporting.
finops:
- name: Hyperping Finops
  service_category: Management and Governance
  slug: hyperping-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyperping.png
layout: provider
modified: '2026-06-21'
name: Hyperping
nav: Providers
network: true
overview: 'Hyperping publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Healthchecks API, Incidents API, Maintenance API, and 4 more. Tagged areas include Uptime Monitoring, Status Pages, Incident Management, Observability, and On-Call.


  Hyperping''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Hyperping Plans Pricing
  plan_count: 5
  slug: hyperping-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Hyperping Rate Limits
  slug: hyperping-rate-limits
score:
  band: thin
  composite: 38.1
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperping/refs/heads/main/screenshots/hyperping-2026-07-25T221925.png
security:
- kind: authentication
  name: Hyperping Authentication
  slug: hyperping-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hyperping Domain Security
  slug: hyperping-domain-security
  summary_line: TLSv1.3 · HSTS
slug: hyperping
tags:
- Uptime Monitoring
- Status Pages
- Incident Management
- Observability
- On-Call
website: https://hyperping.com/
---
