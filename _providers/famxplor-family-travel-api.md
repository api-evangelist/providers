---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Famxplor Family Travel Api Agentic Access
  operation_count: 4
  slug: famxplor-family-travel-api-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.famxplor.com
  baseurl_source: declared
  description: The Activities API from Famxplor Family Travel API — 1 operation(s) for activities.
  name: Famxplor Family Travel API Activities API
  slug: famxplor-family-travel-api-activities-api
- baseURL: https://api.famxplor.com
  baseurl_source: declared
  description: The Nearest Activities API from Famxplor Family Travel API — 1 operation(s) for nearest activities.
  name: Famxplor Family Travel API Nearest Activities API
  slug: famxplor-family-travel-api-nearest-activities-api
- baseURL: https://api.famxplor.com
  baseurl_source: declared
  description: The Nearest Posts API from Famxplor Family Travel API — 1 operation(s) for nearest posts.
  name: Famxplor Family Travel API Nearest Posts API
  slug: famxplor-family-travel-api-nearest-posts-api
- baseURL: https://api.famxplor.com
  baseurl_source: declared
  description: The Travel Time API from Famxplor Family Travel API — 1 operation(s) for travel time.
  name: Famxplor Family Travel API Travel Time API
  slug: famxplor-family-travel-api-travel-time-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/famxplor-family-travel-api/agentic-access/famxplor-family-travel-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/famxplor-family-travel-api-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/famxplor-family-travel-api/authentication/famxplor-family-travel-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/famxplor-family-travel-api-authentication.yml
- group: auth
  href: https://artifacts.apis.io/famxplor-family-travel-api/security/famxplor-family-travel-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/famxplor-family-travel-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://famxplor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://famxplor.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://famxplor.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://famxplor.com/login
- group: company
  title: ''
  type: Blog
  url: https://famxplor.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://famxplor.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://famxplor.com/legal/terms-of-service/
- group: docs
  href: https://artifacts.apis.io/famxplor-family-travel-api/openapi/famxplor-family-travel-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/famxplor-family-travel-api-openapi.yml
- group: other
  title: ''
  type: APIsYAML
  url: https://famxplor.com/apis.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.famxplor.com/redoc
- group: agent
  href: https://artifacts.apis.io/famxplor-family-travel-api/mcp/famxplor-family-travel-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/famxplor-family-travel-api-mcp.yml
- group: build
  href: https://artifacts.apis.io/famxplor-family-travel-api/mcp/famxplor-family-travel-api-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/famxplor-family-travel-api-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/famxplor-family-travel-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/famxplor-family-travel-api/conventions/famxplor-family-travel-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/famxplor-family-travel-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/famxplor-family-travel-api/errors/famxplor-family-travel-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/famxplor-family-travel-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/famxplor-family-travel-api/lifecycle/famxplor-family-travel-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/famxplor-family-travel-api-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/famxplor-family-travel-api/conformance/famxplor-family-travel-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/famxplor-family-travel-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/famxplor-family-travel-api/data-model/famxplor-family-travel-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/famxplor-family-travel-api-data-model.yml
- group: build
  href: https://artifacts.apis.io/famxplor-family-travel-api/packages/famxplor-family-travel-api-packages.yml
  title: ''
  type: Packages
  url: packages/famxplor-family-travel-api-packages.yml
- group: build
  href: https://artifacts.apis.io/famxplor-family-travel-api/examples/famxplor-family-travel-api-examples.yml
  title: ''
  type: Examples
  url: examples/famxplor-family-travel-api-examples.yml
- group: other
  href: https://artifacts.apis.io/famxplor-family-travel-api/overlays/famxplor-family-travel-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/famxplor-family-travel-api-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/famxplor-family-travel-api/llms/famxplor-family-travel-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/famxplor-family-travel-api-llms.txt
- group: operate
  href: https://artifacts.apis.io/famxplor-family-travel-api/rate-limits/famxplor-family-travel-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/famxplor-family-travel-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/famxplor-family-travel-api/plans/famxplor-family-travel-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/famxplor-family-travel-api-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/famxplor-family-travel-api/finops/famxplor-family-travel-api-finops.yml
  title: ''
  type: FinOps
  url: finops/famxplor-family-travel-api-finops.yml
created: '2024-12-18'
description: The First API 100% Dedicated to Family Travel. Designed for developers, travel apps, and businesses, the Famxplor API delivers personalized, family-focused recommendations tested and loved by real families. Seamlessly integrate to provide location-based activities, global travel ideas, and engaging content that enhances user experiences and engagement. Famxplor offers tiered pricing from Starter ($4.99/mo) to Enterprise (custom), with a 14-day free trial.
finops:
- has_sources: true
  method: derived
  name: Famxplor Family Travel Api Finops
  primary_unit: api calls
  service_category: ''
  slug: famxplor-family-travel-api-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/famxplor-family-travel-api.png
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 1 tool listed.
  name: Famxplor Family Travel API MCP Server
  slug: famxplor
modified: '2026-09-07'
name: Famxplor Family Travel API
nav: Providers
network: true
overview: 'Famxplor Family Travel API publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Nearest Activities API, Nearest Posts API, and 1 more. Tagged areas include Activities, Family, Travel, Artificial Intelligence, and MCP.


  The Famxplor Family Travel API catalog on APIs.io includes 1 Spectral governance ruleset.


  Famxplor Family Travel API''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, API reference, code examples, and 21 more developer resources.'
plans:
- name: Famxplor Family Travel Api Plans Pricing
  plan_count: 4
  slug: famxplor-family-travel-api-plans-pricing
- name: Famxplor Family Travel Api Price Estimates
  plan_count: 0
  slug: famxplor-family-travel-api-price-estimates
random_paper: 2
rate_limits:
- limit_count: 4
  name: Famxplor Family Travel Api Rate Limits
  slug: famxplor-family-travel-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Famxplor Family Travel API API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: famxplor-family-travel-api-rules
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 57.1
    developer_ergonomics: 32.7
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/famxplor-family-travel-api/famxplor-family-travel-api-2026-06-20T181032.png
security:
- kind: authentication
  name: Famxplor Family Travel Api Authentication
  slug: famxplor-family-travel-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Famxplor Family Travel Api Domain Security
  slug: famxplor-family-travel-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Find family activities near a place
  slug: famxplor-family-travel-api-find-family-activities
- name: Plan a family route between stops
  slug: famxplor-family-travel-api-plan-a-family-route
- name: Source real family testimony for a destination
  slug: famxplor-family-travel-api-source-family-testimony
slug: famxplor-family-travel-api
tags:
- Activities
- Family
- Travel
- Artificial Intelligence
- MCP
website: https://famxplor.com/
---
