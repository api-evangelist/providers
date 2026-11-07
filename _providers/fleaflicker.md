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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public HTTP API for programmatic access to league data such as activity feeds, boxscores, rosters, standings, transactions, and player listings.
  name: Fleaflicker API
  slug: fleaflicker-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/fleaflicker/hosts/fleaflicker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fleaflicker-hosts.yml
- group: auth
  href: https://artifacts.apis.io/fleaflicker/security/fleaflicker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fleaflicker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fleaflicker.com/
- group: operate
  title: ''
  type: Support
  url: https://www.fleaflicker.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fleaflicker.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fleaflicker.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://www.fleaflicker.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.fleaflicker.com/nfl/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fleaflicker
coverage:
  checked: '2026-10-28'
  detail: No public API documentation or machine‑readable spec was found; attempts to fetch common OpenAPI, Swagger, GraphQL, and well‑known endpoints all returned 404.
  evidence:
  - status: 404
    url: https://www.fleaflicker.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Fleaflicker offers a fast, easy, powerful and free fantasy sports platform that lets users run fantasy football, baseball, basketball, and hockey leagues. It provides live scoring, customizable scoring options, dynasty league support, integrated league chat, and year‑round access via web and mobile apps. The service also supplies a public HTTP API at https://www.fleaflicker.com/api for programmatic access to league data, including activity feeds, boxscores, rosters, standings, transactions, player listings, and more.
image: https://d1h60c43tcq0zx.cloudfront.net/static/images/icons/apple-touch-icon-f3d0ad2586e334ad16152ed2ea83733c.png
layout: provider
modified: '2026-10-28'
name: Fleaflicker API
nav: Providers
network: true
overview: 'Fleaflicker API is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fantasy Sports, Sports, and Football.


  Fleaflicker API''s developer surface includes support, signup flow, and 7 more developer resources.'
random_paper: 16
scopes:
- name: Fleaflicker Scopes
  scope_count: 0
  slug: fleaflicker-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fleaflicker/fleaflicker-2026-11-03T132127.png
security:
- kind: authentication
  name: Fleaflicker Authentication
  slug: fleaflicker-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Fleaflicker Domain Security
  slug: fleaflicker-domain-security
  summary_line: TLSv1.2 · DMARC
slug: fleaflicker
tags:
- Company
- Fantasy Sports
- Sports
- Football
website: https://fleaflicker.com/
---
