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
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Unrealspeech Agentic Access
  operation_count: 4
  slug: unrealspeech-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.v7.unrealspeech.com
  baseurl_source: declared
  description: Synchronous text-to-speech returning an MP3 and timestamp URLs.
  name: Unreal Speech Speech API
  slug: unrealspeech-speech-api
- baseURL: https://api.v7.unrealspeech.com
  baseurl_source: declared
  description: Low-latency HTTP streaming synthesis returning audio bytes.
  name: Unreal Speech Stream API
  slug: unrealspeech-stream-api
- baseURL: https://api.v7.unrealspeech.com
  baseurl_source: declared
  description: Asynchronous synthesis for long-form audio via submit-and-poll.
  name: Unreal Speech Synthesis Tasks API
  slug: unrealspeech-synthesis-tasks-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unreal Speech API
  slug: open-unrealspeech-speech-api
- collection_type: open
  name: Unreal Speech Stream API
  slug: open-unrealspeech-stream-api
- collection_type: open
  name: Unreal Speech Synthesis Tasks API
  slug: open-unrealspeech-synthesis-tasks-api
- collection_type: open
  name: Unreal Speech API
  slug: open-unrealspeech
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unrealspeech-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unrealspeech-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unrealspeech-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unrealspeech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unrealspeech
- group: company
  title: ''
  type: Website
  url: https://unrealspeech.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unrealspeech.com
- group: commercial
  title: ''
  type: Plans
  url: plans/unrealspeech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unrealspeech-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unrealspeech-finops.yml
created: '2026-07-11'
description: Unreal Speech is a low-cost, high-scale text-to-speech (TTS) API for turning text into natural-sounding speech. It exposes a small REST surface - a low-latency HTTP streaming endpoint, a synchronous speech endpoint that returns an MP3 plus per-word or per-sentence timestamps, and an asynchronous synthesis tasks endpoint for long-form audio up to 500,000 characters. Requests are authenticated with a Bearer API key issued from the dashboard, and pricing is metered per character with a free monthly allowance.
finops:
- name: Unrealspeech Finops
  service_category: AI and Machine Learning
  slug: unrealspeech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unrealspeech.png
layout: provider
modified: '2026-07-11'
name: Unreal Speech
nav: Providers
network: true
overview: 'Unreal Speech publishes 3 APIs on the [APIs.io](https://apis.io/) network: Speech API, Stream API, and Synthesis Tasks API. Tagged areas include Text-to-Speech, TTS, Speech Synthesis, Audio, and Voice.


  Unreal Speech''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Unrealspeech Plans Pricing
  plan_count: 6
  slug: unrealspeech-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 7
  name: Unrealspeech Rate Limits
  slug: unrealspeech-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/unrealspeech/refs/heads/main/screenshots/unrealspeech-2026-09-02T164954.png
security:
- kind: authentication
  name: Unrealspeech Authentication
  slug: unrealspeech-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Unrealspeech Domain Security
  slug: unrealspeech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unrealspeech
tags:
- Text-to-Speech
- TTS
- Speech Synthesis
- Audio
- Voice
- Artificial Intelligence
website: https://unrealspeech.com
---
