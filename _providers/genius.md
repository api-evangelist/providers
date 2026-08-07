---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Genius Agentic Access
  operation_count: 30
  slug: genius-agentic-access
  summary_line: 30 operations · 5 acting
api_count: 9
apis:
- description: Authenticated user account.
  name: Genius Account API
  slug: genius-account-api
- description: Album metadata, tracks, cover art, and leaderboards.
  name: Genius Albums API
  slug: genius-albums-api
- description: Community annotations attached to lyric fragments.
  name: Genius Annotations API
  slug: genius-annotations-api
- description: Artist profiles, discography, followers, and leaderboards.
  name: Genius Artists API
  slug: genius-artists-api
- description: Lyric fragments (referents) and their attached annotations.
  name: Genius Referents API
  slug: genius-referents-api
- description: Full-text search across the Genius corpus.
  name: Genius Search API
  slug: genius-search-api
- description: Song metadata, contributors, and activity.
  name: Genius Songs API
  slug: genius-songs-api
- description: Genius user profiles and contributions.
  name: Genius Users API
  slug: genius-users-api
- description: Web page lookup for the annotation network.
  name: Genius Web Pages API
  slug: genius-web-pages-api
artifact_total: 35
collections:
- collection_type: open
  name: Genius API
  slug: open-genius
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/genius-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genius-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/genius-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/genius-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://genius.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.genius.com/
- group: build
  title: ''
  type: APIClientRegistration
  url: https://genius.com/api-clients
- group: commercial
  title: ''
  type: TermsOfService
  url: https://genius.com/static/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Genius
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/genius-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/genius-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/genius-vocabulary.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: MCP Server (jchoi2x/genius-mcp)
  type: Tools
  url: https://github.com/jchoi2x/genius-mcp
- group: build
  title: MCP Server (federicogarciav/genius-mcp)
  type: Tools
  url: https://github.com/federicogarciav/genius-mcp
- group: build
  title: MCP Server (Sergiolm17/genius-mcp-server)
  type: Tools
  url: https://mcp.so/server/genius-mcp-server/Sergiolm17
- group: build
  title: omniauth-genius (OAuth strategy)
  type: Tools
  url: https://github.com/Genius/omniauth-genius
created: '2026-05-28'
description: Crowdsourced music knowledge — the Genius/Rap Genius platform. The Genius API exposes structured metadata for songs, artists, albums, annotations, referents, and contributors. Raw lyric text is not served by the API; consumers receive the public song page URL and scrape lyrics from there.
examples:
- key_count: 2
  name: Genius Get Annotation Example
  slug: genius-get-annotation-example
- key_count: 2
  name: Genius Get Artist Example
  slug: genius-get-artist-example
- key_count: 2
  name: Genius Get Referents Example
  slug: genius-get-referents-example
- key_count: 2
  name: Genius Get Song Example
  slug: genius-get-song-example
- key_count: 2
  name: Genius List Artist Songs Example
  slug: genius-list-artist-songs-example
- key_count: 2
  name: Genius Lookup Web Page Example
  slug: genius-lookup-web-page-example
- key_count: 2
  name: Genius Search Example
  slug: genius-search-example
image: https://assets.genius.com/images/apple-touch-icon.png
json_schemas:
- name: GeniusAlbum
  property_count: 9
  slug: genius-album
- name: GeniusAnnotation
  property_count: 16
  slug: genius-annotation
- name: GeniusArtist
  property_count: 15
  slug: genius-artist
- name: GeniusReferent
  property_count: 14
  slug: genius-referent
- name: GeniusSong
  property_count: 25
  slug: genius-song
- name: GeniusUser
  property_count: 11
  slug: genius-user
- name: GeniusWebPage
  property_count: 9
  slug: genius-web-page
json_structures:
- name: Genius Annotation Structure
  property_count: 0
  slug: genius-annotation-structure
- name: Genius Song Structure
  property_count: 0
  slug: genius-song-structure
jsonld:
- class_count: 0
  name: Genius Context
  property_count: 35
  slug: genius-context
layout: provider
modified: '2026-05-29'
name: Genius
nav: Providers
network: true
overview: 'Genius publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Albums API, Annotations API, and 6 more. Tagged areas include Music, Lyrics, Annotations, Crowdsourced, and Reference Data.


  The Genius catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Genius'' developer surface includes authentication, tooling, and 15 more developer resources.'
plans:
- name: Genius Plans Pricing
  plan_count: 1
  slug: genius-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 0
  name: Genius Rate Limits
  slug: genius-rate-limits
rules:
- name: Genius API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: genius-jsonschema-spectral-rules
- name: Genius API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 4
  slug: genius-rules
scopes:
- name: Genius Scopes
  scope_count: 4
  slug: genius-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 34.7
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 29.6
    developer_ergonomics: 19.6
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Genius Authentication
  slug: genius-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Genius Domain Security
  slug: genius-domain-security
  summary_line: TLSv1.2 · DMARC
slug: genius
tags:
- Music
- Lyrics
- Annotations
- Crowdsourced
- Reference Data
- Public APIs
website: https://genius.com/
---
