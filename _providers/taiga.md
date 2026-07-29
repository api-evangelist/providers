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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Full-featured REST API for the Taiga agile project management platform, providing programmatic access to projects, milestones, epics, user stories, tasks, issues, wiki pages, webhooks, timelines, user
  name: Taiga REST API
  slug: taiga-rest-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/taiga-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/taiga-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taiga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://taiga.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.taiga.io/api.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/taigaio/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/taigaio
- group: company
  title: ''
  type: Blog
  url: https://blog.taiga.io
- group: commercial
  title: ''
  type: Pricing
  url: https://taiga.io/deployment-pricing-options/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.taiga.io
- group: other
  title: ''
  type: X
  url: https://twitter.com/taigaio
- group: commercial
  title: ''
  type: Plans
  url: plans/taiga-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/taiga-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/taiga-finops.yml
created: '2026-06-13'
description: Taiga is an open-source agile project management platform with a comprehensive REST API for managing projects, sprints, user stories, issues, tasks, epics, wiki pages, webhooks, and team member assignments. The API supports both standard bearer token and application token authentication, with optional server-side throttling. Available as a cloud-hosted service or self-hosted deployment.
finops:
- name: Taiga Finops
  service_category: ''
  slug: taiga-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taiga.png
layout: provider
modified: '2026-06-13'
name: Taiga
nav: Providers
network: true
overview: 'Taiga publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agile, Project Management, Scrum, Kanban, and Issue Tracking.


  Taiga''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Taiga Plans Pricing
  plan_count: 6
  slug: taiga-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 2
  name: Taiga Rate Limits
  slug: taiga-rate-limits
score:
  band: emerging
  composite: 26.1
  delta: -2.4
  facets:
    commercial_clarity: 57.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 28.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taiga/refs/heads/main/screenshots/taiga-2026-06-20T194855.png
security:
- kind: domain-security
  name: Taiga Domain Security
  slug: taiga-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Taiga Vulnerability Disclosure
  slug: taiga-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Taiga Trust Center
  slug: taiga-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: taiga
tags:
- Agile
- Project Management
- Scrum
- Kanban
- Issue Tracking
- Open Source
- Sprints
- User Stories
- Epics
- Tasks
website: https://taiga.io
---
