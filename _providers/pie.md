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
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API for approved partners to access Pie Insurance workers compensation quoting and binding workflows. Supports appetite checking, price indication, quote submission, document upload, and retrieva
  name: Pie Insurance Partner API
  slug: pie-partner-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pieinsurance.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.pieinsurance.com/agency/api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/PieInsurance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pieinsurance
- group: company
  title: ''
  type: Blog
  url: https://www.pieinsurance.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pieinsurance.com/agency/api
- group: operate
  title: ''
  type: StatusPage
  url: https://www.pieinsurance.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/pie_insurance
- group: commercial
  title: ''
  type: Plans
  url: plans/pie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pie-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pie-finops.yml
created: '2026-06-13'
description: Pie Insurance is a small business workers compensation insurance platform that provides a REST API for approved partners to quote, bind, and manage workers comp policies. The partner API supports appetite checking, price indication, quote submission, document upload, and retrieval of bindable quotes, enabling agencies, aggregators, and technology platforms to embed workers comp quoting directly into their own workflows. Pie targets small businesses across 39 states and Washington D.C., using data-driven underwriting to offer savings of up to 30% versus traditional carriers. Payroll-based premium calculations and policy management including certificates of insurance are central to the platform.
finops:
- name: Pie Finops
  service_category: ''
  slug: pie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pie.png
layout: provider
modified: '2026-06-13'
name: Pie Insurance
nav: Providers
network: true
overview: 'Pie Insurance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Workers Compensation, Small Business, Insurtech, and Quoting.


  Pie Insurance''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Pie Plans Pricing
  plan_count: 1
  slug: pie-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 0
  name: Pie Rate Limits
  slug: pie-rate-limits
score:
  band: emerging
  composite: 18.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pie/refs/heads/main/screenshots/pie-2026-06-20T191702.png
security:
- kind: domain-security
  name: Pie Domain Security
  slug: pie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pie
tags:
- Insurance
- Workers Compensation
- Small Business
- Insurtech
- Quoting
- Policy Management
- Certificates of Insurance
- Payroll
website: https://www.pieinsurance.com
---
