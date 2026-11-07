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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://charter.boats
  baseurl_source: declared
  description: 'Charter Boats API as documented publicly: 60 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Charter Boats API
  slug: charter-boats-api
artifact_total: 11
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://charter.boats/terms
- group: design
  href: https://artifacts.apis.io/charter-boats/rules/charter-boats-rules.yml
  title: ''
  type: Spectral
  url: rules/charter-boats-rules.yml
- group: design
  href: https://artifacts.apis.io/charter-boats/json-ld/charter-boats-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/charter-boats-context.jsonld
- group: design
  href: https://artifacts.apis.io/charter-boats/vocabulary/charter-boats-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/charter-boats-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/charter-boats/data-model/charter-boats-data-model.yml
  title: ''
  type: DataModel
  url: data-model/charter-boats-data-model.yml
- group: design
  href: https://artifacts.apis.io/charter-boats/conformance/charter-boats-conformance.yml
  title: ''
  type: Conformance
  url: conformance/charter-boats-conformance.yml
- group: agent
  href: https://artifacts.apis.io/charter-boats/llms/charter-boats-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/charter-boats-llms.txt
- group: agent
  href: https://artifacts.apis.io/charter-boats/mcp/charter-boats-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/charter-boats-mcp.yml
- group: agent
  href: https://artifacts.apis.io/charter-boats/well-known/charter-boats-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/charter-boats-well-known.yml
- group: other
  href: https://artifacts.apis.io/charter-boats/hosts/charter-boats-hosts.yml
  title: ''
  type: Hosts
  url: hosts/charter-boats-hosts.yml
- group: other
  href: https://artifacts.apis.io/charter-boats/vendors/charter-boats-vendors.yml
  title: ''
  type: Vendors
  url: vendors/charter-boats-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://charter.boats/login
- group: auth
  href: https://artifacts.apis.io/charter-boats/security/charter-boats-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/charter-boats-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://charter.boats/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.charter.boats/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.charter.boats/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.charter.boats/guide/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://charter.boats/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://charter.boats/privacy
coverage:
  checked: '2026-11-03'
  detail: The API reference requires an X-API-Key header; unauthenticated GETs to spec URLs return 403 bot protection.
  evidence:
  - status: 403
    url: https://charter.boats/openapi.json
  reason: auth-required
  state: gated
created: '2026-11-03'
description: Charter Boats is a global platform offering bareboat and skippered sailing charters across the Mediterranean and worldwide. With a fleet of over 14,000 boats, including catamarans, sailboats, motor yachts, and RIBs, the service provides real-time availability, detailed boat tours, and comprehensive destination guides. Users can search, compare, and book charters, access marina maps, and receive live weather and wind updates. The company partners with MMK and NauSYS for operator dashboards and calendar sync, and supports secure payments via Stripe. It also offers tools for boat owners to list and manage their fleets.
image: https://charter.boats/images/hero-bg.jpg
json_schemas:
- name: GetAiBoatsIdStandoutsResponse
  property_count: 9
  slug: charter-boats-get-ai-boats-id-standouts-response
- name: GetAiPoisIdResponse
  property_count: 15
  slug: charter-boats-get-ai-pois-id-response
- name: GetAiTripsIdResponse
  property_count: 29
  slug: charter-boats-get-ai-trips-id-response
- name: GetApiAiPoisResponse
  property_count: 3
  slug: charter-boats-get-api-ai-pois-response
- name: GetApiAiPois297Cb8Af90Cd4AccAd6A28325Cb105C8Response
  property_count: 15
  slug: charter-boats-get-api-ai-pois297-cb8-af90-cd4-acc-ad6-a28325-cb105-c8-response
- name: GetApiAiTrips0Cbae6C3D6294A2B965E50B26E3Bd37CResponse
  property_count: 17
  slug: charter-boats-get-api-ai-trips0-cbae6-c3-d6294-a2-b965-e50-b26-e3-bd37-cresponse
jsonld:
- class_count: 12
  name: Charter Boats Context
  property_count: 50
  slug: charter-boats-context
layout: provider
mcp_servers:
- description: Remote MCP server at charter.boats.
  name: Charter Boats MCP Server
  slug: charter-boats-mcp-yml
modified: '2026-11-03'
name: Charter Boats
nav: Providers
network: true
overview: 'Charter Boats is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sailing, Charter, Boats, and Travel.


  The Charter Boats catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Charter Boats'' developer surface includes documentation, API reference, getting-started guide, support, and 15 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Charter Boats API Rules
  rule_count: 47
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 4
  slug: charter-boats-rules
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
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
  name: Charter Boats Domain Security
  slug: charter-boats-domain-security
  summary_line: TLSv1.3 · DMARC
slug: charter-boats
tags:
- Company
- Sailing
- Charter
- Boats
- Travel
website: https://charter.boats/
---
