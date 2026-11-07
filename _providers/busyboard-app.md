---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for programmatic access to BusyBoard availability data.
  name: BusyBoard API
  slug: busyboard-api
- baseURL: https://busyboard.app/api/v1
  baseurl_source: declared
  description: REST API for programmatic access to BusyBoard availability data.
  name: BusyBoard API API
  slug: busyboard-api-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/busyboard-app/rules/busyboard-app-rules.yml
  title: ''
  type: Spectral
  url: rules/busyboard-app-rules.yml
- group: design
  href: https://artifacts.apis.io/busyboard-app/json-ld/busyboard-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/busyboard-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/busyboard-app/vocabulary/busyboard-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/busyboard-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/busyboard-app/conventions/busyboard-app-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/busyboard-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/busyboard-app/conventions/busyboard-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/busyboard-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/busyboard-app/conformance/busyboard-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/busyboard-app-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/busyboard-app/plans/busyboard-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/busyboard-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/busyboard-app/data-model/busyboard-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/busyboard-app-data-model.yml
- group: auth
  href: https://artifacts.apis.io/busyboard-app/security/busyboard-app-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/busyboard-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/busyboard-app/authentication/busyboard-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/busyboard-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/busyboard-app/errors/busyboard-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/busyboard-app-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/busyboard-app/llms/busyboard-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/busyboard-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/busyboard-app/well-known/busyboard-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/busyboard-app-security.txt
- group: agent
  href: https://artifacts.apis.io/busyboard-app/well-known/busyboard-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/busyboard-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/busyboard-app/hosts/busyboard-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/busyboard-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/busyboard-app/vendors/busyboard-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/busyboard-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://busyboard.app/terms
- group: start
  title: ''
  type: SignUp
  url: https://busyboard.app/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://busyboard.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://busyboard.app/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://busyboard.app/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://busyboard.app/guides/let-your-ai-assistant-manage-your-availability
- group: docs
  title: ''
  type: APIReference
  url: https://busyboard.app/llms.txt
- group: auth
  href: https://artifacts.apis.io/busyboard-app/security/busyboard-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/busyboard-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/busyboard-app/security/busyboard-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/busyboard-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://busyboard.app/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://busyboard.app/openapi.yaml
  - status: 401
    url: https://busyboard.app/api/mcp
  - status: 200
    url: https://busyboard.app/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: BusyBoard is a free scheduling tool that lets users share their availability without exposing calendar details. It integrates with Google Calendar and Microsoft Outlook, offers group calendar overlays, public shareable links, and a Pro plan with advanced features like event scheduling and real‑time sync. The service emphasizes privacy, encrypting calendar tokens and only showing free/busy blocks.
image: https://busyboard.app/opengraph-image?89b3763a23c15e84
json_schemas:
- name: Block
  property_count: 7
  slug: busyboard-app-block
- name: BookingProposalRequest
  property_count: 6
  slug: busyboard-app-booking-proposal-request
- name: BookingProposalResponse
  property_count: 6
  slug: busyboard-app-booking-proposal-response
- name: Group
  property_count: 8
  slug: busyboard-app-group
- name: Pagination
  property_count: 4
  slug: busyboard-app-pagination
- name: Person
  property_count: 6
  slug: busyboard-app-person
jsonld:
- class_count: 8
  name: Busyboard App Context
  property_count: 33
  slug: busyboard-app-context
layout: provider
modified: '2026-11-03'
name: BusyBoard
nav: Providers
network: true
overview: 'BusyBoard publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Scheduling, Calendar, Privacy, Free, and Software-as-a-Service.


  The BusyBoard catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BusyBoard''s developer surface includes authentication, signup flow, pricing, documentation, getting-started guide, API reference, and 20 more developer resources.'
plans:
- name: Busyboard App Plans Pricing
  plan_count: 6
  slug: busyboard-app-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: BusyBoard API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: busyboard-app-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 58.9
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Busyboard App Authentication
  slug: busyboard-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Busyboard App Domain Security
  slug: busyboard-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Busyboard App Vulnerability Disclosure
  slug: busyboard-app-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: busyboard-app
tags:
- Scheduling
- Calendar
- Privacy
- Free
- Software-as-a-Service
website: https://busyboard.app/
---
