---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: 'Partner-facing v1 REST API for the PayMate global platform. Twenty-five JSON-over-POST operations cover business (KYB) onboarding and maintenance, buyer/supplier contact onboarding, commercial credit '
  name: PayMate Global Partner API
  slug: paymate-global-partner-api
- description: 'Legacy India API (PMXClients service). Twelve JSON-over-POST methods let a business add vendors and customers as contacts, book and approve vendor payments, raise collection requests, generate hosted '
  name: PayMate India Business Payments API
  slug: paymate-india-business-payments-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paymate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paymate.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.paymate.my/GlobalPartnerAPI
- group: docs
  title: ''
  type: Documentation
  url: https://paymate.in/paymateapi/APIDoc.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.paymate.my/GlobalPartnerAPI
- group: operate
  title: ''
  type: Support
  url: https://paymate.in/contactus.html
- group: company
  title: ''
  type: Blog
  url: https://paymate.in/blog.html
- group: commercial
  title: ''
  type: Pricing
  url: https://paymate.in/Pricing_terms.html
- group: start
  title: ''
  type: Login
  url: https://paymate.in/login.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paymate.in/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paymate.in/privacy.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/paymate-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paymate-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/paymate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paymate-error-codes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/paymate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paymate-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paymate-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/paymate-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paymate-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/paymate-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paymate-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paymate-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/paymate-global-partner-api-overlay.yaml
created: '2026-08-26'
description: 'PayMate India Limited is a Mumbai-headquartered B2B payments and supply-chain finance platform that digitizes, automates and streamlines business payables and receivables. Enterprises use PayMate to pay vendors, GST and utility bills on commercial credit cards, to raise and collect invoice payment requests, to run maker/checker approval workflows, and to access working-capital credit and invoice discounting. The platform runs in India as PayMate and across Singapore, Malaysia, the UAE, Oman, Sri Lanka, Saudi Arabia, Australia and South Africa — where the Australian and South African deployments carry the DuNoMo brand. Two distinct API surfaces are published: the legacy India PayMate API (PMXClients WCF/JSON service) and the current Global Partner API, a v1 REST surface for business (KYB) onboarding, contact onboarding, commercial-card management, vendor payments, collection requests and reporting.'
image: https://paymate.in/imgs/pngs/apple-touch-icon.png
layout: provider
modified: '2026-08-26'
name: PayMate
nav: Providers
network: true
overview: 'PayMate publishes 1 API on the [APIs.io](https://apis.io/) network: Global Partner API. Tagged areas include Payments, B2B Payments, Accounts Payable, Accounts Receivable, and Supply Chain Finance.


  PayMate''s developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, sandbox, and 18 more developer resources.'
plans:
- name: Paymate Plans Pricing
  plan_count: 6
  slug: paymate-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 6
  name: Paymate Rate Limits
  slug: paymate-rate-limits
score:
  band: strong
  composite: 59.5
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 30.3
    contract_quality: 59.9
    developer_ergonomics: 54.2
    discoverability: 68.5
    governance: 30.3
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
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
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Paymate Authentication
  slug: paymate-authentication
  summary_line: apiKey · 0 schemes
- kind: domain-security
  name: Paymate Domain Security
  slug: paymate-domain-security
  summary_line: TLSv1.2 · DMARC
slug: paymate
tags:
- Payments
- B2B Payments
- Accounts Payable
- Accounts Receivable
- Supply Chain Finance
- Invoice Discounting
- Working Capital
- Commercial Cards
- Financial Services
- India
- Fintech
- Company
website: https://paymate.in/
---
