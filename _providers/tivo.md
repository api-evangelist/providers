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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tivo Agentic Access
  operation_count: 6
  slug: tivo-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- description: The TiVo Music Metadata API provides access to high-quality music information including artist details, album data, track information, and music imagery. Uses the same HTTP-based query structure and J
  name: TiVo Music Metadata API
  slug: tivo-music-metadata
- description: Search and retrieve entertainment content metadata
  name: Tivo Content API
  slug: tivo-content-api
- description: Look up content by known identifiers
  name: Tivo Lookup API
  slug: tivo-lookup-api
artifact_total: 17
collections:
- collection_type: open
  name: TiVo Video Metadata API
  slug: open-tivo-video-metadata
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tivo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tivo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tivo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tivo
- group: company
  title: ''
  type: Website
  url: https://business.tivo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://business.tivo.com/products-solutions/metadata/tv-movie-metadata-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.tivo.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/openapi/tivo-video-metadata-openapi.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/json-ld/tivo-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/vocabulary/tivo-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/rules/tivo-rules.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tivo
created: '2025-03-01'
description: TiVo provides a universe of high-quality entertainment imagery and information through its metadata APIs. The company offers Video Metadata API and Music Metadata API delivering TV, movie, and music content data for streaming platforms, smart TVs, IPTV systems, and entertainment applications.
examples:
- key_count: 2
  name: Tivo Lookup Content By Id Example
  slug: tivo-lookup-content-by-id-example
- key_count: 2
  name: Tivo Search Content Example
  slug: tivo-search-content-example
finops:
- name: Tivo Finops
  service_category: API
  slug: tivo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tivo.png
json_schemas:
- name: TiVo Content Item
  property_count: 13
  slug: tivo-content
json_structures:
- name: Tivo Content Structure
  property_count: 0
  slug: tivo-content-structure
jsonld:
- class_count: 37
  name: Tivo Context
  property_count: 4
  slug: tivo-context
layout: provider
modified: '2026-05-19'
name: Tivo
nav: Providers
network: true
overview: 'Tivo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Content API and Lookup API. Tagged areas include Entertainment, Metadata, Television, Movies, and Music.


  The Tivo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tivo''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Tivo Plans Pricing
  plan_count: 3
  slug: tivo-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 5
  name: Tivo Rate Limits
  slug: tivo-rate-limits
rules:
- name: Tivo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tivo-jsonschema-spectral-rules
- name: Tivo API Rules
  rule_count: 13
  severity_counts:
    error: 6
    hint: 2
    info: 0
    warn: 5
  slug: tivo-rules
score:
  band: developing
  composite: 51.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 74.4
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tivo/refs/heads/main/screenshots/tivo-2026-06-20T195418.png
security:
- kind: authentication
  name: Tivo Authentication
  slug: tivo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tivo Domain Security
  slug: tivo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tivo
tags:
- Entertainment
- Metadata
- Television
- Movies
- Music
- Streaming
website: https://business.tivo.com/
---
