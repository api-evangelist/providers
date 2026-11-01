---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tinyplates Dev Agentic Access
  operation_count: 12
  slug: tinyplates-dev-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://api.tinyplates.dev
  baseurl_source: declared
  description: The health API from tinyplates-dev — 1 operation(s) for health.
  name: tinyplates-dev Health API
  slug: tinyplates-dev-health-api
- baseURL: https://api.tinyplates.dev
  baseurl_source: declared
  description: The ingredients API from tinyplates-dev — 2 operation(s) for ingredients.
  name: tinyplates-dev Ingredients API
  slug: tinyplates-dev-ingredients-api
- baseURL: https://api.tinyplates.dev
  baseurl_source: declared
  description: The pantry API from tinyplates-dev — 1 operation(s) for pantry.
  name: tinyplates-dev Pantry API
  slug: tinyplates-dev-pantry-api
- baseURL: https://api.tinyplates.dev
  baseurl_source: declared
  description: The popular API from tinyplates-dev — 1 operation(s) for popular.
  name: tinyplates-dev Popular API
  slug: tinyplates-dev-popular-api
- baseURL: https://api.tinyplates.dev
  baseurl_source: declared
  description: The recipes API from tinyplates-dev — 2 operation(s) for recipes.
  name: tinyplates-dev Recipes API
  slug: tinyplates-dev-recipes-api
- baseURL: https://api.tinyplates.dev
  baseurl_source: declared
  description: The root API from tinyplates-dev — 1 operation(s) for root.
  name: tinyplates-dev Root API
  slug: tinyplates-dev-root-api
- baseURL: https://api.tinyplates.dev
  baseurl_source: declared
  description: The search API from tinyplates-dev — 1 operation(s) for search.
  name: tinyplates-dev Search API
  slug: tinyplates-dev-search-api
- baseURL: https://api.tinyplates.dev
  baseurl_source: declared
  description: The shoppingList API from tinyplates-dev — 1 operation(s) for shoppinglist.
  name: tinyplates-dev Shopping List API
  slug: tinyplates-dev-shoppinglist-api
- baseURL: https://api.tinyplates.dev
  baseurl_source: declared
  description: The status API from tinyplates-dev — 1 operation(s) for status.
  name: tinyplates-dev Status API
  slug: tinyplates-dev-status-api
- baseURL: https://api.tinyplates.dev
  baseurl_source: declared
  description: The substitutions API from tinyplates-dev — 1 operation(s) for substitutions.
  name: tinyplates-dev Substitutions API
  slug: tinyplates-dev-substitutions-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/tinyplates-dev/agentic-access/tinyplates-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tinyplates-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/tinyplates-dev/rate-limits/tinyplates-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tinyplates-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tinyplates-dev/plans/tinyplates-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tinyplates-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tinyplates-dev/rules/tinyplates-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/tinyplates-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/tinyplates-dev/json-ld/tinyplates-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tinyplates-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/tinyplates-dev/vocabulary/tinyplates-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tinyplates-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tinyplates-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tinyplates-dev/data-model/tinyplates-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tinyplates-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/tinyplates-dev/changelog/tinyplates-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tinyplates-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/tinyplates-dev/authentication/tinyplates-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tinyplates-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/tinyplates-dev/lifecycle/tinyplates-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tinyplates-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tinyplates-dev/errors/tinyplates-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tinyplates-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tinyplates-dev/conformance/tinyplates-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tinyplates-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tinyplates-dev/llms/tinyplates-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tinyplates-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/tinyplates-dev/well-known/tinyplates-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tinyplates-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/tinyplates-dev/hosts/tinyplates-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tinyplates-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/tinyplates-dev/vendors/tinyplates-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tinyplates-dev-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.tinyplates.dev${path}?${new
- group: auth
  href: https://artifacts.apis.io/tinyplates-dev/security/tinyplates-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tinyplates-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tinyplates.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://www.tinyplates.dev/docs/api/search-recipes
- group: company
  title: ''
  type: Blog
  url: https://www.tinyplates.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.tinyplates.dev/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://www.tinyplates.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tinyplates.dev/docs/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Artmann
- group: start
  title: ''
  type: Login
  url: https://www.tinyplates.dev/sign-in
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tinyplates.dev/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tinyplates.dev/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.tinyplates.dev/sign-up
- group: operate
  title: ''
  type: StatusPage
  url: https://www.tinyplates.dev/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tinyplates.dev/terms
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.tinyplates.dev/openapi.json
  - status: 401
    url: https://api.tinyplates.dev/mcp
  - status: 200
    url: https://tinyplates.dev/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Tiny Plates provides a free recipe API that transforms recipes from across the web into structured, consistent data. Developers can use semantic search, ingredient parsing, and step-by-step cooking instructions to build apps and agents. The service offers tiered pricing, comprehensive documentation, and open-source SDKs.
image: https://www.tinyplates.dev/og.png
json_schemas:
- name: NutritionTotals
  property_count: 4
  slug: tinyplates-dev-nutrition-totals
- name: PantryRecipe
  property_count: 30
  slug: tinyplates-dev-pantry-recipe
- name: PopularRecipe
  property_count: 27
  slug: tinyplates-dev-popular-recipe
- name: Recipe
  property_count: 26
  slug: tinyplates-dev-recipe
- name: SearchResult
  property_count: 27
  slug: tinyplates-dev-search-result
- name: ShoppingItem
  property_count: 7
  slug: tinyplates-dev-shopping-item
jsonld:
- class_count: 45
  name: Tinyplates Dev Context
  property_count: 132
  slug: tinyplates-dev-context
layout: provider
modified: '2026-10-31'
name: tinyplates-dev
nav: Providers
network: true
overview: 'tinyplates-dev publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Ingredients API, Pantry API, and 7 more. Tagged areas include API, Food, Recipes, Search, and Developer.


  The tinyplates-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tinyplates-dev''s developer surface includes changelog, authentication, API reference, engineering blog, documentation, getting-started guide, pricing, and 25 more developer resources.'
plans:
- name: Tinyplates Dev Plans Pricing
  plan_count: 3
  slug: tinyplates-dev-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Tinyplates Dev Rate Limits
  slug: tinyplates-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: tinyplates-dev API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 2
  slug: tinyplates-dev-rules
score:
  band: exemplar
  composite: 67.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 59.2
    developer_ergonomics: 58.8
    discoverability: 66.1
    operational_transparency: 65.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tinyplates Dev Authentication
  slug: tinyplates-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tinyplates Dev Domain Security
  slug: tinyplates-dev-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: tinyplates-dev-all
  slug: tinyplates-dev-all
slug: tinyplates-dev
tags:
- API
- Food
- Recipes
- Search
- Developer
website: https://tinyplates.dev/
---
