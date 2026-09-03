---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://recipe-api.com
  baseurl_source: declared
  description: Requires API key. No credit cost. Browse categories, cuisines, and dietary options.
  name: Recipe API Discovery API
  slug: recipe-api-discovery-api
- baseURL: https://recipe-api.com
  baseurl_source: declared
  description: The Image Generation API from Recipe API — 1 operation(s) for image generation.
  name: Recipe API Image Generation API
  slug: recipe-api-image-generation-api
- baseURL: https://recipe-api.com
  baseurl_source: declared
  description: Search ingredients free. Per-100g USDA nutrition by ID costs 1 credit.
  name: Recipe API Ingredients API
  slug: recipe-api-ingredients-api
- baseURL: https://recipe-api.com
  baseurl_source: declared
  description: No authentication required. Try `/api/v1/dinner` for a complete recipe example.
  name: Recipe API Public API
  slug: recipe-api-public-api
- baseURL: https://recipe-api.com
  baseurl_source: declared
  description: Browse recipes free. Full recipe detail costs 1 credit. Sample data shown inline.
  name: Recipe API Recipes API
  slug: recipe-api-recipes-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Recipe Discovery API
  slug: open-recipe-api-discovery-api
- collection_type: open
  name: Recipe Image Generation API
  slug: open-recipe-api-image-generation-api
- collection_type: open
  name: Recipe Ingredients API
  slug: open-recipe-api-ingredients-api
- collection_type: open
  name: Recipe Public API
  slug: open-recipe-api-public-api
- collection_type: open
  name: Recipe Recipes API
  slug: open-recipe-api-recipes-api
common:
- group: company
  title: ''
  type: Website
  url: https://recipe-api.com
- group: docs
  title: ''
  type: Documentation
  url: https://recipe-api.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://recipe-api.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://recipe-api.com/signup
- group: start
  title: ''
  type: Login
  url: https://recipe-api.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://recipe-api.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://recipe-api.com/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://recipe-api.com/llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/recipe-api-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/recipe-api-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/recipe-api-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/recipe-api-authentication.yml
created: '2026-08-03'
description: Recipe API is a B2B recipe and nutrition API providing structured recipes with comprehensive, USDA-backed nutrition data — 32 nutrients per recipe, structured preparation steps, and per-100g nutrition on individual ingredients. Beyond browsing and filtering an existing catalog by category, cuisine, dietary flag and macro, it will generate a new recipe with nutrition on demand, and generate food photography from a recipe. It positions itself as a lighter-weight alternative for developers who want clean recipe data without much setup, and publishes both an llms.txt and an official MCP server so that AI clients can use it directly. Self-serve from a free evaluation tier through to a paid scale tier, with a documented keyless quick-start call so a developer can try the API before signing up.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recipe-api.png
layout: provider
mcp_servers:
- description: An official Recipe API MCP server, documented for Claude and any MCP client. The JSON-RPC endpoint answers 401 rather than 404, so it exists and is auth-gated — the tool list could not be enumerated a
  name: Recipe API MCP Server
  slug: recipe-api-mcp-server
modified: '2026-08-03'
name: Recipe API
nav: Providers
network: true
overview: 'Recipe API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Image Generation API, Ingredients API, and 2 more. Tagged areas include Recipes, Food, Nutrition, Ingredients, and Data.


  Recipe API''s developer surface includes documentation, pricing, signup flow, authentication, and 8 more developer resources.'
plans:
- name: Recipe Api Plans
  plan_count: 4
  slug: recipe-api-plans
random_paper: 4
rate_limits:
- limit_count: 4
  name: Recipe Api Rate Limits
  slug: recipe-api-rate-limits
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 43.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recipe-api/refs/heads/main/screenshots/recipe-api-2026-08-17T081456.png
security:
- kind: authentication
  name: Recipe Api Authentication
  slug: recipe-api-authentication
  summary_line: 1 scheme
slug: recipe-api
tags:
- Recipes
- Food
- Nutrition
- Ingredients
- Data
- Generative AI
- MCP
- Agents
website: https://recipe-api.com
---
