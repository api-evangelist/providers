---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Castr Live Agentic Access
  operation_count: 31
  slug: castr-live-agentic-access
  summary_line: 31 operations · 18 acting
api_count: 5
apis:
- description: Activity logs, activity events, and stream stats.
  name: Castr Analytics API
  slug: castr-live-analytics-api
- description: Live streams and their multistream platform destinations.
  name: Castr Live Streams API
  slug: castr-live-live-streams-api
- description: Ultra-low-latency (WebRTC) live streams.
  name: Castr Sub-Second Streams API
  slug: castr-live-sub-second-streams-api
- description: Video hosting folders, uploads, and live-to-VOD recordings.
  name: Castr Video Hosting API
  slug: castr-live-video-hosting-api
- description: Webhook endpoints for event delivery.
  name: Castr Webhooks API
  slug: castr-live-webhooks-api
artifact_total: 12
collections:
- collection_type: open
  name: Castr API
  slug: open-castr-live
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/castr-live-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/castr-live-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/castr-live-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://castr.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/castr-live
- group: docs
  title: ''
  type: Documentation
  url: https://developers.castr.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.castr.com/reference/get_v2-live-streams
- group: start
  title: ''
  type: SignUp
  url: https://castr.com/app/manage/api
- group: commercial
  title: ''
  type: Pricing
  url: https://castr.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/castr-live-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/castr-live-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/castr-live-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://castr.com/blog/
created: '2026-07-11'
description: Castr is a live video streaming and multistreaming platform with video hosting (VOD), that lets you ingest a single RTMP/SRT source and restream it to multiple destinations, record and clip live streams, host and deliver on-demand video, run ultra-low-latency sub-second (WebRTC) streams, and embed a player. Castr exposes a documented, self-serve REST API at https://api.castr.com/v2 for managing live streams and their platform destinations, sub-second streams, video hosting folders and uploads, live-to-VOD recordings, activity/analytics logs and events, and webhook endpoints. Requests are authenticated with an API token issued from the account settings and sent in an authorization header.
finops:
- name: Castr Live Finops
  service_category: Media and Video Streaming
  slug: castr-live-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/castr-live.png
layout: provider
modified: '2026-07-11'
name: Castr
nav: Providers
network: true
overview: 'Castr publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Live Streams API, Sub-Second Streams API, and 2 more. Tagged areas include Live Streaming, Multistreaming, Video Hosting, VOD, and Video.


  Castr''s developer surface includes authentication, documentation, API reference, signup flow, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Castr Live Plans Pricing
  plan_count: 6
  slug: castr-live-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 6
  name: Castr Live Rate Limits
  slug: castr-live-rate-limits
score:
  band: developing
  composite: 44.0
  delta: -0.5
  facets:
    commercial_clarity: 63.2
    contract_quality: 56.7
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/castr-live/refs/heads/main/screenshots/castr-live-2026-07-25T204743.png
security:
- kind: authentication
  name: Castr Live Authentication
  slug: castr-live-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Castr Live Domain Security
  slug: castr-live-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: castr-live
tags:
- Live Streaming
- Multistreaming
- Video Hosting
- VOD
- Video
- Restreaming
- Sub-Second Streaming
- WebRTC
- Analytics
- Webhooks
website: https://castr.com
---
