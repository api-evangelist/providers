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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/distrokid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/distrokid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://distrokid.com
- group: commercial
  title: ''
  type: Pricing
  url: https://distrokid.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://distrokid.com/signup/
- group: start
  title: ''
  type: Login
  url: https://distrokid.com/signin/
- group: operate
  title: ''
  type: HelpCenter
  url: https://distrokid.zendesk.com/hc/en-us
- group: other
  title: ''
  type: Stores
  url: https://distrokid.com/stores/
- group: other
  title: ''
  type: HyperFollow
  url: https://distrokid.com/hyperfollow/
- group: other
  title: ''
  type: DistroVid
  url: https://distrokid.com/distrovid/
- group: other
  title: ''
  type: Mixea
  url: https://mixea.com
- group: other
  title: ''
  type: Upstream
  url: https://distrokid.com/upstream/
- group: other
  title: ''
  type: Direct
  url: https://distrokid.com/direct/
- group: other
  title: ''
  type: Teams
  url: https://distrokid.com/teams/
- group: company
  title: ''
  type: Blog
  url: https://blog.distrokid.com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/distrokid
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/distrokid
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/distrokid
- group: company
  title: ''
  type: Facebook
  url: https://facebook.com/distrokid
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@distrokid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/distrokid
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Distrokid
- group: company
  title: ''
  type: Careers
  url: https://jobs.insightpartners.com/companies/distrokid
- group: operate
  title: ''
  type: Contact
  url: https://distrokid.zendesk.com/hc/en-us/requests/new
created: '2026-05-25'
description: DistroKid is a Brooklyn, New York based digital music distribution service founded in 2013 by Philip Kaplan that lets independent musicians and labels upload an unlimited number of songs and albums to Spotify, Apple Music, Amazon Music, YouTube Music, TikTok, Instagram, Pandora, Tidal, Deezer, and dozens of other streaming and download stores for a flat annual subscription fee while keeping 100% of their royalties. By 2020 the platform was distributing roughly a third of all new music released worldwide and serving more than two million artists; Spotify and Insight Partners both hold equity stakes following a 2021 valuation around $1.3B. Around the core distribution product DistroKid has built out a suite of artist services including Teams for automated royalty splits, cover-song mechanical licensing, YouTube Content ID monetization, DistroVid music-video distribution, Upstream label matching, Mixea AI mastering, and DistroKid Direct for fan merchandising and pre-orders. The
  company has historically operated without a public developer API — integrations with stores, DSPs, rights organizations, and partners are handled through private B2B arrangements, and the only public web endpoints exposed under distrokid.com/api are unauthenticated pre-save widgets used to drive Spotify follow/save campaigns. DistroKid is actively hiring API engineers to scale partner and AI-facing integrations, suggesting a more formal developer surface may emerge, but as of 2026 there is no published OpenAPI specification, SDK, CLI, sandbox, or developer portal. Third-party reverse-engineered wrappers such as the unofficial Golang `distrogo` library exist but are not endorsed.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/distrokid.png
layout: provider
modified: '2026-05-25'
name: DistroKid
nav: Providers
network: true
overview: 'DistroKid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Music Distribution, Digital Music, Streaming, and Independent Artists.


  DistroKid''s developer surface includes pricing, signup flow, engineering blog, YouTube channel, GitHub presence, and 19 more developer resources.'
random_paper: 79
score:
  band: minimal
  composite: 10.3
  delta: -1.4
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/distrokid/refs/heads/main/screenshots/distrokid-2026-07-25T212120.png
security:
- kind: domain-security
  name: Distrokid Domain Security
  slug: distrokid-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Distrokid Vulnerability Disclosure
  slug: distrokid-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: distrokid
tags:
- Music
- Music Distribution
- Digital Music
- Streaming
- Independent Artists
- Royalties
- Rights Management
- Content ID
- Music Mastering
- Music Videos
- Merchandise
- Subscription
- Creator Economy
website: https://distrokid.com
---
