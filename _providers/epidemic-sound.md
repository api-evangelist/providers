---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Epidemic Sound Agentic Access
  operation_count: 47
  slug: epidemic-sound-agentic-access
  summary_line: 47 operations · 14 acting
api_count: 1
apis:
- baseURL: https://partner-content-api.epidemicsound.com
  baseurl_source: declared
  description: These endpoints allows your application to upload assets such as images or audio.
  name: Epidemic Sound Assets API
  slug: epidemic-sound-assets-api
- baseURL: https://partner-content-api.epidemicsound.com
  baseurl_source: declared
  description: Endpoints for user authentication.
  name: Epidemic Sound Authentication API
  slug: epidemic-sound-authentication-api
- baseURL: https://partner-content-api.epidemicsound.com
  baseurl_source: declared
  description: These endpoints are in beta.
  name: Epidemic Sound Beta API
  slug: epidemic-sound-beta-api
- baseURL: https://partner-content-api.epidemicsound.com
  baseurl_source: declared
  description: These endpoints will allow you to explore the Epidemic Sound library. You can display tracks grouped in curated playlists, moods or genres or use search to get tracks by any term.
  name: Epidemic Sound Browse & search API
  slug: epidemic-sound-browse-search-api
- baseURL: https://partner-content-api.epidemicsound.com
  baseurl_source: declared
  description: These endpoints will allow you to report how tracks are used in your application.
  name: Epidemic Sound Reporting API
  slug: epidemic-sound-reporting-api
- baseURL: https://partner-content-api.epidemicsound.com
  baseurl_source: declared
  description: Endpoints for managing safelisting licenses. Allows partners to create, list, update, and delete licenses for channels and videos on behalf of their end users.
  name: Epidemic Sound Safelisting API
  slug: epidemic-sound-safelisting-api
- baseURL: https://partner-content-api.epidemicsound.com
  baseurl_source: declared
  description: Endpoints to get sound effect specific information. These endpoints allow you to build a UI to browse and search for sound effects.
  name: Epidemic Sound Sound effects API
  slug: epidemic-sound-sound-effects-api
- baseURL: https://partner-content-api.epidemicsound.com
  baseurl_source: declared
  description: Endpoints to get track specific information.
  name: Epidemic Sound Tracks API
  slug: epidemic-sound-tracks-api
- baseURL: https://partner-content-api.epidemicsound.com
  baseurl_source: declared
  description: These endpoints allows your application to get user specific information such as liked sounds.
  name: Epidemic Sound Users API
  slug: epidemic-sound-users-api
artifact_total: 48
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Partner Content Assets API
  slug: open-epidemic-sound-assets-api
- collection_type: open
  name: Partner Content Assets Authentication API
  slug: open-epidemic-sound-authentication-api
- collection_type: open
  name: Partner Content Assets Beta API
  slug: open-epidemic-sound-beta-api
- collection_type: open
  name: Partner Content Assets Browse & search API
  slug: open-epidemic-sound-browse-search-api
- collection_type: open
  name: Partner Content API
  slug: open-epidemic-sound-partner-content-api
- collection_type: open
  name: Partner Content Assets Reporting API
  slug: open-epidemic-sound-reporting-api
- collection_type: open
  name: Partner Content Assets Safelisting API
  slug: open-epidemic-sound-safelisting-api
- collection_type: open
  name: Partner Content Assets Sound effects API
  slug: open-epidemic-sound-sound-effects-api
- collection_type: open
  name: Partner Content Assets Tracks API
  slug: open-epidemic-sound-tracks-api
- collection_type: open
  name: Partner Content Assets Users API
  slug: open-epidemic-sound-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/epidemic-sound-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epidemic-sound-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/epidemic-sound-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/epidemic-sound-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.epidemicsound.com
- group: start
  title: ''
  type: Portal
  url: https://www.epidemicsound.com/business/developers/
- group: start
  title: ''
  type: Portal
  url: https://developers.epidemicsound.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.epidemicsound.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.epidemicsound.com/docs/api-reference/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.epidemicsound.com/docs/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.epidemicsound.com/docs/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.epidemicsound.com/docs/authentication
- group: docs
  title: ''
  type: SwaggerUI
  url: https://partner-content-api.epidemicsound.com/swagger
- group: docs
  title: ''
  type: OpenAPI
  url: https://partner-content-api.epidemicsound.com/docs/spec.json
- group: docs
  title: ''
  type: Documentation
  url: https://developers.epidemicsound.com/docs/mcp/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.epidemicsound.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/epidemic-sound-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/epidemic-sound-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/epidemic-sound-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.epidemicsound.com/blog/
- group: company
  title: ''
  type: Blog
  url: https://www.epidemicsound.com/blog/epidemic-sound-api/
