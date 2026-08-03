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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 117
  human_in_the_loop: 0
  name: Zoho Cliq Agentic Access
  operation_count: 158
  slug: zoho-cliq-agentic-access
  summary_line: 158 operations · 117 acting
api_count: 22
apis:
- description: The Bots API from Zoho Cliq — 9 operation(s) for bots.
  name: Zoho Cliq Bots API
  slug: zoho-cliq-bots-api
- description: Buttons Module
  name: Zoho Cliq buttons API
  slug: zoho-cliq-buttons-api
- description: Chats Module
  name: Zoho Cliq chats API
  slug: zoho-cliq-chats-api
- description: DND Settings Module
  name: Zoho Cliq dndsettings API
  slug: zoho-cliq-dndsettings-api
- description: Extensions Module
  name: Zoho Cliq Extensions API
  slug: zoho-cliq-extensions-api
- description: Functions Module
  name: Zoho Cliq Functions API
  slug: zoho-cliq-functions-api
- description: Keyboard Shortcuts Module
  name: Zoho Cliq keyboardshortcuts API
  slug: zoho-cliq-keyboardshortcuts-api
- description: Mentions Module
  name: Zoho Cliq mentions API
  slug: zoho-cliq-mentions-api
- description: Message Actions Module
  name: Zoho Cliq messageactions API
  slug: zoho-cliq-messageactions-api
- description: APIs for sending structured interactive message cards (Poll, Modern Inline, and Prompt) inside Zoho Cliq conversations.
  name: Zoho Cliq messagecards API
  slug: zoho-cliq-messagecards-api
- description: Message Format Module
  name: Zoho Cliq messageformat API
  slug: zoho-cliq-messageformat-api
- description: Messages Module
  name: Zoho Cliq messages API
  slug: zoho-cliq-messages-api
- description: Mobile Settings Module
  name: Zoho Cliq mobilesettings API
  slug: zoho-cliq-mobilesettings-api
- description: My Pins and Chat Folders Module
  name: Zoho Cliq mypins API
  slug: zoho-cliq-mypins-api
- description: Pin Messages Module
  name: Zoho Cliq pinmessages API
  slug: zoho-cliq-pinmessages-api
- description: 'Manage Cliq Datastores - structured, schema-defined storage tables scoped to an organisation or extension. Datastores allow platform components to persist and query structured data across executions. '
  name: Zoho Cliq Platform_storage API
  slug: zoho-cliq-platform-storage-api
- description: Reminders Module
  name: Zoho Cliq reminders API
  slug: zoho-cliq-reminders-api
- description: Scheduled Messages Module
  name: Zoho Cliq scheduledmessages API
  slug: zoho-cliq-scheduledmessages-api
- description: Slash Commands Module
  name: Zoho Cliq slashcommands API
  slug: zoho-cliq-slashcommands-api
- description: The Stars API from Zoho Cliq — 2 operation(s) for stars.
  name: Zoho Cliq Stars API
  slug: zoho-cliq-stars-api
- description: Threads Module
  name: Zoho Cliq threads API
  slug: zoho-cliq-threads-api
- description: User Preferences Module
  name: Zoho Cliq userpreferences API
  slug: zoho-cliq-userpreferences-api
artifact_total: 74
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoho-cliq-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-cliq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-cliq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoho-cliq-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoho-cliq-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/cliq/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/cliq/help/restapi/v3/introduction/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/showcase/zoho-cliq
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/blog/cliq
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/cliq/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://us.zohostatus.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/ZohoCliq
- group: commercial
  title: ''
  type: Plans
  url: plans/zoho-cliq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoho-cliq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zoho-cliq-finops.yml
created: '2026-06-13'
description: Zoho Cliq is a team messaging and collaboration platform with a REST API for managing channels, bots, slash commands, message webhooks, and team communications. The API follows RESTful architecture principles with resource-oriented URLs, JSON request and response bodies, and standard HTTP verbs. It supports multi-data center deployments across nine regional domains and uses OAuth 2.0 for authentication.
examples:
- key_count: 8
  name: Bots
  slug: bots
- key_count: 13
  name: Chats
  slug: chats
- key_count: 8
  name: Datastores
  slug: datastores
- key_count: 2
  name: Dndsettings
  slug: dndsettings
- key_count: 3
  name: Extensions
  slug: extensions
- key_count: 6
  name: Functions
  slug: functions
- key_count: 3
  name: Keyboardshortcuts
  slug: keyboardshortcuts
- key_count: 3
  name: Mentions
  slug: mentions
