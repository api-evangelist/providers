---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The REST API behind the Hnry app. It backs the Hnry iOS/Android clients and the published Hnry Zapier integration, which exposes create/find operations over clients, invoices, invoice line items and e
  name: Hnry Platform API
  slug: hnry-platform-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://hnry.co.nz/
- group: commercial
  title: ''
  type: Pricing
  url: https://hnry.co.nz/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.hnry.io/signup/jurisdiction_selection
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hnry.co.nz/agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hnry.co.nz/privacy/
- group: operate
  title: ''
  type: Support
  url: https://hnry.co.nz/product/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.hnry.io/en/
- group: company
  title: ''
  type: Blog
  url: https://hnry.co.nz/resources/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HnryNZ
- group: auth
  title: ''
  type: TrustCenter
  url: security/hnry-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/hnry-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hnry-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hnry-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/hnry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hnry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hnry-security.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/hnry-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hnry-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hnry-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hnry-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/hnry-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hnry-lifecycle.yml
created: '2026-08-22'
description: Hnry is a New Zealand-founded financial administration and accounting service for sole traders, contractors and freelancers, operating in New Zealand, Australia and the United Kingdom. Customers are issued a dedicated "Hnry Account" bank account; every payment that lands in it is automatically split — income tax, GST/VAT, ACC levies, Medicare levy and student loan repayments are calculated, deducted and paid to the revenue authority in real time, and the remainder is passed straight through to the customer. On top of that payment rail Hnry runs invoicing, invoice chasing, expense capture and review, allocations to savings/investments/charities, business reporting, tax filing and a Hnry Business Mastercard. Pricing is a single usage-based fee of 1% of each inbound payment plus tax, annually capped. The platform is a Rails application at app.hnry.io with a REST API that backs the mobile apps and a public Zapier integration; the API reference at app.hnry.io/api-docs and the "Developer
  Platform" workspace page are both credential-gated, so no machine-readable contract is published.
image: https://hnry.co.nz/img/social/opengraph.jpg
layout: provider
modified: '2026-08-22'
name: Hnry
nav: Providers
network: true
overview: 'Hnry publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Tax, Payments, Invoicing, and Expense Management.


  Hnry''s developer surface includes pricing, signup flow, support, engineering blog, authentication, and 17 more developer resources.'
plans:
- name: Hnry Plans Pricing
  plan_count: 3
  slug: hnry-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Hnry Rate Limits
  slug: hnry-rate-limits
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 37.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Hnry Authentication
  slug: hnry-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hnry Domain Security
  slug: hnry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hnry Vulnerability Disclosure
  slug: hnry-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Hnry Trust Center
  slug: hnry-trust-center
  summary_line: ISO/IEC 27001
slug: hnry
tags:
- Accounting
- Tax
- Payments
- Invoicing
- Expense Management
- Financial-Services
- Sole Traders
- Payroll
- Fintech
- New Zealand
- Australia
- United Kingdom
website: https://hnry.co.nz/
---
