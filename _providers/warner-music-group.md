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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Warner Music Group Agentic Access
  operation_count: 6
  slug: warner-music-group-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 4
apis:
- description: Artist information
  name: Warner Music Group Artists API
  slug: warner-music-group-artists-api
- description: Music catalog search and discovery
  name: Warner Music Group Catalog API
  slug: warner-music-group-catalog-api
- description: License request and management
  name: Warner Music Group Licenses API
  slug: warner-music-group-licenses-api
- description: Track and recording details
  name: Warner Music Group Tracks API
  slug: warner-music-group-tracks-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Warner Music Group Licensing Artists API
  slug: open-warner-music-group-artists-api
- collection_type: open
  name: Warner Music Group Licensing Artists Catalog API
  slug: open-warner-music-group-catalog-api
- collection_type: open
  name: Warner Music Group Licensing Artists Licenses API
  slug: open-warner-music-group-licenses-api
- collection_type: open
  name: Warner Music Group Licensing API
  slug: open-warner-music-group-licensing
- collection_type: open
  name: Warner Music Group Licensing Artists Tracks API
  slug: open-warner-music-group-tracks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/warner-music-group-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/warner-music-group-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/warner-music-group-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/warner-music-group-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/warner-music-group
- group: company
  title: ''
  type: Website
  url: https://www.wmg.com/
- group: start
  title: ''
  type: Portal
  url: https://www.wmgmusiclicensing.com/
- group: company
  title: ''
  type: Website
  url: https://warnerchappell.com/
- group: docs
  title: ''
  type: Documentation
  url: https://warnerchappell.com/music-licensing
- group: company
  title: ''
  type: Website
  url: https://www.warnerchappellpm.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.wmg.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wmg
- group: company
  title: ''
  type: Blog
  url: https://www.wmg.com/feed
created: '2026-03-24'
description: Warner Music Group is one of the major record labels in the music industry, with recorded music and music publishing operations spanning a roster of artists, songwriters, and labels around the world. WMG includes Warner Records, Atlantic Records, Elektra Records, and Warner Chappell Music (one of the world's largest music publishing companies). WMG provides music licensing APIs and developer tools for integrating licensed music into applications.
examples:
- key_count: 2
  name: Warner Music Group Searchcatalog Example
  slug: warner-music-group-searchCatalog-example
finops:
- name: Warner Music Group Finops
  service_category: API
  slug: warner-music-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/warner-music-group.png
json_schemas:
- name: Warner Music Group License
  property_count: 13
  slug: warner-music-group-license
json_structures:
- name: Warner Music Group License Structure
  property_count: 0
  slug: warner-music-group-license-structure
jsonld:
- class_count: 5
  name: Warner Music Group Context
  property_count: 15
  slug: warner-music-group-context
layout: provider
modified: '2026-05-19'
name: Warner Music Group
nav: Providers
network: true
overview: 'Warner Music Group publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Artists API, Catalog API, Licenses API, and 1 more. Tagged areas include Music, Entertainment, Streaming, Licensing, and Publishing.


  The Warner Music Group catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Warner Music Group''s developer surface includes authentication, developer portal, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Warner Music Group Plans Pricing
  plan_count: 3
  slug: warner-music-group-plans-pricing
press:
- date: '2026-05-25'
  title: WARNER MUSIC GROUP AND SUNO FORGE ...
  url: https://www.prnewswire.com/news-releases/warner-music-group-and-suno-forge-groundbreaking-partnership-302626017.html
- date: '2026-05-25'
  title: WARNER MUSIC PARTNERS WITH EDITH PIAF'S ...
  url: https://www.wmg.com/news/warner-music-partners-with-edith-piafs-estate-on-groundbreaking-ai-technology
- date: '2026-05-25'
  title: Spotify and Universal Music Group have agreed on a deal ...
  url: https://www.facebook.com/cnn/posts/spotify-and-universal-music-group-have-agreed-on-a-deal-that-will-allow-some-sub/1365341595458488/
- date: '2026-05-25'
  title: Sony Music Group, Universal Music ...
  url: https://newsroom.spotify.com/2025-10-16/artist-first-ai-music-spotify-collaboration/
- date: '2026-05-25'
  title: WARNER MUSIC GROUP AND SUNO FORGE ...
  url: https://www.wmg.com/news/warner-music-group-and-suno-forge-groundbreaking-partnership
random_paper: 20
rate_limits:
- limit_count: 5
  name: Warner Music Group Rate Limits
  slug: warner-music-group-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Warner Music Group API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: warner-music-group-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Warner Music Group API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 3
  slug: warner-music-group-rules
scopes:
- name: Warner Music Group Scopes
  scope_count: 3
  slug: warner-music-group-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 38.4
  delta: 1.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/warner-music-group/refs/heads/main/screenshots/warner-music-group-2026-06-20T201229.png
security:
- kind: authentication
  name: Warner Music Group Authentication
  slug: warner-music-group-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Warner Music Group Domain Security
  slug: warner-music-group-domain-security
  summary_line: TLSv1.3 · DMARC
slug: warner-music-group
tags:
- Music
- Entertainment
- Streaming
- Licensing
- Publishing
website: https://www.wmg.com/
---
