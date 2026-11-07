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
    agent_skills: derived
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
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Carchat Io Agentic Access
  operation_count: 5
  slug: carchat-io-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- baseURL: https://carchat.io
  baseurl_source: declared
  description: The Dealers API from CarChat — 1 operation(s) for dealers.
  name: CarChat Dealers API
  slug: carchat-io-dealers-api
- baseURL: https://carchat.io
  baseurl_source: declared
  description: The Inventory API from CarChat — 1 operation(s) for inventory.
  name: CarChat Inventory API
  slug: carchat-io-inventory-api
- baseURL: https://carchat.io
  baseurl_source: declared
  description: The Lead API from CarChat — 1 operation(s) for lead.
  name: CarChat Lead API
  slug: carchat-io-lead-api
- baseURL: https://carchat.io
  baseurl_source: declared
  description: The Segments API from CarChat — 1 operation(s) for segments.
  name: CarChat Segments API
  slug: carchat-io-segments-api
- baseURL: https://carchat.io
  baseurl_source: declared
  description: The Vehicles API from CarChat — 1 operation(s) for vehicles.
  name: CarChat Vehicles API
  slug: carchat-io-vehicles-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/carchat-io/agentic-access/carchat-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/carchat-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/carchat-io/rules/carchat-io-rules.yml
  title: ''
  type: Spectral
  url: rules/carchat-io-rules.yml
- group: design
  href: https://artifacts.apis.io/carchat-io/json-ld/carchat-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carchat-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/carchat-io/vocabulary/carchat-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carchat-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/carchat-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/carchat-io/data-model/carchat-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carchat-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/carchat-io/errors/carchat-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carchat-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/carchat-io/conformance/carchat-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carchat-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carchat-io/llms/carchat-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carchat-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/carchat-io/mcp/carchat-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/carchat-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/carchat-io/well-known/carchat-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carchat-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/carchat-io/hosts/carchat-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carchat-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/carchat-io/vendors/carchat-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carchat-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carchat.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carchat.io/privacy
- group: auth
  href: https://artifacts.apis.io/carchat-io/security/carchat-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carchat-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carchat.io/
created: '2026-11-03'
description: CarChat (carchat.io) provides a free live dealership inventory marketplace. It aggregates listings from dealership websites, inventory feeds, and Hammer accounts, refreshing daily. Buyers can search in plain English, view advertised prices, and contact dealers directly without creating an account. The service is intended for both human users and AI assistants, offering an open API at /api/v1 for search and /api/lead for inquiries.
jsonld:
- class_count: 1
  name: Carchat Io Context
  property_count: 15
  slug: carchat-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at carchat.io.
  name: CarChat MCP Server
  slug: carchat-io-mcp-yml
modified: '2026-11-03'
name: CarChat
nav: Providers
network: true
overview: 'CarChat publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dealers API, Inventory API, Lead API, and 2 more. Tagged areas include Company, Marketplace, Automotive, Artificial Intelligence, and OpenAPI.


  The CarChat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: CarChat API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: carchat-io-rules
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 47.0
    developer_ergonomics: 1.8
    discoverability: 53.3
    operational_transparency: 0.0
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
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carchat Io Domain Security
  slug: carchat-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: carchat-io-submit-vehicle-inquiry
  slug: carchat-io-submit-vehicle-inquiry
slug: carchat-io
tags:
- Company
- Marketplace
- Automotive
- Artificial Intelligence
- OpenAPI
website: https://carchat.io/
---
