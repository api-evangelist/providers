---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Nutrical Solution Ltd Agentic Access
  operation_count: 21
  slug: nutrical-solution-ltd-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 6
apis:
- description: Provision entities that own recipes and receive a client access token.
  name: Nutrical Solution Ltd Entity API
  slug: nutrical-solution-ltd-entity-api
- description: Search the NutriCal ingredient database (USDA + NutriCal sources).
  name: Nutrical Solution Ltd Ingredients API
  slug: nutrical-solution-ltd-ingredients-api
- description: Manage meal plans and meal-plan customers.
  name: Nutrical Solution Ltd Meal Plans API
  slug: nutrical-solution-ltd-meal-plans-api
- description: Public nutrient and allergen reference data.
  name: Nutrical Solution Ltd Metadata API
  slug: nutrical-solution-ltd-metadata-api
- description: Manage recipe categories and sub-categories.
  name: Nutrical Solution Ltd Recipe Categories API
  slug: nutrical-solution-ltd-recipe-categories-api
- description: Create, read, update, and delete recipes with nutrition analysis.
  name: Nutrical Solution Ltd Recipes API
  slug: nutrical-solution-ltd-recipes-api
artifact_total: 10
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
  url: openapi/nutrical-solution-ltd-openapi.yml
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: nutrical-solution-ltd-mcp.yml
  slug: nutrical-solution-ltd-mcpyml
modified: '2026-07-20'
name: Nutrical Solution Ltd
nav: Providers
network: true
overview: 'Nutrical Solution Ltd publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Entity API, Ingredients API, Meal Plans API, and 3 more. Tagged areas include Company, Food, Nutrition, Health, and Recipes.


  Nutrical Solution Ltd''s developer surface includes authentication, sandbox, documentation, API reference, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 26
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 15.5
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 34.3
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
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
- Restaurants
- GCC
website: https://www.nutrical.co
---
