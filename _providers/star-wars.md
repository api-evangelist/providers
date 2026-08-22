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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Star Wars Agentic Access
  operation_count: 12
  slug: star-wars-agentic-access
  summary_line: 12 operations
api_count: 6
apis:
- description: Star Wars films
  name: Star Wars API Films API
  slug: star-wars-films-api
- description: People and characters in the Star Wars universe
  name: Star Wars API People API
  slug: star-wars-people-api
- description: Planets in the Star Wars universe
  name: Star Wars API Planets API
  slug: star-wars-planets-api
- description: Species in the Star Wars universe
  name: Star Wars API Species API
  slug: star-wars-species-api
- description: Starships in the Star Wars universe
  name: Star Wars API Starships API
  slug: star-wars-starships-api
- description: Vehicles in the Star Wars universe
  name: Star Wars API Vehicles API
  slug: star-wars-vehicles-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Star Wars REST API (SWAPI) Films API
  slug: open-star-wars-films-api
- collection_type: open
  name: Star Wars REST API (SWAPI) Films People API
  slug: open-star-wars-people-api
- collection_type: open
  name: Star Wars REST API (SWAPI) Films Planets API
  slug: open-star-wars-planets-api
- collection_type: open
  name: Star Wars REST API (SWAPI) Films Species API
  slug: open-star-wars-species-api
- collection_type: open
  name: Star Wars REST API (SWAPI) Films Starships API
  slug: open-star-wars-starships-api
- collection_type: open
  name: Star Wars REST API (SWAPI) Films Vehicles API
  slug: open-star-wars-vehicles-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/star-wars-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/star-wars-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://swapi.info
- group: docs
  title: ''
  type: Documentation
  url: https://swapi.info/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/SivaramPg/swapi.info
- group: operate
  title: ''
  type: StatusPage
  url: https://status.swapi.info
- group: other
  title: ''
  type: Playground
  url: https://swapi.info/playground
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/star-wars/refs/heads/main/plans/star-wars-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/star-wars/refs/heads/main/rate-limits/star-wars-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/star-wars/refs/heads/main/finops/star-wars-finops.yml
created: '2026-06-13'
description: The Star Wars REST API (SWAPI / swapi.info) is the world's first quantified and programmatically-accessible data source for all the data from the Star Wars canon universe. It provides structured JSON access to films, characters (people), starships, vehicles, planets, and species from the Star Wars universe via a simple HTTP GET API. The API requires no authentication, has no rate limits, and is completely free and open source. Originally created by Paul Hallett as swapi.co and later swapi.dev, the current maintained iteration at swapi.info was rebuilt by Sivaram P as a CDN-powered, file-based API serving over one million daily requests with sub-50ms global response times via Vercel and Cloudflare.
examples:
- key_count: 14
  name: Film
  slug: film
- key_count: 16
  name: Person
  slug: person
- key_count: 14
  name: Planet
  slug: planet
- key_count: 15
  name: Species
  slug: species
- key_count: 18
  name: Starship
  slug: starship
- key_count: 16
  name: Vehicle
  slug: vehicle
finops:
- name: Star Wars Finops
  service_category: ''
  slug: star-wars-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/star-wars.png
json_schemas:
- name: Film
  property_count: 14
  slug: film
- name: Person
  property_count: 16
  slug: person
- name: Planet
  property_count: 14
  slug: planet
- name: Species
  property_count: 15
  slug: species
- name: Starship
  property_count: 18
  slug: starship
- name: Vehicle
  property_count: 16
  slug: vehicle
jsonld:
- class_count: 6
  name: Star Wars Context
  property_count: 56
  slug: star-wars-context
layout: provider
modified: '2026-06-13'
name: Star Wars API
nav: Providers
network: true
overview: 'Star Wars API publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Films API, People API, Planets API, and 3 more. Tagged areas include Star Wars, Science Fiction, Entertainment, Films, and Characters.


  The Star Wars API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Star Wars API''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Star Wars Plans Pricing
  plan_count: 1
  slug: star-wars-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Star Wars Rate Limits
  slug: star-wars-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Star Wars API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: star-wars-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.7
  delta: -9.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 60.1
    developer_ergonomics: 13.1
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/star-wars/refs/heads/main/screenshots/star-wars-2026-06-20T194509.png
security:
- kind: domain-security
  name: Star Wars Domain Security
  slug: star-wars-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: star-wars
tags:
- Star Wars
- Science Fiction
- Entertainment
- Films
- Characters
- Planets
- Starships
- Vehicles
- Species
- Open Source
website: https://swapi.info
---
