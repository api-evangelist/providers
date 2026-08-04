---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.5
  scored_at: '2026-08-04'
api_count: 1
apis:
- description: B2B Recipe API providing structured recipes with comprehensive nutrition data.
  name: Recipe API
  slug: recipe-api
artifact_total: 5
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
- description: ''
  name: recipe-api-mcp.yml
  slug: recipe-api-mcpyml
modified: '2026-08-03'
name: Recipe API
nav: Providers
network: true
overview: 'Recipe API publishes 1 API on the [APIs.io](https://apis.io/) network: Recipe API. Tagged areas include Recipes, Food, Nutrition, Ingredients, and Data.


  Recipe API''s developer surface includes documentation, pricing, signup flow, authentication, and 8 more developer resources.'
plans:
- name: Recipe Api Plans
  plan_count: 4
  slug: recipe-api-plans
random_paper: 31
rate_limits:
- limit_count: 4
  name: Recipe Api Rate Limits
  slug: recipe-api-rate-limits
score:
  band: developing
  composite: 48.5
  facets:
    commercial_clarity: 76.3
    contract_quality: 63.6
    developer_ergonomics: 28.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 31.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-04'
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
