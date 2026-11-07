---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Freshchat Agentic Access
  operation_count: 31
  slug: freshchat-agentic-access
  summary_line: 31 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The Accounts API from Freshchat — 1 operation(s) for accounts.
  name: Freshchat Accounts API
  slug: freshchat-accounts-api
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The Agents API from Freshchat — 3 operation(s) for agents.
  name: Freshchat Agents API
  slug: freshchat-agents-api
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The Channels API from Freshchat — 1 operation(s) for channels.
  name: Freshchat Channels API
  slug: freshchat-channels-api
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The Conversations API from Freshchat — 3 operation(s) for conversations.
  name: Freshchat Conversations API
  slug: freshchat-conversations-api
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The CSAT API from Freshchat — 1 operation(s) for csat.
  name: Freshchat CSAT API
  slug: freshchat-csat-api
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The Files API from Freshchat — 2 operation(s) for files.
  name: Freshchat Files API
  slug: freshchat-files-api
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The Groups API from Freshchat — 1 operation(s) for groups.
  name: Freshchat Groups API
  slug: freshchat-groups-api
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The Messages API from Freshchat — 1 operation(s) for messages.
  name: Freshchat Messages API
  slug: freshchat-messages-api
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The Metrics API from Freshchat — 2 operation(s) for metrics.
  name: Freshchat Metrics API
  slug: freshchat-metrics-api
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The OutboundMessages API from Freshchat — 2 operation(s) for outboundmessages.
  name: Freshchat OutboundMessages API
  slug: freshchat-outboundmessages-api
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The Roles API from Freshchat — 1 operation(s) for roles.
  name: Freshchat Roles API
  slug: freshchat-roles-api
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The Users API from Freshchat — 4 operation(s) for users.
  name: Freshchat Users API
  slug: freshchat-users-api
- baseURL: https://api.freshchat.com/v2
  baseurl_source: declared
  description: The Business Hours API from Freshchat — 1 operation(s) for business hours.
  name: Freshchat Business Hours API
  slug: freshchat-business-hours-api
artifact_total: 34
collections:
- collection_type: open
  name: Freshchat REST Accounts API
  slug: open-freshchat-accounts-api
- collection_type: open
  name: Freshchat REST Accounts Agents API
  slug: open-freshchat-agents-api
- collection_type: open
  name: Freshchat Webhooks
  slug: open-freshchat-asyncapi
- collection_type: open
  name: Freshchat REST Accounts BusinessHours API
  slug: open-freshchat-businesshours-api
- collection_type: open
  name: Freshchat REST Accounts Channels API
  slug: open-freshchat-channels-api
- collection_type: open
  name: Freshchat REST Accounts Conversations API
  slug: open-freshchat-conversations-api
- collection_type: open
  name: Freshchat REST Accounts CSAT API
  slug: open-freshchat-csat-api
- collection_type: open
  name: Freshchat REST Accounts Files API
  slug: open-freshchat-files-api
- collection_type: open
  name: Freshchat REST Accounts Groups API
  slug: open-freshchat-groups-api
- collection_type: open
  name: Freshchat REST Accounts Messages API
  slug: open-freshchat-messages-api
- collection_type: open
  name: Freshchat REST Accounts Metrics API
  slug: open-freshchat-metrics-api
- collection_type: open
  name: Freshchat REST Accounts OutboundMessages API
  slug: open-freshchat-outboundmessages-api
- collection_type: open
  name: Freshchat REST Accounts Roles API
  slug: open-freshchat-roles-api
- collection_type: open
  name: Freshchat REST Accounts Users API
  slug: open-freshchat-users-api
- collection_type: open
  name: Freshchat REST API
  slug: open-freshchat
common:
- group: other
  href: https://artifacts.apis.io/freshchat/capabilities/freshchat-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/freshchat-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/freshchat/agentic-access/freshchat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/freshchat-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/freshchat/security/freshchat-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/freshchat-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/freshchat/security/freshchat-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/freshchat-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/freshchat/security/freshchat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/freshchat-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/freshchat/authentication/freshchat-authentication.yml
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
overview: 'Freshchat publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Agents API, Channels API, and 10 more. Tagged areas include Customer Messaging, Live Chat, Customer Service, Conversational Engagement, and Omnichannel Messaging.


  The Freshchat catalog on APIs.io includes 1 Spectral governance ruleset.


  Freshchat''s developer surface includes authentication, documentation, pricing, signup flow, support, and 10 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Freshchat API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: freshchat-rules
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 48.8
    developer_ergonomics: 35.7
    discoverability: 73.2
    operational_transparency: 21.1
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/freshchat/freshchat-2026-06-20T181539.png
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
- Customer Service
- Conversational Engagement
- Omnichannel Messaging
- Chatbots
- Freshworks
website: https://www.freshworks.com/live-chat-software/
---
