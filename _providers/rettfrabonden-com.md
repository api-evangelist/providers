---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Rettfrabonden Com Agentic Access
  operation_count: 14
  slug: rettfrabonden-com-agentic-access
  summary_line: 14 operations · 5 acting
api_count: 2
apis:
- description: Remote MCP server (Streamable HTTP, protocol 2025-06-18 negotiated) at https://rettfrabonden.com/mcp with 15 tools — search, discover, producer info, umbrella organisations, Bondens marked events, geo
  name: Rett fra Bonden MCP Server
  slug: rett-fra-bonden-mcp-server
- description: A2A JSON-RPC 2.0 endpoint at https://rettfrabonden.com/a2a (message/send, tasks/get, tasks/list, agent/authenticatedExtendedCard) described by an EdDSA-signed agent card served at /.well-known/agent-c
  name: Rett fra Bonden A2A Agent
  slug: rett-fra-bonden-a2a-agent
- baseURL: https://rettfrabonden.com/api/marketplace
  baseurl_source: declared
  description: The A2a API from Rett fra Bonden — 1 operation(s) for a2a.
  name: Rett fra Bonden A2a API
  slug: rettfrabonden-com-a2a-api
- baseURL: https://rettfrabonden.com/api/marketplace
  baseurl_source: declared
  description: The Marketplace API from Rett fra Bonden — 8 operation(s) for marketplace.
  name: Rett fra Bonden Marketplace API
  slug: rettfrabonden-com-marketplace-api
- baseURL: https://rettfrabonden.com/api/marketplace
  baseurl_source: declared
  description: The Mcp API from Rett fra Bonden — 1 operation(s) for mcp.
  name: Rett fra Bonden MCP API
  slug: rettfrabonden-com-mcp-api
- baseURL: https://rettfrabonden.com/api/marketplace
  baseurl_source: declared
  description: The Stats API from Rett fra Bonden — 1 operation(s) for stats.
  name: Rett fra Bonden Stats API
  slug: rettfrabonden-com-stats-api
- baseURL: https://rettfrabonden.com/api/marketplace
  baseurl_source: declared
  description: The .well Known API from Rett fra Bonden — 1 operation(s) for .well known.
  name: Rett fra Bonden .well Known API
  slug: rettfrabonden-com-well-known-api
artifact_total: 18
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://rettfrabonden.com/llms.txt
- group: company
  title: ''
  type: Website
  url: https://rettfrabonden.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rettfrabonden.com/teknologi
- group: start
  title: ''
  type: GettingStarted
  url: https://rettfrabonden.com/teknologi#mcp-oppsett
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/slookisen/lokal#readme
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/slookisen
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/slookisen/lokal
- group: operate
  title: ''
  type: Support
  url: https://github.com/slookisen/lokal/issues
- group: operate
  title: ''
  type: Contact
  url: https://rettfrabonden.com/kontakt
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/slookisen/lokal/blob/main/LOKAL-ROADMAP-V4.md
- group: start
  title: ''
  type: SignUp
  url: https://rettfrabonden.com/selger
- group: start
  title: ''
  type: Login
  url: https://rettfrabonden.com/selger
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rettfrabonden.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rettfrabonden.com/personvern
- group: docs
  href: https://artifacts.apis.io/rettfrabonden-com/openapi/rettfrabonden-com-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/rettfrabonden-com-openapi.yml
- group: agent
  href: https://artifacts.apis.io/rettfrabonden-com/mcp/rettfrabonden-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rettfrabonden-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/rettfrabonden-com/mcp/rettfrabonden-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/rettfrabonden-com-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/rettfrabonden-com/a2a/rettfrabonden-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/rettfrabonden-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/rettfrabonden-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/rettfrabonden-com/llms/rettfrabonden-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rettfrabonden-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://rettfrabonden.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/rettfrabonden-com/well-known/rettfrabonden-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rettfrabonden-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/rettfrabonden-com/well-known/rettfrabonden-com-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/rettfrabonden-com-api-catalog.json
- group: other
  href: https://artifacts.apis.io/rettfrabonden-com/well-known/rettfrabonden-com-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/rettfrabonden-com-robots.txt
