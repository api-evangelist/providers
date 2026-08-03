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
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: Comprehensive REST API for Unit4 ERPx cloud ERP platform covering time and expenses, personnel, payroll, procurement, project management, customers and sales, inventory management, planning, commitmen
  name: Unit4 ERPx REST API
  slug: unit4-erpx-rest-api
- description: REST API for the Unit4 Access Point PEPPOL service enabling organizations to send and receive electronic business documents (invoices, orders) over the PEPPOL network. Uses Basic Authentication over H
  name: Unit4 Access Point REST API
  slug: unit4-access-point-rest-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unit4-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unit4-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unit4.com/
- group: docs
  title: ''
  type: Documentation
  url: https://develop.unit4rd.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Unit4
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unit4
- group: company
  title: ''
  type: Blog
  url: https://www.unit4.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unit4.com/contact-us
- group: operate
  title: ''
  type: StatusPage
  url: https://statusgator.com/services/df/unit4-erp
- group: other
  title: ''
  type: X
  url: https://twitter.com/unit4global
- group: commercial
  title: ''
  type: Plans
  url: plans/unit4-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unit4-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unit4-finops.yml
created: '2026-06-13'
description: Unit4 provides cloud ERP software for service-centric organizations including professional services, public sector, education, and non-profits. Their REST APIs cover financials, HR, payroll, project management, procurement, inventory, and business planning through the ERPx platform, plus PEPPOL-based electronic document exchange via Unit4 Access Point.
finops:
- name: Unit4 Finops
  service_category: ''
  slug: unit4-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unit4.png
layout: provider
modified: '2026-06-13'
name: Unit4
nav: Providers
network: true
overview: 'Unit4 publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ERP, Cloud ERP, Enterprise Resource Planning, Financials, and Human Resources.


  Unit4''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Unit4 Plans Pricing
  plan_count: 2
  slug: unit4-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 0
  name: Unit4 Rate Limits
  slug: unit4-rate-limits
score:
  band: emerging
  composite: 20.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unit4/refs/heads/main/screenshots/unit4-2026-06-20T200042.png
security:
- kind: domain-security
  name: Unit4 Domain Security
  slug: unit4-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Unit4 Vulnerability Disclosure
  slug: unit4-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: unit4
tags:
- ERP
- Cloud ERP
- Enterprise Resource Planning
- Financials
- Human Resources
- Payroll
- Project Management
- Procurement
- Inventory Management
- Business Planning
- PEPPOL
- E-Invoicing
- Service Organizations
- Public Sector
website: https://www.unit4.com/
---
