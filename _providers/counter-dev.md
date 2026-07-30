---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Counter Dev Agentic Access
  operation_count: 8
  slug: counter-dev-agentic-access
  summary_line: 8 operations · 5 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: The Account API from Counter — 4 operation(s) for account.
  name: Counter Account API
  slug: counter-dev-account-api
- description: The Stats API from Counter — 2 operation(s) for stats.
  name: Counter Stats API
  slug: counter-dev-stats-api
- description: The Tracking API from Counter — 2 operation(s) for tracking.
  name: Counter Tracking API
  slug: counter-dev-tracking-api
artifact_total: 10
collections:
- collection_type: open
  name: Counter API
  slug: open-counter-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/counter-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/counter-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/counter-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ihucos/counter.dev
- group: company
  title: ''
  type: Website
  url: https://counter.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://counter.dev/help/integration.html
- group: commercial
  title: ''
  type: Plans
  url: plans/counter-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/counter-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/counter-dev-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://counter.dev/blog
created: '2026-06-21'
description: Counter (counter.dev) is an open-source, privacy-friendly web analytics service. A lightweight tracking snippet POSTs a single aggregated hit per visit to a public collect endpoint (t.counter.dev), and a token-authenticated dashboard data feed returns aggregated stats. Counter uses no cookies, no logging, and no IP fingerprinting. It is AGPL-3.0 licensed and can be self-hosted; the hosted service is pay-what-you-want.
finops:
- name: Counter Dev Finops
  service_category: Analytics
  slug: counter-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/counter-dev.png
layout: provider
modified: '2026-06-21'
name: Counter
nav: Providers
network: true
overview: 'Counter publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Stats API, and Tracking API. Tagged areas include Web Analytics, Privacy, Open Source, Tracking, and Self-Hosted.


  Counter''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Counter Dev Plans Pricing
  plan_count: 2
  slug: counter-dev-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 3
  name: Counter Dev Rate Limits
  slug: counter-dev-rate-limits
score:
  band: thin
  composite: 36.0
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/counter-dev/refs/heads/main/screenshots/counter-dev-2026-07-25T210507.png
security:
- kind: authentication
  name: Counter Dev Authentication
  slug: counter-dev-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Counter Dev Domain Security
  slug: counter-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: counter-dev
tags:
- Web Analytics
- Privacy
- Open Source
- Tracking
- Self-Hosted
website: https://counter.dev/
---
