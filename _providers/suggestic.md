---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: GraphQL API for personalized nutrition — users, programs/diets, meal-plan generation, recipe and restaurant search, food logging (incl. AI food log), shopping lists, health trackers, lab tests/biomark
  name: Suggestic GraphQL API
  slug: suggestic-graphql-api
artifact_total: 9
asyncapis:
- description: ''
  name: Suggestic Webhooks
  slug: suggestic-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/suggestic/plans/suggestic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/suggestic-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.suggestic.com/feed
- group: auth
  href: https://artifacts.apis.io/suggestic/security/suggestic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/suggestic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://suggestic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.suggestic.com/graphql/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.suggestic.com/graphql/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.suggestic.com/graphql/graphql/graphql-playground
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.suggestic.com/graphql/start-here/getting-started
- group: company
  title: ''
  type: Blog
  url: https://blog.suggestic.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://pricing.suggestic.com/
- group: start
  title: ''
  type: SignUp
  url: https://suggestic.com/
- group: start
  title: ''
  type: Login
  url: https://console.suggestic.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Suggestic
- group: operate
  title: ''
  type: StatusPage
  url: https://status.suggestic.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.suggestic.com/graphql/changelog/2025
- group: auth
  href: https://artifacts.apis.io/suggestic/authentication/suggestic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/suggestic-authentication.yml
- group: build
  href: https://artifacts.apis.io/suggestic/packages/suggestic-packages.yml
  title: ''
  type: Packages
  url: packages/suggestic-packages.yml
- group: build
  href: https://artifacts.apis.io/suggestic/packages/suggestic-packages.yml
  title: ''
  type: SDKs
  url: packages/suggestic-packages.yml
- group: design
  href: https://artifacts.apis.io/suggestic/conventions/suggestic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/suggestic-conventions.yml
- group: design
  href: https://artifacts.apis.io/suggestic/errors/suggestic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/suggestic-problem-types.yml
- group: design
  href: https://artifacts.apis.io/suggestic/lifecycle/suggestic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/suggestic-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.suggestic.com/graphql/helpful-resources/deprecated-features
- group: operate
  href: https://artifacts.apis.io/suggestic/changelog/suggestic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/suggestic-changelog.yml
- group: design
  href: https://artifacts.apis.io/suggestic/conformance/suggestic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/suggestic-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://suggestic.com/
- group: design
  href: https://artifacts.apis.io/suggestic/components/suggestic-components.yml
  title: ''
  type: Components
  url: components/suggestic-components.yml
- group: design
  href: https://artifacts.apis.io/suggestic/asyncapi/suggestic-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/suggestic-webhooks.yml
- group: start
  href: https://artifacts.apis.io/suggestic/sandbox/suggestic-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/suggestic-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/suggestic/mcp/suggestic-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/suggestic-mcp.yml
- group: design
  href: https://artifacts.apis.io/suggestic/data-model/suggestic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/suggestic-data-model.yml
- group: agent
  href: https://artifacts.apis.io/suggestic/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/suggestic/llms/suggestic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/suggestic-llms.txt
created: '2026-07-17'
description: Suggestic is a personalized-nutrition and health platform that exposes a GraphQL API for building meal-planning, food-logging, and coaching applications. Developers use the API to create users, assign nutrition programs and diets, generate personalized meal plans, search a large recipe and restaurant database, log food (including AI photo-based logging), build shopping lists, and track sleep, steps, water, weight, heart rate, symptoms, biomarkers, and supplements. The platform also powers an AI Assistant with journeys and guardrails, a Console for configuration and webhooks, and a Telehealth/Coaching Portal. Suggestic (a Techstars-backed company) markets an enterprise AI offering for regulated health verticals and is HIPAA and SOC 2 Type II certified. Authentication is via a server-side API token plus an sg-user header, or client-side JWT bearer tokens.
finops:
- has_sources: true
  method: derived
  name: Suggestic Finops
  primary_unit: pilot to first production
  service_category: ''
  slug: suggestic-finops
  template: false
image: https://suggestic.com/assets/images/og-image.png
layout: provider
modified: '2026-10-06'
name: Suggestic
nav: Providers
network: true
overview: 'Suggestic is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nutrition, Health, Meal Planning, and Recipes.


  The Suggestic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Suggestic''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 25 more developer resources.'
plans:
- name: Suggestic Plans Pricing
  plan_count: 2
  slug: suggestic-plans-pricing
- name: Suggestic Price Estimates
  plan_count: 0
  slug: suggestic-price-estimates
random_paper: 14
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 68.5
    discoverability: 73.2
    operational_transparency: 42.1
  previous_composite: 51.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/suggestic/suggestic-2026-08-17T082152.png
security:
- kind: authentication
  name: Suggestic Authentication
  slug: suggestic-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Suggestic Domain Security
  slug: suggestic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Onboard a user and generate a meal plan
  slug: suggestic-create-user-and-meal-plan
- name: Log food and read nutrition totals
  slug: suggestic-food-logging
slug: suggestic
tags:
- Company
- Nutrition
- Health
- Meal Planning
- Recipes
- Food
- GraphQL
- Personalization
- Wellness
- Telehealth
- Artificial Intelligence
website: https://suggestic.com/
---
