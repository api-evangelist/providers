---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
api_count: 3
apis:
- description: The Pandora Developer API provides GraphQL-based access to Pandora's music catalog of over 30 million tracks, stations, podcasts, and playlists. It supports personalized playback, search, user feedbac
  name: Pandora Developer API
  slug: pandora-api
- description: The AdsWizz Domain API is a programmatic audio advertising platform API enabling dynamic ad insertion, campaign management, and audience targeting across streaming radio, podcasts, and digital audio c
  name: AdsWizz Domain API
  slug: adswizz-domain-api
- description: The AdsWizz SDK provides mobile and web integration for audio advertising, supporting VAST-compliant ad tech with companion banner support. Available for iOS (Swift), Android (Kotlin), and Web (JavaSc
  name: AdsWizz SDK
  slug: adswizz-sdk
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sirius-xm-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/siriusxm
- group: company
  title: ''
  type: Website
  url: https://www.siriusxm.com/
- group: company
  title: ''
  type: Website
  url: https://www.siriusxmmedia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.pandora.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pandora.com/docs/
- group: company
  title: ''
  type: Blog
  url: https://www.siriusxm.com/blog/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/SiriusXM
- group: other
  title: ''
  type: AdvertisingPlatform
  url: https://www.siriusxmmedia.com/
- group: other
  title: ''
  type: AdsWizz
  url: https://www.adswizz.com/
- group: docs
  title: ''
  type: AdsWizzDocs
  url: https://docs.adswizz.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.siriusxm.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.siriusxm.com/privacy
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.siriusxm.com/
created: '2025-01-01'
description: Sirius XM Holdings is the leading audio entertainment company in North America, providing satellite radio, digital streaming, podcast, and advertising services through SiriusXM, Pandora, and AdsWizz brands. The Pandora Developer API enables partners to build personalized music and podcast streaming experiences using GraphQL. AdsWizz, a SiriusXM company, provides programmatic audio advertising APIs for ad insertion, targeting, and measurement across streaming and podcast platforms.
examples:
- key_count: 4
  name: Sirius Xm Pandora Search Example
  slug: sirius-xm-pandora-search-example
finops:
- name: Sirius Xm Finops
  service_category: Audio Streaming / Advertising
  slug: sirius-xm-finops
graphqls:
- description: The Pandora Developer API provides GraphQL-based access to Pandora's music catalog of over 30 million tracks, stations, podcasts, and playlists. It supports personalized playback, search, user feedbac
  name: Sirius XM GraphQL API
  slug: sirius-xm-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sirius-xm.png
json_schemas:
- name: Pandora Station
  property_count: 9
  slug: sirius-xm-station
- name: Pandora Track
  property_count: 9
  slug: sirius-xm-track
json_structures:
- name: Sirius Xm Playback Structure
  property_count: 0
  slug: sirius-xm-playback-structure
jsonld:
- class_count: 13
  name: Sirius Xm Context
  property_count: 8
  slug: sirius-xm-context
layout: provider
modified: '2026-05-02'
name: Sirius XM
nav: Providers
network: true
overview: 'Sirius XM publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, Streaming, Radio, Music, and Podcast.


  The Sirius XM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sirius XM''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Sirius Xm Plans Pricing
  plan_count: 1
  slug: sirius-xm-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 1
  name: Sirius Xm Rate Limits
  slug: sirius-xm-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sirius XM API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sirius-xm-jsonschema-spectral-rules
score:
  band: emerging
  composite: 23.9
  delta: -5.9
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 11.3
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 29.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sirius-xm/refs/heads/main/screenshots/sirius-xm-2026-06-20T193948.png
security:
- kind: domain-security
  name: Sirius Xm Domain Security
  slug: sirius-xm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sirius-xm
tags:
- Audio
- Streaming
- Radio
- Music
- Podcast
- Advertising
- Entertainment
website: https://www.siriusxm.com/
---
