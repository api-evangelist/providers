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
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: documented
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ecoaloha Com Agentic Access
  operation_count: 22
  slug: ecoaloha-com-agentic-access
  summary_line: 22 operations · 6 acting
api_count: 1
apis:
- baseURL: https://ecoaloha.com/api/v1
  baseurl_source: declared
  description: The A2a API from EcoAloha — 1 operation(s) for a2a.
  name: EcoAloha A2a API
  slug: ecoaloha-com-a2a-api
- baseURL: https://ecoaloha.com/api/v1
  baseurl_source: declared
  description: The Ask API from EcoAloha — 1 operation(s) for ask.
  name: EcoAloha Ask API
  slug: ecoaloha-com-ask-api
- baseURL: https://ecoaloha.com/api/v1
  baseurl_source: declared
  description: Destinations and editorial collections. Always available.
  name: EcoAloha Discovery API
  slug: ecoaloha-com-discovery-api
- baseURL: https://ecoaloha.com/api/v1
  baseurl_source: declared
  description: Live Viator data. Gated and rate limited.
  name: EcoAloha Experiences API
  slug: ecoaloha-com-experiences-api
- baseURL: https://ecoaloha.com/api/v1
  baseurl_source: declared
  description: The Sandbox API from EcoAloha — 4 operation(s) for sandbox.
  name: EcoAloha Sandbox API
  slug: ecoaloha-com-sandbox-api
- baseURL: https://ecoaloha.com/api/v1
  baseurl_source: declared
  description: Public expiring shortlists.
  name: EcoAloha Share API
  slug: ecoaloha-com-share-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/ecoaloha-com/agentic-access/ecoaloha-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ecoaloha-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ecoaloha-com/rules/ecoaloha-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ecoaloha-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ecoaloha-com/json-ld/ecoaloha-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ecoaloha-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ecoaloha-com/vocabulary/ecoaloha-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ecoaloha-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ecoaloha-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ecoaloha-com/data-model/ecoaloha-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ecoaloha-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/ecoaloha-com/cli/ecoaloha-com-cli.yml
  title: ''
  type: CLI
  url: cli/ecoaloha-com-cli.yml
- group: design
  href: https://artifacts.apis.io/ecoaloha-com/conventions/ecoaloha-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ecoaloha-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/ecoaloha-com/conventions/ecoaloha-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ecoaloha-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/ecoaloha-com/errors/ecoaloha-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ecoaloha-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ecoaloha-com/conformance/ecoaloha-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ecoaloha-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ecoaloha-com/llms/ecoaloha-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ecoaloha-com-llms.txt
- group: other
  href: https://artifacts.apis.io/ecoaloha-com/a2a/ecoaloha-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ecoaloha-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ecoaloha-com/mcp/ecoaloha-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ecoaloha-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ecoaloha-com/well-known/ecoaloha-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ecoaloha-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ecoaloha-com/hosts/ecoaloha-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecoaloha-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ecoaloha-com/vendors/ecoaloha-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecoaloha-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/ecoaloha-com/packages/ecoaloha-com-packages.yml
  title: ''
  type: Packages
  url: packages/ecoaloha-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ecoaloha.com/terms
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@ecoaloha/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ecoaloha.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://ecoaloha.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://ecoaloha.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://ecoaloha.com/developers
- group: auth
  href: https://artifacts.apis.io/ecoaloha-com/security/ecoaloha-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecoaloha-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecoaloha.com/
created: '2026-11-06'
description: EcoAloha offers eco tours, hikes, bike and kayak trips, wildlife experiences, garden visits, and local food adventures near 133 gateway cities. Users can compare live offers, save shortlists, and book through Viator, providing sustainable travel options worldwide.
image: https://ecoaloha.com/og.jpg
json_schemas:
- name: BookingLink
  property_count: 4
  slug: ecoaloha-com-booking-link
- name: Collection
  property_count: 8
  slug: ecoaloha-com-collection
- name: Experience
  property_count: 18
  slug: ecoaloha-com-experience
- name: NearestDestination
  property_count: 4
  slug: ecoaloha-com-nearest-destination
- name: ReviewSummary
  property_count: 4
  slug: ecoaloha-com-review-summary
- name: Share
  property_count: 4
  slug: ecoaloha-com-share
jsonld:
- class_count: 9
  name: Ecoaloha Com Context
  property_count: 42
  slug: ecoaloha-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at ecoaloha.com.
  name: EcoAloha MCP Server
  slug: ecoaloha-com-mcp-yml
modified: '2026-11-06'
name: EcoAloha
nav: Providers
network: true
overview: 'EcoAloha publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Ask API, Discovery API, and 3 more. Tagged areas include Travel, Eco-tourism, Outdoor, Sustainable, and Adventure.


  The EcoAloha catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EcoAloha''s developer surface includes CLI, pricing, documentation, API reference, and 22 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: EcoAloha API Rules
  rule_count: 61
  severity_counts:
    error: 54
    hint: 0
    info: 2
    warn: 5
  slug: ecoaloha-com-rules
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 35.6
    contract_quality: 61.6
    developer_ergonomics: 32.7
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ecoaloha Com Domain Security
  slug: ecoaloha-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: discovery
  slug: ecoaloha-com-discovery
slug: ecoaloha-com
tags:
- Travel
- Eco-tourism
- Outdoor
- Sustainable
- Adventure
website: https://ecoaloha.com/
---
