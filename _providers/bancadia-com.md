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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://mcp.bancadia.com
  baseurl_source: declared
  description: 'Bancadia API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Bancadia API
  slug: bancadia-com-api
artifact_total: 9
common:
- group: operate
  href: https://artifacts.apis.io/bancadia-com/rate-limits/bancadia-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bancadia-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/bancadia-com/rules/bancadia-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bancadia-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bancadia-com/json-ld/bancadia-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bancadia-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bancadia-com/vocabulary/bancadia-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bancadia-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bancadia-com/data-model/bancadia-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bancadia-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/bancadia-com/authentication/bancadia-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bancadia-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/bancadia-com/errors/bancadia-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bancadia-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bancadia-com/conformance/bancadia-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bancadia-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bancadia-com/llms/bancadia-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bancadia-com-llms.txt
- group: build
  href: https://artifacts.apis.io/bancadia-com/mcp/bancadia-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bancadia-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bancadia-com/mcp/bancadia-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bancadia-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/bancadia-com/hosts/bancadia-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bancadia-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bancadia-com/vendors/bancadia-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bancadia-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bancadia-com/security/bancadia-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bancadia-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bancadia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bancadia.com/developer/login
- group: docs
  title: ''
  type: Documentation
  url: https://bancadia.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://bancadia.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://bancadia.com/docs/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://bancadia.com/developer/signup
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://bancadia.com/api/mcp
  - status: 200
    url: https://bancadia.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Bancadia provides a data‑layer API that AI agents use to recommend U.S. business banking products. It offers a verified, real‑time registry of business checking accounts, exposing fees, rates, eligibility, and features through a single Model Context Protocol (MCP) call. The service is free for developers, supports fifteen optional filters, and includes product listings, comparison matrices, and explainer articles. Bancadia aims to simplify bank‑account selection for agents, fintechs, and advisors while earning affiliate commissions on funded accounts.
image: https://bancadia.com/_next/image?url=%2Fbancadia-logo.jpg&w=256&q=75
json_schemas:
- name: PostRequest
  property_count: 4
  slug: bancadia-com-post-request
- name: PostResponse
  property_count: 1
  slug: bancadia-com-post-response
jsonld:
- class_count: 2
  name: Bancadia Com Context
  property_count: 5
  slug: bancadia-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.bancadia.com requiring an API key.
  name: Bancadia MCP Server
  slug: bancadia-com-mcp-yml
modified: '2026-11-02'
name: Bancadia
nav: Providers
network: true
overview: 'Bancadia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Banking, Artificial Intelligence, and DataLayer.


  The Bancadia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bancadia''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, and 15 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 1
  name: Bancadia Com Rate Limits
  slug: bancadia-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Bancadia API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: bancadia-com-rules
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 20.9
    developer_ergonomics: 31.0
    discoverability: 56.7
    operational_transparency: 21.1
  previous_composite: 28.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bancadia Com Authentication
  slug: bancadia-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bancadia Com Domain Security
  slug: bancadia-com-domain-security
  summary_line: TLSv1.3
slug: bancadia-com
tags:
- Fintech
- Banking
- Artificial Intelligence
- DataLayer
website: https://bancadia.com/
---
