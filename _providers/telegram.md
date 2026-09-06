---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 51
  human_in_the_loop: 1
  name: Telegram Agentic Access
  operation_count: 51
  slug: telegram-agentic-access
  summary_line: 51 operations · 51 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: TDLib is a cross-platform, fully functional Telegram client library for third-party developers. TDLib takes care of all network implementation details, encryption and local data storage, allowing deve
  name: Telegram TDLib (Telegram Database Library)
  slug: telegram-tdlib
- baseURL: https://api.telegram.org/bot{token}
  baseurl_source: declared
  description: Methods for getting and setting bot information
  name: Telegram Bot Info API
  slug: telegram-bot-info-api
- baseURL: https://api.telegram.org/bot{token}
  baseurl_source: declared
  description: Methods for managing chats and chat settings
  name: Telegram Chat Management API
  slug: telegram-chat-management-api
- baseURL: https://api.telegram.org/bot{token}
  baseurl_source: declared
  description: Methods for receiving incoming updates from Telegram
  name: Telegram Getting Updates API
  slug: telegram-getting-updates-api
- baseURL: https://api.telegram.org/bot{token}
  baseurl_source: declared
  description: Methods for managing chat invite links
  name: Telegram Invites API
  slug: telegram-invites-api
- baseURL: https://api.telegram.org/bot{token}
  baseurl_source: declared
  description: Methods for managing chat members and administrators
  name: Telegram Member Management API
  slug: telegram-member-management-api
- baseURL: https://api.telegram.org/bot{token}
  baseurl_source: declared
  description: Methods for editing and deleting messages
  name: Telegram Message Editing API
  slug: telegram-message-editing-api
- baseURL: https://api.telegram.org/bot{token}
  baseurl_source: declared
  description: Methods for sending messages and media
  name: Telegram Messaging API
  slug: telegram-messaging-api
- baseURL: https://api.telegram.org/bot{token}
  baseurl_source: declared
  description: Methods for handling Telegram Payments
  name: Telegram Payments API
  slug: telegram-payments-api
- baseURL: https://api.telegram.org/bot{token}
  baseurl_source: declared
  description: Methods for working with sticker sets
  name: Telegram Stickers API
  slug: telegram-stickers-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Telegram Bot Bot Info API
  slug: open-telegram-bot-info-api
- collection_type: open
  name: Telegram Bot API
  slug: open-telegram-bot
- collection_type: open
  name: Telegram Bot Bot Info Chat Management API
  slug: open-telegram-chat-management-api
- collection_type: open
  name: Telegram Bot Bot Info Getting Updates API
  slug: open-telegram-getting-updates-api
- collection_type: open
  name: Telegram Bot Bot Info Invites API
  slug: open-telegram-invites-api
- collection_type: open
  name: Telegram Bot Bot Info Member Management API
  slug: open-telegram-member-management-api
- collection_type: open
  name: Telegram Bot Bot Info Message Editing API
  slug: open-telegram-message-editing-api
- collection_type: open
  name: Telegram Bot Bot Info Messaging API
  slug: open-telegram-messaging-api
- collection_type: open
  name: Telegram Bot Bot Info Payments API
  slug: open-telegram-payments-api
- collection_type: open
  name: Telegram Bot Bot Info Stickers API
  slug: open-telegram-stickers-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/tdlib/td/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/tdlib/td/blob/master/LICENSE
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
overview: 'Telegram publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Bot Info API, Chat Management API, Getting Updates API, and 6 more. Tagged areas include Bots, Chat, Messaging, Notification, and Payments.


  The Telegram catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Telegram''s developer surface includes authentication, engineering blog, GitHub presence, and 10 more developer resources.'
plans:
- name: Telegram Plans Pricing
  plan_count: 3
  slug: telegram-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Telegram Rate Limits
  slug: telegram-rate-limits
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Telegram API Rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 6
  slug: telegram-bot-rules
- effective_rule_count: 6
  extends: []
  name: Telegram API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: telegram-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 75.0
    catalog_earned_first_party: 0.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 54.5
    contract_quality: 66.3
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 54.5
    operational_transparency: 44.7
  open_source:
    applies: true
    score: 0.0
  previous_composite: 47.5
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
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Notification
- Payments
- Telegram
website: https://core.telegram.org
---
