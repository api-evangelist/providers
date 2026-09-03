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
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Omdb Agentic Access
  operation_count: 3
  slug: omdb-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Dedicated image endpoint returning high-resolution movie and TV show poster art (up to 2000×3000 px) for over 280,000 titles, updated daily. Access is restricted to Patreon patrons.
  name: OMDb Poster API
  slug: omdb-poster-api
- baseURL: https://www.omdbapi.com/
  baseurl_source: declared
  description: The ID Parameter API from OMDb — 1 operation(s) for id parameter.
  name: OMDb ID Parameter API
  slug: omdb-id-parameter-api
- baseURL: https://www.omdbapi.com/
  baseurl_source: declared
  description: The Search Parameter API from OMDb — 1 operation(s) for search parameter.
  name: OMDb Search Parameter API
  slug: omdb-search-parameter-api
- baseURL: https://www.omdbapi.com/
  baseurl_source: declared
  description: The Title Parameter API from OMDb — 1 operation(s) for title parameter.
  name: OMDb Title Parameter API
  slug: omdb-title-parameter-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OMDb ID Parameter API
  slug: open-omdb-id-parameter-api
- collection_type: open
  name: OMDb ID Parameter Search Parameter API
  slug: open-omdb-search-parameter-api
- collection_type: open
  name: OMDb ID Parameter Title Parameter API
  slug: open-omdb-title-parameter-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/omdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/omdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/omdb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.omdbapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.omdbapi.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/omdbapi/OMDb-API
- group: commercial
  title: ''
  type: Pricing
  url: https://www.omdbapi.com/apikey.aspx
- group: commercial
  title: ''
  type: Plans
  url: plans/omdb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/omdb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/omdb-finops.yml
- group: start
  title: ''
  type: Signup
  url: https://www.omdbapi.com/apikey.aspx
- group: other
  title: ''
  type: Patreon
  url: https://www.patreon.com/omdb
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/omdb/refs/heads/main/vocabulary/omdb-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/omdb/refs/heads/main/json-ld/omdb-context.jsonld
created: '2026-06-12'
description: Open Movie Database REST API providing movie and TV show metadata, ratings, poster images, and episode data from a community-maintained database. Supports lookup by IMDb ID or title, full-text search, and a dedicated Poster API for high-resolution cover art available to patrons.
examples:
- key_count: 2
  name: Omdb Error Response
  slug: omdb-error-response
- key_count: 3
  name: Omdb Search Results
  slug: omdb-search-results
- key_count: 25
  name: Omdb Title By Id
  slug: omdb-title-by-id
finops:
- name: Omdb Finops
  service_category: ''
  slug: omdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/omdb.png
json_schemas:
- name: OMDb Search Result
  property_count: 4
  slug: omdb-search-result
- name: OMDb Title Result
  property_count: 26
  slug: omdb-title-result
jsonld:
- class_count: 3
  name: Omdb Context
  property_count: 30
  slug: omdb-context
layout: provider
modified: '2026-06-12'
name: OMDb
nav: Providers
network: true
overview: 'OMDb publishes 3 APIs on the [APIs.io](https://apis.io/) network: ID Parameter API, Search Parameter API, and Title Parameter API. Tagged areas include Movies, Television, Entertainment, Metadata, and Ratings.


  The OMDb catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OMDb''s developer surface includes authentication, documentation, GitHub presence, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Omdb Plans Pricing
  plan_count: 2
  slug: omdb-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Omdb Rate Limits
  slug: omdb-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OMDb API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: omdb-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 28.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 25.0
    contract_quality: 68.7
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 36.8
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/omdb/refs/heads/main/screenshots/omdb-2026-06-20T190703.png
security:
- kind: authentication
  name: Omdb Authentication
  slug: omdb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Omdb Domain Security
  slug: omdb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: omdb
tags:
- Movies
- Television
- Entertainment
- Metadata
- Ratings
- Posters
- IMDb
- Open Data
website: https://www.omdbapi.com/
---
