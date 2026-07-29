---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
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
- acting_count: 2
  human_in_the_loop: 0
  name: Simpleanalytics Agentic Access
  operation_count: 5
  slug: simpleanalytics-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 4
apis:
- description: The Events API from Simple Analytics — 1 operation(s) for events.
  name: Simple Analytics Events API
  slug: simpleanalytics-events-api
- description: The Export API from Simple Analytics — 1 operation(s) for export.
  name: Simple Analytics Export API
  slug: simpleanalytics-export-api
- description: The Stats API from Simple Analytics — 1 operation(s) for stats.
  name: Simple Analytics Stats API
  slug: simpleanalytics-stats-api
- description: The Websites API from Simple Analytics — 2 operation(s) for websites.
  name: Simple Analytics Websites API
  slug: simpleanalytics-websites-api
artifact_total: 11
collections:
- collection_type: open
  name: Simple Analytics API
  slug: open-simpleanalytics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simpleanalytics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simpleanalytics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simpleanalytics-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://simpleanalytics.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/simpleanalytics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simpleanalytics
- group: company
  title: ''
  type: Website
  url: https://www.simpleanalytics.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.simpleanalytics.com/api
- group: commercial
  title: ''
  type: Plans
  url: plans/simpleanalytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simpleanalytics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/simpleanalytics-finops.yml
created: '2026-06-21'
description: Simple Analytics is a privacy-first, cookieless web analytics platform built in the EU. It collects no personal data and needs no cookie banner, while exposing a REST API to pull aggregated dashboard stats, export raw data points (page views and events), collect custom events server-side, and manage the websites in an account.
finops:
- name: Simpleanalytics Finops
  service_category: Analytics
  slug: simpleanalytics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simpleanalytics.png
layout: provider
modified: '2026-06-21'
name: Simple Analytics
nav: Providers
network: true
overview: 'Simple Analytics publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Events API, Export API, Stats API, and 1 more. Tagged areas include Analytics, Web Analytics, Privacy, Cookieless, and GDPR.


  Simple Analytics'' developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Simpleanalytics Plans Pricing
  plan_count: 4
  slug: simpleanalytics-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 4
  name: Simpleanalytics Rate Limits
  slug: simpleanalytics-rate-limits
score:
  band: thin
  composite: 38.6
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Simpleanalytics Authentication
  slug: simpleanalytics-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Simpleanalytics Domain Security
  slug: simpleanalytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: simpleanalytics
tags:
- Analytics
- Web Analytics
- Privacy
- Cookieless
- GDPR
website: https://www.simpleanalytics.com
---
