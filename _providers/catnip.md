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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Programmatically send messages and trigger flows/blocks to a specific bot user on Messenger, Instagram, or WhatsApp. POST to the send endpoint with the bot's unique chatfuel_token and a flow name, blo
  name: Chatfuel Broadcasting API
  slug: chatfuel-broadcasting-api
- description: Manage Chatfuel bots and their Facebook page bindings. Create empty bots, clone content between bots, generate role-scoped invite links (ADMIN, EDITOR, MARKETER, OPERATOR, VIEWER), and bind/unbind bot
  name: Chatfuel Dashboard API
  slug: chatfuel-dashboard-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://chatfuel.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.chatfuel.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chatfuel.com/en/collections/168839-api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chatfuel.com/en/collections/168839-api
- group: commercial
  title: ''
  type: Pricing
  url: https://chatfuel.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://panel.chatfuel.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chatfuel.com/files/TermsOfUse.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chatfuel.com/privacy-policy.html
- group: auth
  title: ''
  type: Compliance
  url: https://chatfuel.com/gdpr
- group: auth
  title: ''
  type: Authentication
  url: authentication/catnip-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/catnip-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/catnip-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/catnip-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/catnip-domain-security.yml
created: '2026-07-17'
description: 'Catnip Inc is the company behind Chatfuel, an AI-powered business messaging and chatbot automation platform for Facebook Messenger, Instagram, and WhatsApp. Chatfuel lets businesses build conversational flows, run broadcasts, qualify leads, book appointments, and automate customer support with AI agents. For developers Chatfuel exposes three public integration surfaces: a Broadcasting API for programmatically sending messages and triggering flows to bot users, a Dashboard API for managing bots and Facebook page bindings, and a JSON API plugin that lets a bot call an external backend and render dynamic content.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/catnip.png
layout: provider
modified: '2026-07-18'
name: Catnip
nav: Providers
network: true
overview: 'Catnip publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chatbots, Messaging, Conversational AI, and Marketing Automation.


  Catnip''s developer surface includes documentation, API reference, pricing, signup flow, authentication, and 9 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 1
  name: Catnip Rate Limits
  slug: catnip-rate-limits
score:
  band: thin
  composite: 28.2
  delta: -1.3
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/catnip/refs/heads/main/screenshots/catnip-2026-07-25T204810.png
security:
- kind: authentication
  name: Catnip Authentication
  slug: catnip-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Catnip Domain Security
  slug: catnip-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: catnip
tags:
- Company
- Chatbots
- Messaging
- Conversational AI
- Marketing Automation
- Facebook Messenger
- Instagram
- WhatsApp
- Customer Engagement
website: https://chatfuel.com
---
