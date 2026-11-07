---
access_model:
  confidence: high
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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://tempmailgrab.com/api/v1
  baseurl_source: declared
  description: The Byod API from TempMailGrab API — 2 operation(s) for byod.
  name: TempMailGrab API Byod API
  slug: tempmailgrab-byod-api
- baseURL: https://tempmailgrab.com/api/v1
  baseurl_source: declared
  description: The Inbox API from TempMailGrab API — 6 operation(s) for inbox.
  name: TempMailGrab API Inbox API
  slug: tempmailgrab-inbox-api
- baseURL: https://tempmailgrab.com/api/v1
  baseurl_source: declared
  description: The Messages API from TempMailGrab API — 2 operation(s) for messages.
  name: TempMailGrab API Messages API
  slug: tempmailgrab-messages-api
- baseURL: https://tempmailgrab.com/api/v1
  baseurl_source: declared
  description: The TempMailGrab API API from TempMailGrab API — 0 operation(s) for tempmailgrab api.
  name: TempMailGrab API TempMailGrab API
  slug: tempmailgrab-tempmailgrab-api-api
- baseURL: https://tempmailgrab.com/api/v1
  baseurl_source: declared
  description: The Webhooks API from TempMailGrab API — 2 operation(s) for webhooks.
  name: TempMailGrab API Webhooks API
  slug: tempmailgrab-webhooks-api
artifact_total: 17
asyncapis:
- description: ''
  name: Tempmailgrab Webhooks
  slug: tempmailgrab-webhooks
common:
- group: other
  href: https://artifacts.apis.io/tempmailgrab/overlays/tempmailgrab-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tempmailgrab-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.tempmailgrab.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tempmailgrab.com/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://tempmailgrab.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://tempmailgrab.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://tempmailgrab.com/email-testing-api
- group: operate
  title: ''
  type: Support
  url: https://tempmailgrab.com/contact
- group: company
  title: ''
  type: Blog
  url: https://tempmailgrab.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://tempmailgrab.com/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://tempmailgrab.com/premium
- group: start
  title: ''
  type: SignUp
  url: https://tempmailgrab.com/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tempmailgrab.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tempmailgrab.com/privacy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/sathishbanoth-coder/tempmailgrab-js
- group: operate
  title: ''
  type: StatusPage
  url: https://tempmailgrab.com/status
- group: agent
  href: https://artifacts.apis.io/tempmailgrab/llms/tempmailgrab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tempmailgrab-llms.txt
- group: agent
  href: https://artifacts.apis.io/tempmailgrab/well-known/tempmailgrab-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tempmailgrab-well-known.yml
- group: auth
  href: https://artifacts.apis.io/tempmailgrab/well-known/tempmailgrab-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tempmailgrab-security.txt
- group: auth
  href: https://artifacts.apis.io/tempmailgrab/authentication/tempmailgrab-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tempmailgrab-authentication.yml
- group: design
  href: https://artifacts.apis.io/tempmailgrab/conventions/tempmailgrab-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tempmailgrab-conventions.yml
- group: design
  href: https://artifacts.apis.io/tempmailgrab/errors/tempmailgrab-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tempmailgrab-problem-types.yml
- group: build
  href: https://artifacts.apis.io/tempmailgrab/examples/tempmailgrab-examples.yml
  title: ''
  type: Examples
  url: examples/tempmailgrab-examples.yml
- group: design
  href: https://artifacts.apis.io/tempmailgrab/data-model/tempmailgrab-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tempmailgrab-data-model.yml
- group: design
  href: https://artifacts.apis.io/tempmailgrab/lifecycle/tempmailgrab-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tempmailgrab-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/tempmailgrab/changelog/tempmailgrab-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tempmailgrab-changelog.yml
- group: design
  href: https://artifacts.apis.io/tempmailgrab/conformance/tempmailgrab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tempmailgrab-conformance.yml
- group: operate
  href: https://artifacts.apis.io/tempmailgrab/rate-limits/tempmailgrab-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tempmailgrab-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tempmailgrab/plans/tempmailgrab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tempmailgrab-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/tempmailgrab/packages/tempmailgrab-packages.yml
  title: ''
  type: Packages
  url: packages/tempmailgrab-packages.yml
- group: build
  href: https://artifacts.apis.io/tempmailgrab/packages/tempmailgrab-packages.yml
  title: ''
  type: SDKs
  url: packages/tempmailgrab-packages.yml
- group: start
  href: https://artifacts.apis.io/tempmailgrab/sandbox/tempmailgrab-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tempmailgrab-sandbox.yml
- group: design
  href: https://artifacts.apis.io/tempmailgrab/asyncapi/tempmailgrab-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tempmailgrab-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/tempmailgrab/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/tempmailgrab/security/tempmailgrab-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tempmailgrab-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tempmailgrab/security/tempmailgrab-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tempmailgrab-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tempmailgrab/security/tempmailgrab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tempmailgrab-domain-security.yml
created: '2026-09-01'
description: Privacy-first disposable/temporary email service with private 24-hour inboxes, real-time WebSocket delivery, automatic OTP and verification-link extraction, attachments, webhooks, custom domains, and a versioned REST API for QA, test automation, and bots.
finops:
- has_sources: true
  method: derived
  name: Tempmailgrab Finops
  primary_unit: subscription
  service_category: ''
  slug: tempmailgrab-finops
  template: false
image: https://tempmailgrab.com/og.png
layout: provider
modified: '2026-09-01'
name: TempMailGrab API
nav: Providers
network: true
overview: 'TempMailGrab API publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Byod API, Inbox API, Messages API, and 2 more. Tagged areas include Email, temporary-email, Disposable Email, OTP, and Webhook.


  The TempMailGrab API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  TempMailGrab API''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Tempmailgrab Plans Pricing
  plan_count: 3
  slug: tempmailgrab-plans-pricing
- name: Tempmailgrab Price Estimates
  plan_count: 0
  slug: tempmailgrab-price-estimates
random_paper: 21
rate_limits:
- limit_count: 4
  name: Tempmailgrab Rate Limits
  slug: tempmailgrab-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: TempMailGrab API API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: tempmailgrab-rules
score:
  band: exemplar
  composite: 69.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 63.0
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 86.8
  previous_composite: 68.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 80.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tempmailgrab/tempmailgrab-2026-09-02T163054.png
security:
- kind: authentication
  name: Tempmailgrab Authentication
  slug: tempmailgrab-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Tempmailgrab Domain Security
  slug: tempmailgrab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tempmailgrab Vulnerability Disclosure
  slug: tempmailgrab-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: tempmailgrab-custom-domain
  slug: tempmailgrab-custom-domain
- name: tempmailgrab-verify-email-otp
  slug: tempmailgrab-verify-email-otp
- name: tempmailgrab-webhook-delivery
  slug: tempmailgrab-webhook-delivery
slug: tempmailgrab
tags:
- Email
- temporary-email
- Disposable Email
- OTP
- Webhook
- QA
- Testing
- Playwright
- Cypress
- Developer Tools
- Email Testing
- CI
website: https://www.tempmailgrab.com/
---
