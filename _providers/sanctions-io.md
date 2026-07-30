---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Sanctions Io Agentic Access
  operation_count: 29
  slug: sanctions-io-agentic-access
  summary_line: 29 operations · 12 acting
api_count: 6
apis:
- description: API tokens, company and webhook configuration, users, plans, and usage.
  name: sanctions.io Account Management API
  slug: sanctions-io-account-management-api
- description: Keyword search of news articles for adverse media screening (requires Accept version=3.0).
  name: sanctions.io Adverse Media API
  slug: sanctions-io-adverse-media-api
- description: Screen up to 10,000 names in a single request.
  name: sanctions.io Batch Screening API
  slug: sanctions-io-batch-screening-api
- description: Sanctions and watchlist sources available for screening, and database export.
  name: sanctions.io Data Sources API
  slug: sanctions-io-data-sources-api
- description: Continuous monitoring entries, alerts, and result review.
  name: sanctions.io Monitoring API
  slug: sanctions-io-monitoring-api
- description: Real-time single screening against sanctions, PEP, and criminal watchlists.
  name: sanctions.io Screening API
  slug: sanctions-io-screening-api
artifact_total: 13
collections:
- collection_type: open
  name: sanctions.io API
  slug: open-sanctions-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sanctions-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sanctions-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sanctions-io-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sanctions-io-llc
- group: company
  title: ''
  type: Website
  url: https://www.sanctions.io
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.sanctions.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sanctions.io/pricing-calculator
- group: start
  title: ''
  type: Signup
  url: https://api.sanctions.io/users/signup
- group: company
  title: ''
  type: Blog
  url: https://www.sanctions.io/blog
- group: operate
  title: ''
  type: Support
  url: https://help.sanctions.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/sanctions-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sanctions-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sanctions-io-finops.yml
created: '2026-07-11'
description: sanctions.io is a sanctions, PEP, and criminal watchlist screening API for AML (anti-money laundering) compliance. The REST API (base https://api.sanctions.io) screens individuals, entities, vessels, and aircraft against 75+ sanctions lists from 30+ jurisdictions (OFAC SDN and Non-SDN, EU, UN, HM Treasury, and more), over one million politically exposed person (PEP) records, criminal watchlists like Interpol Red Notices and FBI Most Wanted, and adverse media from 60,000+ news sources. It supports real-time single screening, batch screening of up to 10,000 records per request, continuous monitoring with webhook alerts, and a full sanctions database export, all behind Bearer token auth with Accept-header versioning and a self-serve 7-day free trial.
finops:
- name: Sanctions Io Finops
  service_category: Compliance and Risk Screening
  slug: sanctions-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sanctions-io.png
layout: provider
modified: '2026-07-11'
name: sanctions.io
nav: Providers
network: true
overview: 'sanctions.io publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account Management API, Adverse Media API, Batch Screening API, and 3 more. Tagged areas include Anti-Money Laundering, AML, Sanctions Screening, Compliance, and PEP Screening.


  sanctions.io''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, support, and 7 more developer resources.'
plans:
- name: Sanctions Io Plans Pricing
  plan_count: 5
  slug: sanctions-io-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 6
  name: Sanctions Io Rate Limits
  slug: sanctions-io-rate-limits
score:
  band: thin
  composite: 41.9
  delta: -2.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.8
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sanctions Io Authentication
  slug: sanctions-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sanctions Io Domain Security
  slug: sanctions-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sanctions-io
tags:
- Anti-Money Laundering
- AML
- Sanctions Screening
- Compliance
- PEP Screening
- Watchlists
- KYC
- RegTech
website: https://www.sanctions.io
---
