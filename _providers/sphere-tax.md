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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sphere Tax Agentic Access
  operation_count: 4
  slug: sphere-tax-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 2
apis:
- description: The Tax Calculation API from Sphere — 1 operation(s) for tax calculation.
  name: Sphere Tax Calculation API
  slug: sphere-tax-tax-calculation-api
- description: The Transactions Export API from Sphere — 3 operation(s) for transactions export.
  name: Sphere Transactions Export API
  slug: sphere-tax-transactions-export-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sphere Tax Tax Calculation API
  slug: open-sphere-tax-tax-calculation-api
- collection_type: open
  name: Sphere Tax Tax Calculation Transactions Export API
  slug: open-sphere-tax-transactions-export-api
- collection_type: open
  name: Sphere Tax API
  slug: open-sphere-tax
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sphere-tax-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sphere-tax-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sphere-tax-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getsphere
- group: company
  title: ''
  type: Website
  url: https://www.getsphere.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getsphere.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/sphere-tax-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sphere-tax-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sphere-tax-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.getsphere.com/blog
created: '2026-06-21'
description: Sphere is a developer-first global indirect tax compliance platform that automates sales tax, VAT, and GST across nexus monitoring, registration, real-time calculation, and filing/remittance. Its REST API lets billing and checkout flows call the Sphere tax engine to calculate tax on transactions and export transaction data, authenticated with an X-API-KEY header.
finops:
- name: Sphere Tax Finops
  service_category: Tax and Compliance
  slug: sphere-tax-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sphere-tax.png
layout: provider
modified: '2026-06-21'
name: Sphere
nav: Providers
network: true
overview: 'Sphere publishes 2 APIs on the [APIs.io](https://apis.io/) network: Tax Calculation API and Transactions Export API. Tagged areas include Tax, Sales Tax, VAT, GST, and Compliance.


  Sphere''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Sphere Tax Plans Pricing
  plan_count: 2
  slug: sphere-tax-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Sphere Tax Rate Limits
  slug: sphere-tax-rate-limits
score:
  band: thin
  composite: 37.1
  delta: 2.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 58.2
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Sphere Tax Authentication
  slug: sphere-tax-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sphere Tax Domain Security
  slug: sphere-tax-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sphere-tax
tags:
- Tax
- Sales Tax
- VAT
- GST
- Compliance
- Fintech
website: https://www.getsphere.com/
---
