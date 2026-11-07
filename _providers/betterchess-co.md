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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for BetterChess connector and services as described in the documentation. No public machine‑readable contract was found; the docs are rendered HTML without an OpenAPI, GraphQL, AsyncAPI, gRPC or W
  name: BetterChess API
  slug: betterchess-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/betterchess-co/llms/betterchess-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/betterchess-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/betterchess-co/well-known/betterchess-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/betterchess-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/betterchess-co/hosts/betterchess-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betterchess-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/betterchess-co/vendors/betterchess-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betterchess-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betterchess.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betterchess.co/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://betterchess.co/docs
- group: auth
  href: https://artifacts.apis.io/betterchess-co/security/betterchess-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betterchess-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betterchess.co/
coverage:
  checked: '2026-11-02'
  detail: Documentation is a JavaScript‑rendered site with no machine‑readable OpenAPI or other spec.
  evidence:
  - status: 200
    url: https://betterchess.co/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: BetterChess sells printed chess puzzle card decks that provide mate-in-1, mate-in-2, forks, pins and skewers puzzles. Each card shows a position on the front and the solution on the back, with a QR code to play the puzzle online. The company also offers a web app and an MCP connector for Claude that provides real engine analysis and coaching.
image: https://betterchess.co/og.png
layout: provider
modified: '2026-11-02'
name: BetterChess
nav: Providers
network: true
overview: 'BetterChess is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Chess, Puzzles, Cards, E-Commerce, and Education.


  BetterChess'' developer surface includes documentation and 8 more developer resources.'
plans:
- name: Betterchess Co Plans Pricing
  plan_count: 0
  slug: betterchess-co-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Betterchess Co Rate Limits
  slug: betterchess-co-rate-limits
scopes:
- name: Betterchess Co Scopes
  scope_count: 0
  slug: betterchess-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 23.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Betterchess Co Authentication
  slug: betterchess-co-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Betterchess Co Domain Security
  slug: betterchess-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: betterchess-co
tags:
- Chess
- Puzzles
- Cards
- E-Commerce
- Education
website: https://betterchess.co/
---
