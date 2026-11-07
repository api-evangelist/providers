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
  band: agent-native
  dimensions:
    agent_card: flavored
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
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Agentbookable Com Agentic Access
  operation_count: 11
  slug: agentbookable-com-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- baseURL: https://agentbookable.com
  baseurl_source: declared
  description: Live slot lookup
  name: Agentbookable Availability API
  slug: agentbookable-com-availability-api
- baseURL: https://agentbookable.com
  baseurl_source: declared
  description: Create and inspect bookings
  name: Agentbookable Bookings API
  slug: agentbookable-com-bookings-api
- baseURL: https://agentbookable.com
  baseurl_source: declared
  description: Find businesses and read their capabilities
  name: Agentbookable Discovery API
  slug: agentbookable-com-discovery-api
- baseURL: https://agentbookable.com
  baseurl_source: declared
  description: User-authorization records for consequential actions
  name: Agentbookable Mandates API
  slug: agentbookable-com-mandates-api
- baseURL: https://agentbookable.com
  baseurl_source: declared
  description: List bookable services and their requirements
  name: Agentbookable Services API
  slug: agentbookable-com-services-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/agentbookable-com/agentic-access/agentbookable-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentbookable-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentbookable-com/rules/agentbookable-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentbookable-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentbookable-com/json-ld/agentbookable-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentbookable-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentbookable-com/vocabulary/agentbookable-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentbookable-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentbookable-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentbookable-com/data-model/agentbookable-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentbookable-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentbookable-com/conventions/agentbookable-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentbookable-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentbookable-com/conventions/agentbookable-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentbookable-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agentbookable-com/authentication/agentbookable-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentbookable-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentbookable-com/errors/agentbookable-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentbookable-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentbookable-com/conformance/agentbookable-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentbookable-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentbookable-com/llms/agentbookable-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentbookable-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agentbookable-com/a2a/agentbookable-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentbookable-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/agentbookable-com/mcp/agentbookable-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentbookable-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentbookable-com/mcp/agentbookable-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentbookable-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentbookable-com/hosts/agentbookable-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentbookable-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentbookable.com/terms
- group: operate
  title: ''
  type: Support
  url: https://agentbookable.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentbookable.com/privacy
- group: auth
  href: https://artifacts.apis.io/agentbookable-com/security/agentbookable-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentbookable-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentbookable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agentbookable.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agentbookable.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agentbookable.com/onboard
created: '2026-10-31'
description: Agentbookable provides a booking layer that connects AI assistants with existing business scheduling systems. It enables AI-driven customers to discover businesses, check live availability, and book appointments directly through calendars like Cal.com, Calendly, Google Calendar, and others. The platform acts as a secure intermediary, requiring user consent before finalizing bookings, and supports a range of services without replacing existing software. By integrating with popular booking tools, Agentbookable helps businesses become bookable by AI without complex setup.
image: https://agentbookable.com/logo.png
json_schemas:
- name: BookingCreate
  property_count: 8
  slug: agentbookable-com-booking-create
- name: BookingDraft
  property_count: 12
  slug: agentbookable-com-booking-draft
- name: Booking
  property_count: 12
  slug: agentbookable-com-booking
- name: Business
  property_count: 9
  slug: agentbookable-com-business
- name: ConsentCreate
  property_count: 3
  slug: agentbookable-com-consent-create
- name: MandateCreate
  property_count: 5
  slug: agentbookable-com-mandate-create
jsonld:
- class_count: 16
  name: Agentbookable Com Context
  property_count: 54
  slug: agentbookable-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentbookable.com.
  name: Agentbookable MCP Server
  slug: agentbookable-com-mcp-yml
modified: '2026-10-31'
name: Agentbookable
nav: Providers
network: true
overview: 'Agentbookable publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Availability API, Bookings API, Discovery API, and 2 more. Tagged areas include Booking, Artificial Intelligence, Scheduling, Integration, and Automation.


  The Agentbookable catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agentbookable''s developer surface includes authentication, support, documentation, API reference, getting-started guide, and 19 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Agentbookable API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: agentbookable-com-rules
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 62.6
    developer_ergonomics: 35.0
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentbookable Com Authentication
  slug: agentbookable-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentbookable Com Domain Security
  slug: agentbookable-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: booking-flow
  slug: booking-flow
slug: agentbookable-com
tags:
- Booking
- Artificial Intelligence
- Scheduling
- Integration
- Automation
- Company
website: https://agentbookable.com/
---
