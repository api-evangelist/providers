---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Nutrical Solution Ltd Agentic Access
  operation_count: 21
  slug: nutrical-solution-ltd-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.nutrical.co
  baseurl_source: declared
  description: Provision entities that own recipes and receive a client access token.
  name: Nutrical Solution Ltd Entity API
  slug: nutrical-solution-ltd-entity-api
- baseURL: https://api.nutrical.co
  baseurl_source: declared
  description: Search the NutriCal ingredient database (USDA + NutriCal sources).
  name: Nutrical Solution Ltd Ingredients API
  slug: nutrical-solution-ltd-ingredients-api
- baseURL: https://api.nutrical.co
  baseurl_source: declared
  description: Manage meal plans and meal-plan customers.
  name: Nutrical Solution Ltd Meal Plans API
  slug: nutrical-solution-ltd-meal-plans-api
- baseURL: https://api.nutrical.co
  baseurl_source: declared
  description: Public nutrient and allergen reference data.
  name: Nutrical Solution Ltd Metadata API
  slug: nutrical-solution-ltd-metadata-api
- baseURL: https://api.nutrical.co
  baseurl_source: declared
  description: Manage recipe categories and sub-categories.
  name: Nutrical Solution Ltd Recipe Categories API
  slug: nutrical-solution-ltd-recipe-categories-api
- baseURL: https://api.nutrical.co
  baseurl_source: declared
  description: Create, read, update, and delete recipes with nutrition analysis.
  name: Nutrical Solution Ltd Recipes API
  slug: nutrical-solution-ltd-recipes-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NutriCal Food & Nutrition Entity API
  slug: open-nutrical-solution-ltd-entity-api
- collection_type: open
  name: NutriCal Food & Nutrition Entity Ingredients API
  slug: open-nutrical-solution-ltd-ingredients-api
- collection_type: open
  name: NutriCal Food & Nutrition Entity Meal Plans API
  slug: open-nutrical-solution-ltd-meal-plans-api
- collection_type: open
  name: NutriCal Food & Nutrition Entity Metadata API
  slug: open-nutrical-solution-ltd-metadata-api
- collection_type: open
  name: NutriCal Food & Nutrition Entity Recipe Categories API
  slug: open-nutrical-solution-ltd-recipe-categories-api
- collection_type: open
  name: NutriCal Food & Nutrition Entity Recipes API
  slug: open-nutrical-solution-ltd-recipes-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nutrical-solution-ltd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nutrical-solution-ltd-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nutrical-solution-ltd-agentic-access.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/nutrical-solution-ltd-openapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nutrical-solution-ltd-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nutrical-solution-ltd-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nutrical-solution-ltd-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nutrical-solution-ltd-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nutrical-solution-ltd-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nutrical-solution-ltd-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nutrical-solution-ltd-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nutrical-solution-ltd-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nutrical-solution-ltd-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nutrical-solution-ltd-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nutrical.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nutrical.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nutrical.co
- group: company
  title: ''
  type: Blog
  url: https://www.nutrical.co/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nutrical.co/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.nutrical.co
- group: start
  title: ''
  type: Login
  url: https://app.nutrical.co
- group: operate
  title: ''
  type: Support
  url: https://www.nutrical.co/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nutrical.co/terms-of-sales/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nutrical.co/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nutrical-co/
- group: company
  title: ''
  type: Website
  url: https://www.nutrical.co
created: '2026-07-17'
description: NutriCal (Nutrical Solution Ltd) is the GCC's food nutrition and intelligence platform, offering the region's first Saudi FDA / GCC-compliant food-label and calorie-analysis software. Its SaaS lets restaurants, cafes, hotels, food manufacturers, bakeries, catering companies, nutrition centres, and meal-plan businesses register products, generate bilingual (English/Arabic) nutrition and ingredient labels, manage and cost recipes, run nutrition analysis, and build customer meal plans against an ingredient database of 40,000+ foods sourced from USDA data and NutriCal's proprietary local database. NutriCal also exposes a Food & Nutrition API so apps, programs, and websites can search ingredients, create and analyze recipes, manage recipe categories, build meal plans, and read nutrient and allergen metadata. Backed by 500 Global.
image: https://www.nutrical.co/common/OpenGraph.png
layout: provider
modified: '2026-07-20'
name: Nutrical Solution Ltd
nav: Providers
network: true
overview: 'Nutrical Solution Ltd publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Entity API, Ingredients API, Meal Plans API, and 3 more. Tagged areas include Company, Food, Nutrition, Health, and Recipes.


  Nutrical Solution Ltd''s developer surface includes authentication, sandbox, documentation, API reference, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 17.0
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nutrical-solution-ltd/refs/heads/main/screenshots/nutrical-solution-ltd-2026-08-07T185800.png
security:
- kind: authentication
  name: Nutrical Solution Ltd Authentication
  slug: nutrical-solution-ltd-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Nutrical Solution Ltd Domain Security
  slug: nutrical-solution-ltd-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nutrical-solution-ltd
tags:
- Company
- Food
- Nutrition
- Health
- Recipes
- Meal Plans
- Food Labeling
- Compliance
- Restaurant
- GCC
website: https://www.nutrical.co
---
