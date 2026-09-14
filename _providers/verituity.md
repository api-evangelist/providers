---
api_count: 1
apis:
- description: 'Verification-as-a-Service. A single POST /v1/verifications call declares which verification modules to run — organization_identity, individual_identity, payment_method and payee_qualification (PQS) — '
  name: Verituity Verification API
  slug: verituity-verification-api
artifact_total: 6
asyncapis:
- description: ''
  name: Verituity Webhooks
  slug: verituity-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verituity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://verituity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://verituity.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://verituity.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://verituity.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://verituity.com/developers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://verituity.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://verituity.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://verituity.com/developers
- group: start
  title: ''
  type: Sandbox
  url: sandbox/verituity-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/verituity-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/verituity-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/verituity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/verituity-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/verituity-decline-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/verituity-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/verituity-plans-pricing.yml
- group: build
  title: ''
  type: Examples
  url: examples/verituity-verification-examples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/verituity-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/verituity-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/verituity-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/verituity-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/verituity-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verituity-llms.txt
created: '2026-09-02'
description: Verituity is a McLean, Virginia payment integrity platform that verifies the file, the payee, the account and the payment instruction at the moment of authorization, before money moves, across any payment rail. The platform is organized as six services — Connect (ingest any batch file or REST call and normalize it to ISO 20022), Detect (duplicate and out-of-pattern screening), Eligibility (payee qualification against OFAC, SAM and payer-private lists), Verify (identity and bank account ownership verification), Pay (rail optionality and orchestration across ACH, RTP, wire, push-to-card, virtual card, PayPal, Zelle, Venmo, check and cross-border) and Explain (evidence and lineage on every decision). Its developer-facing product is Verification-as-a-Service, a single POST /v1/verifications call that runs four verification modules and returns one normalized decision/tier/reason_code response regardless of which underlying data source answered.
image: https://verituity.com/img/og-default.png
layout: provider
modified: '2026-09-02'
name: Verituity
nav: Providers
network: true
overview: 'Verituity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Payouts, Disbursements, Identity Verification, and Account Verification.


  The Verituity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Verituity''s developer surface includes documentation, API reference, getting-started guide, pricing, sandbox, authentication, code examples, and 17 more developer resources.'
plans:
- name: Verituity Plans Pricing
  plan_count: 0
  slug: verituity-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Verituity Rate Limits
  slug: verituity-rate-limits
security:
- kind: authentication
  name: Verituity Authentication
  slug: verituity-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Verituity Domain Security
  slug: verituity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: verituity
tags:
- Payments
- Payouts
- Disbursements
- Identity Verification
- Account Verification
- Fraud Prevention
- Payment Integrity
- Banking
- Financial Services
- Public Sector
- ISO 20022
- Compliance
- Company
website: https://verituity.com/
---
