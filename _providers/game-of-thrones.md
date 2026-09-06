---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Game Of Thrones Agentic Access
  operation_count: 7
  slug: game-of-thrones-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://www.anapioficeandfire.com/api
  baseurl_source: declared
  description: Books from the A Song of Ice and Fire series
  name: An API of Ice and Fire books API
  slug: game-of-thrones-books-api
- baseURL: https://www.anapioficeandfire.com/api
  baseurl_source: declared
  description: Characters from A Song of Ice and Fire and Game of Thrones
  name: An API of Ice and Fire characters API
  slug: game-of-thrones-characters-api
- baseURL: https://www.anapioficeandfire.com/api
  baseurl_source: declared
  description: Noble houses from the A Song of Ice and Fire universe
  name: An API of Ice and Fire houses API
  slug: game-of-thrones-houses-api
- baseURL: https://anapioficeandfire.com/api
  baseurl_source: declared
  description: API entry-point listing the top-level resource URLs.
  name: An API of Ice And Fire Root API
  slug: an-api-of-ice-and-fire-root-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: AgenticAccess
  url: agentic-access/game-of-thrones-agentic-access.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/game-of-thrones-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/game-of-thrones-rate-limits.yml
- group: commercial
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
- name: Game Of Thrones Finops
  service_category: ''
  slug: game-of-thrones-finops
graphqls:
- description: ''
  name: An API of Ice And Fire GraphQL API
  slug: an-api-of-ice-and-fire-graphql
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
overview: 'An API of Ice and Fire publishes 4 APIs on the [APIs.io](https://apis.io/) network, including books API, characters API, houses API, and 1 more. Tagged areas include Game of Thrones, ASOIAF, A Song of Ice and Fire, Books, and Characters.


  The An API of Ice and Fire catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  An API of Ice and Fire''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Game Of Thrones Plans Pricing
  plan_count: 1
  slug: game-of-thrones-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Game Of Thrones Rate Limits
  slug: game-of-thrones-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: An API of Ice and Fire API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: game-of-thrones-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 70.3
    catalog_earned_first_party: 0.0
    catalog_gap: 44.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 49.3
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 25.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/game-of-thrones/refs/heads/main/screenshots/game-of-thrones-2026-06-20T181637.png
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
