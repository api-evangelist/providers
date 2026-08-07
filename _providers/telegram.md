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
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 51
  human_in_the_loop: 1
  name: Telegram Agentic Access
  operation_count: 51
  slug: telegram-agentic-access
  summary_line: 51 operations · 51 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: TDLib is a cross-platform, fully functional Telegram client library for third-party developers. TDLib takes care of all network implementation details, encryption and local data storage, allowing deve
  name: Telegram TDLib (Telegram Database Library)
  slug: telegram-tdlib
- description: Methods for getting and setting bot information
  name: Telegram Bot Info API
  slug: telegram-bot-info-api
- description: Methods for managing chats and chat settings
  name: Telegram Chat Management API
  slug: telegram-chat-management-api
- description: Methods for receiving incoming updates from Telegram
  name: Telegram Getting Updates API
  slug: telegram-getting-updates-api
- description: Methods for managing chat invite links
  name: Telegram Invites API
  slug: telegram-invites-api
- description: Methods for managing chat members and administrators
  name: Telegram Member Management API
  slug: telegram-member-management-api
- description: Methods for editing and deleting messages
  name: Telegram Message Editing API
  slug: telegram-message-editing-api
- description: Methods for sending messages and media
  name: Telegram Messaging API
  slug: telegram-messaging-api
- description: Methods for handling Telegram Payments
  name: Telegram Payments API
  slug: telegram-payments-api
- description: Methods for working with sticker sets
  name: Telegram Stickers API
  slug: telegram-stickers-api
artifact_total: 27
collections:
- collection_type: open
  name: Telegram Bot API
  slug: open-telegram-bot
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telegram-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telegram-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telegram-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telegram-messenger
- group: auth
  title: ''
  type: Authentication
  url: https://core.telegram.org/bots/api#authorizing-your-bot
- group: commercial
  title: ''
  type: TermsOfService
  url: https://telegram.org/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://telegram.org/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://core.telegram.org
- group: operate
  title: ''
  type: StatusPage
  url: https://downdetector.com/status/telegram/
- group: company
  title: ''
  type: Blog
  url: https://telegram.org/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tdlib
created: '2025-02-12'
description: Telegram is a cloud-based instant messaging and voice-over-IP service that provides a comprehensive Bot API for developers to build bots, automate workflows, send notifications, and create interactive experiences on the Telegram platform. The platform supports text messages, media sharing, payments, inline keyboards, inline queries, webhooks, and live location sharing.
examples:
- key_count: 2
  name: Telegram Get Updates Example
  slug: telegram-get-updates-example
- key_count: 2
  name: Telegram Send Message Example
  slug: telegram-send-message-example
- key_count: 2
  name: Telegram Send Poll Example
  slug: telegram-send-poll-example
finops:
- name: Telegram Finops
  service_category: API
  slug: telegram-finops
graphqls:
- description: A conceptual GraphQL schema for the Telegram Bot API, derived from the official
  name: Telegram GraphQL Schema
  slug: telegram-graphql
image: https://telegram.org/img/t_logo.png
json_schemas:
- name: Telegram Message
  property_count: 21
  slug: telegram-message
- name: Telegram Update
  property_count: 11
  slug: telegram-update
json_structures:
- name: Telegram Message Structure
  property_count: 0
  slug: telegram-message-structure
jsonld:
- class_count: 12
  name: Telegram Context
  property_count: 31
  slug: telegram-context
layout: provider
modified: '2026-05-19'
name: Telegram
nav: Providers
network: true
overview: 'Telegram publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Bot Info API, Chat Management API, Getting Updates API, and 6 more. Tagged areas include Bots, Chat, Messaging, Notifications, and Payments.


  The Telegram catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Telegram''s developer surface includes authentication, engineering blog, GitHub presence, and 8 more developer resources.'
plans:
- name: Telegram Plans Pricing
  plan_count: 3
  slug: telegram-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 5
  name: Telegram Rate Limits
  slug: telegram-rate-limits
rules:
- name: Telegram API Rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 6
  slug: telegram-bot-rules
- name: Telegram API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: telegram-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 73.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 27.1
    operational_transparency: 52.6
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telegram/refs/heads/main/screenshots/telegram-2026-06-20T195033.png
security:
- kind: authentication
  name: Telegram Authentication
  slug: telegram-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Telegram Domain Security
  slug: telegram-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telegram
tags:
- Bots
- Chat
- Messaging
- Notifications
- Payments
- Telegram
website: https://core.telegram.org
---
