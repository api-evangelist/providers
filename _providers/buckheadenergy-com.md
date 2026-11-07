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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Buckheadenergy Com Agentic Access
  operation_count: 20
  slug: buckheadenergy-com-agentic-access
  summary_line: 20 operations
api_count: 1
apis:
- baseURL: https://www.buckheadenergy.com/api/v1
  baseurl_source: declared
  description: County-level metrics
  name: Buckhead Energy Counties API
  slug: buckheadenergy-com-counties-api
- baseURL: https://www.buckheadenergy.com/api/v1
  baseurl_source: declared
  description: Oil & Gas Encyclopedia — root-slug definition pages (educational)
  name: Buckhead Energy Encyclopedia API
  slug: buckheadenergy-com-encyclopedia-api
- baseURL: https://www.buckheadenergy.com/api/v1
  baseurl_source: declared
  description: Formation-level aggregates
  name: Buckhead Energy Formations API
  slug: buckheadenergy-com-formations-api
- baseURL: https://www.buckheadenergy.com/api/v1
  baseurl_source: declared
  description: Per-operator-per-county well-footprint cluster (wells operated and wells that have produced)
  name: Buckhead Energy Operator County API
  slug: buckheadenergy-com-operator-county-api
- baseURL: https://www.buckheadenergy.com/api/v1
  baseurl_source: declared
  description: Operator profiles and leaderboards by wells operated (no drilling activity is attributed to an operator)
  name: Buckhead Energy Operators API
  slug: buckheadenergy-com-operators-api
- baseURL: https://www.buckheadenergy.com/api/v1
  baseurl_source: declared
  description: Royalty-check payor / operator name lookup
  name: Buckhead Energy Payors API
  slug: buckheadenergy-com-payors-api
- baseURL: https://www.buckheadenergy.com/api/v1
  baseurl_source: declared
  description: 'State-level metrics: activity, cycle times, DUC aging, lateral trends, production bands, momentum, leaderboards'
  name: Buckhead Energy State API
  slug: buckheadenergy-com-state-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/buckheadenergy-com/agentic-access/buckheadenergy-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buckheadenergy-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/buckheadenergy-com/rules/buckheadenergy-com-rules.yml
  title: ''
  type: Spectral
  url: rules/buckheadenergy-com-rules.yml
- group: design
  href: https://artifacts.apis.io/buckheadenergy-com/json-ld/buckheadenergy-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buckheadenergy-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/buckheadenergy-com/vocabulary/buckheadenergy-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buckheadenergy-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/buckheadenergy-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/buckheadenergy-com/data-model/buckheadenergy-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buckheadenergy-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/buckheadenergy-com/errors/buckheadenergy-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buckheadenergy-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/buckheadenergy-com/conformance/buckheadenergy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buckheadenergy-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buckheadenergy-com/llms/buckheadenergy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buckheadenergy-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/buckheadenergy-com/mcp/buckheadenergy-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buckheadenergy-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/buckheadenergy-com/well-known/buckheadenergy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buckheadenergy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/buckheadenergy-com/hosts/buckheadenergy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buckheadenergy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/buckheadenergy-com/vendors/buckheadenergy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buckheadenergy-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buckheadenergy.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.buckheadenergy.com/press
- group: auth
  href: https://artifacts.apis.io/buckheadenergy-com/security/buckheadenergy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buckheadenergy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buckheadenergy.com/
created: '2026-11-03'
description: Buckhead Energy is a trusted mineral rights buyer operating since 2006. They help owners sell oil and gas mineral rights and royalties across multiple states, offering fair pricing, tax guidance, and a streamlined selling process. Their website provides extensive resources, guides, and state-specific information for mineral rights owners.
image: https://cdn.buckheadenergy.com/images/preview-basic.webp
json_schemas:
- name: CountyListEnvelope
  property_count: 2
  slug: buckheadenergy-com-county-list-envelope
- name: CycleTimes
  property_count: 8
  slug: buckheadenergy-com-cycle-times
- name: FormationEnvelope
  property_count: 2
  slug: buckheadenergy-com-formation-envelope
- name: Momentum
  property_count: 3
  slug: buckheadenergy-com-momentum
- name: OperatorEnvelope
  property_count: 2
  slug: buckheadenergy-com-operator-envelope
- name: SnapshotEnvelope
  property_count: 2
  slug: buckheadenergy-com-snapshot-envelope
jsonld:
- class_count: 14
  name: Buckheadenergy Com Context
  property_count: 34
  slug: buckheadenergy-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.buckheadenergy.com.
  name: Buckhead Energy MCP Server
  slug: buckheadenergy-com-mcp-yml
modified: '2026-11-03'
name: Buckhead Energy
nav: Providers
network: true
overview: 'Buckhead Energy publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Counties API, Encyclopedia API, Formations API, and 4 more. Tagged areas include Energy, Mineral Rights, Oil and Gas, Real Estate, and Texas.


  The Buckhead Energy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Buckhead Energy API Rules
  rule_count: 51
  severity_counts:
    error: 45
    hint: 0
    info: 3
    warn: 3
  slug: buckheadenergy-com-rules
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 58.6
    developer_ergonomics: 6.4
    discoverability: 65.8
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 10.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buckheadenergy Com Domain Security
  slug: buckheadenergy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buckheadenergy-com
tags:
- Energy
- Mineral Rights
- Oil and Gas
- Real Estate
- Texas
website: https://buckheadenergy.com/
---
