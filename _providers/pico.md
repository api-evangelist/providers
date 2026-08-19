---
access_model:
  confidence: high
  label: Product retired
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.hype.co/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Pico API let developers build custom workflows and integrations on the Pico creator platform — including searching and managing contacts across an account. Every request authenticated with an X-Ap
  name: Pico API
  slug: pico-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.hype.co/
- group: operate
  title: ''
  type: Support
  url: https://help.hype.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hype.co/terms/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hype.co/terms/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/pico-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pico-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pico-domain-security.yml
coverage:
  checked: '2026-08-13'
  detail: Pico became Hype and was acquired by MMA.inc in February 2026 — the API host api.trypico.com is now NXDOMAIN and the docs.trypico.com reference returns an S3 "NoSuchBucket" 404, so the entire developer surface has been deleted rather than gated.
  evidence:
  - status: 0
    url: https://api.trypico.com/
  - status: 404
    url: https://docs.trypico.com/
  - status: 302
    url: https://trypico.com/
  - status: 200
    url: https://www.hype.co/
  - status: 404
    url: https://app.hype.co/
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Pico was a creator-monetization and CRM platform for online creators, publishers, and media companies, built in New York and backed by Bloomberg Beta. It combined an audience CRM with email capture, landing pages, paywalls, memberships, and subscription payments in a single tool so creators could identify their audience, gate premium content, and convert readers into paying members. Pico raised a $6.5M round in 2021 ("Pico 2.0") and a $10M Series A in 2023, when it rebranded to Hype (hype.co) and refocused on link-in-bio, lead generation, and growth tools for creators, gyms, coaches, and athletes. In February 2026 Hype was acquired by MMA.inc and the product was wound down. The developer API — authenticated with an X-Api-Key header and documented at docs.trypico.com — is retired: the API host api.trypico.com no longer resolves, the reference bucket has been deleted, and hype.co now serves only an acquisition notice directing users to support@hype.co.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pico.png
layout: provider
modified: '2026-08-13'
name: Pico
nav: Providers
network: true
overview: 'Pico publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Economy, CRM, Memberships, and Payments.


  Pico''s developer surface includes support, authentication, and 5 more developer resources.'
plans:
- name: Pico Plans Pricing
  plan_count: 0
  slug: pico-plans-pricing
random_paper: 129
rate_limits:
- limit_count: 0
  name: Pico Rate Limits
  slug: pico-rate-limits
score:
  band: emerging
  composite: 14.2
  delta: -2.5
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Pico Authentication
  slug: pico-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pico Domain Security
  slug: pico-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pico
tags:
- Company
- Creator Economy
- CRM
- Memberships
- Payments
- Email Marketing
- Newsletters
- Monetization
- Retired
website: https://www.hype.co/
---
