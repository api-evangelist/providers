---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Signl4 Agentic Access
  operation_count: 2
  slug: signl4-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 4
apis:
- description: Simple HTTPS webhook endpoint for triggering mobile alerts in SIGNL4 from any monitoring, ITSM, or IoT tool. Accepts JSON payloads with Title and Message fields plus optional X-S4 control parameters f
  name: SIGNL4 Inbound Webhook API
  slug: inbound-webhook
- description: RESTful API for programmatic alert lifecycle management including creating events, acknowledging or closing alerts, annotating alerts, and retrieving team data. Authentication is via X-S4-Api-Key head
  name: SIGNL4 REST API
  slug: rest-api
- description: The Events API from SIGNL4 — 1 operation(s) for events.
  name: SIGNL4 Events API
  slug: signl4-events-api
- description: The Webhook API from SIGNL4 — 1 operation(s) for webhook.
  name: SIGNL4 Webhook API
  slug: signl4-webhook-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SIGNL4 Webhook and REST Events API
  slug: open-signl4-events-api
- collection_type: open
  name: SIGNL4 and REST Events Webhook API
  slug: open-signl4-webhook-api
- collection_type: open
  name: SIGNL4 Webhook and REST API
  slug: open-signl4
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/signl4-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/signl4-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signl4-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/signl4-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/signl4
- group: company
  title: ''
  type: Website
  url: https://www.signl4.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.signl4.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.signl4.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://account.signl4.com/register
- group: operate
  title: ''
  type: Support
  url: https://support.signl4.com
- group: company
  title: ''
  type: Blog
  url: https://www.signl4.com/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/signl4
created: '2026-05-11'
description: SIGNL4 is a mobile alerting and on-call duty management service that transforms emails, webhooks, and IoT events into reliable push, SMS, and voice alerts with acknowledgement tracking, escalation, and team on-call scheduling. The platform provides both an inbound webhook for sending alerts and a REST API for managing alerts, statuses, annotations, and team data. Authentication uses a team or webhook secret embedded in the URL path or supplied via the X-S4-Api-Key header.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/signl4.png
layout: provider
modified: '2026-05-11'
name: SIGNL4
nav: Providers
network: true
overview: 'SIGNL4 publishes 2 APIs on the [APIs.io](https://apis.io/) network: Events API and Webhook API. Tagged areas include Alerting, Incident Management, On-Call, Mobile Alerts, and Notifications.


  SIGNL4''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, GitHub presence, and 5 more developer resources.'
random_paper: 146
score:
  band: thin
  composite: 35.0
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 61.6
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/signl4/refs/heads/main/screenshots/signl4-2026-06-20T193912.png
security:
- kind: authentication
  name: Signl4 Authentication
  slug: signl4-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Signl4 Domain Security
  slug: signl4-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Signl4 Trust Center
  slug: signl4-trust-center
  summary_line: ISO 27001, GDPR
slug: signl4
tags:
- Alerting
- Incident Management
- On-Call
- Mobile Alerts
- Notifications
- DevOps
- IT Operations
- Monitoring
website: https://www.signl4.com
---
