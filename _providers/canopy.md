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
api_count: 1
apis:
- description: The Canopy Connect API returns structured property and casualty insurance data directly from 400+ carriers in real time. Applications can verify coverage, retrieve policy documents, pull driver and ve
  name: Canopy Connect API
  slug: canopy-connect-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/canopy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canopy-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CanopyTax
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canopy-connect
- group: company
  title: ''
  type: Website
  url: https://www.usecanopy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.usecanopy.com/api
- group: start
  title: ''
  type: Portal
  url: https://www.usecanopy.com/api
- group: auth
  title: ''
  type: Security
  url: https://www.usecanopy.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usecanopy.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usecanopy.com/legal/terms
- group: company
  title: ''
  type: Blog
  url: https://www.usecanopy.com/blog
- group: company
  title: ''
  type: About
  url: https://www.usecanopy.com/about
- group: company
  title: ''
  type: Careers
  url: https://www.usecanopy.com/careers
created: '2024-07-02'
description: Canopy Connect is an insurance infrastructure platform that lets consumers and businesses quickly and securely share property and casualty insurance information through integrations with 400+ carriers covering 95%+ of the U.S. auto and homeowners markets. The API returns structured policy, driver, vehicle, claims, and property data in seconds, replacing manual verification workflows used across mortgage lending, auto finance, insurance carriers, and embedded insurance products.
finops:
- name: Canopy Finops
  service_category: API
  slug: canopy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/canopy.png
layout: provider
modified: '2026-04-23'
name: Canopy Connect
nav: Providers
network: true
overview: 'Canopy Connect publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Auto Insurance, Casualty, Financial Services, Homeowners Insurance, and Insurance.


  Canopy Connect''s developer surface includes documentation, developer portal, engineering blog, and 10 more developer resources.'
plans:
- name: Canopy Plans Pricing
  plan_count: 3
  slug: canopy-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Canopy Rate Limits
  slug: canopy-rate-limits
score:
  band: thin
  composite: 28.4
  delta: -3.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 32.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canopy/refs/heads/main/screenshots/canopy-2026-06-20T173925.png
security:
- kind: domain-security
  name: Canopy Domain Security
  slug: canopy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Canopy Vulnerability Disclosure
  slug: canopy-vulnerability-disclosure
  summary_line: disclosure policy published
slug: canopy
tags:
- Auto Insurance
- Casualty
- Financial Services
- Homeowners Insurance
- Insurance
- Insurance Verification
- Property
website: https://www.usecanopy.com/
---
