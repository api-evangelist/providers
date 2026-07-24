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
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: 'REST API for end-to-end identity verification including document verification, facial biometrics with liveness detection, address verification, AML screening against 1700+ watchlists, phone and email '
  name: Shufti Pro Verification API
  slug: verification-api
- description: Business verification API providing Know Your Business (KYB) checks from official registries, business AML screening, and Know Your Investor (KYI) services. Enables companies to verify business entiti
  name: Shufti Pro KYB API
  slug: kyb-api
- description: Anti-money laundering screening API covering 1700+ global watchlists, sanctions lists, PEP databases, and adverse media sources. Provides ongoing monitoring and batch screening for individuals and bus
  name: Shufti Pro AML Screening API
  slug: aml-screening-api
- description: Biometric authentication and re-verification API enabling face-based login and identity re-confirmation for returning users. Uses liveness detection to prevent spoofing and supports fast ID reusabilit
  name: Shufti Pro Biometric Authentication API
  slug: biometric-auth-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shufti-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shuftipro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.shuftipro.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/shuftipro
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shufti-pro
- group: company
  title: ''
  type: Blog
  url: https://shuftipro.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://shuftipro.com/plans/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shuftipro.com/
- group: other
  title: ''
  type: X
  url: https://x.com/shufti_pro
- group: commercial
  title: ''
  type: Plans
  url: plans/shufti-pro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shufti-pro-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shufti-pro-finops.yml
created: '2026-06-13'
description: Shufti Pro is an AI-powered identity verification platform offering a REST API for document verification, face biometrics, AML screening, business verification (KYB), and address verification. The platform supports 10,000+ document types across 230+ countries and territories, integrates with 1700+ AML watchlists, and provides mobile SDKs for Android, iOS, Flutter, and React Native.
finops:
- name: Shufti Pro Finops
  service_category: ''
  slug: shufti-pro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shufti-pro.png
jsonld:
- class_count: 18
  name: Shufti Pro Context
  property_count: 27
  slug: shufti-pro-context
layout: provider
modified: '2026-06-13'
name: Shufti Pro
nav: Providers
network: true
overview: 'Shufti Pro publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Identity Verification, KYC, AML, KYB, and Face Biometrics.


  The Shufti Pro catalog on APIs.io includes 1 JSON-LD context.


  Shufti Pro''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Shufti Pro Plans Pricing
  plan_count: 3
  slug: shufti-pro-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Shufti Pro Rate Limits
  slug: shufti-pro-rate-limits
score:
  band: thin
  composite: 34.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 20.8
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 34.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shufti-pro/refs/heads/main/screenshots/shufti-pro-2026-06-20T193953.png
security:
- kind: domain-security
  name: Shufti Pro Domain Security
  slug: shufti-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shufti-pro
tags:
- Identity Verification
- KYC
- AML
- KYB
- Face Biometrics
- Document Verification
- Address Verification
- Liveness Detection
- eIDV
- Compliance
- Fraud Prevention
website: https://shuftipro.com/
---
