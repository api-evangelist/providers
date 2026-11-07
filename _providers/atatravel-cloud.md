---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Atatravel Cloud Agentic Access
  operation_count: 9
  slug: atatravel-cloud-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://api.atatravel.cloud
  baseurl_source: declared
  description: Read published building and complex profiles.
  name: ATA Travel Buildings API
  slug: atatravel-cloud-buildings-api
- baseURL: https://api.atatravel.cloud
  baseurl_source: declared
  description: Read ATA public platform pricing.
  name: ATA Travel Commercial API
  slug: atatravel-cloud-commercial-api
- baseURL: https://api.atatravel.cloud
  baseurl_source: declared
  description: Search ATA public inventory and discovery facets.
  name: ATA Travel Discovery API
  slug: atatravel-cloud-discovery-api
- baseURL: https://api.atatravel.cloud
  baseurl_source: declared
  description: Read published property details and indicative availability.
  name: ATA Travel Properties API
  slug: atatravel-cloud-properties-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/atatravel-cloud/agentic-access/atatravel-cloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/atatravel-cloud-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/atatravel-cloud/plans/atatravel-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atatravel-cloud-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/atatravel-cloud/rules/atatravel-cloud-rules.yml
  title: ''
  type: Spectral
  url: rules/atatravel-cloud-rules.yml
- group: design
  href: https://artifacts.apis.io/atatravel-cloud/json-ld/atatravel-cloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/atatravel-cloud-context.jsonld
- group: design
  href: https://artifacts.apis.io/atatravel-cloud/vocabulary/atatravel-cloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atatravel-cloud-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/atatravel-cloud/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/atatravel-cloud/data-model/atatravel-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atatravel-cloud-data-model.yml
- group: design
  href: https://artifacts.apis.io/atatravel-cloud/errors/atatravel-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/atatravel-cloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/atatravel-cloud/conformance/atatravel-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atatravel-cloud-conformance.yml
- group: other
  href: https://artifacts.apis.io/atatravel-cloud/a2a/atatravel-cloud-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/atatravel-cloud-a2a.yml
- group: other
  href: https://artifacts.apis.io/atatravel-cloud/hosts/atatravel-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atatravel-cloud-hosts.yml
- group: auth
  href: https://artifacts.apis.io/atatravel-cloud/security/atatravel-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atatravel-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atatravel.cloud/
- group: docs
  title: ''
  type: APIReference
  url: https://atatravel.cloud/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://atatravel.cloud/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atatravel.cloud/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atatravel.cloud/privacy
- group: start
  title: ''
  type: SignUp
  url: https://atatravel.cloud/host-signup
- group: operate
  title: ''
  type: Support
  url: https://atatravel.cloud/contact
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atatravel.cloud/developers
- group: docs
  title: ''
  type: Documentation
  url: https://atatravel.cloud/developers
created: '2026-11-01'
description: ATA Travel is an AI‑native travel platform that offers a no‑commission, AI‑driven travel agent for direct accommodation booking. It provides accommodation discovery, live availability search, direct booking assistance, and integrates the Model Context Protocol. Travelers can search and book stays without intermediary fees, while property owners can list their properties. The service includes pricing information, support contact, terms of service, privacy policy, and an OpenAPI specification for developers.
image: https://atatravel.cloud/logo.png
json_schemas:
- name: AvailabilityCalendar
  property_count: 8
  slug: atatravel-cloud-availability-calendar
- name: BuildingSummary
  property_count: 11
  slug: atatravel-cloud-building-summary
- name: DiscoveryContext
  property_count: 11
  slug: atatravel-cloud-discovery-context
- name: DiscoveryResponse
  property_count: 3
  slug: atatravel-cloud-discovery-response
- name: PropertyDetail
  property_count: 20
  slug: atatravel-cloud-property-detail
- name: PropertySummary
  property_count: 17
  slug: atatravel-cloud-property-summary
jsonld:
- class_count: 12
  name: Atatravel Cloud Context
  property_count: 67
  slug: atatravel-cloud-context
layout: provider
modified: '2026-11-01'
name: ATA Travel
nav: Providers
network: true
overview: 'ATA Travel publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Buildings API, Commercial API, Discovery API, and 1 more. Tagged areas include Travel, Artificial Intelligence, Booking, Accommodation, and Software-as-a-Service.


  The ATA Travel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ATA Travel''s developer surface includes API reference, pricing, signup flow, support, documentation, and 16 more developer resources.'
plans:
- name: Atatravel Cloud Plans Pricing
  plan_count: 3
  slug: atatravel-cloud-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: ATA Travel API Rules
  rule_count: 56
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 3
  slug: atatravel-cloud-rules
scopes:
- name: Atatravel Cloud Scopes
  scope_count: 0
  slug: atatravel-cloud-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 61.5
    developer_ergonomics: 21.9
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atatravel Cloud Authentication
  slug: atatravel-cloud-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atatravel Cloud Domain Security
  slug: atatravel-cloud-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: discovery
  slug: atatravel-cloud-discovery-skill
- name: property-search
  slug: atatravel-cloud-property-search-skill
slug: atatravel-cloud
tags:
- Travel
- Artificial Intelligence
- Booking
- Accommodation
- Software-as-a-Service
- NoCommission
website: https://atatravel.cloud/
---
