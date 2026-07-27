---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.swile.co
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swile
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/swile-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/swile-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/swile-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://swile.co/security/disclosure-policy.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swile-domain-security.yml
created: '2026-07-17'
description: 'Swile is a French fintech that operates an all-in-one employee-benefits and engagement super-app built around a single Mastercard smartcard and mobile app. Founded in 2018 as Lunchr and rebranded Swile in 2020, it consolidates meal vouchers (titres-restaurant), gift and culture vouchers, mobility and work-from-home allowances, and team/recognition budgets that were historically spread across paper vouchers and multiple providers. The company merged with Bimpli in France, expanded into Brazil through Vee Benefícios, and is backed by investors including Index Ventures, SoftBank Vision Fund, and Bpifrance. Swile serves employers and their employees rather than external developers: as of this enrichment pass it publishes a security surface (RFC 9116 security.txt, a coordinated vulnerability disclosure policy, and a researcher hall of fame) but no public developer portal, OpenAPI, or API reference.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swile.png
layout: provider
modified: '2026-07-21'
name: Swile
nav: Providers
network: true
overview: Swile is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Employee Benefits, Meal Vouchers, and Payments.
random_paper: 4
score:
  band: minimal
  composite: 11.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 11.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Swile Domain Security
  slug: swile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Swile Vulnerability Disclosure
  slug: swile-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: swile
tags:
- Company
- Fintech
- Employee Benefits
- Meal Vouchers
- Payments
- Prepaid Cards
- Employee Engagement
- Human Resources
- Mastercard
website: https://www.swile.co
---
