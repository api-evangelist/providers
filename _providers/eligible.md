---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: The Coverage API performs real-time insurance eligibility and benefits verification for a patient against a payer. Clients submit provider NPI, payer ID, and member identity information and receive st
  name: Eligible Coverage API
  slug: coverage
- description: The Claims API supports submission, tracking, and status checking of professional and institutional healthcare claims to payers across the Eligible network. The API also provides claim acknowledgement
  name: Eligible Claims API
  slug: claims
- description: The Payment Estimation API calculates expected patient out-of-pocket amounts for a service before it is rendered, combining benefit details from a coverage check with provider contracted rates and acc
  name: Eligible Payment Estimation API
  slug: payment-estimation
- description: 'The Enrollment API manages the trading partner enrollment workflow that providers must complete with payers in order to exchange eligibility, claims, and remittance transactions through Eligible. The '
  name: Eligible Enrollment API
  slug: enrollment
- description: The Payers API exposes the directory of insurance payers supported by Eligible, including payer identifiers, names, supported transaction types, enrollment requirements, and webhook capabilities. Clie
  name: Eligible Payers API
  slug: payers
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eligible-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eligible-api
- group: company
  title: ''
  type: Website
  url: https://eligible.com/
- group: docs
  title: ''
  type: Documentation
  url: https://eligible.com/
- group: company
  title: ''
  type: Blog
  url: https://eligible.com/blog/feed/
created: '2024-07-02'
description: Eligible provides insurance billing APIs for healthcare businesses, enabling the integration of insurance billing experiences into healthcare applications. The platform supports eligibility verification, coverage discovery, claims submission and tracking, payment estimation, enrollment, and remittance processing across a large network of US payers.
finops:
- name: Eligible Finops
  service_category: API
  slug: eligible-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eligible.png
layout: provider
modified: '2026-04-28'
name: Eligible
nav: Providers
network: true
overview: 'Eligible publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Billing, Eligibility, Healthcare, Insurance, and Claims.


  Eligible''s developer surface includes documentation, engineering blog, and 3 more developer resources.'
plans:
- name: Eligible Plans Pricing
  plan_count: 3
  slug: eligible-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Eligible Rate Limits
  slug: eligible-rate-limits
score:
  band: emerging
  composite: 18.9
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 21.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Eligible Domain Security
  slug: eligible-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eligible
tags:
- Billing
- Eligibility
- Healthcare
- Insurance
- Claims
website: https://eligible.com/
---
