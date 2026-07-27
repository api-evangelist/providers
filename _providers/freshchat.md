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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Freshchat Agentic Access
  operation_count: 31
  slug: freshchat-agentic-access
  summary_line: 31 operations · 14 acting
api_count: 13
apis:
- description: The Accounts API from Freshchat — 1 operation(s) for accounts.
  name: Freshchat Accounts API
  slug: freshchat-accounts-api
- description: The Agents API from Freshchat — 3 operation(s) for agents.
  name: Freshchat Agents API
  slug: freshchat-agents-api
- description: The BusinessHours API from Freshchat — 1 operation(s) for businesshours.
  name: Freshchat BusinessHours API
  slug: freshchat-businesshours-api
- description: The Channels API from Freshchat — 1 operation(s) for channels.
  name: Freshchat Channels API
  slug: freshchat-channels-api
- description: The Conversations API from Freshchat — 3 operation(s) for conversations.
  name: Freshchat Conversations API
  slug: freshchat-conversations-api
- description: The CSAT API from Freshchat — 1 operation(s) for csat.
  name: Freshchat CSAT API
  slug: freshchat-csat-api
- description: The Files API from Freshchat — 2 operation(s) for files.
  name: Freshchat Files API
  slug: freshchat-files-api
- description: The Groups API from Freshchat — 1 operation(s) for groups.
  name: Freshchat Groups API
  slug: freshchat-groups-api
- description: The Messages API from Freshchat — 1 operation(s) for messages.
  name: Freshchat Messages API
  slug: freshchat-messages-api
- description: The Metrics API from Freshchat — 2 operation(s) for metrics.
  name: Freshchat Metrics API
  slug: freshchat-metrics-api
- description: The OutboundMessages API from Freshchat — 2 operation(s) for outboundmessages.
  name: Freshchat OutboundMessages API
  slug: freshchat-outboundmessages-api
- description: The Roles API from Freshchat — 1 operation(s) for roles.
  name: Freshchat Roles API
  slug: freshchat-roles-api
- description: The Users API from Freshchat — 4 operation(s) for users.
  name: Freshchat Users API
  slug: freshchat-users-api
artifact_total: 20
collections:
- collection_type: open
  name: Freshchat Webhooks
  slug: open-freshchat-asyncapi
- collection_type: open
  name: Freshchat REST API
  slug: open-freshchat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freshchat-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/freshchat-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/freshchat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freshchat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freshchat-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freshworks
- group: company
  title: ''
  type: Website
  url: https://www.freshworks.com/live-chat-software/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.freshchat.com/api/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.freshchat.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.freshworks.com/live-chat-software/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.freshworks.com/live-chat-software/signup/
- group: operate
  title: ''
  type: Support
  url: https://support.freshchat.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freshworks-inc
- group: agent
  title: ''
  type: LlmsText
  url: https://api.freshchat.com/llms.txt
created: '2026-05-11'
description: Freshchat is Freshworks' modern messaging and customer engagement platform that enables sales and support teams to converse with customers across web, mobile, WhatsApp, Facebook Messenger, Instagram, Apple Business Chat, and email. The Freshchat REST API provides programmatic access to agents, users, conversations, messages, channels, bots, and reports for building custom integrations and workflow automations. Authentication uses Bearer API tokens generated from the Freshchat admin console.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freshchat.png
layout: provider
modified: '2026-05-30'
name: Freshchat
nav: Providers
network: true
overview: 'Freshchat publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Agents API, BusinessHours API, and 10 more. Tagged areas include Customer Messaging, Live Chat, Customer Support, Conversational Engagement, and Omnichannel Messaging.


  Freshchat''s developer surface includes authentication, documentation, pricing, signup flow, support, and 9 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 32.4
  delta: 3.3
  facets:
    commercial_clarity: 18.4
    contract_quality: 46.0
    developer_ergonomics: 32.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freshchat/refs/heads/main/screenshots/freshchat-2026-06-20T181539.png
security:
- kind: authentication
  name: Freshchat Authentication
  slug: freshchat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Freshchat Domain Security
  slug: freshchat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Freshchat Vulnerability Disclosure
  slug: freshchat-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Freshchat Trust Center
  slug: freshchat-trust-center
  summary_line: SOC 2, ISO 27001, CSA STAR
slug: freshchat
tags:
- Customer Messaging
- Live Chat
- Customer Support
- Conversational Engagement
- Omnichannel Messaging
- Chatbots
- Freshworks
website: https://www.freshworks.com/live-chat-software/
---
