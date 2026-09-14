---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Rask Agentic Access
  operation_count: 4
  slug: rask-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.rask.ai/v2
  baseurl_source: declared
  description: Upload and retrieve source media (video and audio).
  name: Rask AI Media API
  slug: rask-media-api
- baseURL: https://api.rask.ai/v2
  baseurl_source: declared
  description: Create, retrieve, update, and delete localization (dubbing) projects.
  name: Rask AI Projects API
  slug: rask-projects-api
- baseURL: https://api.rask.ai/v2
  baseurl_source: declared
  description: Create and retrieve transcriptions from uploaded media or SRT files.
  name: Rask AI Transcription API
  slug: rask-transcription-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rask AI Media API
  slug: open-rask-media-api
- collection_type: open
  name: Rask AI Media Projects API
  slug: open-rask-projects-api
- collection_type: open
  name: Rask AI Media Transcription API
  slug: open-rask-transcription-api
- collection_type: open
  name: Rask AI API
  slug: open-rask
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rask-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rask-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rask-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rask-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/braskai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rask-ai
- group: company
  title: ''
  type: Website
  url: https://www.rask.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.rask.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/rask-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rask-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rask-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.rask.ai/blog
created: '2026-06-21'
description: Rask AI is an AI video and audio localization platform offering automated dubbing, translation, transcription, voice cloning, and lip-sync across 130+ languages. Its REST API lets developers upload media, transcribe and translate it, create localization projects, and retrieve dubbed video, audio, and voiceover artifacts programmatically using an OAuth2 Bearer token.
finops:
- name: Rask Finops
  service_category: AI and Machine Learning
  slug: rask-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rask.png
layout: provider
modified: '2026-06-21'
name: Rask AI
nav: Providers
network: true
overview: 'Rask AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Media API, Projects API, and Transcription API. Tagged areas include Artificial Intelligence, Video Localization, Dubbing, Translation, and Transcription.


  Rask AI''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Rask Plans Pricing
  plan_count: 5
  slug: rask-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Rask Rate Limits
  slug: rask-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/rask/refs/heads/main/screenshots/rask-2026-09-02T152908.png
security:
- kind: authentication
  name: Rask Authentication
  slug: rask-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rask Domain Security
  slug: rask-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Rask Trust Center
  slug: rask-trust-center
  summary_line: SOC 2, GDPR
slug: rask
tags:
- Artificial Intelligence
- Video Localization
- Dubbing
- Translation
- Transcription
website: https://www.rask.ai
---
