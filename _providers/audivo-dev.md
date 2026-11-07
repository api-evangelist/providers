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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 2
  name: Audivo Dev Agentic Access
  operation_count: 36
  slug: audivo-dev-agentic-access
  summary_line: 36 operations · 17 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.audivo.dev
  baseurl_source: declared
  description: Usage, limits, and supported languages for the calling account.
  name: audivo-dev Account API
  slug: audivo-dev-account-api
- baseURL: https://api.audivo.dev
  baseurl_source: declared
  description: Dashboard-JWT key lifecycle management.
  name: audivo-dev API Keys API
  slug: audivo-dev-api-keys-api
- baseURL: https://api.audivo.dev
  baseurl_source: declared
  description: Dashboard-JWT Stripe Checkout, Customer Portal, invoices, and refunds.
  name: audivo-dev Billing API
  slug: audivo-dev-billing-api
- baseURL: https://api.audivo.dev
  baseurl_source: declared
  description: Public podcast show/episode search, charts, detail, and resolution. Every metadata/search/list call in this tag costs 1 credit; no catalog response echoes `credits_charged`, so the charge is stated he
  name: audivo-dev Catalog API
  slug: audivo-dev-catalog-api
- baseURL: https://api.audivo.dev
  baseurl_source: declared
  description: Dashboard-JWT consent for an assistant connecting to the MCP server through OAuth, and the account's connected apps, each revocable.
  name: audivo-dev Connected Apps API
  slug: audivo-dev-connected-apps-api
- baseURL: https://api.audivo.dev
  baseurl_source: declared
  description: Dashboard-JWT portable export and account deletion.
  name: audivo-dev Data API
  slug: audivo-dev-data-api
- baseURL: https://api.audivo.dev
  baseurl_source: declared
  description: 'The job group: what one confirm created. A group holds N ≥ 1 members, each a transcription job or a settled cache read; a single-episode `POST /v1/transcripts` is a group of one. A caller reads a grou'
  name: audivo-dev Groups API
  slug: audivo-dev-groups-api
- baseURL: https://api.audivo.dev
  baseurl_source: declared
  description: Price a selection before spending. A quote resolves every episode in it, records what it resolved under a short TTL, and reserves nothing; the confirm that follows is the operation that spends, and it
  name: audivo-dev Quotes API
  slug: audivo-dev-quotes-api
- baseURL: https://api.audivo.dev
  baseurl_source: declared
  description: Dashboard-JWT session establishment. One operation, called by the dashboard's backend-for-frontend whenever it turns a Cognito sign-in into a Audivo session, and the one place a caller who does not ye
  name: audivo-dev Session API
  slug: audivo-dev-session-api
- baseURL: https://api.audivo.dev
  baseurl_source: declared
  description: Create, poll, retrieve, and cancel transcription jobs.
  name: audivo-dev Transcripts API
  slug: audivo-dev-transcripts-api
- baseURL: https://api.audivo.dev
  baseurl_source: declared
  description: Audio the caller puts in Audivo's bucket and names as a source (ADR-0031).
  name: audivo-dev Uploads API
  slug: audivo-dev-uploads-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/audivo-dev/agentic-access/audivo-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/audivo-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/audivo-dev/rules/audivo-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/audivo-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/audivo-dev/json-ld/audivo-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/audivo-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/audivo-dev/vocabulary/audivo-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/audivo-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/audivo-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/audivo-dev/data-model/audivo-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/audivo-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/audivo-dev/changelog/audivo-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/audivo-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/audivo-dev/conventions/audivo-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/audivo-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/audivo-dev/conventions/audivo-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/audivo-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/audivo-dev/authentication/audivo-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/audivo-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/audivo-dev/errors/audivo-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/audivo-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/audivo-dev/conformance/audivo-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/audivo-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/audivo-dev/llms/audivo-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/audivo-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/audivo-dev/a2a/audivo-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/audivo-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/audivo-dev/well-known/audivo-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/audivo-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/audivo-dev/hosts/audivo-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audivo-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/audivo-dev/vendors/audivo-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audivo-dev-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://dash.audivo.dev/signin
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.audivo.dev/changelog
- group: auth
  href: https://artifacts.apis.io/audivo-dev/security/audivo-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audivo-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audivo.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.audivo.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.audivo.dev/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.audivo.dev/quickstart
- group: operate
  title: ''
  type: Support
  url: https://audivo.dev/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://audivo.dev/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://audivo.dev/terms
created: '2026-10-30'
description: Audivo provides a podcast transcript API that transforms public podcast episodes into structured, timed text in multiple formats such as JSON, SRT, VTT, and Markdown. The service offers a clear pricing model with free credits on signup, supports various input methods like RSS feeds and episode IDs, and includes features like caching, quoting, and rate limits. Audivo aims to simplify integration of podcast content for developers building searchable or analytical applications.
image: https://audivo.dev/opengraph-image?94d944e67a07dad7
json_schemas:
- name: AutoRechargeResponse
  property_count: 7
  slug: audivo-dev-auto-recharge-response
- name: JobGroupResponse
  property_count: 13
  slug: audivo-dev-job-group-response
- name: JobStatus
  property_count: 17
  slug: audivo-dev-job-status
- name: QuoteResponse
  property_count: 14
  slug: audivo-dev-quote-response
- name: TranscriptRead
  property_count: 9
  slug: audivo-dev-transcript-read
- name: UsageResponse
  property_count: 10
  slug: audivo-dev-usage-response
jsonld:
- class_count: 94
  name: Audivo Dev Context
  property_count: 199
  slug: audivo-dev-context
layout: provider
modified: '2026-10-30'
name: audivo-dev
nav: Providers
network: true
overview: 'audivo-dev publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, API Keys API, Billing API, and 8 more. Tagged areas include Company, Podcasts, Transcripts, and Audio.


  The audivo-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  audivo-dev''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, and 21 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: audivo-dev API Rules
  rule_count: 62
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 7
  slug: audivo-dev-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 66.5
    developer_ergonomics: 30.4
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/audivo-dev/audivo-dev-2026-11-03T121316.png
security:
- kind: authentication
  name: Audivo Dev Authentication
  slug: audivo-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Audivo Dev Domain Security
  slug: audivo-dev-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 5
skills:
- name: audivo-dev-billing-setup
  slug: audivo-dev-billing-setup
- name: audivo-dev-create-and-confirm-quote
  slug: audivo-dev-create-and-confirm-quote
- name: audivo-dev-export-and-delete-data
  slug: audivo-dev-export-and-delete-data
- name: audivo-dev-manage-connected-apps
  slug: audivo-dev-manage-connected-apps
- name: audivo-dev-manage-groups
  slug: audivo-dev-manage-groups
slug: audivo-dev
tags:
- Company
- Podcasts
- Transcripts
- Audio
website: https://audivo.dev/
---
