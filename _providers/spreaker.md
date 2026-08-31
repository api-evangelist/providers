---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Spreaker Agentic Access
  operation_count: 61
  slug: spreaker-agentic-access
  summary_line: 61 operations · 28 acting
api_count: 1
apis:
- description: Advertisers, campaigns, and line items for direct ad sales.
  name: Spreaker Advertising API
  slug: spreaker-advertising-api
- description: Episodes, uploads, playback, likes, bookmarks, messages, chapters, cuepoints.
  name: Spreaker Episodes API
  slug: spreaker-episodes-api
- description: Search, explore categories, tags, and oEmbed.
  name: Spreaker Search and Discovery API
  slug: spreaker-search-and-discovery-api
- description: Podcast shows, favorites, and reference data.
  name: Spreaker Shows API
  slug: spreaker-shows-api
- description: Playback and engagement analytics at user, show, and episode level.
  name: Spreaker Statistics API
  slug: spreaker-statistics-api
- description: User profiles and social graph (followers, followings, blocks).
  name: Spreaker Users API
  slug: spreaker-users-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spreaker Advertising API
  slug: open-spreaker-advertising-api
- collection_type: open
  name: Spreaker Advertising Episodes API
  slug: open-spreaker-episodes-api
- collection_type: open
  name: Spreaker Advertising Search and Discovery API
  slug: open-spreaker-search-and-discovery-api
- collection_type: open
  name: Spreaker Advertising Shows API
  slug: open-spreaker-shows-api
- collection_type: open
  name: Spreaker Advertising Statistics API
  slug: open-spreaker-statistics-api
- collection_type: open
  name: Spreaker Advertising Users API
  slug: open-spreaker-users-api
- collection_type: open
  name: Spreaker API
  slug: open-spreaker
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/spreaker-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spreaker-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spreaker-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spreaker-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spreaker-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spreaker-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spreaker
- group: company
  title: ''
  type: Website
  url: https://www.spreaker.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.spreaker.com/guides/
- group: commercial
  title: ''
  type: Plans
  url: plans/spreaker-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spreaker-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spreaker-finops.yml
created: '2026-07-05'
description: Spreaker is a podcast hosting, distribution, and monetization platform owned by iHeartMedia (acquired via parent company Voxnest in 2020). It lets creators record, host, and publish podcasts, auto-distribute to Apple Podcasts, Spotify, and iHeartRadio, and monetize through programmatic ads, listener subscriptions, and a Supporters Club. Spreaker exposes a documented public REST API (v2) over HTTPS at api.spreaker.com, authenticated with OAuth2, covering users, shows, episodes, playback and messaging, analytics/statistics, search and discovery, and advertising campaign management.
finops:
- name: Spreaker Finops
  service_category: Media and Podcasting
  slug: spreaker-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spreaker.png
layout: provider
modified: '2026-07-05'
name: Spreaker
nav: Providers
network: true
overview: 'Spreaker publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Advertising API, Episodes API, Search and Discovery API, and 3 more. Tagged areas include Podcasting, Podcast Hosting, Audio, Media, and Monetization.


  Spreaker''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Spreaker Plans Pricing
  plan_count: 4
  slug: spreaker-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Spreaker Rate Limits
  slug: spreaker-rate-limits
scopes:
- name: Spreaker Scopes
  scope_count: 1
  slug: spreaker-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.6
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Spreaker Authentication
  slug: spreaker-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Spreaker Domain Security
  slug: spreaker-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Spreaker Vulnerability Disclosure
  slug: spreaker-vulnerability-disclosure
  summary_line: disclosure policy published
slug: spreaker
tags:
- Podcasting
- Podcast Hosting
- Audio
- Media
- Monetization
- Analytics
website: https://www.spreaker.com
---
