---
access_model:
  confidence: high
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
  band: agent-ready
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
    error_semantics: documented
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
  score: 28.6
  scored_at: '2026-09-16'
api_count: 2
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
artifact_total: 11
asyncapis:
- description: ''
  name: Tempmailgrab Webhooks
  slug: tempmailgrab-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/overlays/tempmailgrab-openapi-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/llms/tempmailgrab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tempmailgrab-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/well-known/tempmailgrab-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tempmailgrab-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/well-known/tempmailgrab-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tempmailgrab-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/authentication/tempmailgrab-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tempmailgrab-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/conventions/tempmailgrab-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tempmailgrab-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/errors/tempmailgrab-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tempmailgrab-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/examples/tempmailgrab-examples.yml
  title: ''
  type: Examples
  url: examples/tempmailgrab-examples.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/data-model/tempmailgrab-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tempmailgrab-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/lifecycle/tempmailgrab-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tempmailgrab-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/changelog/tempmailgrab-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tempmailgrab-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/conformance/tempmailgrab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tempmailgrab-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/rate-limits/tempmailgrab-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tempmailgrab-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/plans/tempmailgrab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tempmailgrab-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/packages/tempmailgrab-packages.yml
  title: ''
  type: Packages
  url: packages/tempmailgrab-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/packages/tempmailgrab-packages.yml
  title: ''
  type: SDKs
  url: packages/tempmailgrab-packages.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/sandbox/tempmailgrab-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tempmailgrab-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/asyncapi/tempmailgrab-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tempmailgrab-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/security/tempmailgrab-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tempmailgrab-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/security/tempmailgrab-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tempmailgrab-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/security/tempmailgrab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tempmailgrab-domain-security.yml
created: '2026-09-01'
description: Privacy-first disposable/temporary email service with private 24-hour inboxes, real-time WebSocket delivery, automatic OTP and verification-link extraction, attachments, webhooks, custom domains, and a versioned REST API for QA, test automation, and bots.
image: https://tempmailgrab.com/og.png
layout: provider
modified: '2026-09-01'
name: TempMailGrab API
nav: Providers
network: true
overview: 'TempMailGrab API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Byod API, Inbox API, Messages API, and 2 more. Tagged areas include Email, temporary-email, Disposable Email, OTP, and Webhook.


  The TempMailGrab API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TempMailGrab API''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Tempmailgrab Plans Pricing
  plan_count: 2
  slug: tempmailgrab-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Tempmailgrab Rate Limits
  slug: tempmailgrab-rate-limits
score:
  band: strong
  composite: 61.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 60.9
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 86.8
  previous_composite: 62.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/tempmailgrab/refs/heads/main/screenshots/tempmailgrab-2026-09-02T163054.png
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
