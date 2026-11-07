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
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Eckari Com Agentic Access
  operation_count: 24
  slug: eckari-com-agentic-access
  summary_line: 24 operations
api_count: 1
apis:
- baseURL: https://api.eckari.com
  baseurl_source: declared
  description: The company_information API from Eckari — 15 operation(s) for company_information.
  name: Eckari Company Information API
  slug: eckari-com-company-information-api
- baseURL: https://api.eckari.com
  baseurl_source: declared
  description: The domain_intelligence API from Eckari — 2 operation(s) for domain_intelligence.
  name: Eckari Domain Intelligence API
  slug: eckari-com-domain-intelligence-api
- baseURL: https://api.eckari.com
  baseurl_source: declared
  description: The foreign_exchange API from Eckari — 1 operation(s) for foreign_exchange.
  name: Eckari Foreign Exchange API
  slug: eckari-com-foreign-exchange-api
- baseURL: https://api.eckari.com
  baseurl_source: declared
  description: The location API from Eckari — 2 operation(s) for location.
  name: Eckari Location API
  slug: eckari-com-location-api
- baseURL: https://api.eckari.com
  baseurl_source: declared
  description: The logistics API from Eckari — 1 operation(s) for logistics.
  name: Eckari Logistics API
  slug: eckari-com-logistics-api
- baseURL: https://api.eckari.com
  baseurl_source: declared
  description: The weather API from Eckari — 3 operation(s) for weather.
  name: Eckari Weather API
  slug: eckari-com-weather-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/eckari-com/agentic-access/eckari-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/eckari-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/eckari-com/rules/eckari-com-rules.yml
  title: ''
  type: Spectral
  url: rules/eckari-com-rules.yml
- group: design
  href: https://artifacts.apis.io/eckari-com/json-ld/eckari-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/eckari-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/eckari-com/vocabulary/eckari-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eckari-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/eckari-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/eckari-com/data-model/eckari-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eckari-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/eckari-com/errors/eckari-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/eckari-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/eckari-com/conformance/eckari-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eckari-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/eckari-com/llms/eckari-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eckari-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/eckari-com/mcp/eckari-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/eckari-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/eckari-com/well-known/eckari-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eckari-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/eckari-com/hosts/eckari-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eckari-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/eckari-com/vendors/eckari-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eckari-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/eckari-com/authentication/eckari-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eckari-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/eckari-com/security/eckari-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eckari-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eckari.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://eckari.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://eckari.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://api.eckari.com/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://eckari.com/developers#discovery
- group: commercial
  title: ''
  type: Pricing
  url: https://eckari.com/developers#pricing
- group: build
  title: ''
  type: Postman
  url: https://api.eckari.com/.well-known/api-catalog
created: '2026-11-06'
description: Eckari provides deterministic, authoritative, and canonical real‑world data answers for software agents. It aggregates official sources such as Companies House, SEC EDGAR, GLEIF, ECB, NWS, and Census Bureau, delivering structured information on company records, legal entities, domains, official rates, weather, and location data without requiring provider‑specific integration. The service emphasizes stable inputs, bounded execution, and clear provenance, enabling agents to trust and reason about the results.
json_schemas:
- name: company_uk_charges_output
  property_count: 7
  slug: eckari-com-company-uk-charges-output
- name: company_uk_filings_output
  property_count: 6
  slug: eckari-com-company-uk-filings-output
- name: company_uk_owners_output
  property_count: 10
  slug: eckari-com-company-uk-owners-output
- name: company_uk_profile_output
  property_count: 21
  slug: eckari-com-company-uk-profile-output
- name: entity_lei_profile_output
  property_count: 20
  slug: eckari-com-entity-lei-profile-output
- name: parcel_detect_carrier_output
  property_count: 8
  slug: eckari-com-parcel-detect-carrier-output
jsonld:
- class_count: 26
  name: Eckari Com Context
  property_count: 155
  slug: eckari-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.eckari.com.
  name: Eckari MCP Server
  slug: eckari-com-mcp-yml
modified: '2026-11-06'
name: Eckari
nav: Providers
network: true
overview: 'Eckari publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Company Information API, Domain Intelligence API, Foreign Exchange API, and 3 more. Tagged areas include Company Records, Legal Entities, Domain Data, Weather, and Location.


  The Eckari catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Eckari''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 17 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Eckari API Rules
  rule_count: 62
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 3
  slug: eckari-com-rules
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 68.1
    developer_ergonomics: 61.2
    discoverability: 61.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Eckari Com Authentication
  slug: eckari-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Eckari Com Domain Security
  slug: eckari-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: company-uk-accounts
  slug: eckari-com-company_uk_accounts
slug: eckari-com
tags:
- Company Records
- Legal Entities
- Domain Data
- Weather
- Location
- Real-World Data
website: https://eckari.com/
---
