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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-10'
api_count: 5
apis:
- description: Read-only REST API serving over 450 ketogenic diet recipes across 11 categories (drinks, smoothies, keto staples and dips, desserts, soups, fish, beef, appetizers, snacks and breakfast) with nutrition
  name: Encurate Keto Diet API
  slug: encurate-keto-diet-api
- description: Read-only REST API returning basic specifications for commercial airplanes. Seven GET operations cover the full listing, a single airplane by ID, keyword search by name, filtering by brand (Boeing, Ai
  name: Encurate AirplanesDB API
  slug: encurate-airplanesdb-api
- description: Read-only REST API returning basic metadata on cat breeds from around the world. Nine GET operations cover the full listing, a paginated listing at ten results per page, a single breed, keyword search
  name: Encurate CatBreedDB API
  slug: encurate-catbreeddb-api
- description: Read-only REST API returning basic metadata on dog breeds from around the world. Nine GET operations cover the full listing, a paginated listing at ten results per page, a single breed, keyword search
  name: Encurate DogBreedDB API
  slug: encurate-dogbreeddb-api
- description: Read-only REST API returning metadata on cannabis strains — strain type (indica, sativa, hybrid), effect, flavor and origin — aimed at mobile and web apps for dispensary locators, medical marijuana re
  name: Encurate Weed Strain API
  slug: encurate-weed-strain-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://encurate.app/
- group: docs
  title: ''
  type: Documentation
  url: https://encurate.app/keto_diet_api/
- group: docs
  title: ''
  type: APIReference
  url: https://rapidapi.com/encurateapi-api/api/keto-diet
- group: commercial
  title: ''
  type: Pricing
  url: https://encurate.app/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://encurate.app/register/
- group: start
  title: ''
  type: Login
  url: https://encurate.app/login/
- group: operate
  title: ''
  type: Support
  url: https://encurate.app/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://encurate.app/privacy_policy/
- group: start
  title: ''
  type: Sandbox
  url: https://rapidapi.com/encurateapi-api/api/keto-diet/playground
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/encurate
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/encurate
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/encurate.app/
- group: commercial
  title: ''
  type: Plans
  url: plans/encurate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/encurate-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/encurate-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/encurate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/encurate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/encurate-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/encurate-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/encurate-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/encurate-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/encurate-domain-security.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/encurate-finops.yml
created: '2024-03-30'
description: 'Encurate (encurate.app) is a content-management backend for mobile apps that doubles as a publisher of read-only reference-data APIs. Its platform lets developers manage magazine, news and press-release content for their apps from one web interface, with image delivery over a CDN. Alongside it Encurate operates five public REST APIs distributed exclusively through the RapidAPI marketplace: Keto Diet (450+ ketogenic recipes in 11 categories with calorie, fat, carbohydrate and protein values), AirplanesDB (commercial aircraft specifications), CatBreedDB and DogBreedDB (cat and dog breed metadata), and Weed Strain (cannabis strain type, effect, flavor and origin). All 44 published operations are HTTP GET returning JSON, authenticated with a RapidAPI key; there is no write surface, no OpenAPI, no SDK and no event surface.'
finops:
- name: Encurate Finops
  service_category: API
  slug: encurate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/encurate.png
layout: provider
modified: '2026-09-06'
name: Encurate
nav: Providers
network: true
overview: 'Encurate publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Diet, Food, Keto, Nutrition, and Recipes.


  Encurate''s developer surface includes documentation, API reference, pricing, signup flow, support, sandbox, authentication, and 16 more developer resources.'
plans:
- name: Encurate Plans Pricing
  plan_count: 0
  slug: encurate-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 15
  name: Encurate Rate Limits
  slug: encurate-rate-limits
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 88.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 31.2
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/encurate/refs/heads/main/screenshots/encurate-2026-06-20T180653.png
security:
- kind: authentication
  name: Encurate Authentication
  slug: encurate-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Encurate Domain Security
  slug: encurate-domain-security
  summary_line: TLSv1.3
slug: encurate
tags:
- Diet
- Food
- Keto
- Nutrition
- Recipes
- Health
- Fitness
- Datasets
- Reference Data
- Content Management
- Mobile
- Animals
- Aviation
- Cannabis
- RapidAPI
website: https://encurate.app/
---
