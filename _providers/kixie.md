---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: 'The primary Kixie automation surface. A single POST endpoint on the apig.kixie.com gateway that dispatches on an `eventname` discriminator in the JSON body — `call` (place an outbound call through an '
  name: Kixie Event API
  slug: kixie-event-api
- description: A path-versioned management surface for Kixie's event webhooks. Four POST operations — postWebhook (create), putWebhook (update), getWebhooks (list) and removeWebhook (delete) — register HTTP callback
  name: Kixie Webhook Management API
  slug: kixie-webhook-management-api
- description: 'A read-only lookup that returns the current presence of a Kixie agent by email address — whether the agent''s device is registered (logged in) and whether the agent is currently on a call — wrapped in '
  name: Kixie Agent Status API
  slug: kixie-agent-status-api
artifact_total: 10
asyncapis:
- description: ''
  name: Kixie Webhooks
  slug: kixie-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.kixie.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kixie.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kixie.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.kixie.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.kixie.com/hc/en-us/articles/7273987300635-Kixie-Authentication-Overview
- group: operate
  title: ''
  type: Support
  url: https://support.kixie.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.kixie.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.kixie.com/sales-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.kixie.com/sales-blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kixie-com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kixie.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.kixie.com/sign-up/
- group: start
  title: ''
  type: Login
  url: https://app.kixie.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kixie.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kixie.com/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kixie-sales/kixie-public/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kixie.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kixie-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kixie-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kixie-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kixie-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kixie-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kixie-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kixie-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kixie-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/kixie-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kixie-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kixie-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kixie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/kixie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kixie-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kixie-llms.txt
created: '2026-08-12'
description: 'Kixie is a Los Angeles based sales-engagement and revenue-communications platform built around PowerCall, a multi-line power dialer, business phone service and SMS/MMS product that plugs bi-directionally into HubSpot, Salesforce, Pipedrive, Zoho and GoHighLevel. Its public developer surface is a small, event-oriented HTTP API served from the apig.kixie.com gateway: a single POST /app/event endpoint that dispatches on an eventname discriminator to place calls, send SMS and Team SMS, add and remove contacts from PowerLists, push numbers into and out of calling queues and cadences; a webhook management API for creating, listing, updating and deleting the eight documented event webhooks; and an agent-status lookup. Authentication is a single account scoped API key plus a Business ID, and the platform publishes a documented daily usage cap of 10,000 API calls per account. Kixie publishes no OpenAPI, AsyncAPI or GraphQL contract and ships no first-party client SDKs; the reference
  is human-readable HTML on developer.kixie.com and in the Zendesk help center.'
image: https://www.kixie.com/wp-content/uploads/2026/02/Kixie-Logo-Light.png
layout: provider
modified: '2026-08-12'
name: Kixie
nav: Providers
network: true
overview: 'Kixie publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales Engagement, Voice, Telephony, and SMS.


  The Kixie catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kixie''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Kixie Plans Pricing
  plan_count: 3
  slug: kixie-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Kixie Rate Limits
  slug: kixie-rate-limits
score:
  band: strong
  composite: 60.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 60.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 59.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kixie/refs/heads/main/screenshots/kixie-2026-08-17T081010.png
security:
- kind: authentication
  name: Kixie Authentication
  slug: kixie-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Kixie Domain Security
  slug: kixie-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Kixie Vulnerability Disclosure
  slug: kixie-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Kixie Trust Center
  slug: kixie-trust-center
  summary_line: trust center published
slug: kixie
tags:
- Company
- Sales Engagement
- Voice
- Telephony
- SMS
- Messaging
- Contact Center
- Power Dialer
- CRM
- Webhook
- Communications
- Revenue Operations
website: https://www.kixie.com/
---
