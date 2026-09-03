---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Fatsecret Agentic Access
  operation_count: 23
  slug: fatsecret-agentic-access
  summary_line: 23 operations · 6 acting
api_count: 1
apis:
- baseURL: https://platform.fatsecret.com/rest
  baseurl_source: declared
  description: Daily exercise tracking
  name: fatsecret Exercise Diary API
  slug: fatsecret-exercise-diary-api
- baseURL: https://platform.fatsecret.com/rest
  baseurl_source: declared
  description: Daily food entries and summaries
  name: fatsecret Food Diary API
  slug: fatsecret-food-diary-api
- baseURL: https://platform.fatsecret.com/rest
  baseurl_source: declared
  description: Search and retrieve food nutrition data
  name: fatsecret Foods API
  slug: fatsecret-foods-api
- baseURL: https://platform.fatsecret.com/rest
  baseurl_source: declared
  description: Identify foods and their nutrition from a photograph
  name: fatsecret Image Recognition API
  slug: fatsecret-image-recognition-api
- baseURL: https://platform.fatsecret.com/rest
  baseurl_source: declared
  description: Turn a free-text meal description into matched foods and nutrition
  name: fatsecret Natural Language Processing API
  slug: fatsecret-natural-language-processing-api
- baseURL: https://platform.fatsecret.com/rest
  baseurl_source: declared
  description: User-managed custom foods and favorites
  name: fatsecret Profile Foods API
  slug: fatsecret-profile-foods-api
- baseURL: https://platform.fatsecret.com/rest
  baseurl_source: declared
  description: Saved meals and meal items
  name: fatsecret Profile Meals API
  slug: fatsecret-profile-meals-api
- baseURL: https://platform.fatsecret.com/rest
  baseurl_source: declared
  description: Search and retrieve recipes
  name: fatsecret Recipes API
  slug: fatsecret-recipes-api
- baseURL: https://platform.fatsecret.com/rest
  baseurl_source: declared
  description: Reference data for brands, categories, and exercises
  name: fatsecret Reference API
  slug: fatsecret-reference-api
- baseURL: https://platform.fatsecret.com/rest
  baseurl_source: declared
  description: User weight history
  name: fatsecret Weight Tracking API
  slug: fatsecret-weight-tracking-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: fatsecret Exercise Diary API
  slug: open-fatsecret-exercise-diary-api
- collection_type: open
  name: fatsecret Food Diary API
  slug: open-fatsecret-food-diary-api
- collection_type: open
  name: fatsecret Foods API
  slug: open-fatsecret-foods-api
- collection_type: open
  name: fatsecret Image Recognition API
  slug: open-fatsecret-image-recognition-api
- collection_type: open
  name: fatsecret Natural Language Processing API
  slug: open-fatsecret-natural-language-processing-api
- collection_type: open
  name: fatsecret Platform API
  slug: open-fatsecret-platform
- collection_type: open
  name: fatsecret Profile Foods API
  slug: open-fatsecret-profile-foods-api
- collection_type: open
  name: fatsecret Profile Meals API
  slug: open-fatsecret-profile-meals-api
- collection_type: open
  name: fatsecret Recipes API
  slug: open-fatsecret-recipes-api
- collection_type: open
  name: fatsecret Reference API
  slug: open-fatsecret-reference-api
- collection_type: open
  name: fatsecret Weight Tracking API
  slug: open-fatsecret-weight-tracking-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fatsecret-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fatsecret-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fatsecret-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fatsecret-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/fatsecret-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fatsecret-well-known.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/fatsecret-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fatsecret-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/fatsecret-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fatsecret-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fatsecret-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fatsecret-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fatsecret-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fatsecret-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fatsecret-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fatsecret-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fatsecret-finops.yml
- group: docs
  title: Spectral Rules
  type: Documentation
  url: rules/fatsecret-jsonschema-spectral-rules.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fatsecret-group
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fatsecret
- group: company
  title: ''
  type: Website
  url: https://platform.fatsecret.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.fatsecret.com/platform-api
- group: docs
  title: ''
  type: Documentation
  url: https://platform.fatsecret.com/platform-api
- group: docs
  title: ''
  type: APIReference
  url: https://platform.fatsecret.com/docs/guides
- group: start
  title: ''
  type: SignUp
  url: https://platform.fatsecret.com/register
- group: start
  title: ''
  type: Login
  url: https://platform.fatsecret.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://platform.fatsecret.com/api-editions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://platform.fatsecret.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://foods.fatsecret.com/Default.aspx?pa=priv&l=en
- group: operate
  title: ''
  type: Support
  url: https://groups.google.com/g/fatsecret-platform-api
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/fatsecret/workspace/fatsecret-public-apis/collection/25958240-f307c228-34ed-42bb-8866-79dae97523a6
- group: start
  title: ''
  type: Console
  url: https://platform.fatsecret.com/api-demo
- group: docs
  title: ''
  type: Guides
  url: https://platform.fatsecret.com/docs/guides
- group: company
  title: ''
  type: Blog
  url: https://blog.fatsecret.com/rss
created: '2025-03-01'
description: fatsecret is a global nutrition and wellness platform whose Platform API exposes a verified database of more than 2.3 million foods across 58 countries and 26 languages, plus recipes, exercises, image recognition, natural language processing, and user-scoped food diary, exercise diary, and weight tracking. The API is used by more than 50,000 developers and serves over 700 million calls per month. Bootstrapped and profitable since 2006, fatsecret has never raised venture funding.
finops:
- name: Fatsecret Finops
  service_category: API
  slug: fatsecret-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fatsecret.png
json_schemas:
- name: fatsecret Food Diary Entry
  property_count: 11
  slug: fatsecret-food-entry
- name: fatsecret Food
  property_count: 6
  slug: fatsecret-food
- name: fatsecret Recipe
  property_count: 13
  slug: fatsecret-recipe
layout: provider
modified: '2026-08-12'
name: fatsecret
nav: Providers
network: true
overview: 'fatsecret publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Exercise Diary API, Food Diary API, Foods API, and 7 more. Tagged areas include Artificial Intelligence, Barcode Scanning, Calories, Diets, and Image Recognition.


  The fatsecret catalog on APIs.io includes 1 Spectral governance ruleset.


  fatsecret''s developer surface includes authentication, sandbox, documentation, API reference, signup flow, pricing, support, and 28 more developer resources.'
plans:
- name: Fatsecret Plans Pricing
  plan_count: 3
  slug: fatsecret-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Fatsecret Rate Limits
  slug: fatsecret-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: fatsecret API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fatsecret-jsonschema-spectral-rules
scopes:
- name: Fatsecret Scopes
  scope_count: 7
  slug: fatsecret-scopes
  summary_line: 7 scopes · clientCredentials
score:
  band: strong
  composite: 59.7
  coverage:
    artifact_dirs: 26
    catalog_gap: 37.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 14.4
    contract_quality: 49.9
    developer_ergonomics: 54.2
    discoverability: 68.5
    governance: 14.4
    operational_transparency: 34.2
  previous_composite: 59.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 20.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 62.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fatsecret/refs/heads/main/screenshots/fatsecret-2026-06-20T181056.png
security:
- kind: authentication
  name: Fatsecret Authentication
  slug: fatsecret-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Fatsecret Domain Security
  slug: fatsecret-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fatsecret
tags:
- Artificial Intelligence
- Barcode Scanning
- Calories
- Diets
- Image Recognition
- Natural Language Processing
- Exercise
- Fitness
- Food Diary
- Health
- Macronutrients
- Nutrition
- Recipes
- Weight Tracking
website: https://platform.fatsecret.com/
---
