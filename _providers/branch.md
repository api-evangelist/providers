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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: 'A GraphQL API that enables partner platforms to embed Branch home and auto insurance quoting, binding, and policy management into their own workflows. The API covers the full insurance lifecycle from '
  name: Branch Quote to Bind API
  slug: quote-to-bind-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/branch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ourbranch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.v2.api.ourbranch.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ourbranch.com/s/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/branch-insurance
- group: other
  title: ''
  type: X
  url: https://twitter.com/branchinsurance
- group: commercial
  title: ''
  type: Plans
  url: plans/branch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/branch-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/branch-finops.yml
created: '2026-06-13'
description: Branch is a home and auto insurance platform that offers bundled policy quoting, binding, payment processing, and policy management through a GraphQL API. Partners can embed Branch's insurance products directly into their own workflows using the Quote to Bind API, enabling customers to get quotes and purchase home, auto, renters, and umbrella insurance in seconds.
finops:
- name: Branch Finops
  service_category: ''
  slug: branch-finops
graphqls:
- description: 'Branch Insurance (ourbranch.com) is an InsurTech platform that enables partners to embed home, auto, renters, and umbrella insurance directly into their own workflows. Unlike many insurance providers '
  name: Branch Insurance GraphQL API
  slug: branch-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/branch.png
layout: provider
modified: '2026-06-13'
name: Branch Insurance
nav: Providers
network: true
overview: 'Branch Insurance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Home Insurance, Auto Insurance, Renters Insurance, and Umbrella Insurance.


  Branch Insurance''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Branch Plans Pricing
  plan_count: 1
  slug: branch-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 0
  name: Branch Rate Limits
  slug: branch-rate-limits
score:
  band: emerging
  composite: 23.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 43.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/branch/refs/heads/main/screenshots/branch-2026-06-20T173630.png
security:
- kind: domain-security
  name: Branch Domain Security
  slug: branch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: branch
tags:
- Insurance
- Home Insurance
- Auto Insurance
- Renters Insurance
- Umbrella Insurance
- Quote to Bind
- GraphQL
- InsurTech
website: https://www.ourbranch.com/
---
