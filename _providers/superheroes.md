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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Superheroes Agentic Access
  operation_count: 8
  slug: superheroes-agentic-access
  summary_line: 8 operations
api_count: 7
apis:
- description: Per-character physical appearance slices.
  name: Superhero API (akabab) Appearance API
  slug: superheroes-appearance-api
- description: Per-character biographical slices.
  name: Superhero API (akabab) Biography API
  slug: superheroes-biography-api
- description: Full character records and the consolidated dataset.
  name: Superhero API (akabab) Characters API
  slug: superheroes-characters-api
- description: Per-character group affiliations and relatives.
  name: Superhero API (akabab) Connections API
  slug: superheroes-connections-api
- description: Multi-resolution character image assets.
  name: Superhero API (akabab) Images API
  slug: superheroes-images-api
- description: Per-character powerstats slices (intelligence, strength, etc.).
  name: Superhero API (akabab) Powerstats API
  slug: superheroes-powerstats-api
- description: Per-character occupation and base slices.
  name: Superhero API (akabab) Work API
  slug: superheroes-work-api
artifact_total: 25
collections:
- collection_type: open
  name: Superhero API (akabab)
  slug: open-superheroes
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/superheroes-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superheroes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://akabab.github.io/superhero-api/api/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/akabab/superhero-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akabab
- group: commercial
  title: MIT License
  type: License
  url: https://github.com/akabab/superhero-api/blob/master/LICENSE
- group: other
  title: jsDelivr CDN Mirror
  type: CDN
  url: https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/
- group: other
  title: superheroapi.com (Original Source)
  type: OriginalSource
  url: https://superheroapi.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/superheroes-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/superheroes-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/superheroes-context.jsonld
- group: docs
  title: Character
  type: JSONSchema
  url: json-schema/superheroes-character-schema.json
- group: docs
  title: Powerstats
  type: JSONSchema
  url: json-schema/superheroes-powerstats-schema.json
- group: docs
  title: Appearance
  type: JSONSchema
  url: json-schema/superheroes-appearance-schema.json
- group: docs
  title: Biography
  type: JSONSchema
  url: json-schema/superheroes-biography-schema.json
- group: docs
  title: Work
  type: JSONSchema
  url: json-schema/superheroes-work-schema.json
- group: docs
  title: Connections
  type: JSONSchema
  url: json-schema/superheroes-connections-schema.json
- group: docs
  title: Images
  type: JSONSchema
  url: json-schema/superheroes-images-schema.json
- group: design
  title: Character
  type: JSONStructure
  url: json-structure/superheroes-character-structure.json
- group: build
  title: Character Example
  type: Examples
  url: examples/superheroes-character-example.json
- group: build
  title: All Characters Example
  type: Examples
  url: examples/superheroes-all-example.json
- group: build
  title: Powerstats Example
  type: Examples
  url: examples/superheroes-powerstats-example.json
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/superheroes-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/superheroes-plans-pricing.yml
created: '2026-05-28'
description: Open-source REST API exposing 731 superheroes and villains drawn from multiple comic universes (Marvel, DC, Dark Horse, Image, and more) under a single, unauthenticated JSON surface. The dataset is rebuilt from the original superheroapi.com source, cleaned up, and republished as static JSON files served from GitHub Pages and the jsDelivr CDN. Each character includes powerstats, appearance, biography, work, connections, and a multi-resolution image set.
examples:
- key_count: 9
  name: Superheroes Character Example
  slug: superheroes-character-example
- key_count: 6
  name: Superheroes Powerstats Example
  slug: superheroes-powerstats-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superheroes.png
json_schemas:
- name: Appearance
  property_count: 6
  slug: superheroes-appearance
- name: Biography
  property_count: 7
  slug: superheroes-biography
- name: Character
  property_count: 9
  slug: superheroes-character
- name: Connections
  property_count: 2
  slug: superheroes-connections
- name: Images
  property_count: 4
  slug: superheroes-images
- name: Powerstats
  property_count: 6
  slug: superheroes-powerstats
- name: Work
  property_count: 2
  slug: superheroes-work
json_structures:
- name: Superheroes Character Structure
  property_count: 9
  slug: superheroes-character-structure
jsonld:
- class_count: 36
  name: Superheroes Context
  property_count: 1
  slug: superheroes-context
layout: provider
modified: '2026-05-29'
name: Superhero API (akabab)
nav: Providers
network: true
overview: 'Superhero API (akabab) publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Appearance API, Biography API, Characters API, and 4 more. Tagged areas include Games And Comics, Superheroes, Comic Books, Open Source, and Static API.


  The Superhero API (akabab) catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Superhero API (akabab)''s developer surface includes code examples and 24 more developer resources.'
plans:
- name: Superheroes Plans Pricing
  plan_count: 1
  slug: superheroes-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Superheroes Rate Limits
  slug: superheroes-rate-limits
rules:
- name: Superhero API (akabab) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: superheroes-jsonschema-spectral-rules
- name: Superhero API (akabab) API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 3
  slug: superheroes-rules
score:
  band: thin
  composite: 36.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 61.9
    developer_ergonomics: 0.0
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/superheroes/refs/heads/main/screenshots/superheroes-2026-06-20T194712.png
security:
- kind: domain-security
  name: Superheroes Domain Security
  slug: superheroes-domain-security
  summary_line: TLSv1.3 · HSTS
slug: superheroes
tags:
- Games And Comics
- Superheroes
- Comic Books
- Open Source
- Static API
- GitHub Pages
- Public APIs
website: https://akabab.github.io/superhero-api/api/
---
