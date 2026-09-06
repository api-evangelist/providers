---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 9
  human_in_the_loop: 2
  name: Soundstripe Agentic Access
  operation_count: 20
  slug: soundstripe-agentic-access
  summary_line: 20 operations · 9 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.soundstripe.com
  baseurl_source: declared
  description: Tagging and category metadata for songs and SFX.
  name: Soundstripe Categories API
  slug: soundstripe-categories-api
- baseURL: https://api.soundstripe.com
  baseurl_source: declared
  description: Soundstripe-curated playlists and their categories.
  name: Soundstripe Playlists API
  slug: soundstripe-playlists-api
- baseURL: https://api.soundstripe.com
  baseurl_source: declared
  description: User-scoped playlists for organizing songs and sound effects.
  name: Soundstripe Private Playlists API
  slug: soundstripe-private-playlists-api
- baseURL: https://api.soundstripe.com
  baseurl_source: declared
  description: Catalog song retrieval with artists and audio files.
  name: Soundstripe Songs API
  slug: soundstripe-songs-api
- baseURL: https://api.soundstripe.com
  baseurl_source: declared
  description: Sound-effect library and category browsing.
  name: Soundstripe Sound Effects API
  slug: soundstripe-sound-effects-api
- baseURL: https://api.soundstripe.com
  baseurl_source: declared
  description: Reference image and video uploads consumed by Supe Search.
  name: Soundstripe Supe Assets API
  slug: soundstripe-supe-assets-api
- baseURL: https://api.soundstripe.com
  baseurl_source: declared
  description: Asynchronous AI music supervisor for natural-language and image-based catalog matching.
  name: Soundstripe Supe Search API
  slug: soundstripe-supe-search-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Soundstripe Categories API
  slug: open-soundstripe-categories-api
- collection_type: open
  name: Soundstripe Categories Playlists API
  slug: open-soundstripe-playlists-api
- collection_type: open
  name: Soundstripe Categories Private Playlists API
  slug: open-soundstripe-private-playlists-api
- collection_type: open
  name: Soundstripe Categories Songs API
  slug: open-soundstripe-songs-api
- collection_type: open
  name: Soundstripe Categories Sound Effects API
  slug: open-soundstripe-sound-effects-api
- collection_type: open
  name: Soundstripe Categories Supe Assets API
  slug: open-soundstripe-supe-assets-api
- collection_type: open
  name: Soundstripe Categories Supe Search API
  slug: open-soundstripe-supe-search-api
- collection_type: open
  name: Soundstripe API
  slug: open-soundstripe
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/soundstripe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soundstripe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/soundstripe-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.soundstripe.com
- group: start
  title: ''
  type: Signup
  url: https://app.soundstripe.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.soundstripe.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.soundstripe.com/library/pricing
- group: other
  title: ''
  type: Music
  url: https://www.soundstripe.com/royalty-free-music
- group: other
  title: ''
  type: SoundEffects
  url: https://www.soundstripe.com/sfx
- group: learn
  title: ''
  type: Video
  url: https://www.soundstripe.com/stock-video
- group: other
  title: ''
  type: Business
  url: https://www.soundstripe.com/business
- group: other
  title: ''
  type: APILandingPage
  url: https://www.soundstripe.com/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.soundstripe.com
- group: other
  title: ''
  type: Licensing
  url: https://www.soundstripe.com/licensing
- group: company
  title: ''
  type: Blog
  url: https://www.soundstripe.com/blog
- group: operate
  title: ''
  type: Help
  url: https://help.soundstripe.com
- group: operate
  title: ''
  type: Contact
  url: https://www.soundstripe.com/contact-us
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/soundstripeinc
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/soundstripe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/soundstripe
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Soundstripe
- group: commercial
  title: ''
  type: Plans
  url: plans/soundstripe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/soundstripe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/soundstripe-finops.yml
created: '2026-05-25'
description: Soundstripe is a Nashville-based subscription platform that licenses royalty-free music, sound effects, and stock video to creators, agencies, podcasters, filmmakers, and enterprises. The catalog spans roughly 120,000 human-made tracks from Grammy-winning and independent artists, nearly 100,000 sound effects, and 100,000+ stock video clips (HD through 8K) — all pre-cleared under a single digital license that covers YouTube, Instagram, TikTok, podcasting, and commercial use, with stems and cut-downs available for many songs. Soundstripe also publishes a server-to-server REST API at api.soundstripe.com (JSON:API, token auth, 25 req/sec, signed webhooks) that exposes songs, sound effects, playlists, private playlists, and "Supe" — an AI music supervisor that matches catalog tracks to natural-language briefs, scene context, and reference imagery via asynchronous search and asset upload endpoints. Native integrations exist for Adobe Premiere Pro, Adobe Express, and Twitch; partner
  programs cover API embedding, music resale, and custom licensing for tool makers and platforms.
finops:
- name: Soundstripe Finops
  service_category: ''
  slug: soundstripe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soundstripe.png
layout: provider
modified: '2026-05-25'
name: Soundstripe
nav: Providers
network: true
overview: 'Soundstripe publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Playlists API, Private Playlists API, and 4 more. Tagged areas include Music, Sound Effects, Stock Video, Royalty-Free, and Licensing.


  Soundstripe''s developer surface includes authentication, signup flow, pricing, engineering blog, YouTube channel, and 19 more developer resources.'
plans:
- name: Soundstripe Plans Pricing
  plan_count: 7
  slug: soundstripe-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Soundstripe Rate Limits
  slug: soundstripe-rate-limits
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 0.0
    contract_quality: 55.3
    developer_ergonomics: 17.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soundstripe/refs/heads/main/screenshots/soundstripe-2026-06-20T194222.png
security:
- kind: authentication
  name: Soundstripe Authentication
  slug: soundstripe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Soundstripe Domain Security
  slug: soundstripe-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: soundstripe
tags:
- Music
- Sound Effects
- Stock Video
- Royalty-Free
- Licensing
- Subscription
- Creators
- Content Creation
- Video Production
- Podcasting
- AI Music Supervisor
- Stems
website: https://www.soundstripe.com
---
