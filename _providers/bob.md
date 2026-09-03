---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST API for the HiBob HR platform providing programmatic access to employee data, time off management, attendance, tasks, reports, documents, goals, job catalog, workforce planning, hiring, and learn
  name: HiBob Bob API
  slug: bob-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bob-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hibob.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.hibob.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/speakeasy-sdks/hibob
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hibob
- group: company
  title: ''
  type: Blog
  url: https://www.hibob.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hibob.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hibob.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/HiBob_HR
- group: commercial
  title: ''
  type: Plans
  url: plans/bob-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bob-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bob-finops.yml
created: '2026-06-13'
description: HiBob is a modern HR platform (known as Bob) offering a REST API for managing employee profiles, onboarding, time off, attendance, payroll integration, goals, documents, workforce planning, and company culture data. The API supports service user authentication and webhooks for event-driven integrations across HR workflows.
finops:
- name: Bob Finops
  service_category: ''
  slug: bob-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bob.png
layout: provider
modified: '2026-06-13'
name: HiBob
nav: Providers
network: true
overview: 'HiBob publishes 1 API on the [APIs.io](https://apis.io/) network: Bob API. Tagged areas include HR, Human Resources, HRIS, Employee Management, and Time Off.


  HiBob''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Bob Plans Pricing
  plan_count: 5
  slug: bob-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Bob Rate Limits
  slug: bob-rate-limits
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 30.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bob/refs/heads/main/screenshots/bob-2026-06-20T173550.png
security:
- kind: domain-security
  name: Bob Domain Security
  slug: bob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bob
tags:
- HR
- Human Resources
- HRIS
- Employee Management
- Time Off
- Attendance
- Payroll
- Workforce Planning
- Onboarding
- Goals
- OKR
website: https://www.hibob.com/
---
