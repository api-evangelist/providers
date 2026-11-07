---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Agendaforge App Agentic Access
  operation_count: 14
  slug: agendaforge-app-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.agendaforge.app
  baseurl_source: declared
  description: Validate a key and identify the organization it is scoped to.
  name: agendaforge-app Connection API
  slug: agendaforge-app-connection-api
- baseURL: https://api.agendaforge.app
  baseurl_source: declared
  description: 'Async work: 202 Accepted imports and the pollable job resource.'
  name: agendaforge-app Jobs API
  slug: agendaforge-app-jobs-api
- baseURL: https://api.agendaforge.app
  baseurl_source: declared
  description: Cursor-paginated lists, create actions, and batch create for contacts, sessions, and sponsors.
  name: agendaforge-app Records API
  slug: agendaforge-app-records-api
- baseURL: https://api.agendaforge.app
  baseurl_source: declared
  description: REST Hook subscriptions for trigger events, plus sample records for field mapping.
  name: agendaforge-app Webhooks API
  slug: agendaforge-app-webhooks-api
artifact_total: 23
asyncapis:
- description: ''
  name: Agendaforge App Webhooks
  slug: agendaforge-app-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/agendaforge-app/agentic-access/agendaforge-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agendaforge-app-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/agendaforge-app/rate-limits/agendaforge-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agendaforge-app-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agendaforge-app/plans/agendaforge-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agendaforge-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agendaforge-app/rules/agendaforge-app-rules.yml
  title: ''
  type: Spectral
  url: rules/agendaforge-app-rules.yml
- group: design
  href: https://artifacts.apis.io/agendaforge-app/json-ld/agendaforge-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agendaforge-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/agendaforge-app/vocabulary/agendaforge-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agendaforge-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agendaforge-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agendaforge-app/asyncapi/agendaforge-app-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agendaforge-app-webhooks.yml
- group: design
  href: https://artifacts.apis.io/agendaforge-app/data-model/agendaforge-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agendaforge-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/agendaforge-app/conventions/agendaforge-app-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agendaforge-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/agendaforge-app/conventions/agendaforge-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agendaforge-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agendaforge-app/authentication/agendaforge-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agendaforge-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agendaforge-app/scopes/agendaforge-app-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agendaforge-app-scopes.yml
- group: design
  href: https://artifacts.apis.io/agendaforge-app/lifecycle/agendaforge-app-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agendaforge-app-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/agendaforge-app/errors/agendaforge-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agendaforge-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agendaforge-app/conformance/agendaforge-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agendaforge-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agendaforge-app/llms/agendaforge-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agendaforge-app-llms.txt
- group: other
  href: https://artifacts.apis.io/agendaforge-app/a2a/agendaforge-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agendaforge-app-a2a.yml
- group: auth
  href: https://artifacts.apis.io/agendaforge-app/well-known/agendaforge-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agendaforge-app-security.txt
- group: agent
  href: https://artifacts.apis.io/agendaforge-app/well-known/agendaforge-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agendaforge-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/agendaforge-app/hosts/agendaforge-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agendaforge-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/agendaforge-app/vendors/agendaforge-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agendaforge-app-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://agendaforge.app/integrates-with/webhooks
- group: auth
  title: ''
  type: Security
  url: https://agendaforge.app/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agendaforge.app/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://agendaforge.app/docs/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agendaforge.app/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://agendaforge.app/changelog
- group: auth
  href: https://artifacts.apis.io/agendaforge-app/security/agendaforge-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agendaforge-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agendaforge-app/security/agendaforge-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agendaforge-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agendaforge.app/
- group: docs
  title: ''
  type: APIReference
  url: https://agendaforge.app/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agendaforge.app/index.md
- group: operate
  title: ''
  type: Support
  url: https://agendaforge.app/contact
- group: company
  title: ''
  type: Blog
  url: https://agendaforge.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://agendaforge.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agendaforge.app/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agendaforge
created: '2026-10-29'
description: AgendaForge is an AI-native event management platform that enables conferences to run call-for-papers, abstract review, agenda building, speaker and sponsor management, ticketing, door check-in, and event operations in a single workspace. It offers per-event pricing, white-glove onboarding, and integrates with Stripe and USDC for payments.
image: https://agendaforge.app/logo.svg
json_schemas:
- name: Contact
  property_count: 21
  slug: agendaforge-app-contact
- name: CreateSessionRequest
  property_count: 11
  slug: agendaforge-app-create-session-request
- name: Job
  property_count: 6
  slug: agendaforge-app-job
- name: Session
  property_count: 25
  slug: agendaforge-app-session
- name: Sponsor
  property_count: 17
  slug: agendaforge-app-sponsor
- name: TicketsImportJob
  property_count: 6
  slug: agendaforge-app-tickets-import-job
jsonld:
- class_count: 19
  name: Agendaforge App Context
  property_count: 71
  slug: agendaforge-app-context
layout: provider
modified: '2026-10-29'
name: agendaforge-app
nav: Providers
network: true
overview: 'agendaforge-app publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Connection API, Jobs API, Records API, and 1 more. Tagged areas include Event Management, Software-as-a-Service, AI-native, Conferences, and Software.


  The agendaforge-app catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  agendaforge-app''s developer surface includes authentication, documentation, changelog, API reference, getting-started guide, support, engineering blog, and 31 more developer resources.'
plans:
- name: Agendaforge App Plans Pricing
  plan_count: 2
  slug: agendaforge-app-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Agendaforge App Rate Limits
  slug: agendaforge-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: agendaforge-app API Rules
  rule_count: 19
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 1
  slug: agendaforge-app-rules
scopes:
- name: Agendaforge App Scopes
  scope_count: 4
  slug: agendaforge-app-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 35
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 73.8
    developer_ergonomics: 41.0
    discoverability: 73.2
    operational_transparency: 40.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 64.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/agendaforge-app/agendaforge-app-2026-11-03T120345.png
security:
- kind: authentication
  name: Agendaforge App Authentication
  slug: agendaforge-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agendaforge App Domain Security
  slug: agendaforge-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agendaforge App Vulnerability Disclosure
  slug: agendaforge-app-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: create-contact
  slug: agendaforge-app-create-contact
- name: import-tickets
  slug: agendaforge-app-import-tickets
- name: list-contacts
  slug: agendaforge-app-list-contacts
slug: agendaforge-app
tags:
- Event Management
- Software-as-a-Service
- AI-native
- Conferences
- Software
website: https://agendaforge.app/
---
