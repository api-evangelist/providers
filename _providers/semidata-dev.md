---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Semidata Dev Agentic Access
  operation_count: 7
  slug: semidata-dev-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 1
apis:
- baseURL: https://semidata.dev
  baseurl_source: declared
  description: The Agent Integration API from semidata-dev — 1 operation(s) for agent integration.
  name: semidata-dev Agent Integration API
  slug: semidata-dev-agent-integration-api
- baseURL: https://semidata.dev
  baseurl_source: declared
  description: The Supply Chain Intelligence API from semidata-dev — 6 operation(s) for supply chain intelligence.
  name: semidata-dev Supply Chain Intelligence API
  slug: semidata-dev-supply-chain-intelligence-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/semidata-dev/agentic-access/semidata-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/semidata-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/semidata-dev/rules/semidata-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/semidata-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/semidata-dev/vocabulary/semidata-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/semidata-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/semidata-dev/errors/semidata-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/semidata-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/semidata-dev/conformance/semidata-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/semidata-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/semidata-dev/llms/semidata-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/semidata-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/semidata-dev/mcp/semidata-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/semidata-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/semidata-dev/mcp/semidata-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/semidata-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/semidata-dev/well-known/semidata-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/semidata-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/semidata-dev/hosts/semidata-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/semidata-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/semidata-dev/vendors/semidata-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/semidata-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/semidata-dev/authentication/semidata-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/semidata-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/semidata-dev/security/semidata-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/semidata-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://semidata.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://semidata.dev/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://semidata.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://semidata.dev/
created: '2026-10-31'
description: SemiData provides semiconductor and quantum supply-chain intelligence through an API that aggregates US‑government filings, regulatory signals, entity lists, mineral deposits, SEC disclosures, trade flows and quantum funding data. The service offers searchable, structured data to help companies track export controls, trade restrictions and emerging quantum technology investments, refreshed weekly across thousands of records.
layout: provider
mcp_servers:
- description: Remote MCP server at semidata.dev.
  name: semidata-dev MCP Server
  slug: semidata-dev-mcp-yml
modified: '2026-10-31'
name: semidata-dev
nav: Providers
network: true
overview: 'semidata-dev publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Agent Integration API and Supply Chain Intelligence API. Tagged areas include Company, Semiconductor, Quantum, SupplyChain, and DataAPI.


  The semidata-dev catalog on APIs.io includes 1 Spectral governance ruleset.


  semidata-dev''s developer surface includes authentication, API reference, support, pricing, and 13 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: semidata-dev API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 1
  slug: semidata-dev-rules
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.7
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 79.1
    contract_quality: 47.1
    developer_ergonomics: 23.8
    discoverability: 61.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Semidata Dev Authentication
  slug: semidata-dev-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Semidata Dev Domain Security
  slug: semidata-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: semidata-dev
tags:
- Company
- Semiconductor
- Quantum
- SupplyChain
- DataAPI
- Intelligence
website: https://semidata.dev/
---
