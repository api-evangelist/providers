---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
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
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 33
  human_in_the_loop: 4
  name: Daily Co Agentic Access
  operation_count: 53
  slug: daily-co-agentic-access
  summary_line: 53 operations · 33 acting · 4 human-in-the-loop
api_count: 15
apis:
- description: REST API for managing Daily domains, rooms, meeting tokens, recordings, transcripts, meetings, participants, presence, batch operations, dial-in/dial-out (PSTN/SIP), webhooks, live streaming and Daily
  name: Daily REST API
  slug: rest-api
- description: REST API and SDKs for deploying and managing voice AI agents built with the open-source Pipecat framework on Daily's infrastructure.
  name: Pipecat Cloud (Daily Bots) API
  slug: pipecat-cloud
- description: The CallTransfer API from Daily — 2 operation(s) for calltransfer.
  name: Daily CallTransfer API
  slug: daily-co-calltransfer-api
- description: The DialIn API from Daily — 1 operation(s) for dialin.
  name: Daily DialIn API
  slug: daily-co-dialin-api
- description: The DialOut API from Daily — 3 operation(s) for dialout.
  name: Daily DialOut API
  slug: daily-co-dialout-api
- description: The Domain API from Daily — 1 operation(s) for domain.
  name: Daily Domain API
  slug: daily-co-domain-api
- description: The LiveStreaming API from Daily — 3 operation(s) for livestreaming.
  name: Daily LiveStreaming API
  slug: daily-co-livestreaming-api
- description: The Meetings API from Daily — 3 operation(s) for meetings.
  name: Daily Meetings API
  slug: daily-co-meetings-api
- description: The MeetingTokens API from Daily — 2 operation(s) for meetingtokens.
  name: Daily MeetingTokens API
  slug: daily-co-meetingtokens-api
- description: The PhoneNumbers API from Daily — 4 operation(s) for phonenumbers.
  name: Daily PhoneNumbers API
  slug: daily-co-phonenumbers-api
- description: The Presence API from Daily — 1 operation(s) for presence.
  name: Daily Presence API
  slug: daily-co-presence-api
- description: The Recordings API from Daily — 6 operation(s) for recordings.
  name: Daily Recordings API
  slug: daily-co-recordings-api
- description: The Rooms API from Daily — 9 operation(s) for rooms.
  name: Daily Rooms API
  slug: daily-co-rooms-api
- description: The Transcription API from Daily — 6 operation(s) for transcription.
  name: Daily Transcription API
  slug: daily-co-transcription-api
- description: The Webhooks API from Daily — 2 operation(s) for webhooks.
  name: Daily Webhooks API
  slug: daily-co-webhooks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Review
  slug: review
collections:
- collection_type: open
  name: Daily REST API
  slug: open-daily-co
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/daily-co-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/daily-co-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/daily-co-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/daily-co-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dailyco
- group: company
  title: ''
  type: Website
  url: https://www.daily.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.daily.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.daily.co/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.daily.co/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/daily-co
- group: operate
  title: ''
  type: StatusPage
  url: https://status.daily.co/
- group: commercial
  title: ''
  type: Plans
  url: plans/daily-co-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/daily-co-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/daily-co-finops.yml
created: '2026-05-08'
description: Daily provides WebRTC video and audio infrastructure for developers — REST APIs for rooms, recordings, transcripts, meetings, dial-out and Daily Bots / Pipecat Cloud (voice AI agents), plus client SDKs for Web, iOS, Android, React Native and Flutter.
finops:
- name: Daily Co Finops
  service_category: Realtime Communications
  slug: daily-co-finops
graphqls:
- description: Conceptual GraphQL schema for the [Daily REST API](https://docs.daily.co/reference/rest-api), covering the full surface area of Daily's WebRTC video and audio infrastructure platform.
  name: Daily.co GraphQL Schema
  slug: daily-co-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/daily-co.png
layout: provider
modified: '2026-05-08'
name: Daily
nav: Providers
network: true
overview: 'Daily publishes 13 APIs on the [APIs.io](https://apis.io/) network, including CallTransfer API, DialIn API, DialOut API, and 10 more. Tagged areas include Realtime, WebRTC, Video, Audio, and SDK.


  The Daily catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Daily''s developer surface includes authentication, documentation, pricing, engineering blog, GitHub presence, and 9 more developer resources.'
plans:
- name: Daily Co Plans Pricing
  plan_count: 5
  slug: daily-co-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 3
  name: Daily Co Rate Limits
  slug: daily-co-rate-limits
score:
  band: developing
  composite: 45.9
  delta: -0.6
  facets:
    commercial_clarity: 57.9
    contract_quality: 62.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 46.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/daily-co/refs/heads/main/screenshots/daily-co-2026-06-20T175440.png
security:
- kind: authentication
  name: Daily Co Authentication
  slug: daily-co-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Daily Co Domain Security
  slug: daily-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Daily Co Trust Center
  slug: daily-co-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: daily-co
tags:
- Realtime
- WebRTC
- Video
- Audio
- SDK
- Voice AI
- Recording
- Transcription
website: https://www.daily.co/
---
