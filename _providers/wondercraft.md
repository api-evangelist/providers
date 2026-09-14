---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Wondercraft Agentic Access
  operation_count: 7
  slug: wondercraft-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.wondercraft.ai/v1
  baseurl_source: declared
  description: The Account API from Wondercraft — 1 operation(s) for account.
  name: Wondercraft Account API
  slug: wondercraft-account-api
- baseURL: https://api.wondercraft.ai/v1
  baseurl_source: declared
  description: The Audio Generation API from Wondercraft — 2 operation(s) for audio generation.
  name: Wondercraft Audio Generation API
  slug: wondercraft-audio-generation-api
- baseURL: https://api.wondercraft.ai/v1
  baseurl_source: declared
  description: The Convo Mode API from Wondercraft — 2 operation(s) for convo mode.
  name: Wondercraft Convo Mode API
  slug: wondercraft-convo-mode-api
- baseURL: https://api.wondercraft.ai/v1
  baseurl_source: declared
  description: The Jobs API from Wondercraft — 2 operation(s) for jobs.
  name: Wondercraft Jobs API
  slug: wondercraft-jobs-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wondercraft Public Account API
  slug: open-wondercraft-account-api
- collection_type: open
  name: Wondercraft Public Account Audio Generation API
  slug: open-wondercraft-audio-generation-api
- collection_type: open
  name: Wondercraft Public Account Convo Mode API
  slug: open-wondercraft-convo-mode-api
- collection_type: open
  name: Wondercraft Public Account Jobs API
  slug: open-wondercraft-jobs-api
- collection_type: open
  name: Wondercraft Public API
  slug: open-wondercraft
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/wondercraft-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wondercraft-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wondercraft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wondercraft-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://wondercraft.ai/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wondercraftai
- group: company
  title: ''
  type: Website
  url: https://www.wondercraft.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wondercraft.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/wondercraft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wondercraft-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wondercraft-finops.yml
created: '2026-06-21'
description: Wondercraft is an AI audio creation platform for producing podcasts, audio ads, meditations, and audiobooks. Its public REST API generates audio content from an AI-written or user-supplied script, supports a two-host Convo Mode, lets callers attach platform voices and background music by ID, and exposes asynchronous jobs that are polled for status and a finished MP3 download URL.
finops:
- name: Wondercraft Finops
  service_category: AI and Machine Learning
  slug: wondercraft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wondercraft.png
layout: provider
modified: '2026-06-21'
name: Wondercraft
nav: Providers
network: true
overview: 'Wondercraft publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Audio Generation API, Convo Mode API, and 1 more. Tagged areas include Artificial Intelligence, Audio, Podcast, Text-to-Speech, and Generative Audio.


  Wondercraft''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Wondercraft Plans Pricing
  plan_count: 4
  slug: wondercraft-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Wondercraft Rate Limits
  slug: wondercraft-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/wondercraft/refs/heads/main/screenshots/wondercraft-2026-09-02T170915.png
security:
- kind: authentication
  name: Wondercraft Authentication
  slug: wondercraft-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wondercraft Domain Security
  slug: wondercraft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wondercraft
tags:
- Artificial Intelligence
- Audio
- Podcast
- Text-to-Speech
- Generative Audio
website: https://www.wondercraft.ai
---
