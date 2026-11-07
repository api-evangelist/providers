---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: unknown
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 63.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Clearlist Me Agentic Access
  operation_count: 26
  slug: clearlist-me-agentic-access
  summary_line: 26 operations · 18 acting
api_count: 1
apis:
- baseURL: https://clearlist.me
  baseurl_source: declared
  description: Tier, capacity, and payment links.
  name: ClearList Account API
  slug: clearlist-me-account-api
- baseURL: https://clearlist.me
  baseurl_source: declared
  description: Async job polling.
  name: ClearList Jobs API
  slug: clearlist-me-jobs-api
- baseURL: https://clearlist.me
  baseurl_source: declared
  description: Create, read, update, delete, and bulk-create items.
  name: ClearList Listings API
  slug: clearlist-me-listings-api
- baseURL: https://clearlist.me
  baseurl_source: declared
  description: Email-OTP auth and API-key acquisition.
  name: ClearList Onboarding API
  slug: clearlist-me-onboarding-api
- baseURL: https://clearlist.me
  baseurl_source: declared
  description: Reservations and buyer conversations.
  name: ClearList Orders API
  slug: clearlist-me-orders-api
- baseURL: https://clearlist.me
  baseurl_source: declared
  description: Publish the shareable sale page.
  name: ClearList Publishing API
  slug: clearlist-me-publishing-api
- baseURL: https://clearlist.me
  baseurl_source: declared
  description: Pickup availability.
  name: ClearList Scheduling API
  slug: clearlist-me-scheduling-api
- baseURL: https://clearlist.me
  baseurl_source: declared
  description: Health and status probes.
  name: ClearList System API
  slug: clearlist-me-system-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/clearlist-me/agentic-access/clearlist-me-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clearlist-me-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/clearlist-me/plans/clearlist-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clearlist-me-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clearlist-me/rules/clearlist-me-rules.yml
  title: ''
  type: Spectral
  url: rules/clearlist-me-rules.yml
- group: design
  href: https://artifacts.apis.io/clearlist-me/json-ld/clearlist-me-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clearlist-me-context.jsonld
- group: design
  href: https://artifacts.apis.io/clearlist-me/vocabulary/clearlist-me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clearlist-me-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/clearlist-me/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/clearlist-me/data-model/clearlist-me-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clearlist-me-data-model.yml
- group: design
  href: https://artifacts.apis.io/clearlist-me/conventions/clearlist-me-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/clearlist-me-conventions.yml
- group: design
  href: https://artifacts.apis.io/clearlist-me/conventions/clearlist-me-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clearlist-me-conventions.yml
- group: auth
  href: https://artifacts.apis.io/clearlist-me/authentication/clearlist-me-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clearlist-me-authentication.yml
- group: design
  href: https://artifacts.apis.io/clearlist-me/errors/clearlist-me-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clearlist-me-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clearlist-me/conformance/clearlist-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearlist-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clearlist-me/llms/clearlist-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearlist-me-llms.txt
- group: other
  href: https://artifacts.apis.io/clearlist-me/a2a/clearlist-me-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clearlist-me-a2a.yml
- group: auth
  href: https://artifacts.apis.io/clearlist-me/well-known/clearlist-me-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clearlist-me-security.txt
- group: auth
  href: https://artifacts.apis.io/clearlist-me/well-known/clearlist-me-mcprush-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clearlist-me-mcprush-security.txt
- group: agent
  href: https://artifacts.apis.io/clearlist-me/well-known/clearlist-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clearlist-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/clearlist-me/hosts/clearlist-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearlist-me-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clearlist.me/terms
- group: auth
  title: ''
  type: Security
  url: https://clearlist.me/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clearlist.me/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://clearlist.me/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://clearlist.me/press
- group: start
  title: ''
  type: Login
  url: https://clearlist.me/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://clearlist.me/developers
- group: company
  title: ''
  type: Blog
  url: https://clearlist.me/blog
- group: docs
  title: ''
  type: APIReference
  url: https://clearlist.me/docs/api
- group: auth
  href: https://artifacts.apis.io/clearlist-me/scopes/clearlist-me-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/clearlist-me-scopes.yml
- group: auth
  href: https://artifacts.apis.io/clearlist-me/security/clearlist-me-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clearlist-me-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clearlist-me/security/clearlist-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearlist-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clearlist.me/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://clearlist.me/openapi.json
  - status: 401
    url: https://clearlist.me/api/mcp
  - status: 200
    url: https://clearlist.me/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: ClearList is an AI resale manager that helps users quickly create listings for items they want to sell. By uploading photos, the platform’s AI generates complete product listings, prices them, and manages buyer interactions through a single shareable link. It streamlines the resale process, eliminating the need for manual description writing and price negotiation, and provides an automated buyer queue for faster sales.
image: https://clearlist.me/api/og?type=home
json_schemas:
- name: Error
  property_count: 6
  slug: clearlist-me-error
- name: Job
  property_count: 3
  slug: clearlist-me-job
jsonld:
- class_count: 2
  name: Clearlist Me Context
  property_count: 8
  slug: clearlist-me-context
layout: provider
modified: '2026-11-03'
name: ClearList
nav: Providers
network: true
overview: 'ClearList publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Jobs API, Listings API, and 5 more. Tagged areas include Artificial Intelligence, Resale, Marketplace, Automation, and E-Commerce.


  The ClearList catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClearList''s developer surface includes authentication, pricing, engineering blog, API reference, and 27 more developer resources.'
plans:
- name: Clearlist Me Plans Pricing
  plan_count: 3
  slug: clearlist-me-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: ClearList API Rules
  rule_count: 68
  severity_counts:
    error: 59
    hint: 0
    info: 4
    warn: 5
  slug: clearlist-me-rules
scopes:
- name: Clearlist Me Scopes
  scope_count: 2
  slug: clearlist-me-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 59.8
    developer_ergonomics: 27.9
    discoverability: 67.0
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Clearlist Me Authentication
  slug: clearlist-me-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Clearlist Me Domain Security
  slug: clearlist-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clearlist Me Vulnerability Disclosure
  slug: clearlist-me-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-listings
  slug: clearlist-me-getlistings
slug: clearlist-me
tags:
- Artificial Intelligence
- Resale
- Marketplace
- Automation
- E-Commerce
- Company
website: https://clearlist.me/
---
