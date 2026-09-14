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
- acting_count: 5
  human_in_the_loop: 0
  name: Bytark Agentic Access
  operation_count: 7
  slug: bytark-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- baseURL: https://stream.byteark.com/api/v1
  baseurl_source: declared
  description: Fleet live transcode channels.
  name: ByteArk Live API
  slug: bytark-live-api
- baseURL: https://stream.byteark.com/api/v1
  baseurl_source: declared
  description: Uploading source video files to a Stream video record.
  name: ByteArk Uploads API
  slug: bytark-uploads-api
- baseURL: https://stream.byteark.com/api/v1
  baseurl_source: declared
  description: Video-on-demand records and playback in ByteArk Stream.
  name: ByteArk Videos API
  slug: bytark-videos-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ByteArk Live API
  slug: open-bytark-live-api
- collection_type: open
  name: ByteArk Live Uploads API
  slug: open-bytark-uploads-api
- collection_type: open
  name: ByteArk Live Videos API
  slug: open-bytark-videos-api
- collection_type: open
  name: ByteArk API
  slug: open-bytark
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bytark-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bytark-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bytark-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bytark-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/byteark
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/byteark
- group: company
  title: ''
  type: Website
  url: https://www.byteark.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.byteark.com/en/
- group: commercial
  title: ''
  type: Plans
  url: plans/bytark-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bytark-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bytark-finops.yml
created: '2026-07-01'
description: ByteArk is a Thailand-based video streaming and content delivery platform founded in 2012 and headquartered in Bangkok. It provides video-on-demand (ByteArk Stream), live streaming (Fleet / Teatro), an S3-compatible object storage service, a global CDN, and a pre-configured web/mobile video player with DRM content protection. Developers integrate through REST APIs authenticated with personal access tokens and S3-compatible credentials.
finops:
- name: Bytark Finops
  service_category: Media and Content Delivery
  slug: bytark-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bytark.png
layout: provider
modified: '2026-07-01'
name: ByteArk
nav: Providers
network: true
overview: 'ByteArk publishes 3 APIs on the [APIs.io](https://apis.io/) network: Live API, Uploads API, and Videos API. Tagged areas include Video, Streaming, Video-on-Demand, Live Streaming, and CDN.


  ByteArk''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Bytark Plans Pricing
  plan_count: 4
  slug: bytark-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Bytark Rate Limits
  slug: bytark-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/bytark/refs/heads/main/screenshots/bytark-2026-07-25T204141.png
security:
- kind: authentication
  name: Bytark Authentication
  slug: bytark-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bytark Domain Security
  slug: bytark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bytark
tags:
- Video
- Streaming
- Video-on-Demand
- Live Streaming
- CDN
- Object Storage
- Transcoding
- DRM
- Media
website: https://www.byteark.com/
---
