---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: REST API for marketplace payment infrastructure including pay-in, pay-out, wallet management, KYC/KYB onboarding, P2P transfers, and regulatory compliance for European marketplaces.
  name: Lemonway API
  slug: lemonway-api
- description: REST API for online KYC/KYB onboarding flows, enabling marketplace operators to collect identity verification, document uploads, and account creation for both individual and legal entity account holde
  name: Lemonway Onboarding API
  slug: lemonway-onboarding-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lemonway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lemonway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lemonway.com/en
- group: other
  title: ''
  type: Developers
  url: https://www.lemonway.com/en/developers
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.lemonway.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lemonway.com/en/pricing
- group: operate
  title: ''
  type: Status
  url: https://documentation.lemonway.com/page/api-status
- group: operate
  title: ''
  type: ChangeLog
  url: https://documentation.lemonway.com/page/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.lemonway.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.lemonway.com/en/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lemonway
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lemonwaysas
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lemonway.com/en/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lemonway.com/en/privacy-policy
created: '2026-06-13'
description: Lemonway is a European payment institution regulated by the French ACPR (registration 16568) since 2012, providing REST APIs for marketplace payments including IBAN wallet creation, bank transfers, card payments, KYC/KYB verification, P2P transfers, and crowdfunding platform payment flows. Trusted by over 1,400 marketplaces across Europe.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lemonway.png
jsonld:
- class_count: 0
  name: Lemonway Context
  property_count: 7
  slug: lemonway-context
layout: provider
modified: '2026-06-13'
name: Lemonway
nav: Providers
network: true
overview: 'Lemonway publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Marketplace, IBAN, KYC, and Wallets.


  The Lemonway catalog on APIs.io includes 1 JSON-LD context.


  Lemonway''s developer surface includes documentation, pricing, status page, changelog, support, engineering blog, GitHub presence, and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 29
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 34.3
  delta: -6.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 40.3
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 41.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/lemonway/refs/heads/main/screenshots/lemonway-2026-06-20T184419.png
security:
- kind: domain-security
  name: Lemonway Domain Security
  slug: lemonway-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lemonway Vulnerability Disclosure
  slug: lemonway-vulnerability-disclosure
  summary_line: disclosure policy published
slug: lemonway
tags:
- Payments
- Marketplace
- IBAN
- KYC
- Wallets
- Bank Transfers
- Card Payments
- Crowdfunding
- European
- PSD2
website: https://www.lemonway.com/en
---
