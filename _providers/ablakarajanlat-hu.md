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
  band_gated_from: agent-native
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
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Ablakarajanlat Hu Agentic Access
  operation_count: 16
  slug: ablakarajanlat-hu-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 1
apis:
- baseURL: https://ablakarajanlat.hu
  baseurl_source: declared
  description: The Agent API from Ablak Árajánlat — 7 operation(s) for agent.
  name: Ablak Árajánlat Agent API
  slug: ablakarajanlat-hu-agent-api
- baseURL: https://ablakarajanlat.hu
  baseurl_source: declared
  description: The Ai API from Ablak Árajánlat — 2 operation(s) for ai.
  name: Ablak Árajánlat AI API
  slug: ablakarajanlat-hu-ai-api
- baseURL: https://ablakarajanlat.hu
  baseurl_source: declared
  description: The Coverage API from Ablak Árajánlat — 1 operation(s) for coverage.
  name: Ablak Árajánlat Coverage API
  slug: ablakarajanlat-hu-coverage-api
- baseURL: https://ablakarajanlat.hu
  baseurl_source: declared
  description: The Estimate API from Ablak Árajánlat — 1 operation(s) for estimate.
  name: Ablak Árajánlat Estimate API
  slug: ablakarajanlat-hu-estimate-api
- baseURL: https://ablakarajanlat.hu
  baseurl_source: declared
  description: The Knowledge API from Ablak Árajánlat — 1 operation(s) for knowledge.
  name: Ablak Árajánlat Knowledge API
  slug: ablakarajanlat-hu-knowledge-api
- baseURL: https://ablakarajanlat.hu
  baseurl_source: declared
  description: The Mcp API from Ablak Árajánlat — 1 operation(s) for mcp.
  name: Ablak Árajánlat MCP API
  slug: ablakarajanlat-hu-mcp-api
- baseURL: https://ablakarajanlat.hu
  baseurl_source: declared
  description: The Quote API from Ablak Árajánlat — 1 operation(s) for quote.
  name: Ablak Árajánlat Quote API
  slug: ablakarajanlat-hu-quote-api
- baseURL: https://ablakarajanlat.hu
  baseurl_source: declared
  description: The Support API from Ablak Árajánlat — 1 operation(s) for support.
  name: Ablak Árajánlat Support API
  slug: ablakarajanlat-hu-support-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/ablakarajanlat-hu/agentic-access/ablakarajanlat-hu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ablakarajanlat-hu-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/ablakarajanlat-hu/rate-limits/ablakarajanlat-hu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ablakarajanlat-hu-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/ablakarajanlat-hu/rules/ablakarajanlat-hu-rules.yml
  title: ''
  type: Spectral
  url: rules/ablakarajanlat-hu-rules.yml
- group: design
  href: https://artifacts.apis.io/ablakarajanlat-hu/json-ld/ablakarajanlat-hu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ablakarajanlat-hu-context.jsonld
- group: design
  href: https://artifacts.apis.io/ablakarajanlat-hu/vocabulary/ablakarajanlat-hu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ablakarajanlat-hu-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ablakarajanlat-hu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ablakarajanlat-hu/data-model/ablakarajanlat-hu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ablakarajanlat-hu-data-model.yml
- group: design
  href: https://artifacts.apis.io/ablakarajanlat-hu/conventions/ablakarajanlat-hu-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ablakarajanlat-hu-conventions.yml
- group: design
  href: https://artifacts.apis.io/ablakarajanlat-hu/conventions/ablakarajanlat-hu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ablakarajanlat-hu-conventions.yml
- group: design
  href: https://artifacts.apis.io/ablakarajanlat-hu/errors/ablakarajanlat-hu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ablakarajanlat-hu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ablakarajanlat-hu/conformance/ablakarajanlat-hu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ablakarajanlat-hu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ablakarajanlat-hu/llms/ablakarajanlat-hu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ablakarajanlat-hu-llms.txt
- group: build
  href: https://artifacts.apis.io/ablakarajanlat-hu/mcp/ablakarajanlat-hu-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ablakarajanlat-hu-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ablakarajanlat-hu/mcp/ablakarajanlat-hu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ablakarajanlat-hu-mcp.yml
- group: other
  href: https://artifacts.apis.io/ablakarajanlat-hu/hosts/ablakarajanlat-hu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ablakarajanlat-hu-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ablakarajanlat-hu/authentication/ablakarajanlat-hu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ablakarajanlat-hu-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ablakarajanlat-hu/security/ablakarajanlat-hu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ablakarajanlat-hu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ablakarajanlat.hu/
- group: docs
  title: ''
  type: Documentation
  url: https://ablakarajanlat.hu/openapi.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://ablakarajanlat.hu/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://ablakarajanlat.hu/tervezo
created: '2026-10-31'
description: Ablak Árajánlat (ablakarajanlat.hu) offers a free online plastic window calculator and design tool for Hungarian customers. Users can input custom dimensions to instantly receive manufacturer‑calculated price quotes for double‑ or triple‑glazed windows, without registration. The service provides detailed pricing, material options, and visualizations, helping homeowners and builders plan window replacements efficiently.
image: https://ablakarajanlat.hu/og-hero.jpg
json_schemas:
- name: AstBridgeRequest
  property_count: 16
  slug: ablakarajanlat-hu-ast-bridge-request
- name: EstimateRequest
  property_count: 7
  slug: ablakarajanlat-hu-estimate-request
- name: EstimateResponse
  property_count: 6
  slug: ablakarajanlat-hu-estimate-response
- name: KnowledgeSearchResponse
  property_count: 6
  slug: ablakarajanlat-hu-knowledge-search-response
- name: QuoteCreateRequest
  property_count: 3
  slug: ablakarajanlat-hu-quote-create-request
- name: V1EstimateResponse
  property_count: 9
  slug: ablakarajanlat-hu-v1-estimate-response
jsonld:
- class_count: 18
  name: Ablakarajanlat Hu Context
  property_count: 62
  slug: ablakarajanlat-hu-context
layout: provider
mcp_servers:
- description: Remote MCP server at ablakarajanlat.hu.
  name: Ablak Árajánlat MCP Server
  slug: ablakarajanlat-hu-mcp-yml
modified: '2026-10-31'
name: Ablak Árajánlat
nav: Providers
network: true
overview: 'Ablak Árajánlat publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, AI API, Coverage API, and 5 more. Tagged areas include Windows, Calculator, Construction, Hungary, and Pricing.


  The Ablak Árajánlat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ablak Árajánlat''s developer surface includes authentication, documentation, API reference, getting-started guide, and 17 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 2
  name: Ablakarajanlat Hu Rate Limits
  slug: ablakarajanlat-hu-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Ablak Árajánlat API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: ablakarajanlat-hu-rules
scopes:
- name: Ablakarajanlat Hu Scopes
  scope_count: 0
  slug: ablakarajanlat-hu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.8
    catalog_earned_first_party: 0.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 62.3
    developer_ergonomics: 28.0
    discoverability: 65.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - hungary
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ablakarajanlat Hu Authentication
  slug: ablakarajanlat-hu-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ablakarajanlat Hu Domain Security
  slug: ablakarajanlat-hu-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: price-estimate
  slug: price-estimate
slug: ablakarajanlat-hu
tags:
- Windows
- Calculator
- Construction
- Hungary
- Pricing
website: https://ablakarajanlat.hu/
---
