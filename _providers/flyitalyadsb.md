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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Flyitalyadsb Agentic Access
  operation_count: 4
  slug: flyitalyadsb-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api.flyitalyadsb.com
  baseurl_source: declared
  description: What the network is receiving now.
  name: FlyItalyADSB Live API
  slug: flyitalyadsb-live-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/flyitalyadsb/data-model/flyitalyadsb-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flyitalyadsb-data-model.yml
- group: agent
  href: https://artifacts.apis.io/flyitalyadsb/agentic-access/flyitalyadsb-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flyitalyadsb-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/flyitalyadsb/rules/flyitalyadsb-rules.yml
  title: ''
  type: Spectral
  url: rules/flyitalyadsb-rules.yml
- group: design
  href: https://artifacts.apis.io/flyitalyadsb/vocabulary/flyitalyadsb-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/flyitalyadsb-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/flyitalyadsb/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/flyitalyadsb/errors/flyitalyadsb-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flyitalyadsb-problem-types.yml
- group: design
  href: https://artifacts.apis.io/flyitalyadsb/conformance/flyitalyadsb-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flyitalyadsb-conformance.yml
- group: agent
  href: https://artifacts.apis.io/flyitalyadsb/llms/flyitalyadsb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flyitalyadsb-llms.txt
- group: agent
  href: https://artifacts.apis.io/flyitalyadsb/mcp/flyitalyadsb-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/flyitalyadsb-mcp.yml
- group: agent
  href: https://artifacts.apis.io/flyitalyadsb/well-known/flyitalyadsb-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flyitalyadsb-well-known.yml
- group: other
  href: https://artifacts.apis.io/flyitalyadsb/hosts/flyitalyadsb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flyitalyadsb-hosts.yml
- group: other
  href: https://artifacts.apis.io/flyitalyadsb/vendors/flyitalyadsb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flyitalyadsb-vendors.yml
- group: build
  href: https://artifacts.apis.io/flyitalyadsb/packages/flyitalyadsb-packages.yml
  title: ''
  type: SDKs
  url: packages/flyitalyadsb-packages.yml
- group: build
  href: https://artifacts.apis.io/flyitalyadsb/packages/flyitalyadsb-packages.yml
  title: ''
  type: Packages
  url: packages/flyitalyadsb-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flyitalyadsb.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flyitalyadsb.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://flyitalyadsb.com/dati/api/docs/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://flyitalyadsb.com/en/data/api/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/flyitalyadsb/security/flyitalyadsb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flyitalyadsb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flyitalyadsb.com
- group: docs
  title: ''
  type: Documentation
  url: https://flyitalyadsb.com/en/data/api/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flyitalyadsb
- group: docs
  title: ''
  type: APIReference
  url: https://raw.githubusercontent.com/flyitalyadsb/adsb-api/master/openapi/openapi.json
created: '2026-11-02'
description: FlyItalyADSB operates a global community network that collects unfiltered ADS‑B and MLAT data from around 3,200 volunteer receivers worldwide. Founded in Italy in 2020, the service provides live aircraft positions as well as historical tracks, accessible via a public API with generous free limits and paid plans for higher usage. The API returns data in the same format as readsb and tar1090, and also offers an ADS‑B Exchange‑compatible endpoint. Users can obtain self‑serve API keys, view aircraft on the Lightcone map, and contribute data through feeder scripts. The platform supports commercial use under its licensing terms and is documented in an OpenAPI 3.1 specification hosted on GitHub.
image: https://avatars.githubusercontent.com/u/77549844?v=4
json_schemas:
- name: AircraftList
  property_count: 0
  slug: flyitalyadsb-aircraft-list
- name: Aircraft
  property_count: 0
  slug: flyitalyadsb-aircraft
layout: provider
mcp_servers:
- description: Remote MCP server at flyitalyadsb.com.
  name: FlyItalyADSB MCP Server
  slug: flyitalyadsb-mcp-yml
modified: '2026-11-02'
name: FlyItalyADSB
nav: Providers
network: true
overview: 'FlyItalyADSB publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Live API. Tagged areas include ADS-B, MLAT, Aviation, Flight Tracking, and Open Data.


  The FlyItalyADSB catalog on APIs.io includes 1 Spectral governance ruleset.


  FlyItalyADSB''s developer surface includes changelog, getting-started guide, documentation, API reference, and 19 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: FlyItalyADSB API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: flyitalyadsb-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 51.4
    developer_ergonomics: 23.2
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Flyitalyadsb Domain Security
  slug: flyitalyadsb-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 2
skills:
- name: aircraft-history
  slug: aircraft-history
- name: aircraft-near
  slug: aircraft-near
slug: flyitalyadsb
tags:
- ADS-B
- MLAT
- Aviation
- Flight Tracking
- Open Data
website: https://flyitalyadsb.com
---
