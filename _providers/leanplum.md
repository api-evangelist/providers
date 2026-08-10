---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agentic_access: derived
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
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Leanplum Agentic Access
  operation_count: 27
  slug: leanplum-agentic-access
  summary_line: 27 operations · 15 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: The A/B Tests API from Leanplum — 3 operation(s) for a/b tests.
  name: Leanplum A/B Tests API
  slug: leanplum-a-b-tests-api
- description: The Content & Variables API from Leanplum — 3 operation(s) for content & variables.
  name: Leanplum Content & Variables API
  slug: leanplum-content-variables-api
- description: The Data Export API from Leanplum — 5 operation(s) for data export.
  name: Leanplum Data Export API
  slug: leanplum-data-export-api
- description: The Events & Tracking API from Leanplum — 7 operation(s) for events & tracking.
  name: Leanplum Events & Tracking API
  slug: leanplum-events-tracking-api
- description: The Messaging API from Leanplum — 3 operation(s) for messaging.
  name: Leanplum Messaging API
  slug: leanplum-messaging-api
- description: The Postbacks & Batch API from Leanplum — 2 operation(s) for postbacks & batch.
  name: Leanplum Postbacks & Batch API
  slug: leanplum-postbacks-batch-api
- description: The User & Device Attributes API from Leanplum — 4 operation(s) for user & device attributes.
  name: Leanplum User & Device Attributes API
  slug: leanplum-user-device-attributes-api
artifact_total: 13
collections:
- collection_type: open
  name: Leanplum API
  slug: open-leanplum
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leanplum-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leanplum-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Leanplum
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leanplum
- group: company
  title: ''
  type: Website
  url: https://www.leanplum.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leanplum.com
- group: commercial
  title: ''
  type: Plans
  url: plans/leanplum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leanplum-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/leanplum-finops.yml
created: '2026-07-03'
description: Leanplum is a mobile marketing and multichannel customer engagement platform offering push notifications, in-app and email messaging, behavioral event tracking and analytics, A/B testing, and remotely configurable content variables. Leanplum was acquired by CleverTap in 2022 and now operates as "Leanplum by CleverTap"; the brand and its documented REST API remain active while customers are migrated onto the CleverTap platform (CleverTap has wrapped its own methods behind the Leanplum API surface to smooth that transition). All API requests are made to https://api.leanplum.com/api and authenticated with an appId plus an operation-specific clientKey (production, development, data export, or content read-only).
finops:
- name: Leanplum Finops
  service_category: Marketing and Customer Engagement
  slug: leanplum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leanplum.png
layout: provider
modified: '2026-07-03'
name: Leanplum
nav: Providers
network: true
overview: 'Leanplum publishes 7 APIs on the [APIs.io](https://apis.io/) network, including A/B Tests API, Content & Variables API, Data Export API, and 4 more. Tagged areas include Mobile Marketing, Customer Engagement, Push Notifications, Messaging, and A/B Testing.


  Leanplum''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Leanplum Plans Pricing
  plan_count: 2
  slug: leanplum-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 4
  name: Leanplum Rate Limits
  slug: leanplum-rate-limits
score:
  band: thin
  composite: 29.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.6
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leanplum/refs/heads/main/screenshots/leanplum-2026-07-25T224746.png
security:
- kind: domain-security
  name: Leanplum Domain Security
  slug: leanplum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: leanplum
tags:
- Mobile Marketing
- Customer Engagement
- Push Notifications
- Messaging
- A/B Testing
- Analytics
- CleverTap
website: https://www.leanplum.com
---
