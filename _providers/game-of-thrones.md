---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Game Of Thrones Agentic Access
  operation_count: 7
  slug: game-of-thrones-agentic-access
  summary_line: 7 operations
api_count: 2
apis:
- baseURL: https://www.anapioficeandfire.com/api
  baseurl_source: declared
  description: Books from the A Song of Ice and Fire series
  name: An API of Ice and Fire Books API
  slug: game-of-thrones-books-api
- baseURL: https://www.anapioficeandfire.com/api
  baseurl_source: declared
  description: Characters from A Song of Ice and Fire and Game of Thrones
  name: An API of Ice and Fire Characters API
  slug: game-of-thrones-characters-api
- baseURL: https://www.anapioficeandfire.com/api
  baseurl_source: declared
  description: Noble houses from the A Song of Ice and Fire universe
  name: An API of Ice and Fire Houses API
  slug: game-of-thrones-houses-api
artifact_total: 19
collections:
- collection_type: open
  name: An API of Ice and Fire books API
  slug: open-game-of-thrones-books-api
- collection_type: open
  name: An API of Ice and Fire books characters API
  slug: open-game-of-thrones-characters-api
- collection_type: open
  name: An API of Ice and Fire books houses API
  slug: open-game-of-thrones-houses-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/joakimskoog/AnApiOfIceAndFire/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/joakimskoog/AnApiOfIceAndFire/blob/master/CONTRIBUTING.md
- group: agent
  href: https://artifacts.apis.io/game-of-thrones/agentic-access/game-of-thrones-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/game-of-thrones-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/game-of-thrones/security/game-of-thrones-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/game-of-thrones-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anapioficeandfire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/joakimskoog/AnApiOfIceAndFire/wiki
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/joakimskoog
- group: commercial
  href: https://artifacts.apis.io/game-of-thrones/plans/game-of-thrones-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/game-of-thrones-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/game-of-thrones/rate-limits/game-of-thrones-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/game-of-thrones-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/game-of-thrones/finops/game-of-thrones-finops.yml
  title: ''
  type: FinOps
  url: finops/game-of-thrones-finops.yml
created: '2026-06-13'
description: An API of Ice and Fire is a free, open REST API providing comprehensive Game of Thrones and A Song of Ice and Fire data including books, characters, and houses from George R.R. Martin's universe. No authentication is required. The API offers structured, quantified data about the HBO series and book series covering all named characters, their allegiances, relationships, book appearances, TV season appearances, and details on every noble house and published book in the series.
examples:
- key_count: 11
  name: Book
  slug: book
- key_count: 16
  name: Character
  slug: character
- key_count: 16
  name: House
  slug: house
finops:
- has_sources: false
  method: generated
  name: Game Of Thrones Finops
  primary_unit: ''
  service_category: ''
  slug: game-of-thrones-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/game-of-thrones.png
json_schemas:
- name: Book
  property_count: 11
  slug: book
- name: Character
  property_count: 16
  slug: character
- name: House
  property_count: 16
  slug: house
jsonld:
- class_count: 21
  name: context Context
  property_count: 20
  slug: context
layout: provider
modified: '2026-06-13'
name: An API of Ice and Fire
nav: Providers
network: true
overview: 'An API of Ice and Fire publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Books API, Characters API, and Houses API. Tagged areas include Game of Thrones, ASOIAF, A Song of Ice and Fire, Books, and Characters.


  The An API of Ice and Fire catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  An API of Ice and Fire''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Game Of Thrones Plans Pricing
  plan_count: 1
  slug: game-of-thrones-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Game Of Thrones Rate Limits
  slug: game-of-thrones-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: An API of Ice and Fire — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: game-of-thrones-jsonschema-spectral-rules
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 55.3
    catalog_earned_first_party: 0.0
    catalog_gap: 59.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 9.8
    contract_quality: 57.0
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 25.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/game-of-thrones/game-of-thrones-2026-06-20T181637.png
security:
- kind: domain-security
  name: Game Of Thrones Domain Security
  slug: game-of-thrones-domain-security
  summary_line: TLSv1.3 · HSTS
slug: game-of-thrones
tags:
- Game of Thrones
- ASOIAF
- A Song of Ice and Fire
- Books
- Characters
- Houses
- Fantasy
- Entertainment
- OpenAPI
- Free API
website: https://anapioficeandfire.com/
---
