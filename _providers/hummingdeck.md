---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Hummingdeck Agentic Access
  operation_count: 48
  slug: hummingdeck-agentic-access
  summary_line: 48 operations · 32 acting
api_count: 1
apis:
- baseURL: https://app.hummingdeck.com/api/v1
  baseurl_source: declared
  description: The Companies API from HummingDeck — 1 operation(s) for companies.
  name: HummingDeck Companies API
  slug: hummingdeck-companies-api
- baseURL: https://app.hummingdeck.com/api/v1
  baseurl_source: declared
  description: The Contacts API from HummingDeck — 1 operation(s) for contacts.
  name: HummingDeck Contacts API
  slug: hummingdeck-contacts-api
- baseURL: https://app.hummingdeck.com/api/v1
  baseurl_source: declared
  description: The Decisions API from HummingDeck — 1 operation(s) for decisions.
  name: HummingDeck Decisions API
  slug: hummingdeck-decisions-api
- baseURL: https://app.hummingdeck.com/api/v1
  baseurl_source: declared
  description: The Decks API from HummingDeck — 2 operation(s) for decks.
  name: HummingDeck Decks API
  slug: hummingdeck-decks-api
- baseURL: https://app.hummingdeck.com/api/v1
  baseurl_source: declared
  description: The Emails API from HummingDeck — 1 operation(s) for emails.
  name: HummingDeck Emails API
  slug: hummingdeck-emails-api
- baseURL: https://app.hummingdeck.com/api/v1
  baseurl_source: declared
  description: The Hooks API from HummingDeck — 2 operation(s) for hooks.
  name: HummingDeck Hooks API
  slug: hummingdeck-hooks-api
- baseURL: https://app.hummingdeck.com/api/v1
  baseurl_source: declared
  description: The Me API from HummingDeck — 1 operation(s) for me.
  name: HummingDeck Me API
  slug: hummingdeck-me-api
- baseURL: https://app.hummingdeck.com/api/v1
  baseurl_source: declared
  description: The Room Labels API from HummingDeck — 2 operation(s) for room labels.
  name: HummingDeck Room Labels API
  slug: hummingdeck-room-labels-api
- baseURL: https://app.hummingdeck.com/api/v1
  baseurl_source: declared
  description: The Room Views API from HummingDeck — 1 operation(s) for room views.
  name: HummingDeck Room Views API
  slug: hummingdeck-room-views-api
- baseURL: https://app.hummingdeck.com/api/v1
  baseurl_source: declared
  description: The Rooms API from HummingDeck — 22 operation(s) for rooms.
  name: HummingDeck Rooms API
  slug: hummingdeck-rooms-api
- baseURL: https://app.hummingdeck.com/api/v1
  baseurl_source: declared
  description: The Shares API from HummingDeck — 1 operation(s) for shares.
  name: HummingDeck Shares API
  slug: hummingdeck-shares-api
- baseURL: https://app.hummingdeck.com/api/v1
  baseurl_source: declared
  description: The Views API from HummingDeck — 1 operation(s) for views.
  name: HummingDeck Views API
  slug: hummingdeck-views-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/hummingdeck/agentic-access/hummingdeck-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hummingdeck-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/hummingdeck/plans/hummingdeck-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hummingdeck-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hummingdeck/rules/hummingdeck-rules.yml
  title: ''
  type: Spectral
  url: rules/hummingdeck-rules.yml
- group: design
  href: https://artifacts.apis.io/hummingdeck/json-ld/hummingdeck-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hummingdeck-context.jsonld
- group: design
  href: https://artifacts.apis.io/hummingdeck/vocabulary/hummingdeck-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hummingdeck-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hummingdeck/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hummingdeck/data-model/hummingdeck-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hummingdeck-data-model.yml
- group: design
  href: https://artifacts.apis.io/hummingdeck/errors/hummingdeck-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hummingdeck-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hummingdeck/conformance/hummingdeck-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hummingdeck-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hummingdeck/llms/hummingdeck-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hummingdeck-llms.txt
- group: agent
  href: https://artifacts.apis.io/hummingdeck/well-known/hummingdeck-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hummingdeck-well-known.yml
- group: other
  href: https://artifacts.apis.io/hummingdeck/hosts/hummingdeck-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hummingdeck-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hummingdeck.com/terms
- group: operate
  title: ''
  type: Support
  url: https://hummingdeck.com/support
- group: auth
  title: ''
  type: Security
  url: https://hummingdeck.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hummingdeck.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://hummingdeck.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.hummingdeck.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://hummingdeck.com/support/getting-started
- group: company
  title: ''
  type: Blog
  url: https://hummingdeck.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://hummingdeck.com/developers/api
- group: auth
  href: https://artifacts.apis.io/hummingdeck/authentication/hummingdeck-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hummingdeck-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hummingdeck/security/hummingdeck-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hummingdeck-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hummingdeck/security/hummingdeck-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hummingdeck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hummingdeck.com
created: '2026-10-24'
description: HummingDeck provides a secure document sharing platform with engagement analytics, enabling businesses to create digital sales rooms, mutual action plans, client portals, and investor data rooms. The service integrates with CRM, Slack, and other tools, offering analytics on document interactions, proposal tracking, and sales workflows. It targets sales teams, fundraising efforts, marketing, and HR use cases, delivering branded portals and comprehensive tracking for shared documents.
image: https://hummingdeck.com/og-image.png
json_schemas:
- name: CreateRoomLinkRequest
  property_count: 15
  slug: hummingdeck-create-room-link-request
- name: CreateRoomRequest
  property_count: 13
  slug: hummingdeck-create-room-request
- name: DocumentView
  property_count: 9
  slug: hummingdeck-document-view
- name: RoomItem
  property_count: 14
  slug: hummingdeck-room-item
- name: Room
  property_count: 16
  slug: hummingdeck-room
- name: ShareLink
  property_count: 11
  slug: hummingdeck-share-link
jsonld:
- class_count: 63
  name: Hummingdeck Context
  property_count: 143
  slug: hummingdeck-context
layout: provider
modified: '2026-10-24'
name: HummingDeck
nav: Providers
network: true
overview: 'HummingDeck publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Companies API, Contacts API, Decisions API, and 9 more. Tagged areas include Document Sharing, Engagement Analytics, Digital Sales Rooms, Data Rooms, and Client Portals.


  The HummingDeck catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  HummingDeck''s developer surface includes support, pricing, getting-started guide, engineering blog, API reference, authentication, and 19 more developer resources.'
plans:
- name: Hummingdeck Plans Pricing
  plan_count: 3
  slug: hummingdeck-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: HummingDeck API Rules
  rule_count: 70
  severity_counts:
    error: 62
    hint: 0
    info: 3
    warn: 5
  slug: hummingdeck-rules
scopes:
- name: Hummingdeck Scopes
  scope_count: 0
  slug: hummingdeck-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 64.5
    developer_ergonomics: 26.8
    discoverability: 73.2
    operational_transparency: 5.3
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
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
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/hummingdeck/hummingdeck-2026-11-03T133542.png
security:
- kind: authentication
  name: Hummingdeck Authentication
  slug: hummingdeck-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Hummingdeck Domain Security
  slug: hummingdeck-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Hummingdeck Vulnerability Disclosure
  slug: hummingdeck-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 1
skills:
- name: hummingdeck-create-room-with-items
  slug: hummingdeck-create-room-with-items
slug: hummingdeck
tags:
- Document Sharing
- Engagement Analytics
- Digital Sales Rooms
- Data Rooms
- Client Portals
- Integration
- Secure Sharing
website: https://hummingdeck.com
---
