---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Paidy Agentic Access
  operation_count: 11
  slug: paidy-agentic-access
  summary_line: 11 operations · 8 acting
api_count: 1
apis:
- description: 'JavaScript-based checkout integration that enables consumers to authenticate with Paidy and authorize payments or create recurring payment tokens directly from the merchant checkout page. Handles the '
  name: Paidy Checkout
  slug: paidy-checkout
- baseURL: https://api.paidy.com
  baseurl_source: declared
  description: Manage payment authorizations, captures, refunds, updates, and closures.
  name: Paidy Payments API
  slug: paidy-payments-api
- baseURL: https://api.paidy.com
  baseurl_source: declared
  description: Manage recurring payment tokens for subscription billing.
  name: Paidy Tokens API
  slug: paidy-tokens-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Paidy Payments API
  slug: open-paidy-payments-api
- collection_type: open
  name: Paidy Payments Tokens API
  slug: open-paidy-tokens-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.paidy.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paidy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paidy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paidy-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://paidy.com/docs/en/
- group: docs
  title: ''
  type: APIReference
  url: https://paidy.com/docs/api/en/
- group: other
  title: ''
  type: Merchant Dashboard
  url: https://merchant.paidy.com/
- group: design
  title: ''
  type: Webhooks
  url: https://paidy.com/docs/en/webhook.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://paidy.com/docs/en/updates.html
- group: design
  title: ''
  type: Testing
  url: https://paidy.com/docs/en/testing.html
- group: operate
  title: ''
  type: Status
  url: https://paidy.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paidy.com/merchant/
created: '2026-06-13'
description: Paidy is a Japanese buy now, pay later (BNPL) and digital payment service that enables Japanese consumers to make purchases and pay later via monthly consolidated billing. Merchants integrate Paidy Checkout (JavaScript) and the Paidy REST API to accept deferred payments, manage authorizations, capture funds, issue refunds, and handle recurring payments via stored tokens.
examples:
- key_count: 1
  name: Capture Payment
  slug: capture-payment
- key_count: 8
  name: Create Payment
  slug: create-payment
- key_count: 16
  name: Payment Response
  slug: payment-response
- key_count: 4
  name: Refund Payment
  slug: refund-payment
- key_count: 2
  name: Suspend Token
  slug: suspend-token
- key_count: 16
  name: Token Response
  slug: token-response
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paidy.png
json_schemas:
- name: Payment
  property_count: 16
  slug: payment
- name: Token
  property_count: 16
  slug: token
jsonld:
- class_count: 55
  name: context Context
  property_count: 6
  slug: context
layout: provider
modified: '2026-06-13'
name: Paidy
nav: Providers
network: true
overview: 'Paidy publishes 2 APIs on the [APIs.io](https://apis.io/) network: Payments API and Tokens API. Tagged areas include Buy Now Pay Later, Payments, Japan, Checkout, and Deferred Payments.


  The Paidy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Paidy''s developer surface includes authentication, documentation, API reference, changelog, status page, and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 10
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Paidy API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: paidy-jsonschema-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/paidy/refs/heads/main/screenshots/paidy-2026-06-20T191326.png
security:
- kind: authentication
  name: Paidy Authentication
  slug: paidy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paidy Domain Security
  slug: paidy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paidy
tags:
- Buy Now Pay Later
- Payments
- Japan
- Checkout
- Deferred Payments
- Recurring Payments
- Tokens
website: https://www.paidy.com/
---
