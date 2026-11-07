---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The aNotepad API (version 1) provides a RESTful interface to manage notes programmatically. It allows authenticated users to create, retrieve, update, and delete notes. All endpoints require authentic
  name: aNotepad API
  slug: anotepad-api
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/anotepad-com/rate-limits/anotepad-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anotepad-com-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/anotepad-com/authentication/anotepad-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anotepad-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/anotepad-com/errors/anotepad-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anotepad-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/anotepad-com/llms/anotepad-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anotepad-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/anotepad-com/well-known/anotepad-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anotepad-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anotepad-com/hosts/anotepad-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anotepad-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/anotepad-com/vendors/anotepad-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anotepad-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/anotepad-com/security/anotepad-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anotepad-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anotepad.com/
- group: docs
  title: ''
  type: Documentation
  url: https://anotepad.com/api-access
- group: docs
  title: ''
  type: APIReference
  url: https://anotepad.com/api-access
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anotepad.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anotepad.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://anotepad.com/login
coverage:
  checked: '2026-11-01'
  detail: API documentation is publicly readable but provides no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://anotepad.com/api-access
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Anotepad provides a free, fast online notepad that autosaves as you type, requires no sign‑up, and lets you download notes as PDF or Word. It supports plain and rich‑text editing, sharing, and easy note management.
image: https://cdn.anotepad.com/favicon-32x32.png?v=2610282147
layout: provider
modified: '2026-11-01'
name: Anotepad
nav: Providers
network: true
overview: 'Anotepad is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include OnlineNotepad, Note Taking, Productivity, and Text Editor.


  Anotepad''s developer surface includes authentication, documentation, API reference, signup flow, and 10 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 2
  name: Anotepad Com Rate Limits
  slug: anotepad-com-rate-limits
scopes:
- name: Anotepad Com Scopes
  scope_count: 0
  slug: anotepad-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 24.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anotepad Com Authentication
  slug: anotepad-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Anotepad Com Domain Security
  slug: anotepad-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anotepad-com
tags:
- OnlineNotepad
- Note Taking
- Productivity
- Text Editor
website: https://anotepad.com/
---
