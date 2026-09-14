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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
api_count: 1
apis:
- description: 'Legacy India API (PMXClients service). Twelve JSON-over-POST methods let a business add vendors and customers as contacts, book and approve vendor payments, raise collection requests, generate hosted '
  name: PayMate India Business Payments API
  slug: paymate-india-business-payments-api
- baseURL: https://api.paymate.my
  baseurl_source: declared
  description: Business (KYB) onboarding, maintenance, charges and collection account setup
  name: PayMate Businesses API
  slug: paymate-businesses-api
- baseURL: https://api.paymate.my
  baseurl_source: declared
  description: Commercial credit card enrolment and management
  name: PayMate Cards API
  slug: paymate-cards-api
- baseURL: https://api.paymate.my
  baseurl_source: declared
  description: Payment collection requests, status and reporting
  name: PayMate Collections API
  slug: paymate-collections-api
- baseURL: https://api.paymate.my
  baseurl_source: declared
  description: Buyer / supplier contact onboarding and maintenance
  name: PayMate Contacts API
  slug: paymate-contacts-api
- baseURL: https://api.paymate.my
  baseurl_source: declared
  description: Vendor payment initiation, status and reporting
  name: PayMate Payments API
  slug: paymate-payments-api
- baseURL: https://api.paymate.my
  baseurl_source: declared
  description: Reference data
  name: PayMate Reference API
  slug: paymate-reference-api
artifact_total: 11
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/paymate-capability-edges.yml
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
overview: 'PayMate publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Businesses API, Cards API, Collections API, and 3 more. Tagged areas include Payments, B2B Payments, Accounts Payable, Accounts Receivable, and Supply Chain Finance.


  PayMate''s developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, sandbox, and 19 more developer resources.'
plans:
- name: Paymate Plans Pricing
  plan_count: 6
  slug: paymate-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 6
  name: Paymate Rate Limits
  slug: paymate-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/paymate/refs/heads/main/screenshots/paymate-2026-09-02T150923.png
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
- Financial-Services
- India
- Fintech
- Company
website: https://paymate.in/
---
