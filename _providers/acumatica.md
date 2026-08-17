---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Contract-based REST API for Acumatica ERP providing programmatic access to financial management, order management, inventory, purchasing, project accounting, CRM, and manufacturing modules. Over 200 d
  name: Acumatica REST API
  slug: acumatica-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acumatica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acumatica.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.acumatica.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/acumatica
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acumatica
- group: company
  title: ''
  type: Blog
  url: https://www.acumatica.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acumatica.com/acumatica-erp-pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.acumatica.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/Acumatica
- group: commercial
  title: ''
  type: Plans
  url: plans/acumatica-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acumatica-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/acumatica-finops.yml
created: '2026-06-13'
description: Acumatica is a cloud ERP platform with a contract-based REST API for managing financial data, inventory, projects, manufacturing, distribution, and business management workflows. The API exposes over 200 default endpoints covering financial management, order management, inventory, purchasing, project accounting, and CRM modules. Endpoints are versioned by release (e.g., 24.200.001 for 2024 R2) and authenticate via OAuth 2.0 or cookie-based sessions.
finops:
- name: Acumatica Finops
  service_category: ''
  slug: acumatica-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acumatica.png
layout: provider
modified: '2026-06-13'
name: Acumatica
nav: Providers
network: true
overview: 'Acumatica publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include ERP, Cloud ERP, Financial Management, Inventory, and Manufacturing.


  Acumatica''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Acumatica Plans Pricing
  plan_count: 4
  slug: acumatica-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 3
  name: Acumatica Rate Limits
  slug: acumatica-rate-limits
score:
  band: thin
  composite: 33.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 33.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acumatica/refs/heads/main/screenshots/acumatica-2026-06-20T164429.png
security:
- kind: domain-security
  name: Acumatica Domain Security
  slug: acumatica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acumatica
tags:
- ERP
- Cloud ERP
- Financial Management
- Inventory
- Manufacturing
- Distribution
- Project Accounting
- CRM
- Business Management
website: https://www.acumatica.com/
---
