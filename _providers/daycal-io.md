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
    agent_skills: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Daycal Io Agentic Access
  operation_count: 21
  slug: daycal-io-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 1
apis:
- baseURL: https://daycal.io
  baseurl_source: declared
  description: The owner API from Daycal — 13 operation(s) for owner.
  name: Daycal Owner API
  slug: daycal-io-owner-api
- baseURL: https://daycal.io
  baseurl_source: declared
  description: The public API from Daycal — 7 operation(s) for public.
  name: Daycal Public API
  slug: daycal-io-public-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/daycal-io/agentic-access/daycal-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/daycal-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/daycal-io/rules/daycal-io-rules.yml
  title: ''
  type: Spectral
  url: rules/daycal-io-rules.yml
- group: design
  href: https://artifacts.apis.io/daycal-io/json-ld/daycal-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/daycal-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/daycal-io/vocabulary/daycal-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/daycal-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/daycal-io/data-model/daycal-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/daycal-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/daycal-io/security/daycal-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/daycal-io-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/daycal-io/errors/daycal-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/daycal-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/daycal-io/conformance/daycal-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/daycal-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/daycal-io/llms/daycal-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/daycal-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/daycal-io/well-known/daycal-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/daycal-io-security.txt
- group: agent
  href: https://artifacts.apis.io/daycal-io/well-known/daycal-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/daycal-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/daycal-io/hosts/daycal-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daycal-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/daycal-io/vendors/daycal-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daycal-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://daycal.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daycal.io/privacy
- group: auth
  href: https://artifacts.apis.io/daycal-io/authentication/daycal-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/daycal-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/daycal-io/security/daycal-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/daycal-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/daycal-io/security/daycal-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daycal-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daycal.io/
created: '2026-11-05'
description: Daycal provides a simple scheduling page that lets others book time with you, automatically handling time‑zone differences, holidays, focus blocks and daily limits. The service integrates with Google Calendar and works with AI assistants such as Claude, ChatGPT, Cursor, and any MCP‑compatible assistant. Users share a personalized link, and bookings are added directly to their calendar without extra configuration.
image: https://daycal.io/og.png
json_schemas:
- name: Booked
  property_count: 2
  slug: daycal-io-booked
- name: Booking
  property_count: 8
  slug: daycal-io-booking
- name: ManagedBooking
  property_count: 11
  slug: daycal-io-managed-booking
- name: ManagedPage
  property_count: 7
  slug: daycal-io-managed-page
- name: Page
  property_count: 8
  slug: daycal-io-page
- name: Slot
  property_count: 2
  slug: daycal-io-slot
jsonld:
- class_count: 8
  name: Daycal Io Context
  property_count: 22
  slug: daycal-io-context
layout: provider
modified: '2026-11-05'
name: Daycal
nav: Providers
network: true
overview: 'Daycal publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Owner API and Public API. Tagged areas include Scheduling, Calendar, AI Assistant, Productivity, and Automation.


  The Daycal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Daycal''s developer surface includes authentication and 18 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Daycal API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: daycal-io-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 59.1
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Daycal Io Authentication
  slug: daycal-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Daycal Io Domain Security
  slug: daycal-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Daycal Io Vulnerability Disclosure
  slug: daycal-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: daycal-io
tags:
- Scheduling
- Calendar
- AI Assistant
- Productivity
- Automation
- Company
website: https://daycal.io/
---
