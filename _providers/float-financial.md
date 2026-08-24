---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.2
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: REST API (OpenAPI 3.1.0, 71 operations across 47 paths) for automating accounting and reporting against Float. Read card transactions, account transactions, bills, bill attachments, payments, reimburs
  name: Float Public API
  slug: float-public-api
artifact_total: 8
asyncapis:
- description: ''
  name: Float Financial Webhooks
  slug: float-financial-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/float-financial-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/float-financial-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://floatfinancial.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.floatfinancial.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.floatfinancial.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.floatfinancial.com/reference/gettransactions
- group: start
  title: ''
  type: GettingStarted
  url: https://help.floatfinancial.com/hc/en-us/articles/38048585600404-Get-Started-with-Float-s-Public-API
- group: operate
  title: ''
  type: Support
  url: https://help.floatfinancial.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://floatfinancial.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/floatfinancial
- group: commercial
  title: ''
  type: Pricing
  url: https://floatfinancial.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.floatfinancial.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.floatfinancial.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://floatfinancial.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://floatfinancial.com/legal#float-financial-solutions-privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/float-financial-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/float-financial-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/float-financial-conformance.yml
- group: auth
  title: ''
  type: Security
  url: security/float-financial-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/float-financial-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/float-financial-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/float-financial-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/float-financial-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/float-financial-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/float-financial-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/float-financial-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/float-financial-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/float-financial-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/float-financial-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/float-financial-openapi-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/float-financial-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/float-financial-rate-limits.yml
created: '2026-08-16'
description: Float Financial Solutions Inc. is a Toronto-based Canadian business finance platform combining corporate charge cards, high-yield business accounts, expense management, accounts payable / bill pay, employee reimbursements and multi-currency FX into one spend management product for Canadian companies. Founded in 2019 and used by thousands of Canadian businesses, Float publishes a REST "Float Public API" at api.floatfinancial.com that exposes card and account transactions, cards and card limits, bills and bill attachments, payments, reimbursements, receipts, vendors, GL codes, tax codes and components, custom fields, subsidiaries, teams, users, approval and submission policies, accounting connections and webhook subscriptions — designed primarily for finance teams building custom accounting/ERP integrations where Float's packaged QuickBooks Online, Xero and NetSuite connectors do not fit.
image: https://floatfinancial.com/favicon.ico
layout: provider
modified: '2026-08-16'
name: Float Financial
nav: Providers
network: true
overview: 'Float Financial publishes 1 API on the [APIs.io](https://apis.io/) network: Float Public API. Tagged areas include Spend Management, Corporate Cards, Expense Management, Accounts Payable, and Bill Pay.


  The Float Financial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Float Financial''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Float Financial Plans Pricing
  plan_count: 3
  slug: float-financial-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Float Financial Rate Limits
  slug: float-financial-rate-limits
score:
  band: strong
  composite: 61.4
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 30.3
    contract_quality: 62.2
    developer_ergonomics: 45.8
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 36.8
  previous_composite: 61.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/float-financial/refs/heads/main/screenshots/float-financial-2026-08-17T080932.png
security:
- kind: authentication
  name: Float Financial Authentication
  slug: float-financial-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Float Financial Domain Security
  slug: float-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Float Financial Vulnerability Disclosure
  slug: float-financial-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Float Financial Trust Center
  slug: float-financial-trust-center
  summary_line: SOC 2 Type 2, PCI DSS
slug: float-financial
tags:
- Spend Management
- Corporate Cards
- Expense Management
- Accounts Payable
- Bill Pay
- Reimbursement
- Business Banking
- Accounting Integration
- Fintech
- Canada
- Payments
- ERP Integration
website: https://floatfinancial.com/
---
