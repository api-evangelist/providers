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
  band: agent-ready
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
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Planning Center Agentic Access
  operation_count: 61
  slug: planning-center-agentic-access
  summary_line: 61 operations · 10 acting
api_count: 9
apis:
- description: Church calendaring, events, and facility resources.
  name: Planning Center Calendar API
  slug: planning-center-calendar-api
- description: Attendance, events, locations, and stations.
  name: Planning Center Check-Ins API
  slug: planning-center-check-ins-api
- description: Donations, funds, batches, payment sources, and pledges.
  name: Planning Center Giving API
  slug: planning-center-giving-api
- description: Small groups, memberships, and group events.
  name: Planning Center Groups API
  slug: planning-center-groups-api
- description: People, households, contact info, lists, forms, and workflows.
  name: Planning Center People API
  slug: planning-center-people-api
- description: Sermon channels, series, episodes, and speakers (read-only).
  name: Planning Center Publishing API
  slug: planning-center-publishing-api
- description: Event signups, attendees, categories, and campuses.
  name: Planning Center Registrations API
  slug: planning-center-registrations-api
- description: Service planning - service types, plans, songs, teams.
  name: Planning Center Services API
  slug: planning-center-services-api
- description: Cross-product event subscriptions and deliveries.
  name: Planning Center Webhooks API
  slug: planning-center-webhooks-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Planning Center Calendar API
  slug: open-planning-center-calendar-api
- collection_type: open
  name: Planning Center Calendar Check-Ins API
  slug: open-planning-center-check-ins-api
- collection_type: open
  name: Planning Center Calendar Giving API
  slug: open-planning-center-giving-api
- collection_type: open
  name: Planning Center Calendar Groups API
  slug: open-planning-center-groups-api
- collection_type: open
  name: Planning Center Calendar People API
  slug: open-planning-center-people-api
- collection_type: open
  name: Planning Center Calendar Publishing API
  slug: open-planning-center-publishing-api
- collection_type: open
  name: Planning Center Calendar Registrations API
  slug: open-planning-center-registrations-api
- collection_type: open
  name: Planning Center Calendar Services API
  slug: open-planning-center-services-api
- collection_type: open
  name: Planning Center Calendar Webhooks API
  slug: open-planning-center-webhooks-api
- collection_type: open
  name: Planning Center API
  slug: open-planning-center
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/planning-center-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/planning-center-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/planning-center-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/planning-center-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/planning-center-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/planning-center-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/planningcenter
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/planning-center
- group: company
  title: ''
  type: Website
  url: https://www.planningcenter.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.planning.center/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/planning-center-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/planning-center-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/planning-center-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.planningcenter.com/feed
created: '2026-07-03'
description: Planning Center is a suite of church management software products - People, Services, Giving, Groups, Check-Ins, Calendar, Registrations, and Publishing - used by churches to organize their people, plan worship services, process online giving, run small groups, manage attendance and check-in, schedule facilities and events, handle event registrations, and publish sermons. Each product exposes a documented public REST API under a shared base URL (https://api.planningcenteronline.com), authenticated with OAuth 2.0 or a Personal Access Token and returning data in the JSON:API 1.0 format. A Webhooks API delivers create/update/destroy events across the products. The APIs are free to use with a Planning Center account; each product is subscribed to separately.
finops:
- name: Planning Center Finops
  service_category: Church Management Software
  slug: planning-center-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/planning-center.png
layout: provider
modified: '2026-07-03'
name: Planning Center
nav: Providers
network: true
overview: 'Planning Center publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Calendar API, Check-Ins API, Giving API, and 6 more. Tagged areas include Church Management, ChMS, Faith, Giving, and Events.


  Planning Center''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Planning Center Plans Pricing
  plan_count: 5
  slug: planning-center-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Planning Center Rate Limits
  slug: planning-center-rate-limits
scopes:
- name: Planning Center Scopes
  scope_count: 8
  slug: planning-center-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: thin
  composite: 37.9
  delta: -0.2
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 52.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Planning Center Authentication
  slug: planning-center-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Planning Center Domain Security
  slug: planning-center-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Planning Center Vulnerability Disclosure
  slug: planning-center-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Planning Center Trust Center
  slug: planning-center-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: planning-center
tags:
- Church Management
- ChMS
- Faith
- Giving
- Events
- Scheduling
- People
- Nonprofit
website: https://www.planningcenter.com
---
