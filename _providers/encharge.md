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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Encharge Agentic Access
  operation_count: 17
  slug: encharge-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 11
apis:
- description: REST API (v1) for managing people, segments, tags, fields, flows, broadcasts, and events in Encharge. Authentication is via an API key passed as the token query parameter or X-Encharge-Token header.
  name: Encharge REST API
  slug: rest-api
- description: REST API for sending transactional emails through Encharge. Accepts JSON payloads at POST /v1/emails/send and authenticates via the same API token used by the core REST API.
  name: Encharge Transactional Email API
  slug: transactional-email-api
- description: Ingest API for streaming people and activity events into Encharge from backend systems. Posts JSON payloads to ingest.encharge.io/v1/ using the same API token.
  name: Encharge Ingest API
  slug: ingest-api
- description: The Account API from Encharge — 1 operation(s) for account.
  name: Encharge Account API
  slug: encharge-account-api
- description: The Events API from Encharge — 2 operation(s) for events.
  name: Encharge Events API
  slug: encharge-events-api
- description: The Fields API from Encharge — 2 operation(s) for fields.
  name: Encharge Fields API
  slug: encharge-fields-api
- description: The Ingest API from Encharge — 1 operation(s) for ingest.
  name: Encharge Ingest API
  slug: encharge-ingest-api
- description: The People API from Encharge — 2 operation(s) for people.
  name: Encharge People API
  slug: encharge-people-api
- description: The Segments API from Encharge — 2 operation(s) for segments.
  name: Encharge Segments API
  slug: encharge-segments-api
- description: The Tags API from Encharge — 1 operation(s) for tags.
  name: Encharge Tags API
  slug: encharge-tags-api
- description: The Transactional Email API from Encharge — 1 operation(s) for transactional email.
  name: Encharge Transactional Email API
  slug: encharge-transactional-email-api
artifact_total: 16
collections:
- collection_type: open
  name: Encharge REST API
  slug: open-encharge
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/encharge-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/encharge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/encharge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/encharge-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/encharge
- group: company
  title: ''
  type: Website
  url: https://encharge.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.encharge.io
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.encharge.io/api-documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://encharge.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.encharge.io/signup
- group: build
  title: ''
  type: API Integration
  url: https://encharge.io/integrations/api/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.encharge.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://encharge.io/feed/
created: '2026-05-11'
description: Encharge is a behavior-based marketing automation platform built for SaaS companies, with a visual flow builder, broadcasts, segments, lead scoring, A/B testing, and 50+ native integrations (HubSpot, Stripe, Salesforce, Facebook Ads, and more). The platform combines email marketing automation, user profiles, and product-event tracking to send targeted emails based on what users do (or do not do) in a SaaS product. Encharge exposes REST, Ingest, and Transactional Email APIs authenticated with an API token.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/encharge.png
layout: provider
modified: '2026-05-11'
name: Encharge
nav: Providers
network: true
overview: 'Encharge publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Events API, Fields API, and 5 more. Tagged areas include Email Marketing, Marketing Automation, Transactional Email, SaaS, and Behavioral Email.


  Encharge''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 28.8
  delta: -2.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 54.7
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/encharge/refs/heads/main/screenshots/encharge-2026-06-20T180652.png
security:
- kind: authentication
  name: Encharge Authentication
  slug: encharge-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Encharge Domain Security
  slug: encharge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Encharge Vulnerability Disclosure
  slug: encharge-vulnerability-disclosure
  summary_line: disclosure policy published
slug: encharge
tags:
- Email Marketing
- Marketing Automation
- Transactional Email
- SaaS
- Behavioral Email
- Customer Engagement
website: https://encharge.io
---
