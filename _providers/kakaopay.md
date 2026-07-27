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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 4
apis:
- description: REST API for integrating KakaoPay online payment functionality into PC and mobile web or app environments. Supports single payments, subscription (recurring) billing, order inquiry, and payment cancel
  name: KakaoPay Online Payment API
  slug: kakaopay-online-payment-api
- description: REST API providing KakaoPay authentication services including token issuance, token refresh, user information retrieval, and consent management. Enables applications to authenticate users via their Ka
  name: KakaoPay Login API
  slug: kakaopay-login-api
- description: REST API for code-based money transfers, enabling users to send and receive money via generated links. Supports money transfer link generation, retrieval, deletion, bill-splitting settlements, and ser
  name: KakaoPay Money Transfer API
  slug: kakaopay-money-transfer-api
- description: REST API providing facial detection and comparison capabilities for identity verification and authentication within KakaoPay financial services.
  name: KakaoPay Face Recognition API
  slug: kakaopay-face-recognition-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kakaopay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kakaopay.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.kakaopay.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/kakaopay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kakaopay
- group: company
  title: ''
  type: Blog
  url: https://tech.kakaopay.com
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.kakao.com/docs/latest/en/app-setting/paid-api
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.kakaopay.com
- group: other
  title: ''
  type: X
  url: https://x.com/kakaocorpglobal
- group: commercial
  title: ''
  type: Plans
  url: plans/kakaopay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kakaopay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kakaopay-finops.yml
created: '2026-06-13'
description: KakaoPay is a Korean mobile payment platform and fintech service by Kakao Corp providing REST APIs for payment processing, QR code payments, online checkout, subscription billing, money transfers, and financial product management. The platform enables merchants and developers to integrate KakaoPay's payment infrastructure via secure REST APIs authenticated with admin keys or bearer tokens.
finops:
- name: Kakaopay Finops
  service_category: ''
  slug: kakaopay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kakaopay.png
layout: provider
modified: '2026-06-13'
name: KakaoPay
nav: Providers
network: true
overview: 'KakaoPay publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Mobile Payments, QR Code Payments, Subscription Billing, and Money Transfer.


  KakaoPay''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Kakaopay Plans Pricing
  plan_count: 2
  slug: kakaopay-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 2
  name: Kakaopay Rate Limits
  slug: kakaopay-rate-limits
score:
  band: emerging
  composite: 23.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 23.7
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kakaopay/refs/heads/main/screenshots/kakaopay-2026-06-20T183907.png
security:
- kind: domain-security
  name: Kakaopay Domain Security
  slug: kakaopay-domain-security
  summary_line: TLSv1.2 · HSTS
slug: kakaopay
tags:
- Payments
- Mobile Payments
- QR Code Payments
- Subscription Billing
- Money Transfer
- Fintech
- Korean
- REST API
website: https://www.kakaopay.com
---
