---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    agent_card: conformant
    agent_skills: derived
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Opplevagent No Agentic Access
  operation_count: 7
  slug: opplevagent-no-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 1
apis:
- description: 'Remote Model Context Protocol server over Streamable HTTP at https://opplevagent.no/mcp, anonymous and session-based (initialize first, then echo mcp-session-id). A live tools/list returns five tools '
  name: Opplevagent MCP Server
  slug: mcp-server
- description: 'A2A JSON-RPC 2.0 endpoint at https://opplevagent.no/a2a described by a signed agent card (protocolVersion 1.0.0, JSONRPC transport, three skills: discover experiences, get experience details, list cat'
  name: Opplevagent A2A Agent
  slug: a2a-agent
- baseURL: https://opplevagent.no/api/opplevelser
  baseurl_source: declared
  description: The A2a API from Opplevagent — 1 operation(s) for a2a.
  name: Opplevagent A2a API
  slug: opplevagent-no-a2a-api
- baseURL: https://opplevagent.no/api/opplevelser
  baseurl_source: declared
  description: The Llms.txt API from Opplevagent — 1 operation(s) for llms.txt.
  name: Opplevagent Llms.txt API
  slug: opplevagent-no-llms-txt-api
- baseURL: https://opplevagent.no/api/opplevelser
  baseurl_source: declared
  description: The Opplevelser API from Opplevagent — 3 operation(s) for opplevelser.
  name: Opplevagent Opplevelser API
  slug: opplevagent-no-opplevelser-api
- baseURL: https://opplevagent.no/api/opplevelser
  baseurl_source: declared
  description: The .well Known API from Opplevagent — 1 operation(s) for .well known.
  name: Opplevagent .well Known API
  slug: opplevagent-no-well-known-api
artifact_total: 17
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://opplevagent.no/guide-opplevelser-mcp
- group: agent
  href: https://artifacts.apis.io/opplevagent-no/agentic-access/opplevagent-no-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/opplevagent-no-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://opplevagent.no/
- group: docs
  title: ''
  type: Documentation
  url: https://opplevagent.no/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://opplevagent.no/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://opplevagent.no/guide-opplevelser-mcp
- group: operate
  title: ''
  type: Support
  url: https://opplevagent.no/kontakt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opplevagent.no/vilkar
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opplevagent.no/personvern
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/slookisen/lokal
- group: agent
  href: https://artifacts.apis.io/opplevagent-no/llms/opplevagent-no-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opplevagent-no-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://opplevagent.no/llms.txt
- group: agent
  href: https://artifacts.apis.io/opplevagent-no/well-known/opplevagent-no-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/opplevagent-no-well-known.yml
- group: other
  href: https://artifacts.apis.io/opplevagent-no/a2a/opplevagent-no-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/opplevagent-no-a2a.yml
- group: agent
  href: https://artifacts.apis.io/opplevagent-no/mcp/opplevagent-no-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/opplevagent-no-mcp.yml
- group: build
  href: https://artifacts.apis.io/opplevagent-no/mcp/opplevagent-no-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/opplevagent-no-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/opplevagent-no/packages/opplevagent-no-packages.yml
  title: ''
  type: Packages
  url: packages/opplevagent-no-packages.yml
- group: agent
  href: https://artifacts.apis.io/opplevagent-no/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/opplevagent-no/overlays/opplevagent-no-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/opplevagent-no-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/opplevagent-no/conformance/opplevagent-no-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opplevagent-no-conformance.yml
- group: design
  href: https://artifacts.apis.io/opplevagent-no/errors/opplevagent-no-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/opplevagent-no-problem-types.yml
- group: design
  href: https://artifacts.apis.io/opplevagent-no/lifecycle/opplevagent-no-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/opplevagent-no-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/opplevagent-no/authentication/opplevagent-no-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opplevagent-no-authentication.yml
- group: design
  href: https://artifacts.apis.io/opplevagent-no/conventions/opplevagent-no-conventions.yml
  title: ''
  type: Conventions
  url: conventions/opplevagent-no-conventions.yml
- group: design
  href: https://artifacts.apis.io/opplevagent-no/data-model/opplevagent-no-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opplevagent-no-data-model.yml
- group: operate
  href: https://artifacts.apis.io/opplevagent-no/rate-limits/opplevagent-no-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/opplevagent-no-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/opplevagent-no/plans/opplevagent-no-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opplevagent-no-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/opplevagent-no/regulatory/opplevagent-no-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/opplevagent-no-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://opplevagent.no/personvern
- group: auth
  href: https://artifacts.apis.io/opplevagent-no/security/opplevagent-no-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opplevagent-no-domain-security.yml
created: '2026-09-19'
description: Opplevagent is an agent-native (A2A) marketplace of Norwegian experiences and activities — 547 hand-picked tours, courses, attractions and things to do from 417 providers verified against Brønnøysundregistrene, plus a gårdssalg vertical of 252 farm-sale drink producers (breweries, cideries, wineries, distilleries). Agents and humans query the same catalog through an open, read-only REST discovery API described by an OpenAPI 3.1 document, a remote Streamable-HTTP MCP server (also shipped as the opplevagent-mcp npm package for stdio clients) with five tools including a pending-only booking request, and an A2A JSON-RPC endpoint described by a signed agent card at /.well-known/agent-card.json. No authentication is required; an optional free X-API-Key raises the rate limits. Operated from Norway by Daniel Fredriksen on the same codebase as the sibling sites rettfrabonden.com and finn-tannlege.com.
finops:
- has_sources: true
  method: derived
  name: Opplevagent No Finops
  primary_unit: ''
  service_category: ''
  slug: opplevagent-no-finops
  template: true
image: https://opplevagent.no/favicon.svg
layout: provider
mcp_servers:
- description: Opplevagent operates ONE remote MCP server at https://opplevagent.no/mcp (Streamable HTTP, anonymous, session-based) and ships the same server as the opplevagent-mcp npm package for stdio clients. A l
  name: Opplevagent MCP Server
  slug: opplevagent-no-mcp-yml
modified: '2026-09-19'
name: Opplevagent
nav: Providers
network: true
overview: 'Opplevagent publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Llms.txt API, Opplevelser API, and 3 more. Tagged areas include Travel, Tourism, Experience, Activities, and Norway.


  The Opplevagent catalog on APIs.io includes 1 Spectral governance ruleset.


  Opplevagent''s developer surface includes pricing, documentation, API reference, getting-started guide, support, authentication, and 24 more developer resources.'
plans:
- name: Opplevagent No Plans Pricing
  plan_count: 1
  slug: opplevagent-no-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Opplevagent No Rate Limits
  slug: opplevagent-no-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Opplevagent API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: opplevagent-no-rules
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 46.8
    developer_ergonomics: 30.4
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
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/opplevagent-no/opplevagent-no-2026-10-11T112127.png
security:
- kind: authentication
  name: Opplevagent No Authentication
  slug: opplevagent-no-authentication
  summary_line: none/apiKey · 2 schemes
- kind: domain-security
  name: Opplevagent No Domain Security
  slug: opplevagent-no-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: opplevagent-a2a-natural-language-discovery
  slug: opplevagent-no-a2a-natural-language-discovery
- name: opplevagent-discover-experiences
  slug: opplevagent-no-discover-experiences
- name: opplevagent-gardssalg-discover-and-book
  slug: opplevagent-no-gardssalg-discover-and-book
slug: opplevagent-no
tags:
- Travel
- Tourism
- Experience
- Activities
- Norway
- Marketplace
- Agent-Native
- A2A
- MCP
- Booking
- Local Food
- Open Data
website: https://opplevagent.no/
---
