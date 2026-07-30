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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 23
apis:
- description: The Account API from Kumospace — 6 operation(s) for account.
  name: Kumospace Account API
  slug: kumospace-account-api
- description: The Analytics API from Kumospace — 2 operation(s) for analytics.
  name: Kumospace Analytics API
  slug: kumospace-analytics-api
- description: The Calendar API from Kumospace — 7 operation(s) for calendar.
  name: Kumospace Calendar API
  slug: kumospace-calendar-api
- description: The Chat API from Kumospace — 8 operation(s) for chat.
  name: Kumospace Chat API
  slug: kumospace-chat-api
- description: The Daily (Webhook) API from Kumospace — 1 operation(s) for daily (webhook).
  name: Kumospace Daily (Webhook) API
  slug: kumospace-daily-webhook-api
- description: The Demo API from Kumospace — 2 operation(s) for demo.
  name: Kumospace Demo API
  slug: kumospace-demo-api
- description: The Flooring API from Kumospace — 1 operation(s) for flooring.
  name: Kumospace Flooring API
  slug: kumospace-flooring-api
- description: The Furniture API from Kumospace — 2 operation(s) for furniture.
  name: Kumospace Furniture API
  slug: kumospace-furniture-api
- description: The Integrations API from Kumospace — 8 operation(s) for integrations.
  name: Kumospace Integrations API
  slug: kumospace-integrations-api
- description: The MusicTrack API from Kumospace — 2 operation(s) for musictrack.
  name: Kumospace MusicTrack API
  slug: kumospace-musictrack-api
- description: The Payments API from Kumospace — 7 operation(s) for payments.
  name: Kumospace Payments API
  slug: kumospace-payments-api
- description: The Recordings API from Kumospace — 6 operation(s) for recordings.
  name: Kumospace Recordings API
  slug: kumospace-recordings-api
- description: The Redirects API from Kumospace — 1 operation(s) for redirects.
  name: Kumospace Redirects API
  slug: kumospace-redirects-api
- description: The Room Templates API from Kumospace — 2 operation(s) for room templates.
  name: Kumospace Room Templates API
  slug: kumospace-room-templates-api
- description: The Rooms API from Kumospace — 2 operation(s) for rooms.
  name: Kumospace Rooms API
  slug: kumospace-rooms-api
- description: The Spaces API from Kumospace — 13 operation(s) for spaces.
  name: Kumospace Spaces API
  slug: kumospace-spaces-api
- description: The Stock Furniture API from Kumospace — 2 operation(s) for stock furniture.
  name: Kumospace Stock Furniture API
  slug: kumospace-stock-furniture-api
- description: The Stock Walls API from Kumospace — 1 operation(s) for stock walls.
  name: Kumospace Stock Walls API
  slug: kumospace-stock-walls-api
- description: The Transcription API from Kumospace — 5 operation(s) for transcription.
  name: Kumospace Transcription API
  slug: kumospace-transcription-api
- description: The Users API from Kumospace — 26 operation(s) for users.
  name: Kumospace Users API
  slug: kumospace-users-api
- description: The Walls API from Kumospace — 1 operation(s) for walls.
  name: Kumospace Walls API
  slug: kumospace-walls-api
- description: The Zone Templates API from Kumospace — 2 operation(s) for zone templates.
  name: Kumospace Zone Templates API
  slug: kumospace-zone-templates-api
- description: The Zones API from Kumospace — 5 operation(s) for zones.
  name: Kumospace Zones API
  slug: kumospace-zones-api
artifact_total: 26
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/kumospace-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.kumospace.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.kumospace.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.kumospace.com/help
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kumospace.com/virtual-office-guide/getting-started-guide
- group: operate
  title: ''
  type: Support
  url: https://www.kumospace.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.kumospace.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.kumospace.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kumospace
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kumospace.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.kumospace.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kumospace.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kumospace.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kumospace.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/kumospace-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kumospace-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kumospace-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kumospace-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kumospace-llms.txt
created: '2026-07-17'
description: Kumospace is a virtual office platform for remote and distributed teams, providing a persistent spatial workspace where colleagues move between rooms and floors, with proximity-based spatial audio and video, team chat channels, scheduled and ad-hoc meetings, recordings, transcription and meeting summaries, and calendar integrations with Google Calendar and Microsoft Outlook. Spaces are visually customizable through rooms, zones, floors, walls, furniture and music tracks, and the platform integrates presence status with Zoom and Microsoft Teams. Kumospace operates a publicly reachable REST API at api.kumospace.com, documented with a Swagger UI and an OpenAPI 3.0 description covering spaces, rooms, zones, users, invitations, chat, calendar, recordings, transcription, analytics and payments. The company is headquartered in New York and is backed by Lightspeed Venture Partners.
image: https://content.kumospace.com/hubfs/LinkPreviewImage@2x-1.png
layout: provider
modified: '2026-07-19'
name: Kumospace
nav: Providers
network: true
overview: 'Kumospace publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Account API, Analytics API, Calendar API, and 20 more. Tagged areas include Company, Virtual Office, Remote Work, Collaboration, and Video Conferencing.


  Kumospace''s developer surface includes API reference, documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 12 more developer resources.'
random_paper: 66
score:
  band: developing
  composite: 44.4
  delta: 1.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 45.0
    developer_ergonomics: 32.6
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 43.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kumospace/refs/heads/main/screenshots/kumospace-2026-07-25T224329.png
security:
- kind: authentication
  name: Kumospace Authentication
  slug: kumospace-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kumospace Domain Security
  slug: kumospace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kumospace Trust Center
  slug: kumospace-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: kumospace
tags:
- Company
- Virtual Office
- Remote Work
- Collaboration
- Video Conferencing
- Communications
- Real Time
- Productivity
- Meetings
- Spatial Audio
website: https://www.kumospace.com/
---
