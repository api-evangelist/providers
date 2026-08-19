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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Cloudflare Stream Agentic Access
  operation_count: 33
  slug: cloudflare-stream-agentic-access
  summary_line: 33 operations · 21 acting
api_count: 6
apis:
- description: Account storage usage and viewing analytics.
  name: Cloudflare Stream Analytics API
  slug: cloudflare-stream-analytics-api
- description: Per-language captions and subtitles for a video.
  name: Cloudflare Stream Captions API
  slug: cloudflare-stream-captions-api
- description: Live inputs receiving RTMPS or SRT broadcasts, plus simulcast outputs.
  name: Cloudflare Stream Live Inputs API
  slug: cloudflare-stream-live-inputs-api
- description: Signing keys and per-video signed playback tokens.
  name: Cloudflare Stream Signed URLs API
  slug: cloudflare-stream-signed-urls-api
- description: On-demand video upload, storage, encoding, and management.
  name: Cloudflare Stream Videos API
  slug: cloudflare-stream-videos-api
- description: The single per-account webhook for video processing notifications.
  name: Cloudflare Stream Webhooks API
  slug: cloudflare-stream-webhooks-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cloudflare Stream Analytics API
  slug: open-cloudflare-stream-analytics-api
- collection_type: open
  name: Cloudflare Stream Analytics Captions API
  slug: open-cloudflare-stream-captions-api
- collection_type: open
  name: Cloudflare Stream Analytics Live Inputs API
  slug: open-cloudflare-stream-live-inputs-api
- collection_type: open
  name: Cloudflare Stream Analytics Signed URLs API
  slug: open-cloudflare-stream-signed-urls-api
- collection_type: open
  name: Cloudflare Stream Analytics Videos API
  slug: open-cloudflare-stream-videos-api
- collection_type: open
  name: Cloudflare Stream Analytics Webhooks API
  slug: open-cloudflare-stream-webhooks-api
- collection_type: open
  name: Cloudflare Stream API
  slug: open-cloudflare-stream
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudflare-stream-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudflare-stream-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudflare-stream-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudflare-stream-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudflare
- group: company
  title: ''
  type: Website
  url: https://www.cloudflare.com/products/cloudflare-stream/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudflare.com/stream/
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudflare-stream-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudflare-stream-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cloudflare-stream-finops.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudflare
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.cloudflare.com/stream/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blog.cloudflare.com/rss/
created: '2026-07-11'
description: Cloudflare Stream is the video streaming, hosting, and live-video product from Cloudflare - a single REST API for uploading, storing, encoding, and delivering on-demand and live video across Cloudflare's global network. It handles direct and TUS resumable uploads, copy-from-URL ingest, live inputs over RTMPS and SRT (with simulcast outputs and WebRTC/WHIP/WHEP beta), a built-in adaptive-bitrate player and HLS/DASH manifests, AI-generated and uploaded captions, signed-URL access control, per-account webhooks, and viewing analytics. This entry documents the Cloudflare Stream product specifically, not the broader Cloudflare platform. The API is served under https://api.cloudflare.com/client/v4/accounts/{account_id}/stream and authenticates with a Bearer API token. Billed at $5 per 1,000 minutes of video stored and $1 per 1,000 minutes delivered.
finops:
- name: Cloudflare Stream Finops
  service_category: Media and Video Streaming
  slug: cloudflare-stream-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudflare-stream.png
layout: provider
modified: '2026-07-11'
name: Cloudflare Stream
nav: Providers
network: true
overview: 'Cloudflare Stream publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Captions API, Live Inputs API, and 3 more. Tagged areas include Video, Streaming, Live Streaming, Media, and Video Hosting.


  Cloudflare Stream''s developer surface includes authentication, documentation, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Cloudflare Stream Plans Pricing
  plan_count: 3
  slug: cloudflare-stream-plans-pricing
random_paper: 115
rate_limits:
- limit_count: 4
  name: Cloudflare Stream Rate Limits
  slug: cloudflare-stream-rate-limits
score:
  band: developing
  composite: 40.2
  delta: -0.9
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 54.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudflare-stream/refs/heads/main/screenshots/cloudflare-stream-2026-07-25T205657.png
security:
- kind: authentication
  name: Cloudflare Stream Authentication
  slug: cloudflare-stream-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cloudflare Stream Domain Security
  slug: cloudflare-stream-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloudflare Stream Vulnerability Disclosure
  slug: cloudflare-stream-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: cloudflare-stream
tags:
- Video
- Streaming
- Live Streaming
- Media
- Video Hosting
- Cloudflare
website: https://www.cloudflare.com/products/cloudflare-stream/
---
