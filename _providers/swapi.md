---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Swapi Agentic Access
  operation_count: 12
  slug: swapi-agentic-access
  summary_line: 12 operations
api_count: 7
apis:
- description: 'The Node/MongoDB community rebuild of SWAPI, maintained by @semperry at swapi.tech. Wraps the canonical SWAPI payloads inside `result.properties` envelopes and adds Discord/Reddit community surfaces. '
  name: SWAPI REST API (swapi.tech)
  slug: swapi-rest-api-swapitech
- description: The Star Wars films (theatrical episodes I-VII supported by the canonical dataset).
  name: SWAPI - Star Wars API Films API
  slug: swapi-films-api
- description: Characters from the Star Wars universe (Luke Skywalker, Darth Vader, etc.).
  name: SWAPI - Star Wars API People API
  slug: swapi-people-api
- description: Planets featured across the Star Wars films.
  name: SWAPI - Star Wars API Planets API
  slug: swapi-planets-api
- description: Sentient and non-sentient species of the Star Wars universe.
  name: SWAPI - Star Wars API Species API
  slug: swapi-species-api
- description: Hyperdrive-capable starships (X-wings, Star Destroyers, Death Stars).
  name: SWAPI - Star Wars API Starships API
  slug: swapi-starships-api
- description: Non-hyperdrive vehicles (AT-ATs, snowspeeders, sand crawlers).
  name: SWAPI - Star Wars API Vehicles API
  slug: swapi-vehicles-api
artifact_total: 36
collections:
- collection_type: open
  name: SWAPI - Star Wars API
  slug: open-swapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://swapi.dev/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Juriy/swapi
- group: commercial
  title: ''
  type: License
  url: https://github.com/Juriy/swapi/blob/master/LICENSE
- group: build
  title: MCP Server (johnpapa)
  type: Tools
  url: https://github.com/johnpapa/mcp-starwars
- group: build
  title: MCP Server (olaekdahl)
  type: Tools
  url: https://github.com/olaekdahl/swapi-mcp-server
- group: build
  title: MCP Server (glaucia86)
  type: Tools
  url: https://github.com/glaucia86/swapi-mcp-server-app
- group: build
  title: MCP Server (Qwizi)
  type: Tools
  url: https://github.com/Qwizi/swapi-mcp
- group: build
  title: Android SDK (Oleur)
  type: SDKs
  url: https://github.com/Oleur/SWAPI-Android-SDK
- group: build
  title: Swift SDK (bratwursted)
  type: SDKs
  url: https://github.com/bratwursted/swapi-swift
- group: build
  title: R Client (LionyxML)
  type: SDKs
  url: https://github.com/LionyxML/r-swapi-client
- group: build
  title: Java + Spring Sample
  type: CodeExamples
  url: https://github.com/vininjr/starwars
- group: build
  title: Flutter + GraphQL Sample
  type: CodeExamples
  url: https://github.com/kranfix/flutter_graphql_swapi
- group: docs
  title: Community OpenAPI (kamilkodzi)
  type: OpenAPI
  url: https://github.com/kamilkodzi/oas-swapi
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/swapi-context.jsonld
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/swapi-spectral-rules.yml
- group: commercial
  title: ''
  type: APICommonsPlans
  url: plans/swapi-plans-pricing.yml
- group: operate
  title: ''
  type: APICommonsRateLimits
  url: rate-limits/swapi-rate-limits.yml
created: '2026-05-28'
description: SWAPI (Star Wars API) is a free, open Star Wars REST API exposing canonical Star Wars data — films, people, planets, species, starships, and vehicles. Originally built by Paul Hallett (@phalt) at swapi.co, it is now maintained as community mirrors at swapi.dev (Python/Django, @juriy) and www.swapi.tech (Node/MongoDB, @semperry). SWAPI is one of the most widely cited "teaching APIs" in the developer ecosystem.
examples:
- key_count: 5
  name: Swapi Getfilm Example
  slug: swapi-getfilm-example
- key_count: 5
  name: Swapi Getperson Example
  slug: swapi-getperson-example
- key_count: 5
  name: Swapi Getplanet Example
  slug: swapi-getplanet-example
- key_count: 5
  name: Swapi Getspecies Example
  slug: swapi-getspecies-example
- key_count: 5
  name: Swapi Getstarship Example
  slug: swapi-getstarship-example
- key_count: 5
  name: Swapi Getvehicle Example
  slug: swapi-getvehicle-example
- key_count: 5
  name: Swapi Listfilms Example
  slug: swapi-listfilms-example
- key_count: 5
  name: Swapi Listpeople Example
  slug: swapi-listpeople-example
graphqls:
- description: ''
  name: SWAPI - Star Wars API GraphQL API
  slug: swapi-graphql
image: https://avatars.githubusercontent.com/u/2014472?s=200
json_schemas:
- name: SWAPI Film
  property_count: 14
  slug: swapi-film
- name: SWAPI Person
  property_count: 16
  slug: swapi-person
- name: SWAPI Planet
  property_count: 14
  slug: swapi-planet
- name: SWAPI Species
  property_count: 15
  slug: swapi-species
- name: SWAPI Starship
  property_count: 18
  slug: swapi-starship
- name: SWAPI Vehicle
  property_count: 16
  slug: swapi-vehicle
json_structures:
- name: Swapi Film Structure
  property_count: 0
  slug: swapi-film-structure
- name: Swapi Person Structure
  property_count: 0
  slug: swapi-person-structure
- name: Swapi Planet Structure
  property_count: 0
  slug: swapi-planet-structure
- name: Swapi Species Structure
  property_count: 0
  slug: swapi-species-structure
- name: Swapi Starship Structure
  property_count: 0
  slug: swapi-starship-structure
- name: Swapi Vehicle Structure
  property_count: 0
  slug: swapi-vehicle-structure
jsonld:
- class_count: 6
  name: Swapi Context
  property_count: 61
  slug: swapi-context
layout: provider
modified: '2026-05-29'
name: SWAPI - Star Wars API
nav: Providers
network: true
overview: 'SWAPI - Star Wars API publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Films API, People API, Planets API, and 3 more. Tagged areas include Star Wars, Open Source, Teaching API, Public API, and REST.


  The SWAPI - Star Wars API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SWAPI - Star Wars API''s developer surface includes tooling, code examples, and 18 more developer resources.'
plans:
- name: Swapi Plans Pricing
  plan_count: 1
  slug: swapi-plans-pricing
random_paper: 96
rate_limits:
- limit_count: 1
  name: Swapi Rate Limits
  slug: swapi-rate-limits
rules:
- name: SWAPI - Star Wars API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: swapi-jsonschema-spectral-rules
- name: SWAPI - Star Wars API API Rules
  rule_count: 39
  severity_counts:
    error: 10
    hint: 0
    info: 5
    warn: 24
  slug: swapi-spectral-rules
score:
  band: thin
  composite: 31.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 23.1
    developer_ergonomics: 15.2
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swapi/refs/heads/main/screenshots/swapi-2026-06-20T194754.png
security:
- kind: domain-security
  name: Swapi Domain Security
  slug: swapi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: swapi
tags:
- Star Wars
- Open Source
- Teaching API
- Public API
- REST
- GraphQL
- Entertainment
- Datasets
website: https://swapi.dev/
---
