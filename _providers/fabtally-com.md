---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Fabtally Com Agentic Access
  operation_count: 14
  slug: fabtally-com-agentic-access
  summary_line: 14 operations · 11 acting
api_count: 1
apis:
- baseURL: https://fabtally.com
  baseurl_source: declared
  description: The Attest API from fabtally-com — 1 operation(s) for attest.
  name: fabtally-com Attest API
  slug: fabtally-com-attest-api
- baseURL: https://fabtally.com
  baseurl_source: declared
  description: The DFM API from fabtally-com — 3 operation(s) for dfm.
  name: fabtally-com DFM API
  slug: fabtally-com-dfm-api
- baseURL: https://fabtally.com
  baseurl_source: declared
  description: The Discovery API from fabtally-com — 3 operation(s) for discovery.
  name: fabtally-com Discovery API
  slug: fabtally-com-discovery-api
- baseURL: https://fabtally.com
  baseurl_source: declared
  description: The Quote API from fabtally-com — 1 operation(s) for quote.
  name: fabtally-com Quote API
  slug: fabtally-com-quote-api
- baseURL: https://fabtally.com
  baseurl_source: declared
  description: The Slice API from fabtally-com — 6 operation(s) for slice.
  name: fabtally-com Slice API
  slug: fabtally-com-slice-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/fabtally-com/agentic-access/fabtally-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fabtally-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/fabtally-com/rules/fabtally-com-rules.yml
  title: ''
  type: Spectral
  url: rules/fabtally-com-rules.yml
- group: design
  href: https://artifacts.apis.io/fabtally-com/vocabulary/fabtally-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fabtally-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/fabtally-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/fabtally-com/authentication/fabtally-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fabtally-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/fabtally-com/errors/fabtally-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fabtally-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fabtally-com/conformance/fabtally-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fabtally-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/fabtally-com/a2a/fabtally-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/fabtally-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/fabtally-com/mcp/fabtally-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fabtally-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/fabtally-com/well-known/fabtally-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fabtally-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/fabtally-com/hosts/fabtally-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fabtally-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/fabtally-com/security/fabtally-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fabtally-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fabtally.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fabtally.com/openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://fabtally.com/openapi.json
created: '2026-10-29'
description: FabTally provides a REST and MCP API that delivers 3D‑printing quotes, G‑code generation, and printability checks using a real slicer backend. Users can submit 3D models and receive estimated print time, filament usage, layer count, dimensions, a fits‑on‑bed verification, and pricing. The service supports 13 printer models and 12 material types, offering free access for individuals and a pay‑per‑call model in USDC for agents. The API is documented via an OpenAPI 3.1 specification available at /openapi.json.
layout: provider
mcp_servers:
- description: Remote MCP server at fabtally.com.
  name: fabtally-com MCP Server
  slug: fabtally-com-mcp-yml
modified: '2026-10-29'
name: fabtally-com
nav: Providers
network: true
overview: 'fabtally-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attest API, DFM API, Discovery API, and 2 more. Tagged areas include Company, 3D Printing, Slicing, Quotes, and Manufacturing.


  The fabtally-com catalog on APIs.io includes 1 Spectral governance ruleset.


  fabtally-com''s developer surface includes authentication, documentation, API reference, and 12 more developer resources.'
plans:
- name: Fabtally Com Plans Pricing
  plan_count: 0
  slug: fabtally-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Fabtally Com Rate Limits
  slug: fabtally-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: fabtally-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: fabtally-com-rules
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 46.2
    developer_ergonomics: 22.0
    discoverability: 65.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fabtally-com/fabtally-com-2026-11-03T131758.png
security:
- kind: authentication
  name: Fabtally Com Authentication
  slug: fabtally-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fabtally Com Domain Security
  slug: fabtally-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: slice
  slug: fabtally-com-slice
slug: fabtally-com
tags:
- Company
- 3D Printing
- Slicing
- Quotes
- Manufacturing
website: https://fabtally.com/
---
