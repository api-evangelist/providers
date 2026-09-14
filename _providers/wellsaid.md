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
- acting_count: 8
  human_in_the_loop: 0
  name: Wellsaid Agentic Access
  operation_count: 16
  slug: wellsaid-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.wellsaidlabs.com/v1
  baseurl_source: declared
  description: Manage rendered clips.
  name: WellSaid Labs Clips API
  slug: wellsaid-clips-api
- baseURL: https://api.wellsaidlabs.com/v1
  baseurl_source: declared
  description: Respelling suggestions and replacement libraries.
  name: WellSaid Labs Pronunciation API
  slug: wellsaid-pronunciation-api
- baseURL: https://api.wellsaidlabs.com/v1
  baseurl_source: declared
  description: Render text to speech as clips or audio streams.
  name: WellSaid Labs Text-to-Speech API
  slug: wellsaid-text-to-speech-api
- baseURL: https://api.wellsaidlabs.com/v1
  baseurl_source: declared
  description: Discover available voice avatars.
  name: WellSaid Labs Voices API
  slug: wellsaid-voices-api
- baseURL: https://api.wellsaidlabs.com/v1
  baseurl_source: declared
  description: Catalog of available AI voice avatars and their metadata.
  name: WellSaid Labs Voice Avatars API
  slug: wellsaid-labs-voice-avatars-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WellSaid Labs Clips API
  slug: open-wellsaid-clips-api
- collection_type: open
  name: WellSaid Labs Clips Pronunciation API
  slug: open-wellsaid-pronunciation-api
- collection_type: open
  name: WellSaid Labs Clips Text-to-Speech API
  slug: open-wellsaid-text-to-speech-api
- collection_type: open
  name: WellSaid Labs Clips Voices API
  slug: open-wellsaid-voices-api
- collection_type: open
  name: WellSaid Labs API
  slug: open-wellsaid
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wellsaid-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wellsaid-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wellsaid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wellsaid-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wellsaid-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wellsaid-labs
- group: company
  title: ''
  type: Website
  url: https://wellsaidlabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wellsaidlabs.com
- group: commercial
  title: ''
  type: Plans
  url: plans/wellsaid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wellsaid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wellsaid-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wellsaidlabs.com/docs/getting-started
created: '2026-06-21'
description: WellSaid Labs is an AI text-to-speech voice platform. Its REST API renders natural-sounding speech from text using studio-quality voice avatars, supporting synchronous clip creation, low-latency audio streaming, and word-level timing with subtitles, authenticated with an X-Api-Key header.
finops:
- name: Wellsaid Finops
  service_category: AI and Machine Learning
  slug: wellsaid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wellsaid.png
layout: provider
modified: '2026-06-21'
name: WellSaid Labs
nav: Providers
network: true
overview: 'WellSaid Labs publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Clips API, Pronunciation API, Text-to-Speech API, and 2 more. Tagged areas include Artificial Intelligence, Text-to-Speech, Voice, Audio, and TTS.


  WellSaid Labs'' developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Wellsaid Plans Pricing
  plan_count: 3
  slug: wellsaid-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Wellsaid Rate Limits
  slug: wellsaid-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/wellsaid/refs/heads/main/screenshots/wellsaid-2026-09-02T170611.png
security:
- kind: authentication
  name: Wellsaid Authentication
  slug: wellsaid-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wellsaid Domain Security
  slug: wellsaid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wellsaid Trust Center
  slug: wellsaid-trust-center
  summary_line: SOC 2, GDPR
slug: wellsaid
tags:
- Artificial Intelligence
- Text-to-Speech
- Voice
- Audio
- TTS
website: https://wellsaidlabs.com
---
