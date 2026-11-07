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
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://secure.alterestate.com/api/v1
  baseurl_source: declared
  description: Company agents
  name: AlterEstate Agents API
  slug: alterestate-agents-api
- baseURL: https://secure.alterestate.com/api/v1
  baseurl_source: declared
  description: Real-estate projects, their buildings and units
  name: AlterEstate Developments API
  slug: alterestate-developments-api
- baseURL: https://secure.alterestate.com/api/v1
  baseurl_source: declared
  description: Inbound lead submission into the CRM
  name: AlterEstate Leads API
  slug: alterestate-leads-api
- baseURL: https://secure.alterestate.com/api/v1
  baseurl_source: declared
  description: Cities, sectors and provinces
  name: AlterEstate Locations API
  slug: alterestate-locations-api
- baseURL: https://secure.alterestate.com/api/v1
  baseurl_source: declared
  description: Property listings and detail views
  name: AlterEstate Properties API
  slug: alterestate-properties-api
artifact_total: 18
collections:
- collection_type: open
  name: AlterEstate Agents API
  slug: open-alterestate-agents-api
- collection_type: open
  name: AlterEstate Agents Developments API
  slug: open-alterestate-developments-api
- collection_type: open
  name: AlterEstate Agents Leads API
  slug: open-alterestate-leads-api
- collection_type: open
  name: AlterEstate Agents Locations API
  slug: open-alterestate-locations-api
- collection_type: open
  name: AlterEstate Agents Properties API
  slug: open-alterestate-properties-api
common:
- group: commercial
  href: https://artifacts.apis.io/alterestate/plans/alterestate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alterestate-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.alterestate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.alterestate.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.alterestate.com/properties
- group: auth
  href: https://artifacts.apis.io/alterestate/authentication/alterestate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alterestate-authentication.yml
- group: auth
  href: https://artifacts.apis.io/alterestate/scopes/alterestate-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/alterestate-scopes.yml
- group: agent
  href: https://artifacts.apis.io/alterestate/mcp/alterestate-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alterestate-mcp.yml
- group: agent
  href: https://artifacts.apis.io/alterestate/well-known/alterestate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alterestate-well-known.yml
- group: agent
  href: https://artifacts.apis.io/alterestate/llms/alterestate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alterestate-llms.txt
- group: other
  href: https://artifacts.apis.io/alterestate/overlays/alterestate-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/alterestate-overlay.yaml
- group: design
  href: https://artifacts.apis.io/alterestate/conventions/alterestate-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alterestate-conventions.yml
- group: design
  href: https://artifacts.apis.io/alterestate/errors/alterestate-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alterestate-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alterestate/lifecycle/alterestate-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/alterestate-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/alterestate/conformance/alterestate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alterestate-conformance.yml
- group: design
  href: https://artifacts.apis.io/alterestate/data-model/alterestate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alterestate-data-model.yml
- group: agent
  href: https://artifacts.apis.io/alterestate/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/alterestate/security/alterestate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alterestate-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://alterestate.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://ayuda.alterestate.com
- group: operate
  title: ''
  type: Support
  url: https://ayuda.alterestate.com
- group: commercial
  title: ''
  type: Pricing
  url: https://alterestate.com/precios
- group: start
  title: ''
  type: SignUp
  url: https://app.alterestate.com/registro
- group: start
  title: ''
  type: Login
  url: https://app.alterestate.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alterestate.com/terminos-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alterestate.com/politica-de-privacidad
- group: company
  title: ''
  type: Website
  url: https://alterestate.com
created: '2026-07-17'
description: AlterEstate is the leading real-estate CRM SaaS for agents across Latin America, serving more than 5,000 agents in seven countries. Its platform centralizes leads, properties and sales in a visual funnel and adds a WhatsApp-integrated AI assistant (Brik), a no-code website builder, a unified inbox, an inter-agency inventory network, and a marketing hub. AlterEstate exposes a public REST API at secure.alterestate.com/api/v1 covering property listings (with backend currency conversion across USD, DOP, MXN, COP, CRC, GTQ and PEN), project developments (buildings and units), agents, geographic locations, and inbound lead submission, plus an OAuth-protected hosted MCP server for agentic access. Backed by 500 Global.
image: https://alterestate.com/favicon.ico
layout: provider
mcp_servers:
- description: Official AlterEstate hosted MCP server (branded "Brik"/alterai). Discovered via the RFC 9728 protected-resource document. Requires an OAuth 2.0 bearer token (scope "mcp"); an unauthenticated POST retu
  name: AlterEstate MCP Server
  slug: alterestate-alterai
modified: '2026-07-17'
name: AlterEstate
nav: Providers
network: true
overview: 'AlterEstate publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Developments API, Leads API, and 2 more. Tagged areas include Company, Real Estate, CRM, Property Management, and Lead Management.


  The AlterEstate catalog on APIs.io includes 1 Spectral governance ruleset.


  AlterEstate''s developer surface includes documentation, API reference, authentication, engineering blog, support, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Alterestate Plans Pricing
  plan_count: 2
  slug: alterestate-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: AlterEstate API Rules
  rule_count: 66
  severity_counts:
    error: 64
    hint: 0
    info: 1
    warn: 1
  slug: alterestate-rules
scopes:
- name: Alterestate Scopes
  scope_count: 1
  slug: alterestate-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 59.2
    contract_governance: 18.2
    contract_quality: 13.9
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 38.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/alterestate/alterestate-2026-07-25T195823.png
security:
- kind: authentication
  name: Alterestate Authentication
  slug: alterestate-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Alterestate Domain Security
  slug: alterestate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Browse AlterEstate property listings and project units
  slug: alterestate-browse-listings
- name: Capture a real-estate lead into AlterEstate
  slug: alterestate-capture-lead
slug: alterestate
tags:
- Company
- Real Estate
- CRM
- Property Management
- Lead Management
- Latin America
- Software-as-a-Service
- Artificial Intelligence
- MCP
website: https://alterestate.com
---
