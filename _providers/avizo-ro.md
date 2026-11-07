---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Avizo Ro Agentic Access
  operation_count: 1
  slug: avizo-ro-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Read access to tracked items (documents, authorizations, deadlines) via a single endpoint.
  name: Avizo Public API
  slug: avizo-public-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/avizo-ro/agentic-access/avizo-ro-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/avizo-ro-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/avizo-ro/rate-limits/avizo-ro-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/avizo-ro-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/avizo-ro/plans/avizo-ro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avizo-ro-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/avizo-ro/rules/avizo-ro-rules.yml
  title: ''
  type: Spectral
  url: rules/avizo-ro-rules.yml
- group: design
  href: https://artifacts.apis.io/avizo-ro/json-ld/avizo-ro-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/avizo-ro-context.jsonld
- group: design
  href: https://artifacts.apis.io/avizo-ro/vocabulary/avizo-ro-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avizo-ro-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/avizo-ro/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/avizo-ro/data-model/avizo-ro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avizo-ro-data-model.yml
- group: auth
  href: https://artifacts.apis.io/avizo-ro/authentication/avizo-ro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avizo-ro-authentication.yml
- group: auth
  href: https://artifacts.apis.io/avizo-ro/scopes/avizo-ro-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/avizo-ro-scopes.yml
- group: operate
  href: https://artifacts.apis.io/avizo-ro/lifecycle/avizo-ro-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/avizo-ro-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/avizo-ro/lifecycle/avizo-ro-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/avizo-ro-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/avizo-ro/errors/avizo-ro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/avizo-ro-problem-types.yml
- group: design
  href: https://artifacts.apis.io/avizo-ro/conformance/avizo-ro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avizo-ro-conformance.yml
- group: agent
  href: https://artifacts.apis.io/avizo-ro/llms/avizo-ro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avizo-ro-llms.txt
- group: build
  href: https://artifacts.apis.io/avizo-ro/mcp/avizo-ro-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/avizo-ro-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/avizo-ro/mcp/avizo-ro-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/avizo-ro-mcp.yml
- group: agent
  href: https://artifacts.apis.io/avizo-ro/well-known/avizo-ro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avizo-ro-well-known.yml
- group: other
  href: https://artifacts.apis.io/avizo-ro/hosts/avizo-ro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avizo-ro-hosts.yml
- group: other
  href: https://artifacts.apis.io/avizo-ro/vendors/avizo-ro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avizo-ro-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://avizo.ro/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/avizo-ro/security/avizo-ro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avizo-ro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avizo.ro/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://avizo.ro/docs
- group: docs
  title: ''
  type: Documentation
  url: https://avizo.ro/docs
- group: docs
  title: ''
  type: APIReference
  url: https://avizo.ro/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://avizo.ro/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://avizo.ro/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://avizo.ro/signup
- group: start
  title: ''
  type: Login
  url: https://avizo.ro/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avizo.ro/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avizo.ro/legal/privacy
created: '2026-11-02'
description: Avizo provides automated alerts for expiration of company documents such as vehicle technical inspections (ITP), mandatory insurance (RCA), occupational health certificates, permits and other time‑sensitive authorizations. Users receive notifications via email, WhatsApp, SMS and push before deadlines, helping businesses avoid fines and administrative penalties.
image: https://avizo.ro/_next/image?url=%2Favizo-logo.png&w=384&q=75
jsonld:
- class_count: 2
  name: Avizo Ro Context
  property_count: 3
  slug: avizo-ro-context
layout: provider
mcp_servers:
- description: Remote MCP server at avizo.ro.
  name: Avizo MCP Server
  slug: avizo-ro-mcp-yml
modified: '2026-11-02'
name: Avizo
nav: Providers
network: true
overview: 'Avizo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Alerts, Compliance, Document Management, Romanian, and Automotive.


  The Avizo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Avizo''s developer surface includes authentication, getting-started guide, documentation, API reference, support, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Avizo Ro Plans Pricing
  plan_count: 4
  slug: avizo-ro-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Avizo Ro Rate Limits
  slug: avizo-ro-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Avizo API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: avizo-ro-rules
scopes:
- name: Avizo Ro Scopes
  scope_count: 0
  slug: avizo-ro-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 67.8
    catalog_earned_first_party: 20.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 6.7
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Avizo Ro Authentication
  slug: avizo-ro-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Avizo Ro Domain Security
  slug: avizo-ro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 1
skills:
- name: list-items
  slug: avizo-ro-list-items
slug: avizo-ro
tags:
- Alerts
- Compliance
- Document Management
- Romanian
- Automotive
website: https://avizo.ro/
---
