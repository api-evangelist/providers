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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: 'A quick and easy way for partners to offer Lemonade homeowners, condo, and renters insurance to their users. Supports quoting, policy creation, and payment, either through the Maya bot drop-in or via '
  name: Lemonade Insurance API
  slug: lemonade-insurance-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lemonade-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lemonade-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lemonade-inc-
- group: company
  title: ''
  type: Website
  url: https://www.lemonade.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lemonade.com/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-doc-portal.lemonade.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lemonade.com/blog/
- group: operate
  title: ''
  type: FAQ
  url: https://www.lemonade.com/faq
- group: company
  title: ''
  type: Partners
  url: https://www.lemonade.com/partners-program
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lemonade.com/api-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lemonade.com/privacy-policy
- group: build
  title: ''
  type: GitHub
  url: https://github.com/lemonade-hq
- group: agent
  title: ''
  type: LlmsText
  url: https://www.lemonade.com/llms.txt
created: '2024-07-02'
description: Lemonade, Inc. is an American insurance company. The company offers renters, homeowners, car, pet, and term life insurance in the United States, as well as contents and liability policies in Germany and the Netherlands and renters insurance in France. The Lemonade Insurance API allows partners to embed insurance quoting, policy creation, and payment flows for homeowners, condo, and renters policies into their own websites and apps.
finops:
- name: Lemonade Finops
  service_category: API
  slug: lemonade-finops
graphqls:
- description: Lemonade is an AI-native digital insurance company offering renters, homeowners, car, pet, term life, and business insurance. Its platform is built around behavioral economics and AI-powered claims pr
  name: Lemonade GraphQL Schema
  slug: lemonade-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lemonade.png
layout: provider
modified: '2026-04-28'
name: Lemonade
nav: Providers
network: true
overview: 'Lemonade publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Renters Insurance, Homeowners Insurance, and Embedded Insurance.


  Lemonade''s developer surface includes documentation, engineering blog, FAQ, GitHub presence, and 9 more developer resources.'
plans:
- name: Lemonade Plans Pricing
  plan_count: 3
  slug: lemonade-plans-pricing
random_paper: 117
rate_limits:
- limit_count: 5
  name: Lemonade Rate Limits
  slug: lemonade-rate-limits
score:
  band: thin
  composite: 30.7
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 48.1
    developer_ergonomics: 19.6
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 30.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lemonade/refs/heads/main/screenshots/lemonade-2026-06-20T184421.png
security:
- kind: domain-security
  name: Lemonade Domain Security
  slug: lemonade-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lemonade Vulnerability Disclosure
  slug: lemonade-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lemonade
tags:
- Insurance
- Renters Insurance
- Homeowners Insurance
- Embedded Insurance
website: https://www.lemonade.com/
---