- group: build
  href: https://artifacts.apis.io/rettfrabonden-com/packages/rettfrabonden-com-packages.yml
  title: ''
  type: Packages
  url: packages/rettfrabonden-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/rettfrabonden-com/authentication/rettfrabonden-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rettfrabonden-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/rettfrabonden-com/conventions/rettfrabonden-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rettfrabonden-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/rettfrabonden-com/errors/rettfrabonden-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rettfrabonden-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rettfrabonden-com/data-model/rettfrabonden-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rettfrabonden-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/rettfrabonden-com/rate-limits/rettfrabonden-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rettfrabonden-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/rettfrabonden-com/plans/rettfrabonden-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rettfrabonden-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/rettfrabonden-com/lifecycle/rettfrabonden-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rettfrabonden-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/rettfrabonden-com/conformance/rettfrabonden-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rettfrabonden-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/rettfrabonden-com/security/rettfrabonden-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rettfrabonden-com-domain-security.yml
- group: other
  href: https://artifacts.apis.io/rettfrabonden-com/overlays/rettfrabonden-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rettfrabonden-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/rettfrabonden-com/agentic-access/rettfrabonden-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rettfrabonden-com-agentic-access.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://rettfrabonden.com/personvern
- group: other
  title: ''
  type: DataResidency
  url: https://rettfrabonden.com/personvern
- group: other
  title: ''
  type: Subprocessors
  url: https://rettfrabonden.com/personvern
created: '2026-09-19'
description: 'Rett fra Bonden (rettfrabonden.com) is an open, non-profit discovery layer for local food in Norway — a registry of 1,900+ farms, farm shops, REKO rings, farmers'' markets and cooperatives that is built to be read by AI agents first. It exposes the same producer catalogue through three protocols: a REST API (natural-language and structured search, producer detail, geocoding, an ACP-conformant product feed), a remote MCP server at /mcp with 15 tools including an anonymous shopping-cart and pickup-order flow, and an A2A JSON-RPC endpoint at /a2a described by a signed agent card at /.well-known/agent-card.json. Reads are open without a key; producer registration requires an X-API-Key issued on registration. The code is MIT-licensed at github.com/slookisen/lokal and the platform is operated in Norway by Daniel Fredriksen.'
finops:
- has_sources: true
  method: derived
  name: Rettfrabonden Com Finops
  primary_unit: ''
  service_category: ''
  slug: rettfrabonden-com-finops
  template: true
image: https://rettfrabonden.com/logo-512.png
layout: provider
mcp_servers:
- description: 'Rett fra Bonden operates a remote MCP server at https://rettfrabonden.com/mcp (Streamable HTTP, stateful sessions) that answers initialize and tools/list anonymously and exposes FIFTEEN tools and two '
  name: Rett fra Bonden MCP Server
  slug: rettfrabonden-com-mcp-yml
modified: '2026-09-19'
name: Rett fra Bonden
nav: Providers
network: true
overview: 'Rett fra Bonden publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Marketplace API, MCP API, and 4 more. Tagged areas include Local Food, Agriculture, Food, Marketplace, and Directory.


  The Rett fra Bonden catalog on APIs.io includes 1 Spectral governance ruleset.


  Rett fra Bonden''s developer surface includes pricing, documentation, getting-started guide, API reference, support, signup flow, authentication, and 32 more developer resources.'
plans:
- name: Rettfrabonden Com Plans Pricing
  plan_count: 0
  slug: rettfrabonden-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 6
  name: Rettfrabonden Com Rate Limits
  slug: rettfrabonden-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Rett fra Bonden API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: rettfrabonden-com-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 22.4
    contract_governance: 31.8
    contract_quality: 49.5
    developer_ergonomics: 35.7
    discoverability: 75.0
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - norway
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 80.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/rettfrabonden-com/rettfrabonden-com-2026-10-11T125158.png
security:
- kind: authentication
  name: Rettfrabonden Com Authentication
  slug: rettfrabonden-com-authentication
  summary_line: apiKey/none · 4 schemes
- kind: domain-security
  name: Rettfrabonden Com Domain Security
  slug: rettfrabonden-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Find local producers near a Norwegian place
  slug: rettfrabonden-com-find-local-producers
- name: Answer market-day and certification questions
  slug: rettfrabonden-com-markets-and-certifications
- name: Turn a shopping list into pickup orders
  slug: rettfrabonden-com-shopping-list-to-pickup-order
slug: rettfrabonden-com
tags:
- Local Food
- Agriculture
- Food
- Marketplace
- Directory
- Search
- Geolocation
- A2A
- MCP
- Norway
- Open Source
- Company
website: https://rettfrabonden.com/
---
