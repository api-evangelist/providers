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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Kintsugi Agentic Access
  operation_count: 39
  slug: kintsugi-agentic-access
  summary_line: 39 operations · 17 acting
api_count: 9
apis:
- description: Address search and suggestions for jurisdiction assignment.
  name: Kintsugi Address Validation API
  slug: kintsugi-address-validation-api
- description: Customer records and their transactions.
  name: Kintsugi Customers API
  slug: kintsugi-customers-api
- description: Customer tax exemptions and certificates.
  name: Kintsugi Exemptions API
  slug: kintsugi-exemptions-api
- description: Prepared and submitted sales tax returns.
  name: Kintsugi Filings API
  slug: kintsugi-filings-api
- description: Physical and economic nexus tracking.
  name: Kintsugi Nexus API
  slug: kintsugi-nexus-api
- description: Product records and taxability classification.
  name: Kintsugi Products API
  slug: kintsugi-products-api
- description: State tax registrations.
  name: Kintsugi Registrations API
  slug: kintsugi-registrations-api
- description: Real-time sales tax, VAT, and GST estimation.
  name: Kintsugi Tax Estimation API
  slug: kintsugi-tax-estimation-api
- description: Committed sales transactions and credit notes.
  name: Kintsugi Transactions API
  slug: kintsugi-transactions-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kintsugi Tax Address Validation API
  slug: open-kintsugi-address-validation-api
- collection_type: open
  name: Kintsugi Tax Address Validation Customers API
  slug: open-kintsugi-customers-api
- collection_type: open
  name: Kintsugi Tax Address Validation Exemptions API
  slug: open-kintsugi-exemptions-api
- collection_type: open
  name: Kintsugi Tax Address Validation Filings API
  slug: open-kintsugi-filings-api
- collection_type: open
  name: Kintsugi Tax Address Validation Nexus API
  slug: open-kintsugi-nexus-api
- collection_type: open
  name: Kintsugi Tax Address Validation Products API
  slug: open-kintsugi-products-api
- collection_type: open
  name: Kintsugi Tax Address Validation Registrations API
  slug: open-kintsugi-registrations-api
- collection_type: open
  name: Kintsugi Tax Address Validation Tax Estimation API
  slug: open-kintsugi-tax-estimation-api
- collection_type: open
  name: Kintsugi Tax Address Validation Transactions API
  slug: open-kintsugi-transactions-api
- collection_type: open
  name: Kintsugi Tax API
  slug: open-kintsugi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kintsugi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kintsugi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kintsugi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kintsugi-tax
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trykintsugi
- group: company
  title: ''
  type: Website
  url: https://www.trykintsugi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trykintsugi.com
- group: commercial
  title: ''
  type: Plans
  url: plans/kintsugi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kintsugi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kintsugi-finops.yml
created: '2026-06-21'
description: Kintsugi is an AI-driven sales tax compliance and automation platform that calculates US sales tax, VAT, and GST in real time, monitors economic and physical nexus, manages exemptions and registrations, and auto-prepares and files returns. Its REST API exposes tax estimation, transactions, products, address validation, nexus, exemptions, registrations, and filings, authenticated with an API key plus organization ID header.
finops:
- name: Kintsugi Finops
  service_category: Tax Compliance and Automation
  slug: kintsugi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kintsugi.png
layout: provider
modified: '2026-06-21'
name: Kintsugi
nav: Providers
network: true
overview: 'Kintsugi publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Address Validation API, Customers API, Exemptions API, and 6 more. Tagged areas include Sales Tax, Tax Compliance, Tax Automation, VAT, and GST.


  Kintsugi''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Kintsugi Plans Pricing
  plan_count: 4
  slug: kintsugi-plans-pricing
random_paper: 133
rate_limits:
- limit_count: 2
  name: Kintsugi Rate Limits
  slug: kintsugi-rate-limits
score:
  band: thin
  composite: 36.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kintsugi/refs/heads/main/screenshots/kintsugi-2026-07-25T223847.png
security:
- kind: authentication
  name: Kintsugi Authentication
  slug: kintsugi-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Kintsugi Domain Security
  slug: kintsugi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kintsugi
tags:
- Sales Tax
- Tax Compliance
- Tax Automation
- VAT
- GST
- Nexus
- AI
website: https://www.trykintsugi.com
---
