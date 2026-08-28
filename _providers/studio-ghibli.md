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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Studio Ghibli Agentic Access
  operation_count: 10
  slug: studio-ghibli-agentic-access
  summary_line: 10 operations
api_count: 5
apis:
- description: Studio Ghibli theatrical films.
  name: Studio Ghibli Films API
  slug: studio-ghibli-films-api
- description: Settings and places that appear in Studio Ghibli films.
  name: Studio Ghibli Locations API
  slug: studio-ghibli-locations-api
- description: Characters that appear in Studio Ghibli films.
  name: Studio Ghibli People API
  slug: studio-ghibli-people-api
- description: Species classifications of characters appearing in Studio Ghibli films.
  name: Studio Ghibli Species API
  slug: studio-ghibli-species-api
- description: Vehicles featured in Studio Ghibli films.
  name: Studio Ghibli Vehicles API
  slug: studio-ghibli-vehicles-api
artifact_total: 54
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Studio Ghibli Films API
  slug: open-studio-ghibli-films-api
- collection_type: open
  name: Studio Ghibli Films Locations API
  slug: open-studio-ghibli-locations-api
- collection_type: open
  name: Studio Ghibli Films People API
  slug: open-studio-ghibli-people-api
- collection_type: open
  name: Studio Ghibli Films Species API
  slug: open-studio-ghibli-species-api
- collection_type: open
  name: Studio Ghibli Films Vehicles API
  slug: open-studio-ghibli-vehicles-api
- collection_type: open
  name: Studio Ghibli API
  slug: open-studio-ghibli
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/studio-ghibli-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/studio-ghibli-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ghibliapi.vercel.app
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/janaipakos/ghibliapi
- group: commercial
  title: MIT
  type: License
  url: https://github.com/janaipakos/ghibliapi/blob/master/LICENSE
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: JSONLD
  url: json-ld/studio-ghibli-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/studio-ghibli-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/studio-ghibli-vocabulary.yml
- group: build
  title: Elixir SDK (ghibli)
  type: SDKs
  url: https://github.com/sotojuan/ghibli
- group: build
  title: Go SDK (totoro)
  type: SDKs
  url: https://github.com/Rchristiani/totoro
- group: build
  title: GraphQL Wrapper (ghibliQL)
  type: SDKs
  url: https://github.com/kisscool-fr/ghibliql
- group: build
  title: R Client
  type: SDKs
  url: https://github.com/onertipaday/ghibliapi
- group: build
  title: Python SDK
  type: SDKs
  url: https://github.com/Incognito/python_studio_ghibli_api_sdk
- group: build
  title: Swift (iOS) Example
  type: CodeExamples
  url: https://github.com/kxvn-lx/Ghibliii
- group: build
  title: Android Example
  type: CodeExamples
  url: https://github.com/txemasv/ghibli-films
- group: build
  title: Haskell Example
  type: CodeExamples
  url: https://github.com/janaipakos/ghibliapi-example
- group: build
  title: JavaScript Example (ghibli-fans)
  type: CodeExamples
  url: https://github.com/mazipan/ghibli-fans
- group: build
  title: JavaScript Example (sandbox)
  type: CodeExamples
  url: https://github.com/taniarascia/sandbox/tree/master/ghibli
created: '2026-05-28'
description: 'Studio Ghibli API — a community-built, unofficial, fan-made, MIT-licensed REST API that catalogs the people, places, and things found in the worlds of Studio Ghibli. Five resource collections (films, people, locations, species, vehicles) cross-link via canonical URLs. No authentication, no metering, no paid tier. Source: github.com/janaipakos/ghibliapi (archived 2022-12-02); canonical instance now at ghibliapi.vercel.app.'
examples:
- key_count: 4
  name: Studio Ghibli Getfilm Example
  slug: studio-ghibli-getfilm-example
- key_count: 4
  name: Studio Ghibli Getlocation Example
  slug: studio-ghibli-getlocation-example
- key_count: 4
  name: Studio Ghibli Getperson Example
  slug: studio-ghibli-getperson-example
- key_count: 4
  name: Studio Ghibli Getspecies Example
  slug: studio-ghibli-getspecies-example
- key_count: 4
  name: Studio Ghibli Getvehicle Example
  slug: studio-ghibli-getvehicle-example
- key_count: 5
  name: Studio Ghibli Listfilms Example
  slug: studio-ghibli-listfilms-example
- key_count: 5
  name: Studio Ghibli Listlocations Example
  slug: studio-ghibli-listlocations-example
- key_count: 5
  name: Studio Ghibli Listpeople Example
  slug: studio-ghibli-listpeople-example