- key_count: 6
  name: Messageactions
  slug: messageactions
- key_count: 2
  name: Messagecards
  slug: messagecards
- key_count: 3
  name: Messages
  slug: messages
- key_count: 2
  name: Mobilesettings
  slug: mobilesettings
- key_count: 10
  name: Mypins
  slug: mypins
- key_count: 5
  name: Pinmessages
  slug: pinmessages
- key_count: 4
  name: Reminders
  slug: reminders
- key_count: 5
  name: Scheduledmessages
  slug: scheduledmessages
- key_count: 7
  name: Slashcommands
  slug: slashcommands
- key_count: 3
  name: Stars
  slug: stars
- key_count: 4
  name: Threads
  slug: threads
- key_count: 2
  name: Userpreferences
  slug: userpreferences
finops:
- name: Zoho Cliq Finops
  service_category: ''
  slug: zoho-cliq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-cliq.png
json_schemas:
- name: Zoho Cliq Bots Schemas
  property_count: 0
  slug: bots
- name: Zoho Cliq Buttons Schemas
  property_count: 0
  slug: buttons
- name: Zoho Cliq Chats Schemas
  property_count: 0
  slug: chats
- name: Zoho Cliq Datastores Schemas
  property_count: 0
  slug: datastores
- name: Zoho Cliq Dndsettings Schemas
  property_count: 0
  slug: dndsettings
- name: Zoho Cliq Extensions Schemas
  property_count: 0
  slug: extensions
- name: Zoho Cliq Functions Schemas
  property_count: 0
  slug: functions
- name: Zoho Cliq Keyboardshortcuts Schemas
  property_count: 0
  slug: keyboardshortcuts
- name: Zoho Cliq Mentions Schemas
  property_count: 0
  slug: mentions
- name: Zoho Cliq Messageactions Schemas
  property_count: 0
  slug: messageactions
- name: Zoho Cliq Messagecards Schemas
  property_count: 0
  slug: messagecards
- name: Zoho Cliq Messageformat Schemas
  property_count: 0
  slug: messageformat
- name: Zoho Cliq Messages Schemas
  property_count: 0
  slug: messages
- name: Zoho Cliq Mobilesettings Schemas
  property_count: 0
  slug: mobilesettings
- name: Zoho Cliq Mypins Schemas
  property_count: 0
  slug: mypins
- name: Zoho Cliq Pinmessages Schemas
  property_count: 0
  slug: pinmessages
- name: Zoho Cliq Reminders Schemas
  property_count: 0
  slug: reminders
- name: Zoho Cliq Scheduledmessages Schemas
  property_count: 0
  slug: scheduledmessages
- name: Zoho Cliq Slashcommands Schemas
  property_count: 0
  slug: slashcommands
- name: Zoho Cliq Stars Schemas
  property_count: 0
  slug: stars
- name: Zoho Cliq Threads Schemas
  property_count: 0
  slug: threads
- name: Zoho Cliq Userpreferences Schemas
  property_count: 0
  slug: userpreferences
jsonld:
- class_count: 0
  name: Zoho Cliq Context
  property_count: 50
  slug: zoho-cliq
layout: provider
modified: '2026-06-13'
name: Zoho Cliq
nav: Providers
network: true
overview: 'Zoho Cliq publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Bots API, buttons API, chats API, and 19 more. Tagged areas include Messaging, Team Collaboration, Chat, Bots, and Webhooks.


  The Zoho Cliq catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zoho Cliq''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Zoho Cliq Plans Pricing
  plan_count: 4
  slug: zoho-cliq-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 0
  name: Zoho Cliq Rate Limits
  slug: zoho-cliq-rate-limits
rules:
- name: Zoho Cliq API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: zoho-cliq-jsonschema-spectral-rules
scopes:
- name: Zoho Cliq Scopes
  scope_count: 61
  slug: zoho-cliq-scopes
  summary_line: 61 scopes · implicit/authorizationCode
score:
  band: developing
  composite: 50.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 74.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 55.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-cliq/refs/heads/main/screenshots/zoho-cliq-2026-06-20T201935.png
security:
- kind: authentication
  name: Zoho Cliq Authentication
  slug: zoho-cliq-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Zoho Cliq Domain Security
  slug: zoho-cliq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Cliq Vulnerability Disclosure
  slug: zoho-cliq-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-cliq
tags:
- Messaging
- Team Collaboration
- Chat
- Bots
- Webhooks
- Slash Commands
- Communication
website: https://www.zoho.com/cliq/
---
