---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Food Info Agentic Access
  operation_count: 8
  slug: food-info-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- description: The ApiV1 API from Food Info — 6 operation(s) for apiv1.
  name: Food Info API V1 API
  slug: food-info-apiv1-api
- description: The RecipesApi API from Food Info — 2 operation(s) for recipesapi.
  name: Food Info Recipes API API
  slug: food-info-recipesapi-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Food Info API V1 API
  slug: open-food-info-apiv1-api
- collection_type: open
  name: Food Info Recipes API API
  slug: open-food-info-recipesapi-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/food-info-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/food-info-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://food-info.org
- group: docs
  title: ''
  type: Documentation
  url: https://food-info.org/developer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://food-info.org/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://food-info.org/privacy-policy
- group: agent
  title: ''
  type: LlmsText
  url: https://food-info.org/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/food-info-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/food-info-plans.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/food-info-data-provenance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/food-info-conformance.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://food-info.org/developer
- group: operate
  title: ''
  type: Support
  url: https://food-info.org/contact
- group: agent
  title: ''
  type: WellKnown
  url: well-known/food-info-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/food-info-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/food-info-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://food-info.org/.well-known/security.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/food-info-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/food-info-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/food-info-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/food-info-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/food-info-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/food-info-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/food-info-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/food-info-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/food-info-examples.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/food-info-llms.txt
created: '2026-08-04'
description: Food Info serves harmonised nutrient data for reference foods over a versioned REST API. It merges six food-composition datasets — USDA FoodData Central, McCance & Widdowson's CoFID, ANSES Ciqual, DTU Frida, AUSNUT and Open Food Facts — into a single schema, so a caller can query nutrients across sources without reconciling each publisher's format. Endpoints cover food search, a full nutrient panel per food, a nutrient catalogue, reverse nutrient search for the richest and poorest reference foods, and recipe parsing and analysis that resolves raw ingredient lines into per-line nutrition. Authentication is an X-Api-Key header, with a free tier of 10 requests a minute and 100 a day. HTTPS only and CORS disabled, so it is built for server-to-server use. The underlying dataset carries a citable Zenodo DOI, which is unusual provenance for a commercial data API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/food-info.png
layout: provider
mcp_servers:
- description: CANDIDATE MCP tool surface derived from the eight operations in the published OpenAPI. Food Info does NOT operate an MCP server — this is an API Evangelist proposal showing what one would look like, n
  name: Food Info MCP Server
  slug: food-info-mcp-server
modified: '2026-08-04'
name: Food Info
nav: Providers
network: true
overview: 'Food Info publishes 2 APIs on the [APIs.io](https://apis.io/) network: API V1 API and Recipes API API. Tagged areas include Nutrition, Food, Food Composition, Nutrients, and Data.


  Food Info''s developer surface includes documentation, authentication, support, code examples, and 24 more developer resources.'
plans:
- name: Food Info Plans
  plan_count: 0
  slug: food-info-plans
random_paper: 15
rate_limits:
- limit_count: 2
  name: Food Info Rate Limits
  slug: food-info-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 57.1
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Food Info Authentication
  slug: food-info-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Food Info Domain Security
  slug: food-info-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Food Info Vulnerability Disclosure
  slug: food-info-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: food-info
tags:
- Nutrition
- Food
- Food Composition
- Nutrients
- Data
- Open Data
- Dietetics
- Recipes
- Health
- Research
website: https://food-info.org
---
