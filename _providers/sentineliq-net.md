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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Sentineliq Net Agentic Access
  operation_count: 23
  slug: sentineliq-net-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 1
apis:
- description: Per-address computed research for Washington state real‑estate data via RESTful endpoints.
  name: SENTINEL Property Research API
  slug: sentinel-property-research-api
- baseURL: https://app.sentineliq.net
  baseurl_source: declared
  description: The agent-api API from sentineliq-net — 12 operation(s) for agent-api.
  name: sentineliq-net Agent API
  slug: sentineliq-net-agent-api-api
- baseURL: https://app.sentineliq.net
  baseurl_source: declared
  description: The mcp API from sentineliq-net — 2 operation(s) for mcp.
  name: sentineliq-net MCP API
  slug: sentineliq-net-mcp-api
- baseURL: https://app.sentineliq.net
  baseurl_source: declared
  description: The property-research API from sentineliq-net — 2 operation(s) for property-research.
  name: sentineliq-net Property Research API
  slug: sentineliq-net-property-research-api
- baseURL: https://app.sentineliq.net
  baseurl_source: declared
  description: The public API from sentineliq-net — 3 operation(s) for public.
  name: sentineliq-net Public API
  slug: sentineliq-net-public-api
- baseURL: https://app.sentineliq.net
  baseurl_source: declared
  description: The seller-workflows API from sentineliq-net — 4 operation(s) for seller-workflows.
  name: sentineliq-net Seller Workflows API
  slug: sentineliq-net-seller-workflows-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/sentineliq-net/agentic-access/sentineliq-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sentineliq-net-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/sentineliq-net/rules/sentineliq-net-rules.yml
  title: ''
  type: Spectral
  url: rules/sentineliq-net-rules.yml
- group: design
  href: https://artifacts.apis.io/sentineliq-net/json-ld/sentineliq-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sentineliq-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/sentineliq-net/vocabulary/sentineliq-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sentineliq-net-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sentineliq-net/data-model/sentineliq-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sentineliq-net-data-model.yml
- group: design
  href: https://artifacts.apis.io/sentineliq-net/errors/sentineliq-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sentineliq-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sentineliq-net/conformance/sentineliq-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sentineliq-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sentineliq-net/llms/sentineliq-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sentineliq-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/sentineliq-net/mcp/sentineliq-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sentineliq-net-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sentineliq-net/well-known/sentineliq-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sentineliq-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/sentineliq-net/hosts/sentineliq-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sentineliq-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/sentineliq-net/vendors/sentineliq-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sentineliq-net-vendors.yml
- group: auth
  href: https://artifacts.apis.io/sentineliq-net/authentication/sentineliq-net-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sentineliq-net-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sentineliq-net/security/sentineliq-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sentineliq-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sentineliq.net/
- group: docs
  title: ''
  type: Documentation
  url: https://sentineliq.net/developers
- group: docs
  title: ''
  type: APIReference
  url: https://app.sentineliq.net/api/v1/agent-api/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://sentineliq.net/developers/start
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sentineliq.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sentineliq.net/privacy
created: '2026-10-31'
description: Sentinel (sentineliq.net) provides Washington state real‑estate data via a RESTful API and MCP interface. It offers property records, permit changes, and seller‑math calculations for developers to integrate into AI assistants or software. The service includes example workflows, a developer console, and detailed terms, privacy, and pricing information. It targets real‑estate professionals, developers, and AI applications needing verified property evidence.
jsonld:
- class_count: 120
  name: Sentineliq Net Context
  property_count: 521
  slug: sentineliq-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.sentineliq.net.
  name: sentineliq-net MCP Server
  slug: sentineliq-net-mcp-yml
modified: '2026-10-31'
name: sentineliq-net
nav: Providers
network: true
overview: 'sentineliq-net publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, MCP API, Property Research API, and 3 more. Tagged areas include Company, Real Estate, Data API, Washington, and AI Integration.


  The sentineliq-net catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  sentineliq-net''s developer surface includes authentication, documentation, API reference, getting-started guide, and 16 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: sentineliq-net API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 1
  slug: sentineliq-net-rules
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 56.6
    developer_ergonomics: 26.2
    discoverability: 61.7
    operational_transparency: 0.0
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sentineliq-net/sentineliq-net-2026-11-03T143037.png
security:
- kind: authentication
  name: Sentineliq Net Authentication
  slug: sentineliq-net-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sentineliq Net Domain Security
  slug: sentineliq-net-domain-security
  summary_line: TLSv1.3 · HSTS
slug: sentineliq-net
tags:
- Company
- Real Estate
- Data API
- Washington
- AI Integration
website: https://sentineliq.net/
---
