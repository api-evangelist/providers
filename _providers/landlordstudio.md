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
- description: Landlord Studio provides a property management platform with capabilities for managing rental properties, tracking income and expenses, generating financial reports, collecting rent online, and managi
  name: Landlord Studio API
  slug: landlordstudio-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/landlordstudio-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/landlordstudio/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/landlordstudio/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/landlordstudio/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.landlordstudio.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.landlordstudio.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.landlordstudio.com
- group: company
  title: ''
  type: About
  url: https://www.landlordstudio.com/about
created: '2026-06-13'
description: Landlord Studio is a property management platform founded in 2014 that helps landlords and property managers track rental income and expenses, collect rent online, screen tenants, manage documents, and generate financial reports including Schedule E tax-ready summaries. The platform integrates with Xero for accounting synchronization and Plaid for bank feed connectivity. Nexus by Landlord Studio is a Making Tax Digital (MTD) compliance layer for UK letting agents connecting to Reapit, PayProp, SME Professional, LettsPay, and Alto.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/landlordstudio.png
layout: provider
modified: '2026-06-13'
name: Landlord Studio
nav: Providers
network: true
overview: 'Landlord Studio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Real Estate, Rental Income, Expense Tracking, and Tenant Screening.


  Landlord Studio''s developer surface includes pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 36
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 18.2
  delta: -2.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/landlordstudio/refs/heads/main/screenshots/landlordstudio-2026-06-20T184258.png
security:
- kind: domain-security
  name: Landlordstudio Domain Security
  slug: landlordstudio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: landlordstudio
tags:
- Property Management
- Real Estate
- Rental Income
- Expense Tracking
- Tenant Screening
- Rent Collection
- Financial Reporting
- Accounting
- Making Tax Digital
- MTD
---
