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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: The scheduled delivery API for developers. Schedule reminders, notifications, and webhooks with one API call.
  name: Pingfyr API
  slug: pingfyr-api
- description: 'pingfyr-com API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: pingfyr-com API
  slug: pingfyr-com-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/pingfyr-com/rate-limits/pingfyr-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pingfyr-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pingfyr-com/plans/pingfyr-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pingfyr-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pingfyr-com/rules/pingfyr-com-rules.yml
  title: ''
  type: Spectral
  url: rules/pingfyr-com-rules.yml
- group: design
  href: https://artifacts.apis.io/pingfyr-com/json-ld/pingfyr-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pingfyr-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/pingfyr-com/vocabulary/pingfyr-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pingfyr-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pingfyr-com/data-model/pingfyr-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pingfyr-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/pingfyr-com/changelog/pingfyr-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pingfyr-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/pingfyr-com/authentication/pingfyr-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pingfyr-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/pingfyr-com/errors/pingfyr-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pingfyr-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pingfyr-com/conformance/pingfyr-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pingfyr-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/pingfyr-com/hosts/pingfyr-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pingfyr-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pingfyr-com/vendors/pingfyr-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pingfyr-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://pingfyr.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://pingfyr.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pingfyr
- group: auth
  href: https://artifacts.apis.io/pingfyr-com/security/pingfyr-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pingfyr-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pingfyr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pingfyr.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://pingfyr.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://pingfyr.com/docs
- group: company
  title: ''
  type: Blog
  url: https://pingfyr.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pingfyr.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pingfyr.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pingfyr.com/
coverage:
  checked: '2026-10-31'
  detail: Docs are a client‑side SPA; no machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://pingfyr.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Pingfyr provides a Scheduled Delivery API that enables developers to schedule reminders, notifications, and webhooks with a single API call. The service targets AI agents and applications needing reliable timed delivery of messages across channels. It offers a developer portal, comprehensive documentation, pricing plans, and a blog. The company focuses on simplicity, security, and scalability, integrating with Stripe for billing and Supabase for data storage. The platform is built on modern web technologies, hosted on Cloudflare, and includes support contact via support@pingfyr.com.
image: https://pingfyr.com/LogoBlack.svg
json_schemas:
- name: DeleteApiRemindersResponse
  property_count: 2
  slug: pingfyr-com-delete-api-reminders-response
- name: GetApiRemindersIdLogsResponse
  property_count: 5
  slug: pingfyr-com-get-api-reminders-id-logs-response
- name: PatchApiRemindIdRequest
  property_count: 2
  slug: pingfyr-com-patch-api-remind-id-request
- name: PatchApiRemindIdResponse
  property_count: 11
  slug: pingfyr-com-patch-api-remind-id-response
- name: PostApiRemindRequest
  property_count: 9
  slug: pingfyr-com-post-api-remind-request
- name: PostApiRemindResponse
  property_count: 11
  slug: pingfyr-com-post-api-remind-response
jsonld:
- class_count: 7
  name: Pingfyr Com Context
  property_count: 19
  slug: pingfyr-com-context
layout: provider
modified: '2026-10-30'
name: pingfyr-com
nav: Providers
network: true
overview: 'pingfyr-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Scheduling, Notifications, and Webhooks.


  The pingfyr-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pingfyr-com''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Pingfyr Com Plans Pricing
  plan_count: 4
  slug: pingfyr-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Pingfyr Com Rate Limits
  slug: pingfyr-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: pingfyr-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: pingfyr-com-rules
scopes:
- name: Pingfyr Com Scopes
  scope_count: 0
  slug: pingfyr-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 90.7
    catalog_earned_first_party: 0.0
    catalog_gap: 24.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 53.8
    developer_ergonomics: 42.9
    discoverability: 57.1
    operational_transparency: 40.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pingfyr Com Authentication
  slug: pingfyr-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pingfyr Com Domain Security
  slug: pingfyr-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: pingfyr-com
tags:
- Company
- API
- Scheduling
- Notifications
- Webhooks
- AI
website: https://pingfyr.com/
---
