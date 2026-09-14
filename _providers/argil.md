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
  name: Argil Agentic Access
  operation_count: 20
  slug: argil-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.argil.ai/v1
  baseurl_source: declared
  description: Upload and manage B-roll and media assets.
  name: Argil Assets API
  slug: argil-assets-api
- baseURL: https://api.argil.ai/v1
  baseurl_source: declared
  description: Create and list avatars and digital twins.
  name: Argil Avatars API
  slug: argil-avatars-api
- baseURL: https://api.argil.ai/v1
  baseurl_source: declared
  description: Create, render, and manage avatar videos.
  name: Argil Videos API
  slug: argil-videos-api
- baseURL: https://api.argil.ai/v1
  baseurl_source: declared
  description: Clone, list, and sync voices.
  name: Argil Voices API
  slug: argil-voices-api
- baseURL: https://api.argil.ai/v1
  baseurl_source: declared
  description: Register and manage render-event webhooks.
  name: Argil Webhooks API
  slug: argil-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Argil Assets API
  slug: open-argil-assets-api
- collection_type: open
  name: Argil Assets Avatars API
  slug: open-argil-avatars-api
- collection_type: open
  name: Argil Assets Videos API
  slug: open-argil-videos-api
- collection_type: open
  name: Argil Assets Voices API
  slug: open-argil-voices-api
- collection_type: open
  name: Argil Assets Webhooks API
  slug: open-argil-webhooks-api
- collection_type: open
  name: Argil API
  slug: open-argil
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/argil-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/argil-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/argil-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/argil-ai
- group: company
  title: ''
  type: Website
  url: https://www.argil.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.argil.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.argil.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/argil-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/argil-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/argil-finops.yml
created: '2026-07-01'
description: Argil (Argil AI) is an AI avatar video generation platform for the creator economy. Its API programmatically produces talking-avatar videos from text or audio, clones custom avatars and voices, manages B-roll assets, and delivers render events via webhooks - turning a script into a finished, subtitled avatar video.
finops:
- name: Argil Finops
  service_category: AI and Machine Learning
  slug: argil-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/argil.png
layout: provider
modified: '2026-07-01'
name: Argil
nav: Providers
network: true
overview: 'Argil publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Avatars API, Videos API, and 2 more. Tagged areas include Artificial Intelligence, Video Generation, Avatars, Voice Cloning, and Content Automation.


  Argil''s developer surface includes authentication, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Argil Plans Pricing
  plan_count: 4
  slug: argil-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Argil Rate Limits
  slug: argil-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/argil/refs/heads/main/screenshots/argil-2026-07-25T201139.png
security:
- kind: authentication
  name: Argil Authentication
  slug: argil-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Argil Domain Security
  slug: argil-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: argil
tags:
- Artificial Intelligence
- Video Generation
- Avatars
- Voice Cloning
- Content Automation
website: https://www.argil.ai/
---
