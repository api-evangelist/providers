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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/playback-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.playback.tv/
- group: operate
  title: ''
  type: Support
  url: https://help.playback.tv/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/playbacktv
created: '2026-07-17'
description: Playback (playback.tv) is a mobile-first live streaming platform backed by Khosla Ventures, where creators broadcast live streams, audiences watch and interact in real time, and streamers earn through the platform's monetization program. The consumer product is organized around streaming, watching, earning, and community guidelines. As of this enrichment pass Playback publishes a consumer web/app experience and a Notaku-powered help center but exposes no public developer API, OpenAPI specification, SDK, or documented developer surface; this profile therefore carries identity and domain-security signal only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/playback.png
layout: provider
modified: '2026-07-20'
name: Playback
nav: Providers
network: true
overview: 'Playback is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Live Streaming, Streaming, Video, and Creator Economy.


  Playback''s developer surface includes support and 3 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/playback/refs/heads/main/screenshots/playback-2026-09-02T151448.png
security:
- kind: domain-security
  name: Playback Domain Security
  slug: playback-domain-security
  summary_line: TLSv1.3 · DMARC
slug: playback
tags:
- Company
- Live Streaming
- Streaming
- Video
- Creator Economy
- Entertainment
- Consumer
- Media
website: https://www.playback.tv/
---
