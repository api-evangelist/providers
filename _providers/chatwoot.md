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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 82
  human_in_the_loop: 0
  name: Chatwoot Agentic Access
  operation_count: 144
  slug: chatwoot-agentic-access
  summary_line: 144 operations · 82 acting
api_count: 33
apis:
- description: The Client API is designed for building custom messaging interfaces for end users. Authenticates using inbox identifiers and contact identifiers rather than user tokens. Supports conversation creation
  name: Chatwoot Client API
  slug: client-api
- description: The Platform API is used to manage Chatwoot installations at the super admin level, including managing accounts, users, and installation-wide settings. Requires Platform App access tokens from the Sup
  name: Chatwoot Platform API
  slug: platform-api
- description: Account-specific Agent Bots
  name: Chatwoot Account AgentBots API
  slug: chatwoot-account-agentbots-api
- description: The Account API from Chatwoot — 1 operation(s) for account.
  name: Chatwoot Account API
  slug: chatwoot-account-api
- description: Account user management APIs
  name: Chatwoot Account Users API
  slug: chatwoot-account-users-api
- description: Account management APIs
  name: Chatwoot Accounts API
  slug: chatwoot-accounts-api
- description: Bot integrations
  name: Chatwoot AgentBots API
  slug: chatwoot-agentbots-api
- description: Agent management APIs
  name: Chatwoot Agents API
  slug: chatwoot-agents-api
- description: The Audit Logs API from Chatwoot — 1 operation(s) for audit logs.
  name: Chatwoot Audit Logs API
  slug: chatwoot-audit-logs-api
- description: Workflow automation rules
  name: Chatwoot Automation Rule API
  slug: chatwoot-automation-rule-api
- description: Pre-defined responses for common queries
  name: Chatwoot Canned Responses API
  slug: chatwoot-canned-responses-api
- description: Manage contact labels
  name: Chatwoot Contact Labels API
  slug: chatwoot-contact-labels-api
- description: Public contact APIs
  name: Chatwoot Contacts API API
  slug: chatwoot-contacts-api-api
- description: Contact management APIs
  name: Chatwoot Contacts API
  slug: chatwoot-contacts-api
- description: The Conversation API from Chatwoot — 1 operation(s) for conversation.
  name: Chatwoot Conversation API
  slug: chatwoot-conversation-api
- description: Manage conversation assignments
  name: Chatwoot Conversation Assignments API
  slug: chatwoot-conversation-assignments-api
- description: Public conversation APIs
  name: Chatwoot Conversations API API
  slug: chatwoot-conversations-api-api
- description: Conversation management APIs
  name: Chatwoot Conversations API
  slug: chatwoot-conversations-api
- description: Customer satisfaction survey
  name: Chatwoot CSAT Survey Page API
  slug: chatwoot-csat-survey-page-api
- description: Custom fields for contacts and conversations
  name: Chatwoot Custom Attributes API
  slug: chatwoot-custom-attributes-api
- description: Saved filters for conversations
  name: Chatwoot Custom Filters API
  slug: chatwoot-custom-filters-api
- description: Knowledge base management
  name: Chatwoot Help Center API
  slug: chatwoot-help-center-api
- description: The Inbox API API from Chatwoot — 1 operation(s) for inbox api.
  name: Chatwoot Inbox API API
  slug: chatwoot-inbox-api-api
- description: Communication channels setup
  name: Chatwoot Inboxes API
  slug: chatwoot-inboxes-api
- description: Third-party integrations
  name: Chatwoot Integrations API
  slug: chatwoot-integrations-api
- description: Account label management APIs
  name: Chatwoot Labels API
  slug: chatwoot-labels-api
- description: Public message APIs
  name: Chatwoot Messages API API
  slug: chatwoot-messages-api-api
- description: Message management APIs
  name: Chatwoot Messages API
  slug: chatwoot-messages-api
- description: User profile APIs
  name: Chatwoot Profile API
  slug: chatwoot-profile-api
