---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Create and confirm Afterpay checkouts for merchant integrations.
  name: Afterpay Checkout API
  slug: afterpay-checkout-api
- description: Auth, capture, void and refund Afterpay payments.
  name: Afterpay Payments API
  slug: afterpay-payments-api
- description: Retrieve merchant-level configuration and supported regions.
  name: Afterpay Configuration API
  slug: afterpay-configuration-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/afterpay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/afterpay-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/afterpay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/afterpay-com-au
- group: company
  title: ''
  type: Website
  url: https://www.afterpay.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/afterpay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/afterpay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/afterpay-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.afterpay.com/llms.txt
created: '2026-05-08'
description: Afterpay (acquired by Block / Square) is a buy-now-pay-later platform offering Pay-in-4 installments at thousands of merchants. APIs for merchants to integrate via Square or direct.
finops:
- name: Afterpay Finops
  service_category: Fintech
  slug: afterpay-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Afterpay (Clearpay) Buy Now Pay Later (BNPL) API. Afterpay is a payment platform that allows merchants to offer installment-based payment options to consume
  name: Afterpay GraphQL Schema
  slug: afterpay-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/afterpay.png
layout: provider
modified: '2026-05-08'
name: Afterpay
nav: Providers
network: true
overview: Afterpay publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, BNPL, Payments, Consumer, and Block.
plans:
- name: Afterpay Plans Pricing
  plan_count: 1
  slug: afterpay-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Afterpay Rate Limits
  slug: afterpay-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: -2.9
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 43.3
    developer_ergonomics: 0.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 22.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/afterpay/refs/heads/main/screenshots/afterpay-2026-06-20T165725.png
security:
- kind: domain-security
  name: Afterpay Domain Security
  slug: afterpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Afterpay Vulnerability Disclosure
  slug: afterpay-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: afterpay
tags:
- Fintech
- BNPL
- Payments
- Consumer
- Block
website: https://www.afterpay.com/
---
