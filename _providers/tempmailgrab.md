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
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://tempmailgrab.com/api/v1
  baseurl_source: declared
  description: Versioned v1 REST API for creating private disposable inboxes, reading parsed messages with extracted OTPs and verification links, managing webhooks, and registering custom domains. Machine-readable O
  name: TempMailGrab REST API
  slug: tempmailgrab-rest-api
artifact_total: 7
asyncapis:
- description: ''
  name: Tempmailgrab Webhooks
  slug: tempmailgrab-webhooks
common:
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
  title: ''
  type: LLMsTxt
  url: llms/tempmailgrab-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tempmailgrab-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tempmailgrab-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/tempmailgrab-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tempmailgrab-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tempmailgrab-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/tempmailgrab-examples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tempmailgrab-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tempmailgrab-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tempmailgrab-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tempmailgrab-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tempmailgrab-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tempmailgrab-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/tempmailgrab-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tempmailgrab-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tempmailgrab-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tempmailgrab-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: security/tempmailgrab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tempmailgrab-vulnerability-disclosure.yml
- group: auth
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
overview: 'TempMailGrab API publishes 1 API on the [APIs.io](https://apis.io/) network: TempMailGrab REST API. Tagged areas include email, temporary-email, disposable-email, otp, and webhooks.


  The TempMailGrab API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TempMailGrab API''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Tempmailgrab Plans Pricing
  plan_count: 2
  slug: tempmailgrab-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Tempmailgrab Rate Limits
  slug: tempmailgrab-rate-limits
score:
  band: strong
  composite: 63.3
  coverage:
    artifact_dirs: 21
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 64.4
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 86.8
  previous_composite: 63.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
- email
- temporary-email
- disposable-email
- otp
- webhooks
- qa
- testing
- playwright
- cypress
- developer-tools
- email-testing
- ci
website: https://tempmailgrab.com/api-docs
---
