---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Search 70,000+ independently-owned stays and retrieve every way to book each one, including the host's own direct booking site. CielStay never processes payments and takes no commission.
  name: CielStay Agent API
  slug: cielstay-agent-api
- description: 'CielStay API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: CielStay API
  slug: cielstay-com-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/cielstay-com/rules/cielstay-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cielstay-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cielstay-com/json-ld/cielstay-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cielstay-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cielstay-com/vocabulary/cielstay-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cielstay-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cielstay-com/data-model/cielstay-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cielstay-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cielstay-com/conformance/cielstay-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cielstay-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cielstay-com/llms/cielstay-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cielstay-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cielstay-com/mcp/cielstay-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cielstay-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cielstay-com/well-known/cielstay-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cielstay-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cielstay-com/hosts/cielstay-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cielstay-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cielstay-com/vendors/cielstay-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cielstay-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cielstay-com/security/cielstay-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cielstay-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cielstay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cielstay.com/ai-agent-guide
- group: docs
  title: ''
  type: APIReference
  url: https://www.cielstay.com/api/v1
- group: agent
  title: ''
  type: MCP
  url: https://mcp.cielstay.com/mcp
- group: agent
  title: ''
  type: llms
  url: https://www.cielstay.com/llms.txt
coverage:
  checked: '2026-11-03'
  detail: Provider offers JSON API reference but no OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://www.cielstay.com/api/v1
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: CielStay provides a free AI-powered index for direct booking homes, aggregating over 90,000 properties for short‑term, seasonal, or long‑term stays. Users can search by preferences, location, or through their own AI agents, accessing listings across all channels without intermediary fees. The platform aims to simplify vacation rentals by offering transparent, AI‑enhanced discovery and direct booking options.
json_schemas:
- name: GetApiV1ListingsIdLiveQuoteResponse
  property_count: 1
  slug: cielstay-com-get-api-v1-listings-id-live-quote-response
jsonld:
- class_count: 1
  name: Cielstay Com Context
  property_count: 1
  slug: cielstay-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.cielstay.com.
  name: CielStay MCP Server
  slug: cielstay-com-mcp-yml
modified: '2026-11-03'
name: CielStay
nav: Providers
network: true
overview: 'CielStay is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Vacation Rentals, Artificial Intelligence, Direct Booking, Real Estate, and Travel.


  The CielStay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CielStay''s developer surface includes documentation, API reference, and 14 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: CielStay API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: cielstay-com-rules
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.2
    catalog_earned_first_party: 0.0
    catalog_gap: 68.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 16.4
    developer_ergonomics: 8.3
    discoverability: 53.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cielstay Com Domain Security
  slug: cielstay-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cielstay-com
tags:
- Vacation Rentals
- Artificial Intelligence
- Direct Booking
- Real Estate
- Travel
website: https://www.cielstay.com/
---
