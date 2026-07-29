---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Dailymotion Developer API
  name: Dailymotion
  slug: dailymotion
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dailymotion-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dailymotion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.dailymotion.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: Webhooks
  url: https://developers.dailymotion.com/docs/webhooks
created: '2026-05-28'
description: Dailymotion Developer API
graphqls:
- description: Dailymotion is a video sharing platform. The API covers video search, channel management, playlists, user profiles, content moderation, advertising configuration, analytics, and live streaming.
  name: Dailymotion GraphQL API
  slug: dailymotion-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dailymotion.png
layout: provider
modified: '2026-05-30'
name: Dailymotion
nav: Providers
network: true
overview: Dailymotion publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video and Public APIs.
random_paper: 8
score:
  band: emerging
  composite: 17.6
  delta: 9.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 43.2
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 7.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/dailymotion/refs/heads/main/screenshots/dailymotion-2026-06-20T175448.png
security:
- kind: domain-security
  name: Dailymotion Domain Security
  slug: dailymotion-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dailymotion Vulnerability Disclosure
  slug: dailymotion-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dailymotion
tags:
- Video
- Public APIs
website: https://developer.dailymotion.com/
---
