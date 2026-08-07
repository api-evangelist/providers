---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: 'HTTP API for sending any block or flow from a bot to a user via a POST request, including targeting users by attribute. Rate limited to 25 requests per second per bot. Requests are authenticated with '
  name: Chatfuel Broadcasting API
  slug: chatfuel-broadcasting-api
- description: HTTP API to programmatically create and modify bots and pages — create bots, clone bot content, generate role-based invite links, and bind/unbind bots to Facebook pages. Authenticated with a Bearer Da
  name: Chatfuel Dashboard API
  slug: chatfuel-dashboard-api
artifact_total: 5
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.chatfuel.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chatfuel.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chatfuel.com/en/collections/168839-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chatfuel.com/en/collections/168839-api
- group: operate
  title: ''
  type: Support
  url: https://docs.chatfuel.com/en/
- group: company
  title: ''
  type: Blog
  url: https://chatfuel.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://chatfuel.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.chatfuel.com/
- group: start
  title: ''
  type: Login
  url: https://app.chatfuel.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chatfuel.com/files/TermsOfUse.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chatfuel.com/privacy-policy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chatfuel.com/
- group: auth
  title: ''
  type: Compliance
  url: https://chatfuel.com/gdpr
- group: company
  title: ''
  type: Website
  url: https://chatfuel.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/chatfuel-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chatfuel-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chatfuel-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chatfuel-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chatfuel-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chatfuel-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/chatfuel-packages.yml
- group: design
  title: ''
  type: Components
  url: components/chatfuel-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chatfuel-llms.txt
created: '2026-07-17'
description: Chatfuel is a no-code AI-powered chatbot and business-automation platform for conversational commerce across Meta-owned messaging channels — WhatsApp, Instagram, Facebook Messenger, TikTok, and an embeddable website chat widget. Trusted by 18,000+ businesses and an official Meta Business Partner, Chatfuel lets teams build automated flows and AI agents that qualify leads, answer customer questions, take bookings, run re-engagement campaigns, and hand off to live agents. For developers Chatfuel exposes an HTTP Broadcasting API (api.chatfuel.com) for sending blocks and flows to users, a Dashboard API (dashboard.chatfuel.com/api) for programmatically creating and managing bots and page bindings, and a JSON API plugin for calling external services from inside a bot flow.
image: https://chatfuel.com/favicons/apple-touch-icon.png
layout: provider
modified: '2026-07-18'
name: Chatfuel
nav: Providers
network: true
overview: 'Chatfuel publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chatbots, Conversational AI, Messaging, and Marketing Automation.


  Chatfuel''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 53
rate_limits:
- limit_count: 1
  name: Chatfuel Rate Limits
  slug: chatfuel-rate-limits
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 35.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chatfuel/refs/heads/main/screenshots/chatfuel-2026-07-25T205116.png
security:
- kind: authentication
  name: Chatfuel Authentication
  slug: chatfuel-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Chatfuel Domain Security
  slug: chatfuel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chatfuel
tags:
- Company
- Chatbots
- Conversational AI
- Messaging
- Marketing Automation
- Customer Support
- WhatsApp
- Instagram
- Facebook Messenger
- No-Code
website: https://chatfuel.com
---
