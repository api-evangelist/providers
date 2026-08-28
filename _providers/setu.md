---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    agentic_commerce: false
    auth_clarity: false
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
  score: 2.5
  scored_at: '2026-08-26'
api_count: 8
apis:
- description: End-to-end UPI product suite for merchants and aggregators - collect requests, deep-link / intent flows, UPI AutoPay mandates, payment verification, and settlement reporting on India's Unified Payment
  name: Setu UPI (UPI Setu)
  slug: upi
- description: Enables businesses to become BBPS billers so that customers can pay their bills from any BBPS-enabled app. APIs cover biller onboarding, bill fetch, bill payment, and settlement reporting.
  name: Setu BBPS BillCollect
  slug: bbps-billcollect
- description: Lets apps and platforms offer bill payment to any BBPS biller in India. Provides biller catalogue, fetch-bill, payment, and status APIs along with pre-built UI options.
  name: Setu BBPS BillPay
  slug: bbps-billpay
- description: Automates payment reminders and bill-pay journeys over WhatsApp, combining BBPS bill fetch and UPI collection inside a conversational flow.
  name: Setu WhatsApp Collect
  slug: whatsapp-collect
- description: Setu's Account Aggregator stack lets regulated entities consume consent-based financial data from a customer's other institutions under RBI's AA framework, for personal finance management and loan und
  name: Setu Account Aggregator
  slug: account-aggregator
- description: KYC API suite for verifying individuals and businesses in India (Aadhaar, PAN, GSTIN, bank account, business identity), used during onboarding by fintechs, lenders, and marketplaces.
  name: Setu KYC
  slug: kyc
- description: Aadhaar-based electronic signature API for collecting legally valid signatures on documents, with audit trail and signed PDF retrieval.
  name: Setu Aadhaar eSign
  slug: esign
- description: The Bridge is Setu's developer console for configuring products, issuing API credentials, viewing transaction and settlement reports, and managing webhook endpoints.
  name: Setu The Bridge (Developer Console)
  slug: bridge
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/setu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://setu.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.setu.co/
- group: start
  title: ''
  type: Console
  url: https://bridge.setu.co/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/setuhq
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SetuHQ
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.setu.co/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://setu.co/blog
created: '2026-05-23'
description: Setu (a Pine Labs company) is an API-first embedded finance infrastructure provider for India. Its product catalogue covers UPI acceptance and payouts, BBPS bill collection and bill payment, WhatsApp-based payment journeys, Account Aggregator (RBI's consent-based financial data sharing framework), KYC for individuals and businesses, and Aadhaar eSign. The Bridge is Setu's developer console for configuring products, issuing credentials, and reviewing transactions and settlement. All products are exposed as REST APIs documented at docs.setu.co.
finops:
- name: Setu Finops
  service_category: API
  slug: setu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/setu.png
layout: provider
modified: '2026-05-23'
name: Setu
nav: Providers
network: true
overview: 'Setu publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Embedded Finance, UPI, BBPS, Account Aggregator, and KYC.


  Setu''s developer surface includes documentation, developer console, GitHub presence, engineering blog, and 4 more developer resources.'
plans:
- name: Setu Plans Pricing
  plan_count: 1
  slug: setu-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Setu Rate Limits
  slug: setu-rate-limits
score:
  band: emerging
  composite: 20.6
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/setu/refs/heads/main/screenshots/setu-2026-06-20T193740.png
security:
- kind: domain-security
  name: Setu Domain Security
  slug: setu-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: setu
tags:
- Embedded Finance
- UPI
- BBPS
- Account Aggregator
- KYC
- eSign
- India
- Fintech
website: https://setu.co/
---
