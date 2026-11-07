---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Grabbit Live Agentic Access
  operation_count: 10
  slug: grabbit-live-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.grabbit.live/v1
  baseurl_source: declared
  description: Credits, usage, and pricing.
  name: grabbit-live Account API
  slug: grabbit-live-account-api
- baseURL: https://api.grabbit.live/v1
  baseurl_source: declared
  description: Capture and retrieve screenshots.
  name: grabbit-live Grabs API
  slug: grabbit-live-grabs-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/grabbit-live/agentic-access/grabbit-live-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/grabbit-live-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/grabbit-live/rules/grabbit-live-rules.yml
  title: ''
  type: Spectral
  url: rules/grabbit-live-rules.yml
- group: design
  href: https://artifacts.apis.io/grabbit-live/json-ld/grabbit-live-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/grabbit-live-context.jsonld
- group: design
  href: https://artifacts.apis.io/grabbit-live/vocabulary/grabbit-live-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/grabbit-live-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/grabbit-live/data-model/grabbit-live-data-model.yml
  title: ''
  type: DataModel
  url: data-model/grabbit-live-data-model.yml
- group: design
  href: https://artifacts.apis.io/grabbit-live/conventions/grabbit-live-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/grabbit-live-conventions.yml
- group: design
  href: https://artifacts.apis.io/grabbit-live/conventions/grabbit-live-conventions.yml
  title: ''
  type: Conventions
  url: conventions/grabbit-live-conventions.yml
- group: design
  href: https://artifacts.apis.io/grabbit-live/errors/grabbit-live-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/grabbit-live-problem-types.yml
- group: design
  href: https://artifacts.apis.io/grabbit-live/conformance/grabbit-live-conformance.yml
  title: ''
  type: Conformance
  url: conformance/grabbit-live-conformance.yml
- group: agent
  href: https://artifacts.apis.io/grabbit-live/llms/grabbit-live-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/grabbit-live-llms.txt
- group: agent
  href: https://artifacts.apis.io/grabbit-live/well-known/grabbit-live-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/grabbit-live-well-known.yml
- group: other
  href: https://artifacts.apis.io/grabbit-live/hosts/grabbit-live-hosts.yml
  title: ''
  type: Hosts
  url: hosts/grabbit-live-hosts.yml
- group: other
  href: https://artifacts.apis.io/grabbit-live/vendors/grabbit-live-vendors.yml
  title: ''
  type: Vendors
  url: vendors/grabbit-live-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.grabbit.live/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.grabbit.live/docs/changelog
- group: auth
  href: https://artifacts.apis.io/grabbit-live/scopes/grabbit-live-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/grabbit-live-scopes.yml
- group: auth
  href: https://artifacts.apis.io/grabbit-live/authentication/grabbit-live-authentication.yml
  title: ''
  type: Authentication
  url: authentication/grabbit-live-authentication.yml
- group: auth
  href: https://artifacts.apis.io/grabbit-live/security/grabbit-live-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grabbit-live-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grabbit.live/
- group: docs
  title: ''
  type: Documentation
  url: https://www.grabbit.live/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.grabbit.live/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://www.grabbit.live/blog
- group: operate
  title: ''
  type: Support
  url: https://www.grabbit.live/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.grabbit.live/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.grabbit.live/terms
created: '2026-10-30'
description: Grabbit Live provides an agent‑first screenshot API that lets autonomous agents capture pixel‑perfect images of any web page without managing a browser fleet. It offers a simple REST endpoint, supports async processing with signed webhooks, and includes SDKs for popular agent runtimes like Claude, Codex, Cursor, and Crewai. Pricing is per‑grab with free test keys, and the service includes built‑in idempotency, SSRF protection, and CDN hosting of results. The platform is designed for integration into AI‑driven workflows, enabling agents to verify UI changes, capture receipts, and enrich data with visual context.
image: https://www.grabbit.live/opengraph-image?0ec00b6c1b51af63
json_schemas:
- name: CreateGrabRequest
  property_count: 7
  slug: grabbit-live-create-grab-request
- name: GrabList
  property_count: 2
  slug: grabbit-live-grab-list
- name: Grab
  property_count: 11
  slug: grabbit-live-grab
- name: Pricing
  property_count: 3
  slug: grabbit-live-pricing
- name: Usage
  property_count: 5
  slug: grabbit-live-usage
jsonld:
- class_count: 6
  name: Grabbit Live Context
  property_count: 26
  slug: grabbit-live-context
layout: provider
modified: '2026-10-30'
name: grabbit-live
nav: Providers
network: true
overview: 'grabbit-live publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Account API and Grabs API. Tagged areas include Company, Screenshots, AI Agents, Automation, and Visual.


  The grabbit-live catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  grabbit-live''s developer surface includes changelog, authentication, documentation, API reference, engineering blog, support, and 19 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: grabbit-live API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: grabbit-live-rules
scopes:
- name: Grabbit Live Scopes
  scope_count: 1
  slug: grabbit-live-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 65.0
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/grabbit-live/grabbit-live-2026-11-03T133002.png
security:
- kind: authentication
  name: Grabbit Live Authentication
  slug: grabbit-live-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Grabbit Live Domain Security
  slug: grabbit-live-domain-security
  summary_line: TLSv1.3 · HSTS
slug: grabbit-live
tags:
- Company
- Screenshots
- AI Agents
- Automation
- Visual
website: https://grabbit.live/
---
