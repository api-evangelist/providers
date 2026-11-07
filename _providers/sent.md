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
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Sent provides messaging APIs for SMS, WhatsApp and RCS.
  name: Sent API
  slug: sent-api
artifact_total: 9
asyncapis:
- description: ''
  name: Sent Webhooks
  slug: sent-webhooks
common:
- group: build
  href: https://artifacts.apis.io/sent/packages/sent-packages.yml
  title: ''
  type: SDKs
  url: packages/sent-packages.yml
- group: build
  href: https://artifacts.apis.io/sent/packages/sent-packages.yml
  title: ''
  type: Packages
  url: packages/sent-packages.yml
- group: operate
  href: https://artifacts.apis.io/sent/rate-limits/sent-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sent-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sent/plans/sent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sent-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sent/rules/sent-rules.yml
  title: ''
  type: Spectral
  url: rules/sent-rules.yml
- group: design
  href: https://artifacts.apis.io/sent/json-ld/sent-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sent-context.jsonld
- group: design
  href: https://artifacts.apis.io/sent/vocabulary/sent-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sent-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sent/asyncapi/sent-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sent-webhooks.yml
- group: design
  href: https://artifacts.apis.io/sent/data-model/sent-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sent-data-model.yml
- group: operate
  href: https://artifacts.apis.io/sent/changelog/sent-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sent-changelog.yml
- group: design
  href: https://artifacts.apis.io/sent/conventions/sent-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sent-conventions.yml
- group: design
  href: https://artifacts.apis.io/sent/conventions/sent-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sent-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sent.dm/resources/privacy-policy
- group: auth
  href: https://artifacts.apis.io/sent/authentication/sent-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sent-authentication.yml
- group: design
  href: https://artifacts.apis.io/sent/conformance/sent-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sent-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sent/llms/sent-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sent-llms.txt
- group: auth
  href: https://artifacts.apis.io/sent/well-known/sent-sent-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sent-sent-security.txt
- group: auth
  href: https://artifacts.apis.io/sent/well-known/sent-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sent-security.txt
- group: auth
  href: https://artifacts.apis.io/sent/well-known/sent-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sent-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/sent/well-known/sent-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sent-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/sent/well-known/sent-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sent-app-security.txt
- group: auth
  href: https://artifacts.apis.io/sent/well-known/sent-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sent-api-security.txt
- group: agent
  href: https://artifacts.apis.io/sent/well-known/sent-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sent-well-known.yml
- group: other
  href: https://artifacts.apis.io/sent/hosts/sent-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sent-hosts.yml
- group: other
  href: https://artifacts.apis.io/sent/vendors/sent-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sent-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sent.dm/legal/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.sent.dm
- group: start
  title: ''
  type: SignUp
  url: https://app.sent.dm/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sent.dm/en/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sent.dm/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.sent.dm/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sentdm
- group: company
  title: ''
  type: Blog
  url: https://www.sent.dm/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sent.dm/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sent.dm/reference/api/profiles/SentDmServicesEndpointsCustomerAPIv3ProfilesCompleteProfileEndpoint
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sent.dm/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sent.dm\
- group: auth
  href: https://artifacts.apis.io/sent/security/sent-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sent-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sent/security/sent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sent.dm/
coverage:
  checked: '2026-10-21'
  detail: The provider's documentation site is a JavaScript-rendered Next.js application with no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract files.
  evidence:
  - status: 200
    url: https://www.sent.dm/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Sent provides a single API that enables developers to send messages via SMS, WhatsApp, and RCS. The service handles routing, compliance, formatting, and delivery, allowing customers in e‑commerce, SaaS, fintech, and healthcare to deliver authentication codes, order notifications, cart‑recovery messages, and marketing campaigns. Sent offers SDKs for multiple languages and signed webhooks for delivery tracking.
image: https://www.sent.dm/media/images/og-image-4fee8e22.png
jsonld:
- class_count: 75
  name: Sent Context
  property_count: 11
  slug: sent-context
layout: provider
modified: '2026-10-21'
name: Sent
nav: Providers
network: true
overview: 'Sent is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SMS, WhatsApp, RCS, Messaging API, and Communications.


  The Sent catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Sent''s developer surface includes changelog, authentication, support, signup flow, pricing, engineering blog, API reference, and 33 more developer resources.'
plans:
- name: Sent Plans Pricing
  plan_count: 1
  slug: sent-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Sent Rate Limits
  slug: sent-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Sent API Rules
  rule_count: 49
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 2
  slug: sent-rules
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 68.8
    catalog_earned_first_party: 20.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 42.9
    developer_ergonomics: 41.7
    discoverability: 65.2
    operational_transparency: 63.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 53.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sent/sent-2026-11-03T143035.png
security:
- kind: authentication
  name: Sent Authentication
  slug: sent-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sent Domain Security
  slug: sent-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sent Vulnerability Disclosure
  slug: sent-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sent
tags:
- SMS
- WhatsApp
- RCS
- Messaging API
- Communications
- Developer Platform
- Authentication
- Order Notifications
website: https://sent.dm/
---
