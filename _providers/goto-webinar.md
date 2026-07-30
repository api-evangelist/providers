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
- acting_count: 6
  human_in_the_loop: 0
  name: Goto Webinar Agentic Access
  operation_count: 20
  slug: goto-webinar-agentic-access
  summary_line: 20 operations · 6 acting
api_count: 8
apis:
- description: REST API for managing organizers, webinars, sessions, registrants, attendees, panelists, polls, surveys, and recordings on the GoTo Webinar platform. Authentication uses OAuth 2.0 via the GoTo identit
  name: GoTo Webinar REST API v2
  slug: rest-api-v2
- description: The Attendees API from GoTo Webinar — 2 operation(s) for attendees.
  name: GoTo Webinar Attendees API
  slug: goto-webinar-attendees-api
- description: The Panelists API from GoTo Webinar — 1 operation(s) for panelists.
  name: GoTo Webinar Panelists API
  slug: goto-webinar-panelists-api
- description: The Polls API from GoTo Webinar — 1 operation(s) for polls.
  name: GoTo Webinar Polls API
  slug: goto-webinar-polls-api
- description: The Questions API from GoTo Webinar — 1 operation(s) for questions.
  name: GoTo Webinar Questions API
  slug: goto-webinar-questions-api
- description: The Registrants API from GoTo Webinar — 2 operation(s) for registrants.
  name: GoTo Webinar Registrants API
  slug: goto-webinar-registrants-api
- description: The Sessions API from GoTo Webinar — 3 operation(s) for sessions.
  name: GoTo Webinar Sessions API
  slug: goto-webinar-sessions-api
- description: The Webinars API from GoTo Webinar — 4 operation(s) for webinars.
  name: GoTo Webinar Webinars API
  slug: goto-webinar-webinars-api
artifact_total: 13
collections:
- collection_type: open
  name: GoTo Webinar REST API v2
  slug: open-goto-webinar
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/goto-webinar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goto-webinar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/goto-webinar-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/goto-webinar-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.goto.com/webinar
- group: docs
  title: ''
  type: Documentation
  url: https://developer.goto.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.goto.com/webinar/pricing
- group: start
  title: ''
  type: Signup
  url: https://developer.goto.com/Registration
- group: operate
  title: ''
  type: StatusPage
  url: https://status.developer.goto.com
- group: operate
  title: ''
  type: Support
  url: https://developer.goto.com/support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goto
created: '2026-05-11'
description: GoTo Webinar is a webinar and virtual event platform from GoTo (formerly LogMeIn) used by marketing, training, and corporate communications teams to host live and on-demand webinars with registration, polling, Q&A, recordings, and analytics. The product integrates with marketing automation and CRM systems to drive lead capture and attendee follow-up. The GoTo Webinar v2 REST API exposes organizer, webinar, session, registrant, attendee, and analytics endpoints under api.getgo.com and uses OAuth2 for authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goto-webinar.png
layout: provider
modified: '2026-05-11'
name: GoTo Webinar
nav: Providers
network: true
overview: 'GoTo Webinar publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Panelists API, Polls API, and 4 more. Tagged areas include Webinars, Virtual Events, Video Conferencing, Marketing, and Lead Capture.


  GoTo Webinar''s developer surface includes authentication, documentation, pricing, signup flow, support, and 6 more developer resources.'
random_paper: 0
scopes:
- name: Goto Webinar Scopes
  scope_count: 1
  slug: goto-webinar-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 28.8
  delta: -2.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.0
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goto-webinar/refs/heads/main/screenshots/goto-webinar-2026-06-20T182256.png
security:
- kind: authentication
  name: Goto Webinar Authentication
  slug: goto-webinar-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Goto Webinar Domain Security
  slug: goto-webinar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goto-webinar
tags:
- Webinars
- Virtual Events
- Video Conferencing
- Marketing
- Lead Capture
- Registration
website: https://www.goto.com/webinar
---
