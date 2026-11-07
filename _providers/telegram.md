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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 42
  human_in_the_loop: 1
  name: Telegram Agentic Access
  operation_count: 51
  slug: telegram-agentic-access
  summary_line: 51 operations · 42 acting · 1 human-in-the-loop
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
artifact_total: 55
asyncapis:
- description: ''
  name: Telegram Webhooks
  slug: telegram-webhooks
collections:
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
- group: design
  href: https://artifacts.apis.io/telegram/rules/telegram-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/telegram-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/telegram/rules/telegram-bot-rules.yml
  title: ''
  type: Spectral
  url: rules/telegram-bot-rules.yml
- group: design
  href: https://artifacts.apis.io/telegram/rules/telegram-rules.yml
  title: ''
  type: Spectral
  url: rules/telegram-rules.yml
- group: design
  href: https://artifacts.apis.io/telegram/json-ld/telegram-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/telegram-context.jsonld
- group: design
  href: https://artifacts.apis.io/telegram/vocabulary/telegram-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/telegram-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/telegram/asyncapi/telegram-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/telegram-webhooks.yml
- group: design
  href: https://artifacts.apis.io/telegram/data-model/telegram-data-model.yml
  title: ''
  type: DataModel
  url: data-model/telegram-data-model.yml
- group: build
  href: https://artifacts.apis.io/telegram/cli/telegram-cli.yml
  title: ''
  type: CLI
  url: cli/telegram-cli.yml
- group: operate
  href: https://artifacts.apis.io/telegram/changelog/telegram-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/telegram-changelog.yml
- group: design
  href: https://artifacts.apis.io/telegram/conventions/telegram-conventions.yml
  title: ''
  type: Conventions
  url: conventions/telegram-conventions.yml
- group: start
  href: https://artifacts.apis.io/telegram/sandbox/telegram-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/telegram-sandbox.yml
- group: design
  href: https://artifacts.apis.io/telegram/lifecycle/telegram-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/telegram-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/telegram/errors/telegram-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/telegram-problem-types.yml
- group: design
  href: https://artifacts.apis.io/telegram/conformance/telegram-conformance.yml
  title: ''
  type: Conformance
  url: conformance/telegram-conformance.yml
- group: agent
  href: https://artifacts.apis.io/telegram/llms/telegram-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/telegram-llms.txt
- group: other
  href: https://artifacts.apis.io/telegram/hosts/telegram-hosts.yml
  title: ''
  type: Hosts
  url: hosts/telegram-hosts.yml
- group: build
  href: https://artifacts.apis.io/telegram/integrations/telegram-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/telegram-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/telegram/packages/telegram-packages.yml
  title: ''
  type: SDKs
  url: packages/telegram-packages.yml
- group: build
  href: https://artifacts.apis.io/telegram/packages/telegram-packages.yml
  title: ''
  type: Packages
  url: packages/telegram-packages.yml
- group: start
  title: ''
  type: Login
  url: https://core.telegram.org/widgets/login
- group: start
  title: ''
  type: GettingStarted
  url: https://core.telegram.org/bots/tutorial
- group: operate
  title: ''
  type: FAQ
  url: https://core.telegram.org/bots/faq
- group: design
  title: ''
  type: Webhooks
  url: https://core.telegram.org/bots/webhooks
- group: operate
  title: ''
  type: ChangeLog
  url: https://core.telegram.org/bots/api-changelog
- group: operate
  title: ''
  type: Support
  url: https://t.me/botsupport
- group: company
  title: ''
  type: Newsroom
  url: https://telegram.org/press
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/tdlib/telegram-bot-api
- group: commercial
  title: ''
  type: Pricing
  url: https://core.telegram.org/bots/faq#my-bot-is-hitting-limits-how-do-i-avoid-this
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  href: https://artifacts.apis.io/telegram/plans/telegram-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/telegram-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/telegram/rate-limits/telegram-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/telegram-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/telegram/finops/telegram-finops.yml
  title: ''
  type: FinOps
  url: finops/telegram-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.telegram.org/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/tdlib/td/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/tdlib/td/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/telegram/agentic-access/telegram-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/telegram-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/telegram/security/telegram-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/telegram-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/telegram/authentication/telegram-authentication.yml
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
- group: start
  title: ''
  type: DeveloperPortal
  url: https://core.telegram.org/bots
- group: docs
  title: ''
  type: Documentation
  url: https://core.telegram.org/bots
- group: docs
  title: ''
  type: APIReference
  url: https://core.telegram.org/bots/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TelegramMessenger
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
- has_sources: false
  method: generated
  name: Telegram Finops
  primary_unit: request
  service_category: API
  slug: telegram-finops
  template: true
image: https://telegram.org/img/t_logo.png
json_schemas:
- name: BooleanResponse
  property_count: 2
  slug: telegram-boolean-response
- name: BotCommand
  property_count: 2
  slug: telegram-bot-command
- name: BotCommandsResponse
  property_count: 2
  slug: telegram-bot-commands-response
- name: ChatInviteLinkResponse
  property_count: 2
  slug: telegram-chat-invite-link-response
- name: ChatMemberResponse
  property_count: 2
  slug: telegram-chat-member-response
- name: ChatMembersResponse
  property_count: 2
  slug: telegram-chat-members-response
- name: ChatPermissions
  property_count: 11
  slug: telegram-chat-permissions
- name: ChatResponse
  property_count: 2
  slug: telegram-chat-response
- name: FileResponse
  property_count: 2
  slug: telegram-file-response
- name: IntegerResponse
  property_count: 2
  slug: telegram-integer-response
- name: LabeledPrice
  property_count: 2
  slug: telegram-labeled-price
- name: MessageIdResponse
  property_count: 2
  slug: telegram-message-id-response
- name: MessageResponse
  property_count: 2
  slug: telegram-message-response
- name: Telegram Message
  property_count: 21
  slug: telegram-message
- name: StringResponse
  property_count: 2
  slug: telegram-string-response
- name: Telegram Update
  property_count: 11
  slug: telegram-update
- name: UpdatesResponse
  property_count: 2
  slug: telegram-updates-response
- name: UserProfilePhotosResponse
  property_count: 2
  slug: telegram-user-profile-photos-response
- name: UserResponse
  property_count: 2
  slug: telegram-user-response
- name: WebhookInfoResponse
  property_count: 2
  slug: telegram-webhook-info-response
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
overview: 'Telegram publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bot Info API, Chat Management API, Getting Updates API, and 7 more. Tagged areas include Bots, Chat, Messaging, Notification, and Payments.


  The Telegram catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Telegram''s developer surface includes CLI, changelog, sandbox, getting-started guide, FAQ, support, pricing, and 43 more developer resources.'
plans:
- name: Telegram Plans Pricing
  plan_count: 2
  slug: telegram-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Telegram Rate Limits
  slug: telegram-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Telegram — bot rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 6
  slug: telegram-bot-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Telegram — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: telegram-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Telegram API Rules
  rule_count: 64
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 5
  slug: telegram-rules
score:
  band: strong
  composite: 58.4
  coverage:
    artifact_dirs: 36
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.4
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 69.8
    developer_ergonomics: 76.2
    discoverability: 67.9
    operational_transparency: 76.3
  open_source:
    applies: true
    score: 0.0
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/telegram/telegram-2026-06-20T195033.png
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
- Social
- Public APIs
- Chatbots
- Webhook
- Mini Apps
website: https://www.telegram.org/
---
