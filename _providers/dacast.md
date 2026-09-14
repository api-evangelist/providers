---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Dacast Agentic Access
  operation_count: 19
  slug: dacast-agentic-access
  summary_line: 19 operations · 11 acting
api_count: 1
apis:
- baseURL: https://developer.dacast.com/v2
  baseurl_source: declared
  description: Viewer analytics and reporting.
  name: Dacast Analytics API
  slug: dacast-analytics-api
- baseURL: https://developer.dacast.com/v2
  baseurl_source: declared
  description: Live streaming channels and simulcast.
  name: Dacast Live Channels API
  slug: dacast-live-channels-api
- baseURL: https://developer.dacast.com/v2
  baseurl_source: declared
  description: Ordered collections of VOD and live content.
  name: Dacast Playlists API
  slug: dacast-playlists-api
- baseURL: https://developer.dacast.com/v2
  baseurl_source: declared
  description: Video on demand upload and management.
  name: Dacast VOD API
  slug: dacast-vod-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dacast Analytics API
  slug: open-dacast-analytics-api
- collection_type: open
  name: Dacast Analytics Live Channels API
  slug: open-dacast-live-channels-api
- collection_type: open
  name: Dacast Analytics Playlists API
  slug: open-dacast-playlists-api
- collection_type: open
  name: Dacast Analytics VOD API
  slug: open-dacast-vod-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/dacast-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dacast-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dacast-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dacast-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dacast
- group: company
  title: ''
  type: Website
  url: https://www.dacast.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dacast.com
- group: commercial
  title: ''
  type: Plans
  url: plans/dacast-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dacast-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dacast-finops.yml
created: '2026-07-11'
description: Dacast is a unified live streaming and video hosting (OTT) platform that lets businesses broadcast live channels, host and monetize video on demand (VOD), organize content into playlists, and embed a white-label HTML5 player. Dacast exposes a RESTful JSON API (base https://developer.dacast.com/v2) for programmatically creating live channels, uploading and managing VOD, building playlists, and reading viewer analytics. API requests authenticate with an X-Api-Key header. API access is gated to Scale and Custom plans (trial accounts can request temporary access from sales), so the endpoints below are grounded in Dacast's public developer docs but several exact paths beyond the confirmed /v2/channel, /v2/vod, and /v2/playlist are honestly modeled.
finops:
- name: Dacast Finops
  service_category: Media and Streaming
  slug: dacast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dacast.png
layout: provider
modified: '2026-07-11'
name: Dacast
nav: Providers
network: true
overview: 'Dacast publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Live Channels API, Playlists API, and 1 more. Tagged areas include Live Streaming, Video, VOD, OTT, and Video Hosting.


  Dacast''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Dacast Plans Pricing
  plan_count: 5
  slug: dacast-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Dacast Rate Limits
  slug: dacast-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/dacast/refs/heads/main/screenshots/dacast-2026-07-25T211123.png
security:
- kind: authentication
  name: Dacast Authentication
  slug: dacast-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dacast Domain Security
  slug: dacast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dacast
tags:
- Live Streaming
- Video
- VOD
- OTT
- Video Hosting
- Media
- Analytics
website: https://www.dacast.com
---
