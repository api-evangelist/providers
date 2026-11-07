---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Soundcloud Agentic Access
  operation_count: 19
  slug: soundcloud-agentic-access
  summary_line: 19 operations · 12 acting
api_count: 1
apis:
- description: REST API for SoundCloud covering tracks (upload, metadata, stream), users (/me, profiles), playlists (CRUD), search (title/username/description), social (follow, like, comment), and audio playback. OA
  name: SoundCloud API
  slug: platform
- baseURL: https://api.soundcloud.com
  baseurl_source: declared
  description: Playlist CRUD
  name: SoundCloud Playlists API
  slug: soundcloud-playlists-api
- baseURL: https://api.soundcloud.com
  baseurl_source: declared
  description: Search and resolution
  name: SoundCloud Search API
  slug: soundcloud-search-api
- baseURL: https://api.soundcloud.com
  baseurl_source: declared
  description: Follow and like actions
  name: SoundCloud Social API
  slug: soundcloud-social-api
- baseURL: https://api.soundcloud.com
  baseurl_source: declared
  description: Track CRUD, streaming, and comments
  name: SoundCloud Tracks API
  slug: soundcloud-tracks-api
- baseURL: https://api.soundcloud.com
  baseurl_source: declared
  description: Authenticated user and profile actions
  name: SoundCloud Users API
  slug: soundcloud-users-api
artifact_total: 21
collections:
- collection_type: open
  name: SoundCloud Playlists API
  slug: open-soundcloud-playlists-api
- collection_type: open
  name: SoundCloud Playlists Search API
  slug: open-soundcloud-search-api
- collection_type: open
  name: SoundCloud Playlists Social API
  slug: open-soundcloud-social-api
- collection_type: open
  name: SoundCloud Playlists Tracks API
  slug: open-soundcloud-tracks-api
- collection_type: open
  name: SoundCloud Playlists Users API
  slug: open-soundcloud-users-api
- collection_type: open
  name: SoundCloud API
  slug: open-soundcloud
common:
- group: other
  href: https://artifacts.apis.io/soundcloud/capabilities/soundcloud-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/soundcloud-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/soundcloud/agentic-access/soundcloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/soundcloud-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/soundcloud/security/soundcloud-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/soundcloud-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/soundcloud/security/soundcloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/soundcloud-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/soundcloud/authentication/soundcloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/soundcloud-authentication.yml
- group: auth
  href: https://artifacts.apis.io/soundcloud/scopes/soundcloud-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/soundcloud-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soundcloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/soundcloud
- group: company
  title: ''
  type: Website
  url: https://soundcloud.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.soundcloud.com/
- group: commercial
  href: https://artifacts.apis.io/soundcloud/plans/soundcloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/soundcloud-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/soundcloud/rate-limits/soundcloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/soundcloud-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/soundcloud/finops/soundcloud-finops.yml
  title: ''
  type: FinOps
  url: finops/soundcloud-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://developers.soundcloud.com/blog/blog.rss
created: '2026-05-08'
description: SoundCloud is a music and audio streaming platform with a developer REST API for tracks, users, playlists, search, comments, likes, and uploads. Authentication is OAuth 2.1 with PKCE; access tokens expire approximately every hour.
finops:
- has_sources: true
  method: generated
  name: Soundcloud Finops
  primary_unit: ''
  service_category: Music Streaming
  slug: soundcloud-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soundcloud.png
layout: provider
modified: '2026-05-30'
name: SoundCloud
nav: Providers
network: true
overview: 'SoundCloud publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Playlists API, Search API, Social API, and 3 more. Tagged areas include Music, Streaming, Audio, OAuth, and Tracks.


  The SoundCloud catalog on APIs.io includes 1 Spectral governance ruleset.


  SoundCloud''s developer surface includes authentication, engineering blog, and 12 more developer resources.'
plans:
- name: Soundcloud Plans Pricing
  plan_count: 2
  slug: soundcloud-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Soundcloud Rate Limits
  slug: soundcloud-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: SoundCloud API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: soundcloud-rules
scopes:
- name: Soundcloud Scopes
  scope_count: 1
  slug: soundcloud-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 44.7
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/soundcloud/soundcloud-2026-06-20T194220.png
security:
- kind: authentication
  name: Soundcloud Authentication
  slug: soundcloud-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Soundcloud Domain Security
  slug: soundcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Soundcloud Vulnerability Disclosure
  slug: soundcloud-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: soundcloud
tags:
- Music
- Streaming
- Audio
- OAuth
- Tracks
- Playlists
- Authentication
website: https://soundcloud.com/
---
