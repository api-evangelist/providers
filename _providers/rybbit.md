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
- acting_count: 1
  human_in_the_loop: 0
  name: Rybbit Agentic Access
  operation_count: 10
  slug: rybbit-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 3
apis:
- description: Stats API for events and reporting per site.
  name: Rybbit Analytics API
  slug: rybbit-analytics-api
- description: Public ingestion endpoint for pageviews and custom events.
  name: Rybbit Event Tracking API
  slug: rybbit-event-tracking-api
- description: Session-level analytics and cohort retention.
  name: Rybbit Sessions API
  slug: rybbit-sessions-api
artifact_total: 12
collections:
- collection_type: open
  name: Rybbit API
  slug: open-rybbit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rybbit-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rybbit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rybbit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rybbit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rybbit-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://rybbit.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rybbit-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rybbit
- group: company
  title: ''
  type: Website
  url: https://www.rybbit.io
- group: docs
  title: ''
  type: Documentation
  url: https://rybbit.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/rybbit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rybbit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rybbit-finops.yml
created: '2026-06-21'
description: Rybbit is an open-source, privacy-friendly web and product analytics platform positioned as a cookieless alternative to Google Analytics and Plausible. It ingests pageviews and custom events through a lightweight tracking script and HTTP /api/track endpoint, and exposes a Bearer-key-authenticated Stats API for sites, sessions, users, retention, and events. Rybbit can be self-hosted under AGPL-3.0 or consumed as a managed cloud service.
finops:
- name: Rybbit Finops
  service_category: Analytics
  slug: rybbit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rybbit.png
layout: provider
modified: '2026-06-21'
name: Rybbit
nav: Providers
network: true
overview: 'Rybbit publishes 3 APIs on the [APIs.io](https://apis.io/) network: Analytics API, Event Tracking API, and Sessions API. Tagged areas include Analytics, Web Analytics, Product Analytics, Privacy, and Open Source.


  Rybbit''s developer surface includes authentication, engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Rybbit Plans Pricing
  plan_count: 5
  slug: rybbit-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Rybbit Rate Limits
  slug: rybbit-rate-limits
score:
  band: thin
  composite: 40.3
  delta: -2.2
  facets:
    commercial_clarity: 47.4
    contract_quality: 57.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.5
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
security:
- kind: authentication
  name: Rybbit Authentication
  slug: rybbit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rybbit Domain Security
  slug: rybbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rybbit Vulnerability Disclosure
  slug: rybbit-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Rybbit Trust Center
  slug: rybbit-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: rybbit
tags:
- Analytics
- Web Analytics
- Product Analytics
- Privacy
- Open Source
- Cookieless
website: https://www.rybbit.io
---
