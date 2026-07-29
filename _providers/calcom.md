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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API providing full programmatic control over Cal.com resources including calendars, event types, bookings, schedules, teams, and organizations. Supports OAuth and API key authentication with rate
  name: Cal.com REST API v2
  slug: rest-api-v2
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/calcom-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/calcom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calcom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cal.com
- group: docs
  title: ''
  type: Documentation
  url: https://cal.com/docs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cal-com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/calcom
- group: commercial
  title: ''
  type: Pricing
  url: https://cal.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/calcom-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/calcom-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/calcom-finops.md
- group: company
  title: ''
  type: Blog
  url: https://cal.com/blog/category/all-categories
created: 2026-06-14
description: Open-source scheduling infrastructure with a public REST API for managing calendars, event types, bookings, teams, and availability, self-hostable or available as Cal.com Cloud.
graphqls:
- description: Cal.com does not expose a native GraphQL endpoint. The platform's public-facing API is a REST API (v2, hosted at `https://api.cal.com/v2`), and its internal application layer uses tRPC for client-serv
  name: Cal.com GraphQL API
  slug: calcom-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/calcom.png
layout: provider
modified: 2026-06-14
name: Cal.com
nav: Providers
network: true
overview: 'Cal.com publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Scheduling, Calendars, Bookings, Open Source, and Event Types.


  Cal.com''s developer surface includes documentation, pricing, engineering blog, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 24.0
  delta: 9.5
  facets:
    commercial_clarity: 18.4
    contract_quality: 43.2
    developer_ergonomics: 10.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/calcom/refs/heads/main/screenshots/calcom-2026-06-20T173843.png
security:
- kind: domain-security
  name: Calcom Domain Security
  slug: calcom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Calcom Vulnerability Disclosure
  slug: calcom-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Calcom Trust Center
  slug: calcom-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: calcom
tags:
- Scheduling
- Calendars
- Bookings
- Open Source
- Event Types
website: https://cal.com
---