- group: company
  title: ''
  type: Careers
  url: https://www.epidemicsound.com/careers/
- group: company
  title: ''
  type: About
  url: https://www.epidemicsound.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://www.epidemicsound.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.epidemicsound.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.epidemicsound.com/privacy-notice/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/epidemicsound
- group: build
  title: ''
  type: SDKs
  url: https://github.com/epidemicsound/partner-content-api-demo-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/epidemicsound/homebrew-epidemicsound
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/epidemic-sound
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/epidemicsound
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@EpidemicSound
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/epidemicsound/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/epidemicsound
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@epidemicsound
- group: other
  title: ''
  type: Apps
  url: https://www.epidemicsound.com/apps/
- group: company
  title: ''
  type: Partners
  url: https://www.epidemicsound.com/business/partners/
created: '2026-05-25'
description: Epidemic Sound is a Stockholm-based royalty-free music and sound effects licensing platform for video creators, businesses, and platforms. The catalog includes 55,000+ tracks across 390 genres, 250,000+ sound effects, stems and instrumental versions, all under an all-inclusive license that covers mechanical, sync, and public performance rights globally. The Partner Content API ("Epidemic Sound Connect") exposes the full catalog and Epidemic Sound's AI-powered soundtracking tools — Soundmatch (video-to-music recommendation), semantic search, similar-track and similar-section lookup, image-based matching, beat detection, HLS streaming previews, AI voiceover generation, and the new track-versions endpoint that adapts a recording to a target duration while preserving musical structure. An official Model Context Protocol (MCP) server (beta) makes the same catalog and tools available to AI agents at https://www.epidemicsound.com/a/mcp-service/mcp. Access to the Partner API is gated
  behind a partnership agreement; once signed, partner engineers receive credentials via the Developer Portal and authenticate using API Key, Partner Token, or Epidemic Sound Connect (OAuth 2.0).
features:
- 55,000+ royalty-free music tracks across 390 genres
- 250,000+ sound effects across categorized collections
- Stems and instrumental versions included with every track
- All-inclusive licensing covering mechanical, sync, and public performance rights worldwide
- Semantic search by natural-language description
- Soundmatch — video-frame analysis returning mood-matched track recommendations
- Similar-track and similar-section discovery for seamless audio replacement
- Image-based track matching (`/v0/tracks/matching-image/{imageId}`)
- Beat detection for video-sync workflows (`/v0/tracks/{trackId}/beats`)
- HLS streaming previews with cookie-authenticated playback
- Track-versions generation (beta) — adapt a track to a target duration while preserving structure
- AI voiceover generation via the MCP server (browse artists, generate, status, download)
- Partner audio and image uploads for similarity / matching workflows
- Safelisting licenses for end-user YouTube/social channels
- Usage and analytics reporting endpoints for partner billing reconciliation
- Three authentication modes — ApiKey, Partner Token, Epidemic Sound Connect (OAuth 2.0)
- Official Model Context Protocol (MCP) server (Beta) at https://www.epidemicsound.com/a/mcp-service/mcp
- Audio delivered via Fastly's global CDN; API hosted in Europe
- Versioned API surface with `/v0/` path prefix
- 30-day-rotation API keys for programmatic MCP access
- Partnership-gated access; credentials provisioned via the Developer Portal
finops:
- name: Epidemic Sound Finops
  service_category: Media and Content Licensing
  slug: epidemic-sound-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/epidemic-sound.png
layout: provider
modified: '2026-05-25'
name: Epidemic Sound
nav: Providers
network: true
overview: 'Epidemic Sound publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Authentication API, Beta API, and 6 more. Tagged areas include Music, Sound Effects, Royalty-Free Music, Audio, and Audio Licensing.


  Epidemic Sound''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, YouTube channel, and 30 more developer resources.'
plans:
- name: Epidemic Sound Plans Pricing
  plan_count: 5
  slug: epidemic-sound-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Epidemic Sound Rate Limits
  slug: epidemic-sound-rate-limits
scopes:
- name: Epidemic Sound Scopes
  scope_count: 0
  slug: epidemic-sound-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 11
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 56.4
    developer_ergonomics: 52.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epidemic-sound/refs/heads/main/screenshots/epidemic-sound-2026-06-20T180755.png
security:
- kind: authentication
  name: Epidemic Sound Authentication
  slug: epidemic-sound-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Epidemic Sound Domain Security
  slug: epidemic-sound-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: epidemic-sound
tags:
- Music
- Sound Effects
- Royalty-Free Music
- Audio
- Audio Licensing
- Soundtracking
- Sync Licensing
- Creators
- Video
- AI Voiceover
- Semantic Search
- MCP
website: https://www.epidemicsound.com
---
