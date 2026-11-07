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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 2
  name: Tako Agentic Access
  operation_count: 13
  slug: tako-agentic-access
  summary_line: 13 operations · 5 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://tako.com/api
  baseurl_source: declared
  description: The agent API from Tako — 4 operation(s) for agent.
  name: Tako Agent API
  slug: tako-agent-api
- baseURL: https://tako.com/api
  baseurl_source: declared
  description: The tako API from Tako — 7 operation(s) for tako.
  name: Tako API
  slug: tako-tako-api
artifact_total: 16
collections:
- collection_type: open
  name: Knowledge Search agent API
  slug: open-tako-agent-api
- collection_type: open
  name: Knowledge Search agent tako API
  slug: open-tako-tako-api
common:
- group: commercial
  href: https://artifacts.apis.io/tako/plans/tako-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tako-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.tako.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tako.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tako.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tako.com/api-reference/search-v3
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tako.com/documentation/getting-started/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://tako.com/console/api-keys
- group: commercial
  title: ''
  type: Pricing
  url: https://tako.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://tako.com/blog
- group: other
  title: ''
  type: Playground
  url: https://tako.com/playground
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tako.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tako.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://docs.tako.com
- group: agent
  href: https://artifacts.apis.io/tako/llms/tako-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tako-llms.txt
- group: agent
  href: https://artifacts.apis.io/tako/mcp/tako-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tako-mcp.yml
- group: build
  href: https://artifacts.apis.io/tako/packages/tako-packages.yml
  title: ''
  type: Packages
  url: packages/tako-packages.yml
- group: build
  href: https://artifacts.apis.io/tako/packages/tako-packages.yml
  title: ''
  type: SDKs
  url: packages/tako-packages.yml
- group: auth
  href: https://artifacts.apis.io/tako/authentication/tako-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tako-authentication.yml
- group: design
  href: https://artifacts.apis.io/tako/errors/tako-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tako-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tako/conventions/tako-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tako-conventions.yml
- group: operate
  href: https://artifacts.apis.io/tako/rate-limits/tako-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tako-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tako/finops/tako-finops.yml
  title: ''
  type: FinOps
  url: finops/tako-finops.yml
- group: design
  href: https://artifacts.apis.io/tako/lifecycle/tako-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tako-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tako/conformance/tako-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tako-conformance.yml
- group: design
  href: https://artifacts.apis.io/tako/data-model/tako-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tako-data-model.yml
- group: other
  href: https://artifacts.apis.io/tako/overlays/tako-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tako-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/tako/components/tako-components.yml
  title: ''
  type: Components
  url: components/tako-components.yml
- group: agent
  href: https://artifacts.apis.io/tako/well-known/tako-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tako-well-known.yml
- group: other
  href: https://artifacts.apis.io/tako/well-known/tako-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/tako-api-catalog.json
- group: auth
  href: https://artifacts.apis.io/tako/security/tako-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tako-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/tako/agentic-access/tako-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tako-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/tako/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tako is an AI answer-engine API for authoritative, source-grounded data. It serves live financial, macroeconomic, and company data as cited answers, structured knowledge cards (charts, tables, maps), and embeddable visualizations for agents and applications. Developers build with four core APIs — Search (fast structured knowledge cards with no LLM in the loop), Answer (a single written, cited response), Contents (the exact numbers behind a card, as CSV), and Agent (asynchronous deep research runs) — plus a Data Graph for discovering what data exists, and Thin-Viz for turning your own data into embeddable Tako cards. Tako pulls from authoritative government, academic, think-tank, and licensed providers (S&P Global, SimilarWeb, YouGov, NOAA) — not scraped web content. It publishes an OpenAPI 3.1 spec, an official hosted MCP server, Python and TypeScript SDKs, an installable Agent Skill, an llms.txt, a Machine Payments Protocol surface, and emphasizes zero data retention, SOC 2
  compliance, and guaranteed SLAs. Surfaced as a portfolio company of Ribbit Capital.
finops:
- has_sources: true
  method: searched
  name: Tako Finops
  primary_unit: ''
  service_category: ''
  slug: tako-finops
  template: false
image: https://tako.com/apple-touch-icon
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.tako.com over HTTP; 5 tools listed.
  name: Tako MCP Server
  slug: tako
modified: '2026-09-16'
name: Tako
nav: Providers
network: true
overview: 'Tako publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, and 1 more. Tagged areas include Company, Artificial Intelligence, Data, Search, and Answer Engine.


  The Tako catalog on APIs.io includes 1 Spectral governance ruleset.


  Tako''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 25 more developer resources.'
plans:
- name: Tako Plans Pricing
  plan_count: 6
  slug: tako-plans-pricing
- name: Tako Price Estimates
  plan_count: 0
  slug: tako-price-estimates
random_paper: 23
rate_limits:
- limit_count: 1
  name: Tako Rate Limits
  slug: tako-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Tako API Rules
  rule_count: 54
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 3
  slug: tako-rules
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 75.0
    discoverability: 75.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
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
screenshot: https://apis.io/screenshots/tako/tako-2026-08-17T082243.png
security:
- kind: authentication
  name: Tako Authentication
  slug: tako-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tako Domain Security
  slug: tako-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: tako-agent-deep-research
  slug: tako-agent-deep-research
- name: tako-answer-with-data
  slug: tako-answer-with-data
- name: tako-graph-agent
  slug: tako-graph-agent
slug: tako
tags:
- Company
- Artificial Intelligence
- Data
- Search
- Answer Engine
- Financial Data
- Knowledge Graph
- Agents
- MCP
- Data Visualization
website: https://www.tako.com/
---
