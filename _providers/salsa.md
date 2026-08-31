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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Salsa Agentic Access
  operation_count: 42
  slug: salsa-agentic-access
  summary_line: 42 operations · 25 acting
api_count: 1
apis:
- description: Employer (company) entities and configuration.
  name: Salsa Companies API
  slug: salsa-companies-api
- description: User tokens, hosted onboarding, and mock onboarding.
  name: Salsa Onboarding & Sessions API
  slug: salsa-onboarding-sessions-api
- description: Worker pay groups and work weeks.
  name: Salsa Pay Schedules API
  slug: salsa-pay-schedules-api
- description: Individual worker payments and disbursements.
  name: Salsa Payments API
  slug: salsa-payments-api
- description: Payroll runs and reports.
  name: Salsa Payrolls API
  slug: salsa-payrolls-api
- description: Employer and worker tax setup.
  name: Salsa Tax API
  slug: salsa-tax-api
- description: Webhook endpoint management.
  name: Salsa Webhooks API
  slug: salsa-webhooks-api
- description: Employees and contractors.
  name: Salsa Workers API
  slug: salsa-workers-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salsa Payroll Companies API
  slug: open-salsa-companies-api
- collection_type: open
  name: Salsa Payroll Companies Onboarding & Sessions API
  slug: open-salsa-onboarding-sessions-api
- collection_type: open
  name: Salsa Payroll Companies Pay Schedules API
  slug: open-salsa-pay-schedules-api
- collection_type: open
  name: Salsa Payroll Companies Payments API
  slug: open-salsa-payments-api
- collection_type: open
  name: Salsa Payroll Companies Payrolls API
  slug: open-salsa-payrolls-api
- collection_type: open
  name: Salsa Payroll Companies Tax API
  slug: open-salsa-tax-api
- collection_type: open
  name: Salsa Payroll Companies Webhooks API
  slug: open-salsa-webhooks-api
- collection_type: open
  name: Salsa Payroll Companies Workers API
  slug: open-salsa-workers-api
- collection_type: open
  name: Salsa Payroll API
  slug: open-salsa
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salsa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salsa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salsa-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salsa-payroll
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/salsa-dev
- group: company
  title: ''
  type: Website
  url: https://www.salsa.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.salsa.dev/
- group: commercial
  title: ''
  type: Plans
  url: plans/salsa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/salsa-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/salsa-finops.yml
created: '2026-07-01'
description: Salsa is embedded payroll infrastructure that lets SaaS platforms add native, multi-country (US and Canada) payroll to their products through REST and GraphQL APIs, embeddable UI components (Salsa Express), and real-time webhooks. Partner platforms provision employers and workers, run payroll, disburse worker payments, and handle tax setup and filings without leaving their own app. API access is partner-gated - Salsa issues sandbox and production Bearer API keys to approved platform partners.
finops:
- name: Salsa Finops
  service_category: Payroll and Embedded Finance
  slug: salsa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salsa.png
layout: provider
modified: '2026-07-01'
name: Salsa
nav: Providers
network: true
overview: 'Salsa publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Onboarding & Sessions API, Pay Schedules API, and 5 more. Tagged areas include Payroll, Embedded Finance, Payroll as a Service, Fintech, and Payments.


  Salsa''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Salsa Plans Pricing
  plan_count: 3
  slug: salsa-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Salsa Rate Limits
  slug: salsa-rate-limits
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Salsa Authentication
  slug: salsa-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Salsa Domain Security
  slug: salsa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: salsa
tags:
- Payroll
- Embedded Finance
- Payroll as a Service
- Fintech
- Payments
- HR
- Tax
- Multi-Country
website: https://www.salsa.dev/
---
