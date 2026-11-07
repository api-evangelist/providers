---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Acornonaut App Agentic Access
  operation_count: 7
  slug: acornonaut-app-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- baseURL: https://acornonaut.app/api/v1
  baseurl_source: declared
  description: The Cards API from acornonaut-app — 1 operation(s) for cards.
  name: acornonaut-app Cards API
  slug: acornonaut-app-cards-api
- baseURL: https://acornonaut.app/api/v1
  baseurl_source: declared
  description: The Export API from acornonaut-app — 1 operation(s) for export.
  name: acornonaut-app Export API
  slug: acornonaut-app-export-api
- baseURL: https://acornonaut.app/api/v1
  baseurl_source: declared
  description: The Playlists API from acornonaut-app — 3 operation(s) for playlists.
  name: acornonaut-app Playlists API
  slug: acornonaut-app-playlists-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/acornonaut-app/data-model/acornonaut-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/acornonaut-app-data-model.yml
- group: agent
  href: https://artifacts.apis.io/acornonaut-app/agentic-access/acornonaut-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/acornonaut-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/acornonaut-app/plans/acornonaut-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/acornonaut-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/acornonaut-app/rules/acornonaut-app-rules.yml
  title: ''
  type: Spectral
  url: rules/acornonaut-app-rules.yml
- group: design
  href: https://artifacts.apis.io/acornonaut-app/vocabulary/acornonaut-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/acornonaut-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/acornonaut-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/acornonaut-app/authentication/acornonaut-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/acornonaut-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/acornonaut-app/errors/acornonaut-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/acornonaut-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/acornonaut-app/conformance/acornonaut-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/acornonaut-app-conformance.yml
- group: other
  href: https://artifacts.apis.io/acornonaut-app/a2a/acornonaut-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/acornonaut-app-a2a.yml
- group: other
  href: https://artifacts.apis.io/acornonaut-app/hosts/acornonaut-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acornonaut-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/acornonaut-app/vendors/acornonaut-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acornonaut-app-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://acornonaut.app/status
- group: auth
  href: https://artifacts.apis.io/acornonaut-app/security/acornonaut-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acornonaut-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acornonaut.app/
- group: docs
  title: ''
  type: Documentation
  url: https://acornonaut.app/docs/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://acornonaut.app/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://acornonaut.app/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://acornonaut.app/sign-up
- group: start
  title: ''
  type: Login
  url: https://acornonaut.app/sign-in
- group: operate
  title: ''
  type: Support
  url: https://acornonaut.app/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acornonaut.app/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acornonaut.app/terms
created: '2026-10-29'
description: Acornonaut is an AI-powered platform that transforms YouTube videos into spaced-repetition flashcards. Users can paste video URLs or playlists, and the service extracts transcripts, identifies key concepts, and generates concise flashcards that are exported to Anki or studied directly. The tool offers three free playlists, no credit card required, and aims to help learners retain knowledge efficiently.
image: https://acornonaut.app/brand/og-acornonaut.png
json_schemas:
- name: CreatePlaylistRequest
  property_count: 0
  slug: acornonaut-app-create-playlist-request
- name: PlaylistListResponse
  property_count: 0
  slug: acornonaut-app-playlist-list-response
layout: provider
modified: '2026-10-29'
name: acornonaut-app
nav: Providers
network: true
overview: 'acornonaut-app publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Cards API, Export API, and Playlists API. Tagged areas include Company, Artificial Intelligence, Education, Flashcards, and YouTube.


  The acornonaut-app catalog on APIs.io includes 1 Spectral governance ruleset.


  acornonaut-app''s developer surface includes authentication, documentation, getting-started guide, pricing, signup flow, support, and 17 more developer resources.'
plans:
- name: Acornonaut App Plans Pricing
  plan_count: 3
  slug: acornonaut-app-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Acornonaut App Rate Limits
  slug: acornonaut-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: acornonaut-app API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: acornonaut-app-rules
scopes:
- name: Acornonaut App Scopes
  scope_count: 0
  slug: acornonaut-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 50.8
    developer_ergonomics: 31.4
    discoverability: 66.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/acornonaut-app/acornonaut-app-2026-11-03T120222.png
security:
- kind: authentication
  name: Acornonaut App Authentication
  slug: acornonaut-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Acornonaut App Domain Security
  slug: acornonaut-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: playlist-management
  slug: acornonaut-app-playlist-management
slug: acornonaut-app
tags:
- Company
- Artificial Intelligence
- Education
- Flashcards
- YouTube
website: https://acornonaut.app/
---
