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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tivo Agentic Access
  operation_count: 6
  slug: tivo-agentic-access
  summary_line: 6 operations
api_count: 1
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TiVo Video Metadata Content API
  slug: open-tivo-content-api
- collection_type: open
  name: TiVo Video Metadata Content Lookup API
  slug: open-tivo-lookup-api
- collection_type: open
  name: TiVo Video Metadata API
  slug: open-tivo-video-metadata
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tivo-capability-edges.yml
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


  Tivo''s developer surface includes authentication, documentation, and 11 more developer resources.'
plans:
- name: Tivo Plans Pricing
  plan_count: 3
  slug: tivo-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Tivo Rate Limits
  slug: tivo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tivo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tivo-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Tivo API Rules
  rule_count: 13
  severity_counts:
    error: 6
    hint: 2
    info: 0
    warn: 5
  slug: tivo-rules
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
