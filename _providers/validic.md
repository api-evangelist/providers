---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Validic Agentic Access
  operation_count: 21
  slug: validic-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 6
apis:
- description: Cellular-enabled health device activation and suspension.
  name: Validic Devices API
  slug: validic-devices-api
- description: Hosted Marketplace tokens and connection (connect/disconnect) event history.
  name: Validic Marketplace & Connections API
  slug: validic-marketplace-connections-api
- description: Standardized health observations recorded by connected apps and devices.
  name: Validic Observations & Data API
  slug: validic-observations-data-api
- description: Event-based webhook delivery to a customer endpoint.
  name: Validic Push Service API
  slug: validic-push-service-api
- description: Server-Sent Events stream of organization-wide health events.
  name: Validic Streaming API
  slug: validic-streaming-api
- description: Provision and manage users within an organization.
  name: Validic Users API
  slug: validic-users-api
artifact_total: 14
collections:
- collection_type: open
  name: Validic Inform API
  slug: open-validic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/validic-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/validic-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/validic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/validic-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/validic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/validic
- group: company
  title: ''
  type: Website
  url: https://validic.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.validic.com
- group: commercial
  title: ''
  type: Plans
  url: plans/validic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/validic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/validic-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://validic.com/blog/
created: '2026-07-05'
description: Validic is an enterprise health-data platform that connects patient-recorded data from digital health applications, medical devices, and wearables to healthcare organizations. Its Inform API and Mobile SDK provision users against an organization, present a hosted Marketplace for connecting API/cloud and Bluetooth sources, and return standardized health observations - CGM, intraday activity, point-in-time measurements, nutrition, sleep, daily summaries, and workouts. Validic also manages cellular-enabled devices, exposes connection-event history, and delivers data in real time through a Server-Sent Events Streaming API and a webhook Push Service. The platform is HITRUST-certified and HIPAA-compliant. Requests authenticate with an organization access token passed as the token query parameter over HTTPS.
finops:
- name: Validic Finops
  service_category: Health Data Platform
  slug: validic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/validic.png
layout: provider
modified: '2026-07-05'
name: Validic
nav: Providers
network: true
overview: 'Validic publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Marketplace & Connections API, Observations & Data API, and 3 more. Tagged areas include Health Data, Digital Health, Wearables, Remote Patient Monitoring, and Health IoT.


  Validic''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Validic Plans Pricing
  plan_count: 3
  slug: validic-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 5
  name: Validic Rate Limits
  slug: validic-rate-limits
score:
  band: thin
  composite: 42.0
  delta: 2.7
  facets:
    commercial_clarity: 47.4
    contract_quality: 57.2
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.3
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Validic Authentication
  slug: validic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Validic Domain Security
  slug: validic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Validic Trust Center
  slug: validic-trust-center
  summary_line: SOC 2, ISO 27001
slug: validic
tags:
- Health Data
- Digital Health
- Wearables
- Remote Patient Monitoring
- Health IoT
- Interoperability
- HIPAA
website: https://validic.com
---
