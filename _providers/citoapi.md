---
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Cito UFC API provides esports data including UFC match info and statistics.
  name: Cito UFC API
  slug: cito-ufc-api
- baseURL: https://api.citoapi.com/api/v1
  baseurl_source: declared
  description: 'Bare Knuckle Fighting Championship: every event since 2018, full cards, results, round-by-round punch statistics, fighters, official rankings and live cards.'
  name: Cito CS2 API BKFC API
  slug: citoapi-bkfc-api
- baseURL: https://api.citoapi.com/api/v1
  baseurl_source: declared
  description: Call of Duty (CDL) matches, live scores, players, organizations, tournaments, standings, transfers, and leaderboards.
  name: Cito CS2 API Call of Duty API
  slug: citoapi-call-of-duty-api
- baseURL: https://api.citoapi.com/api/v1
  baseurl_source: declared
  description: 'Counter-Strike 2: live matches, results, maps, rounds, teams, players, events, rankings, stats and skins. **Beta.** CS2 is in beta. If anything looks wrong, email support@citoapi.com with the endpoint'
  name: Cito CS2 API CS2 API
  slug: citoapi-cs2-api
- baseURL: https://api.citoapi.com/api/v1
  baseurl_source: declared
  description: Dota 2 esports matches, teams, players, tournaments, player stats, and radar snapshots.
  name: Cito CS2 API Dota 2 API
  slug: citoapi-dota-2-api
- baseURL: https://api.citoapi.com/api/v1
  baseurl_source: declared
  description: Fortnite competitive matches, tournaments/events, live leaderboards, players, orgs, pro rankings, transfers, and earnings leaderboards.
  name: Cito CS2 API Fortnite API
  slug: citoapi-fortnite-api
- baseURL: https://api.citoapi.com/api/v1
  baseurl_source: declared
  description: Generate QR codes with optional logo overlay.
  name: Cito CS2 API QR Code API
  slug: citoapi-qr-code-api
- baseURL: https://api.citoapi.com/api/v1
  baseurl_source: declared
  description: 'Real American Freestyle professional wrestling: events, cards, results with per-period scores and takedowns, athletes, champions and live results.'
  name: Cito CS2 API RAF Wrestling API
  slug: citoapi-raf-wrestling-api
- baseURL: https://api.citoapi.com/api/v1
  baseurl_source: declared
  description: The Tennis API from Cito CS2 API — 54 operation(s) for tennis.
  name: Cito CS2 API Tennis API
  slug: citoapi-tennis-api
- baseURL: https://api.citoapi.com/api/v1
  baseurl_source: declared
  description: UFC rankings, fighters, fighter profile stats, events, fight cards, bouts, and results.
  name: Cito CS2 API UFC API
  slug: citoapi-ufc-api
- baseURL: https://api.citoapi.com/api/v1
  baseurl_source: declared
  description: Health and status endpoints.
  name: Cito CS2 API Utility API
  slug: citoapi-utility-api
artifact_total: 24
asyncapis:
- description: ''
  name: Citoapi Webhooks
  slug: citoapi-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/rules/citoapi-rules.yml
  title: ''
  type: Spectral
  url: rules/citoapi-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/json-ld/citoapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/citoapi-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/vocabulary/citoapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/citoapi-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/conformance/citoapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/citoapi-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/rate-limits/citoapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/citoapi-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/plans/citoapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/citoapi-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/asyncapi/citoapi-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/citoapi-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/data-model/citoapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/citoapi-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/changelog/citoapi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/citoapi-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/authentication/citoapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/citoapi-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/errors/citoapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/citoapi-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/llms/citoapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citoapi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/well-known/citoapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citoapi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/hosts/citoapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citoapi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/vendors/citoapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citoapi-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://citoapi.com/webhooks/
- group: operate
  title: ''
  type: StatusPage
  url: https://citoapi.com/status/
- group: start
  title: ''
  type: Sandbox
  url: https://citoapi.com/playground/
- group: operate
  title: ''
  type: ChangeLog
  url: https://citoapi.com/docs/changelog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/citoapi/refs/heads/main/security/citoapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citoapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citoapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://citoapi.com/docs/api/cs2
- group: docs
  title: ''
  type: APIReference
  url: https://citoapi.com/docs/api/cs2
- group: start
  title: ''
  type: GettingStarted
  url: https://citoapi.com/signup/
- group: operate
  title: ''
  type: Support
  url: https://citoapi.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://citoapi.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://citoapi.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://citoapi.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citoapi.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citoapi.com/privacy/
created: '2026-10-08'
description: Cito CS2 API provides live data for Counter-Strike 2, League of Legends, Dota 2, Call of Duty, Apex Legends, and UFC. It aggregates match scores, player statistics, team rosters, rankings, and skin/item prices across dozens of marketplaces, delivering clean JSON via a single API key. The service includes an MCP server for agent integration and SDKs for JavaScript and Python, targeting developers building esports analytics, betting, or game‑related applications.
image: https://citoapi.com/images/og-image.png
json_schemas:
- name: BkfcBout
  property_count: 17
  slug: citoapi-bkfc-bout
- name: RafBout
  property_count: 13
  slug: citoapi-raf-bout
- name: LiveMatchDetail
  property_count: 22
  slug: citoapi-tennis-live-match-detail
- name: MatchDetailResponse
  property_count: 26
  slug: citoapi-tennis-match-detail-response
- name: PlayerProfile
  property_count: 28
  slug: citoapi-tennis-player-profile
- name: TournamentDetailResponse
  property_count: 15
  slug: citoapi-tennis-tournament-detail-response
jsonld:
- class_count: 73
  name: Citoapi Context
  property_count: 292
  slug: citoapi-context
layout: provider
modified: '2026-10-08'
name: Cito CS2 API
nav: Providers
network: true
overview: 'Cito CS2 API publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including BKFC API, Call of Duty API, CS2 API, and 8 more. Tagged areas include Company, Esports, Gaming, and Data.


  The Cito CS2 API catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Cito CS2 API''s developer surface includes changelog, authentication, sandbox, documentation, API reference, getting-started guide, support, and 23 more developer resources.'
plans:
- name: Citoapi Plans Pricing
  plan_count: 4
  slug: citoapi-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Citoapi Rate Limits
  slug: citoapi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Cito CS2 API API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 5
    warn: 4
  slug: citoapi-rules
score:
  band: strong
  composite: 63.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 71.2
    developer_ergonomics: 54.8
    discoverability: 64.3
    operational_transparency: 71.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Citoapi Authentication
  slug: citoapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Citoapi Domain Security
  slug: citoapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citoapi
tags:
- Company
- Esports
- Gaming
- Data
website: https://citoapi.com/
---
