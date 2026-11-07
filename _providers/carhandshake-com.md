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
    agent_card: conformant
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Car Handshake API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Car Handshake API
  slug: carhandshake-com-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/carhandshake-com/rules/carhandshake-com-rules.yml
  title: ''
  type: Spectral
  url: rules/carhandshake-com-rules.yml
- group: design
  href: https://artifacts.apis.io/carhandshake-com/json-ld/carhandshake-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carhandshake-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/carhandshake-com/vocabulary/carhandshake-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carhandshake-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/carhandshake-com/data-model/carhandshake-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carhandshake-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/carhandshake-com/security/carhandshake-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/carhandshake-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/carhandshake-com/conformance/carhandshake-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carhandshake-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carhandshake-com/llms/carhandshake-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carhandshake-com-llms.txt
- group: other
  href: https://artifacts.apis.io/carhandshake-com/a2a/carhandshake-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/carhandshake-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/carhandshake-com/mcp/carhandshake-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/carhandshake-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/carhandshake-com/well-known/carhandshake-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carhandshake-com-security.txt
- group: auth
  href: https://artifacts.apis.io/carhandshake-com/well-known/carhandshake-com-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carhandshake-com-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/carhandshake-com/well-known/carhandshake-com-autoagentprotocol-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carhandshake-com-autoagentprotocol-security.txt
- group: agent
  href: https://artifacts.apis.io/carhandshake-com/well-known/carhandshake-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carhandshake-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/carhandshake-com/hosts/carhandshake-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carhandshake-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/carhandshake-com/vendors/carhandshake-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carhandshake-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carhandshake.com/terms
- group: operate
  title: ''
  type: Support
  url: https://carhandshake.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carhandshake.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://carhandshake.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://carhandshake.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/carhandshake-com/security/carhandshake-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/carhandshake-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/carhandshake-com/security/carhandshake-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carhandshake-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carhandshake.com/
created: '2026-11-03'
description: Car Handshake is a consumer-facing platform that aggregates new and used car listings from participating dealerships across the United States and Canada. It allows shoppers to compare vehicles, filter by price, make, model, and location, and directly contact dealers. The service also offers a public API (https://api.carhandshake.com/v1) providing vehicle inventory data for developers. Operated by Dealer Handshake Inc., Car Handshake emphasizes transparent pricing and a no‑login shopping experience.
image: https://carhandshake.com/assets/hero-marketplace/hero-marketplace-1774.c7976bde55c56923.jpg
json_schemas:
- name: PostV1VehiclesSearchRequest
  property_count: 1
  slug: carhandshake-com-post-v1-vehicles-search-request
- name: PostV1VehiclesSearchResponse
  property_count: 2
  slug: carhandshake-com-post-v1-vehicles-search-response
- name: PostV31CarHandshakeA2ARequest
  property_count: 4
  slug: carhandshake-com-post-v31-car-handshake-a2-arequest
- name: PostV31CarHandshakeA2AResponse
  property_count: 2
  slug: carhandshake-com-post-v31-car-handshake-a2-aresponse
jsonld:
- class_count: 4
  name: Carhandshake Com Context
  property_count: 7
  slug: carhandshake-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.carhandshake.com.
  name: Car Handshake MCP Server
  slug: carhandshake-com-mcp-yml
modified: '2026-11-03'
name: Car Handshake
nav: Providers
network: true
overview: 'Car Handshake is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Car, Marketplace, and Automotive.


  The Car Handshake catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Car Handshake''s developer surface includes support, documentation, API reference, and 20 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Car Handshake API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: carhandshake-com-rules
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 10.7
    discoverability: 48.3
    operational_transparency: 10.5
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carhandshake Com Domain Security
  slug: carhandshake-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Carhandshake Com Vulnerability Disclosure
  slug: carhandshake-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: carhandshake-com
tags:
- Company
- Car
- Marketplace
- Automotive
website: https://carhandshake.com/
---
