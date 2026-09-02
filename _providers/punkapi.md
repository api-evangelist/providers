---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Punkapi Agentic Access
  operation_count: 3
  slug: punkapi-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: BrewDog DIY Dog beer recipes — 325 entries
  name: Punk API Beers API
  slug: punkapi-beers-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Punk API — Brewdog DIY Dog Beer Recipes Beers API
  slug: open-punkapi-beers-api
- collection_type: open
  name: Punk API — Brewdog DIY Dog Beer Recipes
  slug: open-punkapi
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/sammdec/punkapi/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/punkapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/punkapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://punkapi.com
- group: build
  title: punkapi-db (Recipe Dataset — archived 2023-06-28)
  type: GitHubRepository
  url: https://github.com/sammdec/punkapi
- group: build
  title: punkapi-server (Express server — archived 2023-06-28)
  type: GitHubRepository
  url: https://github.com/sammdec/punkapi-server
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sammdec
- group: build
  title: punkapi-db (npm — recipe dataset)
  type: SDKs
  url: https://www.npmjs.com/package/punkapi-db
- group: build
  title: punkapi (C client)
  type: SDKs
  url: https://github.com/apfohl/punkapi
- group: build
  title: punkapi-ruby (Ruby client)
  type: SDKs
  url: https://github.com/samjbmason/punkapi-ruby
- group: build
  title: PunkApi (PHP client)
  type: SDKs
  url: https://github.com/billythekid/PunkApi
- group: build
  title: brewdog.js (JavaScript client)
  type: SDKs
  url: https://github.com/mikefrancis/brewdog.js
- group: build
  title: PunkAPI (Swift/iOS client)
  type: SDKs
  url: https://github.com/Oni-zerone/PunkAPI
- group: build
  title: VueDogs-API (Vue.js client)
  type: SDKs
  url: https://github.com/yoohahn/VueDogs-API
- group: build
  title: brewdog-recipe (Docker mirror)
  type: SDKs
  url: https://hub.docker.com/r/yoohahn/brewdog-recipe
- group: build
  title: brewdogr (R client)
  type: SDKs
  url: https://github.com/phillc73/brewdogr
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/punkapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/punkapi-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/punkapi-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/punkapi-vocabulary.yml
created: '2026-05-28'
description: 'Punk API is a free, no-auth REST API exposing BrewDog''s "DIY Dog" open-source beer recipe collection — 325 detailed homebrew recipes crowdsourced and transcribed from the BrewDog DIY Dog PDF. The v2 surface (api.punkapi.com/v2) offered three read-only endpoints: list beers (with rich query filtering on ABV, IBU, EBC, brew date, beer name, hops, malt, yeast, and food pairing), get a beer by id, and get a random beer. Each beer carries a full recipe — ABV, IBU, EBC/SRM colour, target gravities, mash temperature schedule, fermentation temperature, twist, malt and hop bills, yeast strain, food pairings, brewer''s tips, and contributor attribution. STATUS — DEPRECATED. BrewDog decommissioned the public api.punkapi.com endpoint in 2023 and the source repositories (sammdec/punkapi-db, sammdec/punkapi-server) were archived on 2023-06-28. The dataset and server source remain MIT-licensed and available; community-hosted mirrors and the `punkapi-db` npm package preserve the contract
  documented here.'
examples:
- key_count: 21
  name: Punkapi Beer Example
  slug: punkapi-beer-example
- key_count: 3
  name: Punkapi Error Example
  slug: punkapi-error-example