- description: Analytics and reporting APIs
  name: Chatwoot Reports API
  slug: chatwoot-reports-api
- description: Team management APIs
  name: Chatwoot Teams API
  slug: chatwoot-teams-api
- description: User management APIs
  name: Chatwoot Users API
  slug: chatwoot-users-api
- description: Event notification webhooks
  name: Chatwoot Webhooks API
  slug: chatwoot-webhooks-api
artifact_total: 63
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chatwoot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chatwoot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chatwoot-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.chatwoot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.chatwoot.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/chatwoot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chatwoot
- group: company
  title: ''
  type: Blog
  url: https://www.chatwoot.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chatwoot.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chatwoot.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/chatwootapp
- group: commercial
  title: ''
  type: Plans
  url: plans/chatwoot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chatwoot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chatwoot-finops.yml
created: '2026-06-13'
description: Chatwoot is an open-source customer support and omni-channel messaging platform that provides REST APIs for managing conversations, contacts, agents, teams, labels, and integrating customer communication workflows. It supports live chat, email, WhatsApp, Facebook, Instagram, Telegram, SMS, and more, with Application APIs for agent-level automation, Client APIs for custom chat interfaces, and Platform APIs for managing self-hosted installations at scale.
examples:
- key_count: 10
  name: Agent Example
  slug: agent-example
- key_count: 13
  name: Contact Example
  slug: contact-example
- key_count: 15
  name: Conversation Example
  slug: conversation-example
- key_count: 12
  name: Inbox Example
  slug: inbox-example
- key_count: 13
  name: Message Example
  slug: message-example
finops:
- name: Chatwoot Finops
  service_category: ''
  slug: chatwoot-finops
graphqls:
- description: This is a conceptual GraphQL schema for Chatwoot, the open-source customer support and omni-channel messaging platform. Chatwoot exposes a REST API; this schema models the same domain surface in Graph
  name: Chatwoot GraphQL Schema
  slug: chatwoot-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chatwoot.png
json_schemas:
- name: Account
  property_count: 3
  slug: account
- name: Agent
  property_count: 11
  slug: agent
- name: Article
  property_count: 14
  slug: article
- name: Automation Rule
  property_count: 1
  slug: automation_rule
- name: Canned Response
  property_count: 6
  slug: canned_response
- name: Category
  property_count: 10
  slug: category
- name: Contact
  property_count: 1
  slug: contact
- name: Conversation
  property_count: 27
  slug: conversation
- name: Custom Attribute
  property_count: 12
  slug: custom_attribute
- name: Inbox
  property_count: 33
  slug: inbox
- name: Label
  property_count: 5
  slug: label
- name: Message
  property_count: 22
  slug: message
- name: Portal
  property_count: 1
  slug: portal
- name: Team
  property_count: 6
  slug: team
- name: User
  property_count: 20
  slug: user
- name: Webhook
  property_count: 6
  slug: webhook
jsonld:
- class_count: 2
  name: Chatwoot Context
  property_count: 47
  slug: chatwoot-context
layout: provider
modified: '2026-06-13'
name: Chatwoot
nav: Providers
network: true
overview: 'Chatwoot publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Platform API, Account AgentBots API, Account API, and 29 more. Tagged areas include Customer Support, Messaging, Live Chat, Omni-channel, and Conversations.


  The Chatwoot catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chatwoot''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Chatwoot Plans Pricing
  plan_count: 4
  slug: chatwoot-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Chatwoot Rate Limits
  slug: chatwoot-rate-limits
rules:
- name: Chatwoot API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: chatwoot-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.8
  delta: -8.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/chatwoot/refs/heads/main/screenshots/chatwoot-2026-06-20T174237.png
security:
- kind: authentication
  name: Chatwoot Authentication
  slug: chatwoot-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chatwoot Domain Security
  slug: chatwoot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chatwoot
tags:
- Customer Support
- Messaging
- Live Chat
- Omni-channel
- Conversations
- Contacts
- Agents
- Open Source
website: https://www.chatwoot.com/
---
