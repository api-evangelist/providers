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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Public API for evaluating cart and transaction risk pre-authorization and submitting post-event signals for model improvement, plus device, identity, and email risk endpoints.
  name: Fraud.net Public API
  slug: public-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fraud-net-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fraudnet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fraud-net
- group: company
  title: ''
  type: Website
  url: https://fraud.net/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.fraud.net/
- group: start
  title: ''
  type: Signup
  url: https://fraud.net/contact/
created: '2024-11-13'
description: Fraud.net provides AI-driven fraud prevention and risk management APIs. The Public API offers pre-authorization Cart Check, Transaction Check, post-event Update, and supporting device, identity, and email risk signals powered by the Collective Intelligence Network.
finops:
- name: Fraud Net Finops
  service_category: API
  slug: fraud-net-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fraud-net.png
layout: provider
modified: '2026-04-28'
name: Fraud.net
nav: Providers
network: true
overview: 'Fraud.net publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fraud, Risk, Commerce, Payments, and Security.


  The Fraud.net catalog on APIs.io includes 1 Spectral governance ruleset.


  Fraud.net''s developer surface includes documentation, signup flow, and 4 more developer resources.'
plans:
- name: Fraud Net Plans Pricing
  plan_count: 3
  slug: fraud-net-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Fraud Net Rate Limits
  slug: fraud-net-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Fraud.net API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: fraud-net-rules
score:
  band: emerging
  composite: 11.5
  delta: -3.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fraud-net/refs/heads/main/screenshots/fraud-net-2026-06-20T181510.png
security:
- kind: domain-security
  name: Fraud Net Domain Security
  slug: fraud-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fraud-net
tags:
- Fraud
- Risk
- Commerce
- Payments
- Security
website: https://fraud.net/
---
