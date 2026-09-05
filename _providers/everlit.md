---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: The one Everlit surface an agent or a third-party CMS can call today with no credential and no onboarding. GET /oembed resolves an Everlit embed or hosted URL to an oEmbed 1.0 "rich" record (title, de
  name: Everlit oEmbed and Embed Player
  slug: everlit-oembed-and-embed-player
- description: Everlit markets a REST API for connecting a custom CMS or platform that has no native integration — "our REST API makes it possible to connect Everlit to any platform" — and its WordPress plugin is co
  name: Everlit REST API
  slug: everlit-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everlit-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/everlit-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/everlit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/everlit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/everlit-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/everlit-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://everlit.audio/legal/dpa
- group: design
  title: ''
  type: DataModel
  url: data-model/everlit-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/everlit-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/everlit-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/everlit-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/everlit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/everlit-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://everlit.audio/faq
- group: company
  title: ''
  type: Blog
  url: https://everlit.audio/dispatches
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/everlit-audio
- group: start
  title: ''
  type: Login
  url: https://studio.everlit.audio
- group: commercial
  title: ''
  type: TermsOfService
  url: https://everlit.audio/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://everlit.audio/legal/privacy
created: '2026-08-19'
description: Everlit is a B2B SaaS distribution and engagement platform that converts written content (articles, blog posts, newsletters) into audio, social video, and podcasts, then auto-distributes it. Capabilities include AI text-to-audio with voice cloning across 70+ languages, an embeddable audio player and smart playlists, podcast syndication to Apple Podcasts, Spotify and any RSS 2.0 / Podcast 2.0 app, social video generation in 16:9, 1:1 and 9:16, programmatic audio monetization through Google Ad Manager plus direct sponsorships and house ads, engagement analytics, and CMS integration through a native WordPress plugin or a zero-touch JavaScript embed. Customers include The Texas Tribune, Hearst Newspapers, the San Francisco Chronicle, Advance Local, Shaw Media and Auburn University. Everlit's only publicly reachable machine-readable surfaces are an oEmbed 1.0 resolver, a player-bootstrap JSON endpoint, and llms.txt / llms-full.txt; the REST API it markets for custom CMS integration
  is undocumented and access-gated through sales.
image: https://everlit.audio/site/images/preview.jpg
layout: provider
modified: '2026-08-20'
name: Everlit
nav: Providers
network: true
overview: 'Everlit publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, Video, Social, Podcasts, and Media.


  Everlit''s developer surface includes authentication, support, engineering blog, and 16 more developer resources.'
plans:
- name: Everlit Plans Pricing
  plan_count: 0
  slug: everlit-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Everlit Rate Limits
  slug: everlit-rate-limits
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.0
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/everlit/refs/heads/main/screenshots/everlit-2026-09-02T145428.png
security:
- kind: authentication
  name: Everlit Authentication
  slug: everlit-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Everlit Domain Security
  slug: everlit-domain-security
  summary_line: TLSv1.3
slug: everlit
tags:
- Audio
- Video
- Social
- Podcasts
- Media
- Publishers
- News
- Text-to-Speech
- AI-voice
- Content Distribution
- Monetization
- Accessibility
- oEmbed
- embeddable-player
- Advertising
---
