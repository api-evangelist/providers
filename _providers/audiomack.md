---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Audiomack Agentic Access
  operation_count: 58
  slug: audiomack-agentic-access
  summary_line: 58 operations · 25 acting
api_count: 8
apis:
- description: Artist profiles, uploads, favorites, followers, and pinned items.
  name: Audiomack Artist API
  slug: audiomack-artist-api
- description: Aggregate song, album, and playlist charts across timeframes and genres.
  name: Audiomack Chart API
  slug: audiomack-chart-api
- description: Songs, albums, streaming, favorites, reposts, and metrics.
  name: Audiomack Music API
  slug: audiomack-music-api
- description: OAuth 1.0a request-token and access-token exchanges.
  name: Audiomack OAuth API
  slug: audiomack-oauth-api
- description: Playlist creation, editing, favoriting, and discovery.
  name: Audiomack Playlist API
  slug: audiomack-playlist-api
- description: Free-text search and autosuggest across music, albums, and artists.
  name: Audiomack Search API
  slug: audiomack-search-api
- description: Tokenised view and play event reporting.
  name: Audiomack Stats API
  slug: audiomack-stats-api
- description: Authenticated user profile, feed, uploads, playlists, and notifications.
  name: Audiomack User API
  slug: audiomack-user-api
artifact_total: 28
collections:
- collection_type: open
  name: Audiomack Data API
  slug: open-audiomack-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/audiomack-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/audiomack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/audiomack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/audiomack-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://audiomack.com
- group: start
  title: ''
  type: Portal
  url: https://creators.audiomack.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.audiomack.com/data-api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.audiomack.com/data-api/docs
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/audiomack/audiomack-api-examples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/audiomack
- group: operate
  title: ''
  type: Support
  url: https://audiomack.zendesk.com/
- group: operate
  title: ''
  type: Contact
  url: https://creators.audiomack.com/contact-us
- group: docs
  title: ''
  type: Documentation
  url: https://creators.audiomack.com/about/legal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://audiomack.com/about/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://audiomack.com/about/privacy-policy
- group: auth
  title: ''
  type: ResponsibleDisclosure
  url: https://creators.audiomack.com/responsible-disclosure
- group: docs
  title: ''
  type: Documentation
  url: https://guide.audiomack.com
- group: docs
  title: ''
  type: Documentation
  url: https://styleguide.audiomack.com
- group: other
  title: ''
  type: Product
  url: https://audiomack.studio
- group: start
  title: ''
  type: Signup
  url: https://audiomack.com/login
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/audiomack
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/audiomack
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/audiomack
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/audiomack
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/audiomack
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@audiomack
- group: other
  title: ''
  type: Twitch
  url: https://www.twitch.tv/audiomack
- group: other
  title: ''
  type: Apps
  url: https://apps.apple.com/us/app/audiomack-music-downloader/id669528610
- group: other
  title: ''
  type: Apps
  url: https://play.google.com/store/apps/details?id=com.audiomack
created: '2026-05-25'
description: Audiomack is an on-demand music streaming and audio discovery platform that lets artists and creators upload unlimited music and podcasts and reach listeners through its iOS, Android, and web apps. The service is widely associated with hip-hop, rap, R&B, Afrobeats, dancehall, reggae, electronic, and Latin genres, and is a launchpad for independent and emerging artists worldwide, with particularly strong adoption across Africa, the Caribbean, and the U.S. Audiomack publishes a public Data API at https://api.audiomack.com/v1 that exposes the catalog (songs, albums, playlists), artist profiles and follower graph, search and autosuggest, charts by genre and timeframe, streaming URL issuance, favorites and reposts, ad and view/play stats reporting, and authenticated user resources. Authentication is OAuth 1.0a (three-legged), with an optional unauthenticated `key` parameter for read-only access on some endpoints. Audiomack also publishes a Creators portal, an Artist Guide, Audiomack
  Studios, and the AMP monetization program for artist payouts.
features:
- On-demand music and podcast streaming on iOS, Android, and web
- Unlimited free uploads for artists and creators with no premium creator account
- Public Data API at https://api.audiomack.com/v1 with OAuth 1.0a authentication
- Catalog endpoints for songs, albums, artists, and playlists
- Charts by genre and timeframe (daily, weekly, monthly, yearly, total)
- Full-text search and autosuggest across music, albums, and artists
- Short-lived streaming URL issuance (~10 second TTL) via /music/{id}/play
- Favorites, reposts, follows, pinned items, and activity feeds
- View and play stats reporting via tokenised stats events
- Authenticated user resources: profile, feed, uploads, playlists, favorites, notifications
- AMP (Audiomack Monetization Program) for artist payouts
- Artist Dashboard with consumption analytics
- Hype Machine distribution compatibility
- Strong genre focus on hip-hop, rap, Afrobeats, reggae, dancehall, R&B, electronic, Latin
- React Native open-source components published under the audiomack GitHub org
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/audiomack.png
layout: provider
modified: '2026-05-25'
name: Audiomack
nav: Providers
network: true
overview: 'Audiomack publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Artist API, Chart API, Music API, and 5 more. Tagged areas include Music, Music Streaming, Audio, Podcasts, and Hip-Hop.


  Audiomack''s developer surface includes authentication, developer portal, documentation, getting-started guide, code examples, support, signup flow, and 22 more developer resources.'
random_paper: 51
score:
  band: thin
  composite: 34.4
  delta: -2.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 53.6
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/audiomack/refs/heads/main/screenshots/audiomack-2026-06-20T172548.png
security:
- kind: authentication
  name: Audiomack Authentication
  slug: audiomack-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Audiomack Domain Security
  slug: audiomack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Audiomack Vulnerability Disclosure
  slug: audiomack-vulnerability-disclosure
  summary_line: disclosure policy published
slug: audiomack
tags:
- Music
- Music Streaming
- Audio
- Podcasts
- Hip-Hop
- Rap
- Afrobeats
- Reggae
- Dancehall
- R&B
- Electronic
- Charts
- Playlists
- Discovery
- Creator Economy
- Independent Artists
website: https://audiomack.com
---
