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
- acting_count: 4
  human_in_the_loop: 0
  name: Listnr Agentic Access
  operation_count: 6
  slug: listnr-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: https://bff.listnr.tech/api/tts/v1
  baseurl_source: declared
  description: Poll the status of asynchronous conversion jobs.
  name: Listnr Jobs API
  slug: listnr-jobs-api
- baseURL: https://bff.listnr.tech/api/tts/v1
  baseurl_source: declared
  description: Convert SSML text or an article URL into audio.
  name: Listnr Text-to-Speech API
  slug: listnr-text-to-speech-api
- baseURL: https://bff.listnr.tech/api/tts/v1
  baseurl_source: declared
  description: List the AI voices available on Listnr.
  name: Listnr Voices API
  slug: listnr-voices-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Listnr Text-to-Speech Jobs API
  slug: open-listnr-jobs-api
- collection_type: open
  name: Listnr Jobs Text-to-Speech API
  slug: open-listnr-text-to-speech-api
- collection_type: open
  name: Listnr Text-to-Speech Jobs Voices API
  slug: open-listnr-voices-api
- collection_type: open
  name: Listnr Text-to-Speech API
  slug: open-listnr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/listnr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/listnr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/listnr-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/listnr
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/team-listnr
- group: company
  title: ''
  type: Website
  url: https://listnr.ai
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/team-listnr/text-to-speech-api
- group: start
  title: ''
  type: SignUp
  url: https://voices.listnr.tech
- group: commercial
  title: ''
  type: Plans
  url: plans/listnr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/listnr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/listnr-finops.yml
created: '2026-07-11'
description: Listnr AI is a text-to-speech and AI voice platform offering 1,000+ ultra-realistic voices across 142+ languages and accents, used for voiceovers, podcasts, and text-to-video. Beyond the web app, Listnr exposes a documented public Text-to-Speech API (base https://bff.listnr.tech/api/tts/v1) that converts SSML text or article URLs into MP3/WAV audio synchronously or asynchronously, lists available voices, and reports async job status. API keys are generated from the Listnr dashboard at voices.listnr.tech and passed via an x-listnr-token header.
finops:
- name: Listnr Finops
  service_category: AI and Machine Learning
  slug: listnr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/listnr.png
layout: provider
modified: '2026-07-11'
name: Listnr
nav: Providers
network: true
overview: 'Listnr publishes 3 APIs on the [APIs.io](https://apis.io/) network: Jobs API, Text-to-Speech API, and Voices API. Tagged areas include Artificial Intelligence, Text-to-Speech, TTS, Voice, and Speech Synthesis.


  Listnr''s developer surface includes authentication, documentation, signup flow, and 8 more developer resources.'
plans:
- name: Listnr Plans Pricing
  plan_count: 4
  slug: listnr-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Listnr Rate Limits
  slug: listnr-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/listnr/refs/heads/main/screenshots/listnr-2026-07-25T225328.png
security:
- kind: authentication
  name: Listnr Authentication
  slug: listnr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Listnr Domain Security
  slug: listnr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: listnr
tags:
- Artificial Intelligence
- Text-to-Speech
- TTS
- Voice
- Speech Synthesis
- Audio
- Voiceover
website: https://listnr.ai
---