features:
- description: Crowdsourced transcription of the complete BrewDog DIY Dog PDF — every recipe from Punk IPA (#001) through the final published batch.
  name: 325 BrewDog DIY Dog Recipes
- description: Each beer carries ABV, IBU, EBC, SRM, target gravities, mash schedule, fermentation temperature, malt bill, hop bill, yeast strain, food pairings, and brewer's tips.
  name: Full Brewing Recipe
- description: List endpoint supports filters on ABV (gt/lt), IBU (gt/lt), EBC (gt/lt), brewed-before/after dates, and substring search on beer name, hops, malt, yeast, and food pairing.
  name: Recipe-Oriented Query Filters
- description: page (>=1) and per_page (1-80, default 25) on the list endpoint.
  name: Pagination
- description: /beers/random returns a uniformly random recipe — useful for "beer of the day" demos.
  name: Random Beer
- description: Fully public — no API keys, OAuth, or signup required.
  name: No Authentication
- description: Best-effort public service while it was live. Only the per_page ceiling of 80 is enforced.
  name: No Rate Limits Documented
- description: Both punkapi-db (dataset) and punkapi-server (Express app) are MIT-licensed — self-host or fork freely.
  name: MIT-Licensed Source
- description: The complete dataset is published as the `punkapi-db` package for direct in-process use without HTTP.
  name: npm Distribution
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/punkapi.png
integrations:
- description: The upstream source of every recipe — BrewDog's open-source DIY Dog homebrew PDF.
  name: BrewDog DIY Dog
- description: The recipe dataset packaged for direct npm install — no HTTP needed.
  name: punkapi-db (npm)
- description: The reference Express + node server that exposes the dataset as the v2 REST API.
  name: punkapi-server (Express)
- description: Several community-run instances of punkapi-server keep the v2 contract reachable after BrewDog's 2023 decommission.
  name: Community Mirrors
- description: Listed in github.com/public-apis/public-apis under the Food & Drink category.
  name: Public APIs Catalog
json_schemas:
- name: Beer
  property_count: 21
  slug: punkapi-beer
- name: Error
  property_count: 3
  slug: punkapi-error
json_structures:
- name: Punkapi Beer Structure
  property_count: 21
  slug: punkapi-beer-structure
- name: Punkapi Error Structure
  property_count: 3
  slug: punkapi-error-structure
jsonld:
- class_count: 8
  name: Punkapi Context
  property_count: 34
  slug: punkapi-context
layout: provider
modified: '2026-05-29'
name: Punk API
nav: Providers
network: true
overview: 'Punk API publishes 1 API on the [APIs.io](https://apis.io/) network: Beers API. Tagged areas include Food And Drink, Beer, BrewDog, DIY Dog, and Recipes.


  The Punk API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Punkapi Plans Pricing
  plan_count: 1
  slug: punkapi-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Punkapi Rate Limits
  slug: punkapi-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Punk API API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: punkapi-jsonschema-spectral-rules
- effective_rule_count: 77
  extends:
  - spectral:oas
  name: Punk API API Rules
  rule_count: 36
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 21
  slug: punkapi-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 27.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 28.8
    contract_quality: 65.5
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 0.0
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Punkapi Domain Security
  slug: punkapi-domain-security
  summary_line: DNSSEC
slug: punkapi
solutions:
- description: Clone sammdec/punkapi-server, run `npm i` then `npm run dev` — get the full v2 contract on http://localhost:3333.
  name: Self-Host the Server
- description: Run `npm i --save punkapi-db` to pull the full 325-recipe data.json into your application without HTTP.
  name: Embed the Dataset
- description: For purely read use cases, host data.json on a CDN and serve clients directly.
  name: Static JSON Mirror
tags:
- Food And Drink
- Beer
- BrewDog
- DIY Dog
- Recipes
- Open-Source
- Public APIs
- REST
- Deprecated
use_cases:
- description: Look up a recipe by ABV, hop, or malt to replicate or adapt a BrewDog beer at home-batch scale.
  name: Homebrewing Reference
- description: Front-end and mobile tutorials use Punk API as a fun, schema-rich, no-auth REST target.
  name: Sample / Tutorial API
- description: Power beer recommendation apps, food-pairing tools, and BrewDog fan sites.
  name: Beer Discovery App
- description: Filter by hop (e.g. `hops=simcoe`) or malt (e.g. `malt=maris_otter`) to discover recipes using a specific ingredient.
  name: Search by Ingredient
- description: Filter by `food=spicy_food` to find beers explicitly recommended for spicy cuisine.
  name: Food Pairing Lookup
- description: Stable, well-defined schema makes Punk API a good fixture for codegen tools, OpenAPI tooling, and SDK builders.
  name: HTTP Client QA
website: https://punkapi.com
---
