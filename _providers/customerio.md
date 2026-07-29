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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Customerio Agentic Access
  operation_count: 35
  slug: customerio-agentic-access
  summary_line: 35 operations · 25 acting
api_count: 14
apis:
- description: Outbound reporting webhooks that POST real-time message activity events (email/sms/push/in-app delivered, opened, clicked, bounced, converted, unsubscribed, and more) as JSON to a customer-supplied HT
  name: Customer.io Reporting Webhooks
  slug: reporting-webhooks
- description: App API - trigger API-driven broadcasts.
  name: Customer.io Broadcasts API
  slug: customerio-broadcasts-api
- description: App API - read campaigns, their metrics, and actions.
  name: Customer.io Campaigns API
  slug: customerio-campaigns-api
- description: App API - manage reusable data collections.
  name: Customer.io Collections API
  slug: customerio-collections-api
- description: App API - look up people, their attributes, segments, and messages.
  name: Customer.io Customers API
  slug: customerio-customers-api
- description: Track API - register and remove customer device tokens.
  name: Customer.io Devices API
  slug: customerio-devices-api
- description: Track API - send customer or anonymous behavioral events.
  name: Customer.io Events API
  slug: customerio-events-api
- description: App API - export customers and deliveries.
  name: Customer.io Exports API
  slug: customerio-exports-api
- description: App API - read sent messages and their metadata.
  name: Customer.io Messages API
  slug: customerio-messages-api
- description: Track API - add, update, suppress, or delete people (customers).
  name: Customer.io People API
  slug: customerio-people-api
- description: Pipelines / CDP API - identify, track, page, screen, group, alias, batch.
  name: Customer.io Pipelines API
  slug: customerio-pipelines-api
- description: Manual segment membership management.
  name: Customer.io Segments API
  slug: customerio-segments-api
- description: Track API v2 entity and batch endpoints.
  name: Customer.io Track v2 API
  slug: customerio-track-v2-api
- description: App API - send transactional email, push, SMS, and in-app messages.
  name: Customer.io Transactional API
  slug: customerio-transactional-api
artifact_total: 23
collections:
- collection_type: open
  name: Customer.io API
  slug: open-customerio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/customerio-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/customerio-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/customerio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/customerio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/customerio-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/customerio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/customer-io
- group: company
  title: ''
  type: Website
  url: https://customer.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.customer.io
- group: commercial
  title: ''
  type: Plans
  url: plans/customerio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/customerio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/customerio-finops.yml
created: '2026-06-20'
description: Customer.io is a customer messaging and marketing automation platform. Its APIs let teams pipe behavioral data in, manage people and their attributes, trigger campaigns and broadcasts, send transactional email, push, SMS, and in-app messages, and stream delivery activity back out via reporting webhooks. The surface spans the Track API (basic site-id + api-key auth), the App / Transactional API (Bearer), and the Pipelines / Data Pipelines CDP API.
finops:
- name: Customerio Finops
  service_category: Marketing and Customer Engagement
  slug: customerio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/customerio.png
layout: provider
modified: '2026-06-20'
name: Customer.io
nav: Providers
network: true
overview: 'Customer.io publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Broadcasts API, Campaigns API, Collections API, and 10 more. Tagged areas include Customer Messaging, Marketing Automation, Email, CDP, and Transactional.


  Customer.io''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Customerio Plans Pricing
  plan_count: 3
  slug: customerio-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 6
  name: Customerio Rate Limits
  slug: customerio-rate-limits
score:
  band: thin
  composite: 39.8
  delta: -2.2
  facets:
    commercial_clarity: 47.4
    contract_quality: 57.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/customerio/refs/heads/main/screenshots/customerio-2026-06-20T175350.png
security:
- kind: authentication
  name: Customerio Authentication
  slug: customerio-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Customerio Domain Security
  slug: customerio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Customerio Vulnerability Disclosure
  slug: customerio-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Customerio Trust Center
  slug: customerio-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: customerio
tags:
- Customer Messaging
- Marketing Automation
- Email
- CDP
- Transactional
website: https://customer.io
---
