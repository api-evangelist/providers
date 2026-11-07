---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: K Agentpay Com Agentic Access
  operation_count: 7
  slug: k-agentpay-com-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://api.k-agentpay.com
  baseurl_source: declared
  description: The Airport API from k-agentpay-com — 1 operation(s) for airport.
  name: k-agentpay-com Airport API
  slug: k-agentpay-com-airport-api
- baseURL: https://api.k-agentpay.com
  baseurl_source: declared
  description: The Kpop API from k-agentpay-com — 2 operation(s) for kpop.
  name: k-agentpay-com Kpop API
  slug: k-agentpay-com-kpop-api
- baseURL: https://api.k-agentpay.com
  baseurl_source: declared
  description: The Seoul API from k-agentpay-com — 4 operation(s) for seoul.
  name: k-agentpay-com Seoul API
  slug: k-agentpay-com-seoul-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/k-agentpay-com/agentic-access/k-agentpay-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/k-agentpay-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/k-agentpay-com/rules/k-agentpay-com-rules.yml
  title: ''
  type: Spectral
  url: rules/k-agentpay-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/k-agentpay-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/k-agentpay-com/errors/k-agentpay-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/k-agentpay-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/k-agentpay-com/conformance/k-agentpay-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/k-agentpay-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/k-agentpay-com/llms/k-agentpay-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/k-agentpay-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/k-agentpay-com/mcp/k-agentpay-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/k-agentpay-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/k-agentpay-com/hosts/k-agentpay-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/k-agentpay-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/k-agentpay-com/security/k-agentpay-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/k-agentpay-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://k-agentpay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.k-agentpay.com/openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://api.k-agentpay.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://rapidapi.com/JBML/api/korea-travel-k-pop-live-data
created: '2026-10-30'
description: K-AgentPay provides a suite of real‑time data APIs focused on Korean travel and K‑pop live events. Its offerings include Incheon Airport security wait times, Seoul subway arrival predictions, live crowd and weather data for Seoul, and K‑pop concert schedules and ticket information. The APIs deliver JSON responses in English, Japanese, and Korean, and are accessible via RapidAPI or the proprietary x402 protocol. Designed for app developers and AI agents, K‑AgentPay aims to enrich travel planning and entertainment experiences with up‑to‑date Korean locale data.
layout: provider
mcp_servers:
- description: Remote MCP server at k-agentpay.com.
  name: k-agentpay-com MCP Server
  slug: k-agentpay-com-mcp-yml
modified: '2026-10-30'
name: k-agentpay-com
nav: Providers
network: true
overview: 'k-agentpay-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Airport API, Kpop API, and Seoul API. Tagged areas include Company, Travel, K-Pop, Data, and South Korea.


  The k-agentpay-com catalog on APIs.io includes 1 Spectral governance ruleset.


  k-agentpay-com''s developer surface includes documentation, API reference, pricing, and 10 more developer resources.'
plans:
- name: K Agentpay Com Plans Pricing
  plan_count: 0
  slug: k-agentpay-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: K Agentpay Com Rate Limits
  slug: k-agentpay-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: k-agentpay-com API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: k-agentpay-com-rules
scopes:
- name: K Agentpay Com Scopes
  scope_count: 0
  slug: k-agentpay-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 38.8
    catalog_earned_first_party: 0.0
    catalog_gap: 76.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 5.3
    contract_governance: 15.9
    contract_quality: 44.9
    developer_ergonomics: 14.8
    discoverability: 61.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 26.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/k-agentpay-com/k-agentpay-com-2026-11-03T134251.png
security:
- kind: authentication
  name: K Agentpay Com Authentication
  slug: k-agentpay-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: K Agentpay Com Domain Security
  slug: k-agentpay-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: kpop-search
  slug: k-agentpay-com-kpop-search
slug: k-agentpay-com
tags:
- Company
- Travel
- K-Pop
- Data
- South Korea
website: https://k-agentpay.com/
---
