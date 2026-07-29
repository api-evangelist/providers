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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/audible-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.audible.com
- group: company
  title: ''
  type: Blog
  url: https://www.audible.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.audible.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.audible.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.audible.com/legal/conditions-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.audible.com/legal/privacy-notice
- group: build
  title: ''
  type: Packages
  url: packages/audible-packages.yml
created: '2026-07-17'
description: Audible is an Amazon-owned online audiobook, podcast, and spoken-word entertainment service. It sells and streams audiobooks, Audible Originals, and podcasts through membership plans and a la carte purchases, delivered via web, iOS, Android, Alexa, and Kindle apps. Audible does not operate a public developer program or documented API — its catalog, library, and playback endpoints are a private internal API consumed by its own first-party apps. Community projects (the mkb79/Audible Python library, audible-cli, and omarroth/audible.cr) reverse-engineer that internal API; none are first-party or officially supported. This profile catalogs Audible's public web, help, and legal surface plus the unofficial client ecosystem.
image: https://www.audible.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Audible
nav: Providers
network: true
overview: 'Audible is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Audiobooks, Podcasts, and Entertainment.


  Audible''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.5
  delta: -1.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/audible/refs/heads/main/screenshots/audible-2026-07-25T201650.png
security:
- kind: domain-security
  name: Audible Domain Security
  slug: audible-domain-security
  summary_line: TLSv1.3 · DMARC
slug: audible
tags:
- Company
- Consumer
- Audiobooks
- Podcasts
- Entertainment
- Media
- Streaming
- Amazon
website: https://www.audible.com
---
