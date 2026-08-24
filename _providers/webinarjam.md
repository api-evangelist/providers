---
access_model:
  confidence: high
  label: Paid with approval-gated API
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://webinarjam.com/pricing/
  - https://support.webinarjam.com/en/articles/15370143-apply-for-an-api-key-for-webinarjam-or-everwebinar
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: 'REST API for managing WebinarJam live webinars — list all webinars, retrieve one webinar''s schedules, presenters and custom registration fields, register attendees and return their unique room links, '
  name: WebinarJam API
  slug: api
- description: REST API for managing EverWebinar automated and evergreen webinars — list webinars, read one webinar's detail, register attendees against a specific session date and timezone, list registrants and att
  name: EverWebinar API
  slug: everwebinar-api
artifact_total: 7
asyncapis:
- description: ''
  name: Webinarjam Webhooks
  slug: webinarjam-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://webinarjam.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.webinarjam.com/en/collections/19655423-developer-api
- group: docs
  title: ''
  type: Documentation
  url: https://support.webinarjam.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://support.webinarjam.com/en/articles/15370142-use-webinarjam-and-everwebinar-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://support.webinarjam.com/en/articles/15370144-connect-to-webinarjam-or-everwebinar-api
- group: operate
  title: ''
  type: Support
  url: https://support.webinarjam.com/en/
- group: company
  title: ''
  type: Blog
  url: https://webinarjam.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://webinarjam.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://webinarjam.com/14-day-trial-checkout/
- group: start
  title: ''
  type: Login
  url: https://app.webinarjam.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://webinarjam.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://webinarjam.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://support.webinarjam.com/en/articles/15370067-understand-account-security-and-technology
- group: operate
  title: ''
  type: StatusPage
  url: https://status.webinarjam.com/
- group: auth
  title: ''
  type: API Key Application
  url: https://support.webinarjam.com/en/articles/15370143-apply-for-an-api-key-for-webinarjam-or-everwebinar
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/webinarjam-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/webinarjam-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/webinarjam-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/webinarjam-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/webinarjam-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/webinarjam-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/webinarjam-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/webinarjam-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/webinarjam-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/webinarjam-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/webinarjam-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/webinarjam-domain-security.yml
created: '2026-05-11'
description: WebinarJam is a live webinar platform for marketing, training, and sales events, while its sibling product EverWebinar provides automated and evergreen webinar replays. Both are published by Genesis Digital LLC and share one REST API that lets integrators list webinars, read webinar detail including schedules, presenters and custom registration fields, register attendees, pull registrant and attendee analytics, and unsubscribe leads. Every operation is a POST carrying a single account-wide 64-character api_key form field over TLS, with separate /webinarjam and /everwebinar base paths on api.webinarjam.com. API access requires a paid subscription plus an application approved by WebinarJam. No OpenAPI, AsyncAPI, MCP server or SDK is published; the reference is a human help centre and outbound custom webhooks are the only event surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/webinarjam.png
layout: provider
modified: '2026-08-13'
name: WebinarJam
nav: Providers
network: true
overview: 'WebinarJam publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Webinars, Marketing, Live Events, Automated Webinars, and Evergreen Webinars.


  The WebinarJam catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WebinarJam''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Webinarjam Plans Pricing
  plan_count: 5
  slug: webinarjam-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Webinarjam Rate Limits
  slug: webinarjam-rate-limits
score:
  band: strong
  composite: 55.5
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 55.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/webinarjam/refs/heads/main/screenshots/webinarjam-2026-06-20T201333.png
security:
- kind: authentication
  name: Webinarjam Authentication
  slug: webinarjam-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Webinarjam Domain Security
  slug: webinarjam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: webinarjam
tags:
- Webinars
- Marketing
- Live Events
- Automated Webinars
- Evergreen Webinars
- Lead Generation
- Registration
- Video Streaming
- Marketing Automation
- Software-as-a-Service
website: https://webinarjam.com
---
