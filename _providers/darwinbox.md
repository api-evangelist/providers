---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: REST API for Darwinbox HRMS covering employee management, attendance, recruitment, organizational management, payroll, background verification, project management, and travel. Authentication uses toke
  name: Darwinbox API
  slug: darwinbox-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/darwinbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://darwinbox.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.darwinbox.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/darwinbox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thedarwinbox
- group: company
  title: ''
  type: Blog
  url: https://darwinbox.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://explore.darwinbox.com/lp/request-a-quote
- group: operate
  title: ''
  type: StatusPage
  url: https://darwinbox.com
- group: other
  title: ''
  type: X
  url: https://x.com/thedarwinbox
- group: commercial
  title: ''
  type: Plans
  url: plans/darwinbox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/darwinbox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/darwinbox-finops.yml
created: '2026-06-13'
description: Darwinbox is a cloud-based HRMS platform offering a REST API for managing employee records, recruitment, performance, payroll, attendance, travel, and workforce analytics in enterprise organizations. The API supports programmatic access to data stored in Darwinbox instances and enables importing data into the platform. Access is provided on a request-only basis to privileged users and supports token-based authentication using SHA512 hashing.
finops:
- name: Darwinbox Finops
  service_category: ''
  slug: darwinbox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/darwinbox.png
layout: provider
modified: '2026-06-13'
name: Darwinbox
nav: Providers
network: true
overview: 'Darwinbox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include HRMS, HR, Human Resources, Payroll, and Recruitment.


  Darwinbox''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Darwinbox Plans Pricing
  plan_count: 1
  slug: darwinbox-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Darwinbox Rate Limits
  slug: darwinbox-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/darwinbox/refs/heads/main/screenshots/darwinbox-2026-06-20T175524.png
security:
- kind: domain-security
  name: Darwinbox Domain Security
  slug: darwinbox-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: darwinbox
tags:
- HRMS
- HR
- Human Resources
- Payroll
- Recruitment
- Performance Management
- Attendance
- Workforce Analytics
- Enterprise
- HCM
website: https://darwinbox.com
---
