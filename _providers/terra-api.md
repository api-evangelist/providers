---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 5
  human_in_the_loop: 0
  name: Terra Api Agentic Access
  operation_count: 16
  slug: terra-api-agentic-access
  summary_line: 16 operations · 5 acting
api_count: 11
apis:
- description: Terra's primary data-delivery mechanism. Rather than a polling or WebSocket transport, Terra streams normalized health data and lifecycle events - auth, deauth, connection errors, and activity/body/da
  name: Terra Webhooks
  slug: terra-api-webhooks
- description: Workout and exercise sessions.
  name: Terra Activity API
  slug: terra-api-activity-api
- description: Connected-user athlete profile and demographics.
  name: Terra Athlete API
  slug: terra-api-athlete-api
- description: Connect and disconnect end-user wearable and health accounts.
  name: Terra Authentication API
  slug: terra-api-authentication-api
- description: Body and biometric measurements.
  name: Terra Body API
  slug: terra-api-body-api
- description: Day-level aggregated summaries.
  name: Terra Daily API
  slug: terra-api-daily-api
- description: Catalog of supported wearables, trackers, and health apps.
  name: Terra Integrations API
  slug: terra-api-integrations-api
- description: Menstrual cycle and reproductive health data.
  name: Terra Menstruation API
  slug: terra-api-menstruation-api
- description: Logged nutrition and dietary intake.
  name: Terra Nutrition API
  slug: terra-api-nutrition-api
- description: Sleep sessions and stages.
  name: Terra Sleep API
  slug: terra-api-sleep-api
- description: Look up and manage connected users and subscriptions.
  name: Terra Users API
  slug: terra-api-users-api
artifact_total: 18
collections:
- collection_type: open
  name: Terra API
  slug: open-terra-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/terra-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terra-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/terra-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tryterra
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/terraapi
- group: company
  title: ''
  type: Website
  url: https://tryterra.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryterra.co
- group: commercial
  title: ''
  type: Plans
  url: plans/terra-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/terra-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/terra-api-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tryterra.co/blog
created: '2026-07-03'
description: Terra is a unified wearables and health-data API that aggregates data from 500+ wearables, fitness trackers, and health apps - Garmin, Fitbit, Oura, Apple Health, Whoop, Strava, Google Fit, Polar, Withings, and many more - behind a single normalized REST interface. Developers connect end users through the Terra Widget or a custom authentication flow, then receive normalized Activity, Body, Daily, Sleep, Nutrition, Menstruation, and Athlete data. Terra's primary delivery model is asynchronous - requested and newly available health data is streamed to a developer-configured webhook destination rather than returned inline, with REST read endpoints available for on-demand historical pulls.
finops:
- name: Terra Api Finops
  service_category: Health and Wearable Data
  slug: terra-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/terra-api.png
layout: provider
modified: '2026-07-03'
name: Terra
nav: Providers
network: true
overview: 'Terra publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Athlete API, Authentication API, and 7 more. Tagged areas include Wearables, Health Data, Fitness, Aggregator, and Webhooks.


  Terra''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Terra Api Plans Pricing
  plan_count: 4
  slug: terra-api-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 3
  name: Terra Api Rate Limits
  slug: terra-api-rate-limits
score:
  band: thin
  composite: 35.8
  delta: -3.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Terra Api Authentication
  slug: terra-api-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Terra Api Domain Security
  slug: terra-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: terra-api
tags:
- Wearables
- Health Data
- Fitness
- Aggregator
- Webhooks
- Digital Health
website: https://tryterra.co
---
