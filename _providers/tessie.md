---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 67
  human_in_the_loop: 11
  name: Tessie Agentic Access
  operation_count: 92
  slug: tessie-agentic-access
  summary_line: 92 operations · 67 acting · 11 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.tessie.com
  baseurl_source: declared
  description: Driver management endpoints
  name: Tessie Driver Management API
  slug: tessie-driver-management-api
- baseURL: https://api.tessie.com
  baseurl_source: declared
  description: Vehicle telemetry configuration endpoints
  name: Tessie Telemetry Configuration API
  slug: tessie-telemetry-configuration-api
- baseURL: https://api.tessie.com
  baseurl_source: declared
  description: Vehicle command endpoints
  name: Tessie Vehicle Commands API
  slug: tessie-vehicle-commands-api
- baseURL: https://api.tessie.com
  baseurl_source: declared
  description: Vehicle data endpoints
  name: Tessie Vehicle Data API
  slug: tessie-vehicle-data-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/tessie/agentic-access/tessie-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tessie-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/tessie/rules/tessie-rules.yml
  title: ''
  type: Spectral
  url: rules/tessie-rules.yml
- group: design
  href: https://artifacts.apis.io/tessie/json-ld/tessie-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tessie-context.jsonld
- group: design
  href: https://artifacts.apis.io/tessie/vocabulary/tessie-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tessie-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tessie/data-model/tessie-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tessie-data-model.yml
- group: design
  href: https://artifacts.apis.io/tessie/conformance/tessie-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tessie-conformance.yml
- group: other
  href: https://artifacts.apis.io/tessie/overlays/tessie-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tessie-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/tessie/llms/tessie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tessie-llms.txt
- group: other
  href: https://artifacts.apis.io/tessie/a2a/tessie-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tessie-a2a.yml
- group: agent
  href: https://artifacts.apis.io/tessie/mcp/tessie-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tessie-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tessie/well-known/tessie-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tessie-well-known.yml
- group: other
  href: https://artifacts.apis.io/tessie/hosts/tessie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tessie-hosts.yml
- group: other
  href: https://artifacts.apis.io/tessie/vendors/tessie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tessie-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tessie.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tessietech
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.tessie.com/reference/quick-start
- group: docs
  title: ''
  type: APIReference
  url: https://developer.tessie.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/tessie/authentication/tessie-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tessie-authentication.yml
- group: auth
  href: https://artifacts.apis.io/tessie/security/tessie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tessie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tessie.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tessie.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.tessie.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tessie.com/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.tessie.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tessie.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tessie.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tessie.com/terms
created: '2026-10-28'
description: Tessie provides a Tesla management platform offering apps, analytics, automations and APIs for the world's most sophisticated vehicles. Trusted by over 500,000 Tesla drivers and fleet managers, it enables comprehensive vehicle data access, remote control, and fleet optimization through robust RESTful APIs and webhooks.
json_schemas:
- name: Charge
  property_count: 15
  slug: tessie-charge
- name: Condensed History States
  property_count: 35
  slug: tessie-condensed-history-states
- name: CurrentState
  property_count: 21
  slug: tessie-current-state
- name: Drive
  property_count: 20
  slug: tessie-drive
- name: Historical State
  property_count: 35
  slug: tessie-history-state
- name: ReleaseNotes
  property_count: 3
  slug: tessie-release-notes
jsonld:
- class_count: 7
  name: Tessie Context
  property_count: 113
  slug: tessie-context
layout: provider
mcp_servers:
- description: Remote MCP server at developer.tessie.com.
  name: Tessie MCP Server
  slug: tessie-mcp-yml
modified: '2026-10-28'
name: Tessie
nav: Providers
network: true
overview: 'Tessie publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Driver Management API, Telemetry Configuration API, Vehicle Commands API, and 1 more. Tagged areas include Company, Tesla, Fleet Management, Automotive, and APIs.


  The Tessie catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tessie''s developer surface includes getting-started guide, API reference, authentication, documentation, pricing, and 22 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Tessie API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: tessie-rules
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 19.7
    contract_quality: 61.1
    developer_ergonomics: 54.8
    discoverability: 61.7
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tessie Authentication
  slug: tessie-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tessie Domain Security
  slug: tessie-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tessie
tags:
- Company
- Tesla
- Fleet Management
- Automotive
- APIs
website: https://tessie.com/
---
