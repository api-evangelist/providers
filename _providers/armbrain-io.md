---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API (gated behind authentication) for Armbrain AI memory platform.
  name: Armbrain API
  slug: armbrain-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/armbrain-io/llms/armbrain-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/armbrain-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/armbrain-io/well-known/armbrain-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/armbrain-io-security.txt
- group: auth
  href: https://artifacts.apis.io/armbrain-io/well-known/armbrain-io-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/armbrain-io-api-security.txt
- group: agent
  href: https://artifacts.apis.io/armbrain-io/well-known/armbrain-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/armbrain-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/armbrain-io/hosts/armbrain-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/armbrain-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/armbrain-io/vendors/armbrain-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/armbrain-io-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://armbrain.io/status
- group: auth
  title: ''
  type: Security
  url: https://armbrain.io/security
- group: docs
  title: ''
  type: Documentation
  url: https://armbrain.io/guides
- group: operate
  title: ''
  type: ChangeLog
  url: https://armbrain.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://armbrain.io/guides/best-agentic-memory-setup
- group: auth
  href: https://artifacts.apis.io/armbrain-io/security/armbrain-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/armbrain-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/armbrain-io/security/armbrain-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/armbrain-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://armbrain.io/
- group: operate
  title: ''
  type: Support
  url: https://armbrain.io/support
- group: company
  title: ''
  type: Blog
  url: https://armbrain.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://armbrain.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://armbrain.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://armbrain.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://armbrain.io/privacy
coverage:
  checked: '2026-11-02'
  detail: API documentation is behind a sign‑in page at https://hq.armbrain.io, requiring authentication to access.
  evidence:
  - status: 200
    url: https://hq.armbrain.io
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Armbrain is AI memory for fractionals running multiple clients, made by Volacci in Austin, Texas. It keeps a separate mind for each client or business, so your AI assistant remembers each one without mixing them up. It works across several AI platforms, including Claude, Claude Code, Cursor, ChatGPT, Grok, Gemini and Muse.
image: https://armbrain.io/logo-512.png
layout: provider
modified: '2026-11-01'
name: Armbrain
nav: Providers
network: true
overview: 'Armbrain is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, Productivity, Software-as-a-Service, and Multi-Client.


  Armbrain''s developer surface includes documentation, changelog, getting-started guide, support, engineering blog, pricing, signup flow, and 13 more developer resources.'
random_paper: 1
scopes:
- name: Armbrain Io Scopes
  scope_count: 0
  slug: armbrain-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.6
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 28.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Armbrain Io Authentication
  slug: armbrain-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Armbrain Io Domain Security
  slug: armbrain-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Armbrain Io Vulnerability Disclosure
  slug: armbrain-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: armbrain-io
tags:
- Artificial Intelligence
- Memory
- Productivity
- Software-as-a-Service
- Multi-Client
website: https://armbrain.io/
---
