---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Marubox Agentic Access
  operation_count: 12
  slug: marubox-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.marubox.jp/v1
  baseurl_source: declared
  description: Who the token belongs to
  name: Business Box Account API
  slug: marubox-account-api
- baseURL: https://api.marubox.jp/v1
  baseurl_source: declared
  description: Read, create and cancel bookings
  name: Business Box Bookings API
  slug: marubox-bookings-api
- baseURL: https://api.marubox.jp/v1
  baseurl_source: declared
  description: What people can book, and when
  name: Business Box Event types API
  slug: marubox-event-types-api
- baseURL: https://api.marubox.jp/v1
  baseurl_source: declared
  description: Single-use booking links
  name: Business Box Invites API
  slug: marubox-invites-api
- baseURL: https://api.marubox.jp/v1
  baseurl_source: declared
  description: Subscribe to events
  name: Business Box Webhooks API
  slug: marubox-webhooks-api
artifact_total: 16
asyncapis:
- description: ''
  name: Marubox Webhooks
  slug: marubox-webhooks
common:
- group: other
  href: https://artifacts.apis.io/marubox/capabilities/marubox-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/marubox-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/marubox/agentic-access/marubox-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/marubox-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/marubox/rate-limits/marubox-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/marubox-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/marubox/plans/marubox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/marubox-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/marubox/rules/marubox-rules.yml
  title: ''
  type: Spectral
  url: rules/marubox-rules.yml
- group: design
  href: https://artifacts.apis.io/marubox/json-ld/marubox-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/marubox-context.jsonld
- group: design
  href: https://artifacts.apis.io/marubox/vocabulary/marubox-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/marubox-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/marubox/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/marubox/asyncapi/marubox-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/marubox-webhooks.yml
- group: design
  href: https://artifacts.apis.io/marubox/data-model/marubox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/marubox-data-model.yml
- group: operate
  href: https://artifacts.apis.io/marubox/changelog/marubox-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/marubox-changelog.yml
- group: design
  href: https://artifacts.apis.io/marubox/conventions/marubox-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/marubox-conventions.yml
- group: design
  href: https://artifacts.apis.io/marubox/conventions/marubox-conventions.yml
  title: ''
  type: Conventions
  url: conventions/marubox-conventions.yml
- group: auth
  href: https://artifacts.apis.io/marubox/authentication/marubox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/marubox-authentication.yml
- group: design
  href: https://artifacts.apis.io/marubox/errors/marubox-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/marubox-problem-types.yml
- group: design
  href: https://artifacts.apis.io/marubox/conformance/marubox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/marubox-conformance.yml
- group: agent
  href: https://artifacts.apis.io/marubox/llms/marubox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/marubox-llms.txt
- group: other
  href: https://artifacts.apis.io/marubox/hosts/marubox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/marubox-hosts.yml
- group: other
  href: https://artifacts.apis.io/marubox/vendors/marubox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/marubox-vendors.yml
- group: build
  href: https://artifacts.apis.io/marubox/packages/marubox-packages.yml
  title: ''
  type: SDKs
  url: packages/marubox-packages.yml
- group: build
  href: https://artifacts.apis.io/marubox/packages/marubox-packages.yml
  title: ''
  type: Packages
  url: packages/marubox-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://marubox.jp/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://marubox.jp/developers/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/marubox
- group: auth
  href: https://artifacts.apis.io/marubox/security/marubox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/marubox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marubox.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://marubox.jp/developers/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://marubox.jp/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://marubox.jp/developers/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://marubox.jp/guide/
- group: operate
  title: ''
  type: Support
  url: https://marubox.jp/support
- group: start
  title: ''
  type: SignUp
  url: https://app.marubox.jp/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://marubox.jp/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://marubox.jp/privacy
created: '2026-10-02'
description: Business Box provides an integrated booking and payment platform tailored for Japanese small businesses. It combines a booking page, calendar synchronization with Google and Outlook, and Stripe‑based pre‑payment handling, all in one service. Users can publish booking pages, automatically sync availability, and receive payments directly into their Stripe accounts without additional fees. The service includes free usage tiers, supports Japanese public holidays, offers bilingual (Japanese/English) interfaces, and is built for the Japanese market.
finops:
- has_sources: true
  method: derived
  name: Marubox Finops
  primary_unit: ''
  service_category: ''
  slug: marubox-finops
  template: true
image: https://marubox.jp/logo.png
jsonld:
- class_count: 1
  name: Marubox Context
  property_count: 17
  slug: marubox-context
layout: provider
modified: '2026-10-02'
name: Business Box
nav: Providers
network: true
overview: 'Business Box publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Bookings API, Event types API, and 2 more. Tagged areas include Company, Booking, Payments, Calendar, and Japan.


  The Business Box catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Business Box''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, signup flow, and 27 more developer resources.'
plans:
- name: Marubox Plans Pricing
  plan_count: 2
  slug: marubox-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Marubox Rate Limits
  slug: marubox-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: Business Box API Rules
  rule_count: 19
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 1
  slug: marubox-rules
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 66.8
    catalog_earned_first_party: 16.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 38.2
    contract_governance: 22.0
    contract_quality: 63.7
    developer_ergonomics: 42.3
    discoverability: 74.1
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/marubox/marubox-2026-11-03T135343.png
security:
- kind: authentication
  name: Marubox Authentication
  slug: marubox-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Marubox Domain Security
  slug: marubox-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: marubox-bookings-create-and-manage
  slug: marubox-bookings-create-and-manage
- name: marubox-manage-webhook-subscription
  slug: marubox-manage-webhook-subscription
slug: marubox
tags:
- Company
- Booking
- Payments
- Calendar
- Japan
website: https://marubox.jp/
---
