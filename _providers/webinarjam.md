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
  band: human-only
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: REST API for managing WebinarJam live webinars, retrieving schedules, and registering attendees. Authenticated via an API key obtained after approval, transmitted in the request body over SSL.
  name: WebinarJam API
  slug: api
- description: REST API for managing EverWebinar automated and evergreen webinars, schedules, and registrations. Shares the same API key authentication pattern as WebinarJam.
  name: EverWebinar API
  slug: everwebinar-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/webinarjam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.webinarjam.com
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.webinarjam.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.webinarjam.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.webinarjam.com/signup
- group: operate
  title: ''
  type: Support
  url: https://support.webinarjam.com
- group: auth
  title: ''
  type: API Key Application
  url: https://support.webinarjam.com/support/solutions/articles/153000168623-apply-for-a-webinarjam-everwebinar-api-key
- group: company
  title: ''
  type: Blog
  url: https://www.webinarjam.com/blog
created: '2026-05-11'
description: WebinarJam is a live webinar platform for marketing, training, and sales events, while its sibling product EverWebinar provides automated and evergreen webinar replays. Both products share a REST API that lets integrators retrieve webinars, register attendees, manage registrants, and drive marketing automations. The WebinarJam/EverWebinar API uses an API key (requiring approval) included in request payloads, with separate base paths for each product family.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/webinarjam.png
layout: provider
modified: '2026-05-11'
name: WebinarJam
nav: Providers
network: true
overview: 'WebinarJam publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Webinars, Marketing, Live Events, Automated Webinars, and Lead Generation.


  WebinarJam''s developer surface includes documentation, pricing, signup flow, support, engineering blog, and 3 more developer resources.'
random_paper: 72
score:
  band: minimal
  composite: 12.0
  delta: -2.4
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/webinarjam/refs/heads/main/screenshots/webinarjam-2026-06-20T201333.png
security:
- kind: domain-security
  name: Webinarjam Domain Security
  slug: webinarjam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: webinarjam
tags:
- Webinars
- Marketing
- Live Events
- Automated Webinars
- Lead Generation
- SaaS
website: https://www.webinarjam.com
---