- key_count: 5
  name: Studio Ghibli Listspecies Example
  slug: studio-ghibli-listspecies-example
- key_count: 4
  name: Studio Ghibli Listvehicles Example
  slug: studio-ghibli-listvehicles-example
features:
- description: Films, people, locations, species, and vehicles — each addressable as a paginated collection and as a single resource by UUID.
  name: Five Resource Collections
- description: Resources cross-link to related resources using canonical URLs, so consumers can walk the graph without join logic.
  name: Graph Traversal Via URLs
- description: Optional `fields=` query parameter returns only the named fields, reducing payload size.
  name: Field Projection
- description: Optional `limit=` query parameter (default 50, max 250) bounds list responses.
  name: Pagination
- description: Fully anonymous public API; no API key, no OAuth, no token.
  name: No Authentication
- description: The backing JSON Server implementation is open source and can be forked and self-hosted.
  name: MIT-Licensed Source
graphqls:
- description: ''
  name: Studio Ghibli GraphQL API
  slug: studio-ghibli-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/studio-ghibli.png
integrations:
- description: The API is implemented on top of typicode/json-server (https://github.com/typicode/json-server).
  name: JSON Server
- description: The documentation site is rendered with Redocly's ReDoc (https://github.com/Rebilly/ReDoc).
  name: ReDoc
- description: Film poster and banner images are served from image.tmdb.org.
  name: TMDB Image CDN
json_schemas:
- name: Studio Ghibli Film
  property_count: 17
  slug: studio-ghibli-film
- name: Studio Ghibli Location
  property_count: 8
  slug: studio-ghibli-location
- name: Studio Ghibli Person
  property_count: 9
  slug: studio-ghibli-person
- name: Studio Ghibli Species
  property_count: 8
  slug: studio-ghibli-species
- name: Studio Ghibli Vehicle
  property_count: 8
  slug: studio-ghibli-vehicle
json_structures:
- name: Studio Ghibli Film Structure
  property_count: 0
  slug: studio-ghibli-film-structure
- name: Studio Ghibli Location Structure
  property_count: 0
  slug: studio-ghibli-location-structure
- name: Studio Ghibli Person Structure
  property_count: 0
  slug: studio-ghibli-person-structure
- name: Studio Ghibli Species Structure
  property_count: 0
  slug: studio-ghibli-species-structure
- name: Studio Ghibli Vehicle Structure
  property_count: 0
  slug: studio-ghibli-vehicle-structure
jsonld:
- class_count: 0
  name: Studio Ghibli Context
  property_count: 33
  slug: studio-ghibli-context
layout: provider
modified: '2026-05-29'
name: Studio Ghibli
nav: Providers
network: true
overview: 'Studio Ghibli publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Films API, Locations API, People API, and 2 more. Tagged areas include Anime, Studio Ghibli, Film, Characters, and Locations.


  The Studio Ghibli catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Studio Ghibli''s developer surface includes code examples and 18 more developer resources.'
plans:
- name: Studio Ghibli Plans Pricing
  plan_count: 1
  slug: studio-ghibli-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Studio Ghibli Rate Limits
  slug: studio-ghibli-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Studio Ghibli API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: studio-ghibli-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Studio Ghibli API Rules
  rule_count: 23
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 14
  slug: studio-ghibli-rules
score:
  band: thin
  composite: 33.8
  delta: 4.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 28.8
    contract_quality: 27.9
    developer_ergonomics: 38.1
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/studio-ghibli/refs/heads/main/screenshots/studio-ghibli-2026-06-20T194625.png
security:
- kind: domain-security
  name: Studio Ghibli Domain Security
  slug: studio-ghibli-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: studio-ghibli
solutions:
- description: Fork janaipakos/ghibliapi and deploy to Vercel, Render, Fly.io, or any Node host for guaranteed availability.
  name: Self-Hosted Fork
tags:
- Anime
- Studio Ghibli
- Film
- Characters
- Locations
- Species
- Vehicles
- Public APIs
- Open-Source
- Read Only
use_cases:
- description: A safe, stable, no-auth API frequently used in front-end tutorials, REST workshops, and language-SDK demonstrations.
  name: Tutorial / Workshop Target
- description: Builders of Studio Ghibli fan sites can hydrate film/character/location detail pages directly from the API.
  name: Fan Sites and Discovery Apps
- description: Used by projects like ghibliQL to demonstrate wrapping a REST API in a GraphQL layer.
  name: GraphQL Wrapping Demos
- description: A self-contained, read-only domain that makes a good fixture for MCP server demos, tool-use examples, and agent walkthroughs.
  name: LLM / Agent Tooling Examples
website: https://ghibliapi.vercel.app
---
