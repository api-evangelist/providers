---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Disney Agentic Access
  operation_count: 4
  slug: disney-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: 'GraphQL Disney character API hosted at /graphql. Single root field `characters(page, pageSize, filter)` returns a `CharacterPage` with `items` and `paginationInfo`. The `CharacterFilterInput` accepts '
  name: Disney API (GraphQL)
  slug: disney-api-graphql
- description: Endpoints that list, retrieve, and filter Disney characters.
  name: Disney API Characters API
  slug: disney-characters-api
- description: Service discovery endpoint that enumerates available REST routes.
  name: Disney API Index API
  slug: disney-index-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Disney Characters API
  slug: open-disney-characters-api
- collection_type: open
  name: Disney Characters Index API
  slug: open-disney-index-api
- collection_type: open
  name: Disney API
  slug: open-disney
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ManuCastrillonM/disney-api/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/ManuCastrillonM/disney-api/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/ManuCastrillonM/disney-api/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/disney-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/disney-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://disneyapi.dev
- group: docs
  title: ''
  type: Documentation
  url: https://disneyapi.dev/docs/
- group: build
  title: Disney API (RESTful and GraphQL server)
  type: SourceCode
  url: https://github.com/ManuCastrillonM/disney-api
- group: build
  title: disneyapi.dev documentation site (Gatsby)
  type: SourceCode
  url: https://github.com/ManuCastrillonM/disneyapi.dev
- group: commercial
  title: BSD-3-Clause
  type: License
  url: https://github.com/ManuCastrillonM/disney-api/blob/main/LICENSE
- group: operate
  title: ''
  type: StatusPage
  url: https://status.disneyapi.dev/
- group: start
  title: Support Us (donations to underwrite hosting)
  type: Signup
  url: https://disneyapi.dev/support-us/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ManuCastrillonM/disney-api
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ManuCastrillonM/disneyapi.dev
- group: design
  title: ''
  type: SpectralRules
  url: rules/disney-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/disney-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/disney-context.jsonld
- group: docs
  title: Character
  type: JSONSchema
  url: json-schema/disney-character-schema.json
- group: docs
  title: CharacterPage
  type: JSONSchema
  url: json-schema/disney-character-page-schema.json
- group: docs
  title: PageInfo
  type: JSONSchema
  url: json-schema/disney-page-info-schema.json
- group: docs
  title: ServiceIndex
  type: JSONSchema
  url: json-schema/disney-service-index-schema.json
- group: design
  title: Character
  type: JSONStructure
  url: json-structure/disney-character-structure.json
- group: design
  title: CharacterPage
  type: JSONStructure
  url: json-structure/disney-character-page-structure.json
- group: design
  title: PageInfo
  type: JSONStructure
  url: json-structure/disney-page-info-structure.json
- group: design
  title: ServiceIndex
  type: JSONStructure
  url: json-structure/disney-service-index-structure.json
- group: build
  title: Character Example
  type: Examples
  url: examples/disney-character-example.json
- group: build
  title: CharacterPage Example
  type: Examples
  url: examples/disney-character-page-example.json
- group: build
  title: ServiceIndex Example
  type: Examples
  url: examples/disney-service-index-example.json
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/disney-rate-limits.yml
created: '2026-05-29'
description: Community-maintained RESTful and GraphQL API exposing a database of 9,820+ Disney characters and the films, short films, TV shows, video games, and park attractions they appear in. The project (BSD-3-Clause) is developed in the open by Manu Castrillon at https://github.com/ManuCastrillonM/disney-api and documented at https://disneyapi.dev. The REST surface is unauthenticated and read-only. Disney and Disney characters are trademarks of The Walt Disney Company; this project is community fan-content and is not affiliated with or endorsed by Disney.
examples:
- key_count: 11
  name: Disney Character Example
  slug: disney-character-example
- key_count: 2
  name: Disney Character Page Example
  slug: disney-character-page-example
- key_count: 3
  name: Disney Service Index Example
  slug: disney-service-index-example
graphqls:
- description: 'GraphQL Disney character API hosted at /graphql. Single root field `characters(page, pageSize, filter)` returns a `CharacterPage` with `items` and `paginationInfo`. The `CharacterFilterInput` accepts '
  name: Disney API GraphQL API
  slug: disney-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/disney.png
json_schemas:
- name: CharacterPage
  property_count: 2
  slug: disney-character-page
- name: Character
  property_count: 13
  slug: disney-character
- name: PageInfo
  property_count: 4
  slug: disney-page-info
- name: ServiceIndex
  property_count: 3
  slug: disney-service-index
json_structures:
- name: Disney Character Page Structure
  property_count: 2
  slug: disney-character-page-structure
- name: Disney Character Structure
  property_count: 13
  slug: disney-character-structure
- name: Disney Page Info Structure
  property_count: 4
  slug: disney-page-info-structure
- name: Disney Service Index Structure
  property_count: 3
  slug: disney-service-index-structure
jsonld:
- class_count: 9
  name: Disney Context
  property_count: 15
  slug: disney-context
layout: provider
modified: '2026-05-29'
name: Disney API
nav: Providers
network: true
overview: 'Disney API publishes 2 APIs on the [APIs.io](https://apis.io/) network: Characters API and Index API. Tagged areas include Entertainment, Characters, Disney, Open Source, and Fan API.


  The Disney API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Disney API''s developer surface includes documentation, signup flow, code examples, and 26 more developer resources.'
random_paper: 56
rate_limits:
- limit_count: 3
  name: Disney Rate Limits
  slug: disney-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Disney API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: disney-jsonschema-spectral-rules
- effective_rule_count: 82
  extends:
  - spectral:oas
  name: Disney API API Rules
  rule_count: 41
  severity_counts:
    error: 12
    hint: 0
    info: 9
    warn: 20
  slug: disney-rules
score:
  band: emerging
  composite: 25.1
  delta: -7.4
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 25.0
    contract_quality: 21.1
    developer_ergonomics: 9.5
    discoverability: 81.5
    governance: 25.0
    operational_transparency: 31.6
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/disney/refs/heads/main/screenshots/disney-2026-06-20T180046.png
security:
- kind: domain-security
  name: Disney Domain Security
  slug: disney-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: disney
tags:
- Entertainment
- Characters
- Disney
- Open Source
- Fan API
- REST
- GraphQL
website: https://disneyapi.dev
---
