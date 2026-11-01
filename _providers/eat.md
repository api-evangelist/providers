---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Reservation platform API documented at Eat's Getting Started page.
  name: Eat Reservations API
  slug: eat-reservations-api
- description: 'Eat API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-25); not the provider''s own document.'
  name: Eat API
  slug: eat-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/eat/plans/eat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eat-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/eat/rules/eat-rules.yml
  title: ''
  type: Spectral
  url: rules/eat-rules.yml
- group: design
  href: https://artifacts.apis.io/eat/json-ld/eat-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/eat-context.jsonld
- group: design
  href: https://artifacts.apis.io/eat/vocabulary/eat-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eat-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/eat/data-model/eat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eat-data-model.yml
- group: design
  href: https://artifacts.apis.io/eat/conventions/eat-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/eat-conventions.yml
- group: design
  href: https://artifacts.apis.io/eat/conventions/eat-conventions.yml
  title: ''
  type: Conventions
  url: conventions/eat-conventions.yml
- group: design
  href: https://artifacts.apis.io/eat/conformance/eat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eat-conformance.yml
- group: agent
  href: https://artifacts.apis.io/eat/well-known/eat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eat-well-known.yml
- group: other
  href: https://artifacts.apis.io/eat/hosts/eat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eat-hosts.yml
- group: other
  href: https://artifacts.apis.io/eat/vendors/eat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eat-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.eatapp.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://restaurant.eatapp.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://restaurant.eatapp.co/privacy?utm_source=Homepage&utm_medium=footer&utm_campaign=eatapp.co&utm_content=Privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://restaurant.eatapp.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://restaurant.eatapp.co/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://restaurant.eatapp.co/knowledge/getting-started
- group: auth
  href: https://artifacts.apis.io/eat/security/eat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eatapp.co
coverage:
  checked: '2026-10-24'
  detail: Docs are rendered via JavaScript with no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://restaurant.eatapp.co/knowledge/getting-started
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Eat App provides an all‑in‑one reservation platform for restaurants, cafés, bars and hotels. It offers online booking, table management, CRM, marketing tools, analytics, waitlist handling and integrations with payment and messaging services. The platform helps venues streamline front‑of‑house operations, improve guest experiences and increase reservations through AI‑powered features and multi‑channel booking.
image: https://framerusercontent.com/assets/r86joZvMVPAO9LFSSdAM0ygprE.png
json_schemas:
- name: PatchReservationsIdorkeyRequest
  property_count: 3
  slug: eat-patch-reservations-idorkey-request
- name: PostAvailabilityRangeRequest
  property_count: 4
  slug: eat-post-availability-range-request
- name: PostAvailabilityRangeResponse
  property_count: 1
  slug: eat-post-availability-range-response
- name: PostReservationsRequest
  property_count: 14
  slug: eat-post-reservations-request
jsonld:
- class_count: 4
  name: Eat Context
  property_count: 20
  slug: eat-context
layout: provider
modified: '2026-10-24'
name: Eat
nav: Providers
network: true
overview: 'Eat is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Reservations API, and 1 more. Tagged areas include Company, Restaurant, Reservation, SaaS, and Hospitality.


  The Eat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Eat''s developer surface includes pricing, engineering blog, getting-started guide, and 16 more developer resources.'
plans:
- name: Eat Plans Pricing
  plan_count: 12
  slug: eat-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Eat API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: eat-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 35.6
    contract_quality: 20.9
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eat Domain Security
  slug: eat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: eat
tags:
- Company
- Restaurant
- Reservation
- SaaS
- Hospitality
website: https://eatapp.co
---
