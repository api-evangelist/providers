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
- acting_count: 9
  human_in_the_loop: 0
  name: Sequence Hq Agentic Access
  operation_count: 20
  slug: sequence-hq-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 1
apis:
- description: Recurring contract terms that generate invoices.
  name: Sequence Billing Schedules API
  slug: sequence-hq-billing-schedules-api
- description: Billable customer entities, contacts, and aliases.
  name: Sequence Customers API
  slug: sequence-hq-customers-api
- description: Invoice and credit note lifecycle.
  name: Sequence Invoices API
  slug: sequence-hq-invoices-api
- description: Product and price catalog.
  name: Sequence Products API
  slug: sequence-hq-products-api
- description: Quotes and quote analytics.
  name: Sequence Quotes API
  slug: sequence-hq-quotes-api
- description: Usage event ingestion, usage metrics, and seats.
  name: Sequence Usage API
  slug: sequence-hq-usage-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sequence Billing Schedules API
  slug: open-sequence-hq-billing-schedules-api
- collection_type: open
  name: Sequence Billing Schedules Customers API
  slug: open-sequence-hq-customers-api
- collection_type: open
  name: Sequence Billing Schedules Invoices API
  slug: open-sequence-hq-invoices-api
- collection_type: open
  name: Sequence Billing Schedules Products API
  slug: open-sequence-hq-products-api
- collection_type: open
  name: Sequence Billing Schedules Quotes API
  slug: open-sequence-hq-quotes-api
- collection_type: open
  name: Sequence Billing Schedules Usage API
  slug: open-sequence-hq-usage-api
- collection_type: open
  name: Sequence API
  slug: open-sequence-hq
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sequence-hq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sequence-hq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sequence-hq-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sequencehq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sequence-hq
- group: company
  title: ''
  type: Website
  url: https://www.sequencehq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sequencehq.com
- group: commercial
  title: ''
  type: Plans
  url: plans/sequence-hq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sequence-hq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sequence-hq-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.sequencehq.com/blog
created: '2026-07-12'
description: Sequence is a usage-based billing, pricing, and revenue orchestration platform for B2B SaaS and other recurring-revenue businesses. It turns product usage and negotiated contract terms into automated billing schedules, invoices, credit notes, and quotes, backed by a metering engine for usage events and usage metrics, plus revenue recognition and integrations to ERP/CRM, tax, and payment providers. The REST API (production base https://eu.sequencehq.com) uses HTTP Basic authentication with a Client ID and Client Secret, date-based API versioning (for example sequence-version 2024-07-30), and signed webhooks for event notifications. A Sandbox environment (https://sandbox.sequencehq.com) mirrors production for testing.
finops:
- name: Sequence Hq Finops
  service_category: Financial Operations and Billing
  slug: sequence-hq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sequence-hq.png
layout: provider
modified: '2026-07-12'
name: Sequence
nav: Providers
network: true
overview: 'Sequence publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Billing Schedules API, Customers API, Invoices API, and 3 more. Tagged areas include Billing, Usage-Based Billing, Revenue Recognition, Metering, and Invoicing.


  Sequence''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sequence Hq Plans Pricing
  plan_count: 3
  slug: sequence-hq-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Sequence Hq Rate Limits
  slug: sequence-hq-rate-limits
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 13.9
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 83.3
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Sequence Hq Authentication
  slug: sequence-hq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sequence Hq Domain Security
  slug: sequence-hq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sequence-hq
tags:
- Billing
- Usage-Based Billing
- Revenue Recognition
- Metering
- Invoicing
- Pricing
- Revenue Orchestration
- FinOps
website: https://www.sequencehq.com
---
