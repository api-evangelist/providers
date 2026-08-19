---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: A cloud-based text-to-speech API. When using the API from within your software or application, you simply send text to the ReadSpeaker speechCloud API servers and receive audio data in the file format
  name: ReadSpeaker speechCloud API
  slug: speechcloud-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/readspeaker-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ReadSpeaker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/readspeaker
- group: start
  title: ''
  type: Portal
  url: https://www.readspeaker.com/
- group: other
  title: ''
  type: Products
  url: https://www.readspeaker.com/products/
- group: operate
  title: ''
  type: Support
  url: https://www.readspeaker.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.readspeaker.com/blog/
- group: company
  title: ''
  type: About
  url: https://www.readspeaker.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.readspeaker.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.readspeaker.com/privacy-policy/
created: '2025-02-06'
description: ReadSpeaker provides text-to-speech (TTS) cloud and embedded solutions used to add voice to websites, mobile apps, e-learning, transportation systems, and more. The speechCloud API converts text into high-quality audio in multiple languages and voices that can be returned in formats such as MP3 for use within applications.
finops:
- name: Readspeaker Finops
  service_category: API
  slug: readspeaker-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/readspeaker.png
layout: provider
modified: '2026-04-28'
name: ReadSpeaker
nav: Providers
network: true
overview: 'ReadSpeaker publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Text-to-Speech, Speech, Audio, Voice, and AI.


  ReadSpeaker''s developer surface includes developer portal, support, engineering blog, and 7 more developer resources.'
plans:
- name: Readspeaker Plans Pricing
  plan_count: 3
  slug: readspeaker-plans-pricing
random_paper: 116
rate_limits:
- limit_count: 5
  name: Readspeaker Rate Limits
  slug: readspeaker-rate-limits
score:
  band: emerging
  composite: 15.9
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 15.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/readspeaker/refs/heads/main/screenshots/readspeaker-2026-06-20T192643.png
security:
- kind: domain-security
  name: Readspeaker Domain Security
  slug: readspeaker-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: readspeaker
tags:
- Text-to-Speech
- Speech
- Audio
- Voice
- AI
- Accessibility
website: https://www.readspeaker.com/
---
