---
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
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Kartra's inbound developer API. One endpoint, POST only, form-encoded, with the operation selected by `actions[].cmd`. Twenty-nine documented commands cover leads, tags, lists, automation sequences, c
  name: Kartra API
  slug: kartra-api
artifact_total: 8
asyncapis:
- description: ''
  name: Kartra Webhooks
  slug: kartra-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://kartra.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.kartra.com/en/collections/19655232-developers
- group: docs
  title: ''
  type: Documentation
  url: https://support.kartra.com/en/collections/19655232-developers
- group: docs
  title: ''
  type: APIReference
  url: https://support.kartra.com/en/articles/15369013-connecting-to-the-api
- group: start
  title: ''
  type: GettingStarted
  url: https://support.kartra.com/en/articles/15369011-activating-your-app
- group: operate
  title: ''
  type: Support
  url: https://support.kartra.com/en/
- group: company
  title: ''
  type: Blog
  url: https://kartra.com/learning-center/
- group: commercial
  title: ''
  type: Pricing
  url: https://kartra.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://kartra.com/kartra-trial/
- group: start
  title: ''
  type: Login
  url: https://app.kartra.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kartra.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kartra.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://kartra.com/gdpr/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kartra.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/kartra-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kartra-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kartra-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kartra-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kartra-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kartra-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kartra-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kartra-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kartra-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kartra-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/kartra-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kartra-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kartra-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kartra-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kartra-domain-security.yml
created: '2026-08-12'
description: 'Kartra is an all-in-one online business platform operated by Kartra, Inc. of Las Vegas, Nevada, that bundles landing pages and funnels, email marketing with automation sequences, checkouts and recurring billing, membership sites and courses, video hosting, calendars and booking, helpdesks, affiliate management and lead scoring into a single subscription. Its developer surface is three distinct things: an inbound API that is a single form-encoded POST endpoint at https://app.kartra.com/api driven by 29 documented `cmd` values and scoped to exactly one lead per call; an outbound API that POSTs 24 JSON lead and commerce events to URLs configured in the account; and an IPN system that POSTs six payment-lifecycle notifications as flat form variables. Kartra publishes no OpenAPI, no SDK in any language, no signed webhooks and no idempotency contract, and it returns HTTP 200 for every outcome including authentication failure — the numeric `type` field in the response body is the real
  error signal.'
image: https://kartra.com/wp-content/uploads/2024/06/Kartra-logo-icon-blue-transparent.png
layout: provider
mcp_servers:
- description: ''
  name: kartra-mcp.yml
  slug: kartra-mcpyml
modified: '2026-08-12'
name: Kartra
nav: Providers
network: true
overview: 'Kartra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing Automation, Email Marketing, CRM, and Contacts.


  The Kartra catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kartra''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Kartra Plans Pricing
  plan_count: 4
  slug: kartra-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 1
  name: Kartra Rate Limits
  slug: kartra-rate-limits
score:
  band: strong
  composite: 64.1
  delta: 3.9
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 66.1
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 60.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kartra/refs/heads/main/screenshots/kartra-2026-08-17T081006.png
security:
- kind: authentication
  name: Kartra Authentication
  slug: kartra-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Kartra Domain Security
  slug: kartra-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kartra Vulnerability Disclosure
  slug: kartra-vulnerability-disclosure
  summary_line: Hackerone
slug: kartra
tags:
- Company
- Marketing Automation
- Email Marketing
- CRM
- Contacts
- E-Commerce
- Payments
- Subscriptions
- Membership
- Landing Pages
- Webhooks
- SaaS
website: https://kartra.com/
---
