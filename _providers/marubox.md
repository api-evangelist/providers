---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.7
  scored_at: '2026-10-04'
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
artifact_total: 13
asyncapis:
- description: ''
  name: Marubox Webhooks
  slug: marubox-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/agentic-access/marubox-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/marubox-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/rate-limits/marubox-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/marubox-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/plans/marubox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/marubox-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/rules/marubox-rules.yml
  title: ''
  type: Spectral
  url: rules/marubox-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/json-ld/marubox-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/marubox-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/vocabulary/marubox-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/marubox-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/asyncapi/marubox-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/marubox-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/data-model/marubox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/marubox-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/changelog/marubox-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/marubox-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/conventions/marubox-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/marubox-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/conventions/marubox-conventions.yml
  title: ''
  type: Conventions
  url: conventions/marubox-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/authentication/marubox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/marubox-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/errors/marubox-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/marubox-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/conformance/marubox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/marubox-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/llms/marubox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/marubox-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/hosts/marubox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/marubox-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/vendors/marubox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/marubox-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/packages/marubox-packages.yml
  title: ''
  type: SDKs
  url: packages/marubox-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/packages/marubox-packages.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/marubox/refs/heads/main/security/marubox-domain-security.yml
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
overview: 'Business Box publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Bookings API, Event types API, and 2 more. Tagged areas include Company, Booking, Payments, Calendar, and Japan.


  The Business Box catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Business Box''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, signup flow, and 26 more developer resources.'
plans:
- name: Marubox Plans Pricing
  plan_count: 2
  slug: marubox-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Marubox Rate Limits
  slug: marubox-rate-limits
rules:
- effective_rule_count: 60
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
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 66.8
    catalog_earned_first_party: 16.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 63.7
    developer_ergonomics: 63.7
    discoverability: 75.0
    operational_transparency: 50.0
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
    score: 22.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Marubox Authentication
  slug: marubox-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Marubox Domain Security
  slug: marubox-domain-security
  summary_line: TLSv1.3 · DMARC
slug: marubox
tags:
- Company
- Booking
- Payments
- Calendar
- Japan
website: https://marubox.jp/
---
