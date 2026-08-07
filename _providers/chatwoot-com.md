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
- acting_count: 45
  human_in_the_loop: 0
  name: Chatwoot Com Agentic Access
  operation_count: 74
  slug: chatwoot-com-agentic-access
  summary_line: 74 operations · 45 acting
api_count: 17
apis:
- description: Application API - manage account agents.
  name: Chatwoot Agents API
  slug: chatwoot-com-agents-api
- description: Application API - manage automation rules.
  name: Chatwoot Automation Rules API
  slug: chatwoot-com-automation-rules-api
- description: Application API - manage saved reply templates.
  name: Chatwoot Canned Responses API
  slug: chatwoot-com-canned-responses-api
- description: Client API - end-user contact management.
  name: Chatwoot Client Contacts API
  slug: chatwoot-com-client-contacts-api
- description: Client API - end-user conversation management.
  name: Chatwoot Client Conversations API
  slug: chatwoot-com-client-conversations-api
- description: Client API - end-user message management.
  name: Chatwoot Client Messages API
  slug: chatwoot-com-client-messages-api
- description: Application API - manage contacts.
  name: Chatwoot Contacts API
  slug: chatwoot-com-contacts-api
- description: Application API - manage conversations.
  name: Chatwoot Conversations API
  slug: chatwoot-com-conversations-api
- description: Application API - manage custom attribute definitions.
  name: Chatwoot Custom Attributes API
  slug: chatwoot-com-custom-attributes-api
- description: Application API - manage channels/inboxes.
  name: Chatwoot Inboxes API
  slug: chatwoot-com-inboxes-api
- description: Application API - manage labels.
  name: Chatwoot Labels API
  slug: chatwoot-com-labels-api
- description: Application API - manage conversation messages.
  name: Chatwoot Messages API
  slug: chatwoot-com-messages-api
- description: Platform API - super-admin account management.
  name: Chatwoot Platform Accounts API
  slug: chatwoot-com-platform-accounts-api
- description: Platform API - super-admin agent bot management.
  name: Chatwoot Platform Agent Bots API
  slug: chatwoot-com-platform-agent-bots-api
- description: Platform API - super-admin user management.
  name: Chatwoot Platform Users API
  slug: chatwoot-com-platform-users-api
- description: Application API - retrieve analytics and reports.
  name: Chatwoot Reports API
  slug: chatwoot-com-reports-api
- description: Application API - manage teams and membership.
  name: Chatwoot Teams API
  slug: chatwoot-com-teams-api
artifact_total: 24
collections:
- collection_type: open
  name: Chatwoot API
  slug: open-chatwoot-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chatwoot-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chatwoot-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chatwoot-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chatwoot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chatwoot
- group: company
  title: ''
  type: Website
  url: https://www.chatwoot.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.chatwoot.com
- group: commercial
  title: ''
  type: Plans
  url: plans/chatwoot-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chatwoot-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chatwoot-com-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.chatwoot.com/blog
created: '2026-07-01'
description: Chatwoot is an open-source customer engagement and support suite that unifies email, live-chat, social, and messaging channels into a single shared inbox. Agents, teams, contacts, conversations, and messages are all managed through a REST API surface split across an Application API, a Client API for end-user widgets, and a Platform API for super-admin installation control. Chatwoot is available as self-hostable open-source software and as Chatwoot Cloud.
finops:
- name: Chatwoot Com Finops
  service_category: Business Applications
  slug: chatwoot-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chatwoot-com.png
layout: provider
modified: '2026-07-01'
name: Chatwoot
nav: Providers
network: true
overview: 'Chatwoot publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Automation Rules API, Canned Responses API, and 14 more. Tagged areas include Customer Support, Customer Engagement, Shared Inbox, Live Chat, and Open Source.


  Chatwoot''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Chatwoot Com Plans Pricing
  plan_count: 5
  slug: chatwoot-com-plans-pricing
random_paper: 107
rate_limits:
- limit_count: 3
  name: Chatwoot Com Rate Limits
  slug: chatwoot-com-rate-limits
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.8
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chatwoot-com/refs/heads/main/screenshots/chatwoot-com-2026-07-25T205121.png
security:
- kind: authentication
  name: Chatwoot Com Authentication
  slug: chatwoot-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chatwoot Com Domain Security
  slug: chatwoot-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chatwoot-com
tags:
- Customer Support
- Customer Engagement
- Shared Inbox
- Live Chat
- Open Source
- Omnichannel
- Help Desk
website: https://www.chatwoot.com
---
