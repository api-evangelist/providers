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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Giantbomb Agentic Access
  operation_count: 17
  slug: giantbomb-agentic-access
  summary_line: 17 operations
api_count: 1
apis:
- baseURL: https://www.giantbomb.com/api
  baseurl_source: declared
  description: Access to character data
  name: Giant Bomb Characters API
  slug: giantbomb-characters-api
- baseURL: https://www.giantbomb.com/api
  baseurl_source: declared
  description: Access to company data
  name: Giant Bomb Companies API
  slug: giantbomb-companies-api
- baseURL: https://www.giantbomb.com/api
  baseurl_source: declared
  description: Access to franchise data
  name: Giant Bomb Franchises API
  slug: giantbomb-franchises-api
- baseURL: https://www.giantbomb.com/api
  baseurl_source: declared
  description: Access to video game data
  name: Giant Bomb Games API
  slug: giantbomb-games-api
- baseURL: https://www.giantbomb.com/api
  baseurl_source: declared
  description: Access to platform data
  name: Giant Bomb Platforms API
  slug: giantbomb-platforms-api
- baseURL: https://www.giantbomb.com/api
  baseurl_source: declared
  description: Access to game release data
  name: Giant Bomb Releases API
  slug: giantbomb-releases-api
- baseURL: https://www.giantbomb.com/api
  baseurl_source: declared
  description: Access to game reviews
  name: Giant Bomb Reviews API
  slug: giantbomb-reviews-api
- baseURL: https://www.giantbomb.com/api
  baseurl_source: declared
  description: Search across all resources
  name: Giant Bomb Search API
  slug: giantbomb-search-api
- baseURL: https://www.giantbomb.com/api
  baseurl_source: declared
  description: Access to videos
  name: Giant Bomb Videos API
  slug: giantbomb-videos-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Giant Bomb Characters API
  slug: open-giantbomb-characters-api
- collection_type: open
  name: Giant Bomb Characters Companies API
  slug: open-giantbomb-companies-api
- collection_type: open
  name: Giant Bomb Characters Franchises API
  slug: open-giantbomb-franchises-api
- collection_type: open
  name: Giant Bomb Characters Games API
  slug: open-giantbomb-games-api
- collection_type: open
  name: Giant Bomb Characters Platforms API
  slug: open-giantbomb-platforms-api
- collection_type: open
  name: Giant Bomb Characters Releases API
  slug: open-giantbomb-releases-api
- collection_type: open
  name: Giant Bomb Characters Search API
  slug: open-giantbomb-search-api
- collection_type: open
  name: Giant Bomb Characters Videos API
  slug: open-giantbomb-videos-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/giantbomb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/giantbomb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/giantbomb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.giantbomb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.giantbomb.com/api/documentation/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/topics/giantbomb-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/giant-bomb/
- group: company
  title: ''
  type: Blog
  url: https://www.giantbomb.com/articles/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.giantbomb.com/api/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.giantbomb.com/
- group: other
  title: ''
  type: X
  url: https://x.com/giantbomb
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/giantbomb/refs/heads/main/plans/giantbomb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/giantbomb/refs/heads/main/rate-limits/giantbomb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/giantbomb/refs/heads/main/finops/giantbomb-finops.yml
created: '2026-06-13'
description: Giant Bomb is a video game database and media platform providing comprehensive data on over 100,000 games, characters, companies, concepts, franchises, locations, objects, and other game-related entities. The Giant Bomb API offers RESTful access to this rich dataset, enabling developers to query and integrate video game information into their applications using simple GET requests authenticated with a personal API key.
examples:
- key_count: 4
  name: Get Games
  slug: get-games
- key_count: 4
  name: Search
  slug: search
finops:
- name: Giantbomb Finops
  service_category: API
  slug: giantbomb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/giantbomb.png
json_schemas:
- name: ApiResponse
  property_count: 8
  slug: api-response
- name: Game
  property_count: 19
  slug: game
jsonld:
- class_count: 22
  name: Giantbomb Context
  property_count: 14
  slug: giantbomb-context
layout: provider
modified: '2026-06-13'
name: Giant Bomb
nav: Providers
network: true
overview: 'Giant Bomb publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Characters API, Companies API, Franchises API, and 6 more. Tagged areas include Entertainment, Video Games, Game Database, Gaming, and Media.


  The Giant Bomb catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Giant Bomb''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Giantbomb Plans Pricing
  plan_count: 1
  slug: giantbomb-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Giantbomb Rate Limits
  slug: giantbomb-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Giant Bomb API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: giantbomb-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 44.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 58.5
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 42.1
  previous_composite: 43.2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/giantbomb/refs/heads/main/screenshots/giantbomb-2026-08-17T080951.png
security:
- kind: authentication
  name: Giantbomb Authentication
  slug: giantbomb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Giantbomb Domain Security
  slug: giantbomb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: giantbomb
tags:
- Entertainment
- Video Games
- Game Database
- Gaming
- Media
website: https://www.giantbomb.com/
---
