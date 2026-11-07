---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 69
  human_in_the_loop: 1
  name: Aisle Wedding Agentic Access
  operation_count: 118
  slug: aisle-wedding-agentic-access
  summary_line: 118 operations · 69 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Reusable event dress guidance.
  name: Aisle Dress codes API
  slug: aisle-wedding-dress-codes-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Wedding schedule and invitations.
  name: Aisle Events API
  slug: aisle-wedding-events-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Individual and group invitation codes for custom frontends. Access grants name explicit guests and never change RSVP Parties. All operations require a server-side wedding API key; a guest session toke
  name: Aisle Guest access API
  slug: aisle-wedding-guest-access-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Guestbook notes, song requests, and predictions.
  name: Aisle Guest content API
  slug: aisle-wedding-guest-content-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Manage the wedding guest list and room assignments.
  name: Aisle Guests API
  slug: aisle-wedding-guests-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Wedding-owned uploads, gallery photos, and the site cover.
  name: Aisle Media API
  slug: aisle-wedding-media-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Service discovery and connectivity checks.
  name: Aisle Meta API
  slug: aisle-wedding-meta-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Named households whose members reply together. Codes and guest sessions are managed by your application.
  name: Aisle Parties API
  slug: aisle-wedding-parties-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Create guest checkouts and read the wedding-scoped payment ledger.
  name: Aisle Payments API
  slug: aisle-wedding-payments-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Connect and inspect the couple payout account.
  name: Aisle Payouts API
  slug: aisle-wedding-payouts-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Recommendations and frequently asked questions.
  name: Aisle Recommendations API
  slug: aisle-wedding-recommendations-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Registry items and settled contribution ledger views.
  name: Aisle Registry API
  slug: aisle-wedding-registry-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Read and record guest replies and event invitations.
  name: Aisle RSVP API
  slug: aisle-wedding-rsvp-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Guest-site content and publication.
  name: Aisle Site API
  slug: aisle-wedding-site-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Canonical wedding counts and settled money totals.
  name: Aisle Statistics API
  slug: aisle-wedding-statistics-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Properties, rooms, rates, payment schedules, and stay dates.
  name: Aisle Stays API
  slug: aisle-wedding-stays-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Airports and their transport options.
  name: Aisle Travel API
  slug: aisle-wedding-travel-api
- baseURL: https://api.aisle.wedding/v1
  baseurl_source: declared
  description: Wedding identity and dates.
  name: Aisle Wedding API
  slug: aisle-wedding-wedding-api
artifact_total: 31
common:
- group: agent
  href: https://artifacts.apis.io/aisle-wedding/agentic-access/aisle-wedding-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aisle-wedding-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/aisle-wedding/plans/aisle-wedding-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aisle-wedding-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aisle-wedding/rules/aisle-wedding-rules.yml
  title: ''
  type: Spectral
  url: rules/aisle-wedding-rules.yml
- group: design
  href: https://artifacts.apis.io/aisle-wedding/json-ld/aisle-wedding-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aisle-wedding-context.jsonld
- group: design
  href: https://artifacts.apis.io/aisle-wedding/vocabulary/aisle-wedding-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aisle-wedding-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aisle-wedding/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aisle-wedding/data-model/aisle-wedding-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aisle-wedding-data-model.yml
- group: design
  href: https://artifacts.apis.io/aisle-wedding/errors/aisle-wedding-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aisle-wedding-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aisle-wedding/conformance/aisle-wedding-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aisle-wedding-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aisle-wedding/llms/aisle-wedding-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aisle-wedding-llms.txt
- group: agent
  href: https://artifacts.apis.io/aisle-wedding/well-known/aisle-wedding-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aisle-wedding-well-known.yml
- group: other
  href: https://artifacts.apis.io/aisle-wedding/hosts/aisle-wedding-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aisle-wedding-hosts.yml
- group: other
  href: https://artifacts.apis.io/aisle-wedding/vendors/aisle-wedding-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aisle-wedding-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aisle.wedding/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aisle.wedding/privacy
- group: start
  title: ''
  type: Login
  url: https://aisle.wedding/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://aisle.wedding/guides
- group: docs
  title: ''
  type: APIReference
  url: https://api.aisle.wedding/docs
- group: auth
  href: https://artifacts.apis.io/aisle-wedding/authentication/aisle-wedding-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aisle-wedding-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aisle-wedding/security/aisle-wedding-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aisle-wedding-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aisle.wedding/
- group: commercial
  title: ''
  type: Pricing
  url: https://aisle.wedding/pricing
created: '2026-11-01'
description: Aisle provides a destination wedding venue marketplace and website builder, enabling couples to discover venues worldwide, estimate costs, and manage planning through an integrated platform. Users can browse venues, create wedding websites, collect RSVPs, and handle payments, with features like budgeting tools, checklists, and timeline planning. The service also offers AI assistance via ChatGPT and supports planners with customizable tools and real‑wedding showcases.
image: https://aisle.wedding/og/founders.jpg
json_schemas:
- name: Event
  property_count: 22
  slug: aisle-wedding-event
- name: GuestCreate
  property_count: 13
  slug: aisle-wedding-guest-create
- name: GuestImportRow
  property_count: 9
  slug: aisle-wedding-guest-import-row
- name: GuestPatch
  property_count: 24
  slug: aisle-wedding-guest-patch
- name: Guest
  property_count: 33
  slug: aisle-wedding-guest
- name: Wedding
  property_count: 18
  slug: aisle-wedding-wedding
jsonld:
- class_count: 111
  name: Aisle Wedding Context
  property_count: 289
  slug: aisle-wedding-context
layout: provider
modified: '2026-11-01'
name: Aisle
nav: Providers
network: true
overview: 'Aisle publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dress codes API, Events API, Guest access API, and 15 more. Tagged areas include Wedding, Planning, Software-as-a-Service, and Marketplace.


  The Aisle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aisle''s developer surface includes documentation, API reference, authentication, pricing, and 18 more developer resources.'
plans:
- name: Aisle Wedding Plans Pricing
  plan_count: 2
  slug: aisle-wedding-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Aisle API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 2
  slug: aisle-wedding-rules
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 22.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aisle Wedding Authentication
  slug: aisle-wedding-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aisle Wedding Domain Security
  slug: aisle-wedding-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: aisle-wedding-create-guest-assign-room
  slug: aisle-wedding-create-guest-assign-room
slug: aisle-wedding
tags:
- Wedding
- Planning
- Software-as-a-Service
- Marketplace
website: https://aisle.wedding/
---
