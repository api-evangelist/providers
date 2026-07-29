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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Manychat Agentic Access
  operation_count: 35
  slug: manychat-agentic-access
  summary_line: 35 operations · 22 acting
api_count: 5
apis:
- description: REST API for managing subscribers, custom fields, tags, flows, and sending messages in ManyChat across Instagram, Messenger, WhatsApp, and SMS. Authentication uses an API Key generated from the page S
  name: ManyChat REST API
  slug: rest-api
- description: Page-level configuration, tags, custom fields, bot fields, flows
  name: ManyChat Page API
  slug: manychat-page-api
- description: White-label profile/template management
  name: ManyChat Profile API
  slug: manychat-profile-api
- description: Send content and flows to subscribers
  name: ManyChat Sending API
  slug: manychat-sending-api
- description: Lookup and manage subscribers
  name: ManyChat Subscriber API
  slug: manychat-subscriber-api
artifact_total: 10
collections:
- collection_type: open
  name: ManyChat API
  slug: open-manychat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/manychat-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/manychat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manychat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/manychat-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/manychat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/manychat
- group: company
  title: ''
  type: Website
  url: https://manychat.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.manychat.com/swagger
- group: commercial
  title: ''
  type: Pricing
  url: https://manychat.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://manychat.com/signup
- group: operate
  title: ''
  type: Help Center
  url: https://help.manychat.com
created: '2026-05-11'
description: ManyChat is a messenger marketing platform that enables businesses to build automated conversations and chat marketing flows across Instagram Direct Messages, Facebook Messenger, WhatsApp, TikTok, and SMS. It provides a visual flow builder, audience segmentation, broadcasts, and integrations with ecommerce and CRM tools to drive engagement, lead capture, and sales. The ManyChat API allows programmatic access to subscribers, custom fields, flows, and messaging using API key (Bearer token) authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/manychat.png
layout: provider
modified: '2026-05-11'
name: ManyChat
nav: Providers
network: true
overview: 'ManyChat publishes 5 APIs on the [APIs.io](https://apis.io/) network, including REST API, Page API, Profile API, and 2 more. Tagged areas include Chat Marketing, Messenger Marketing, Conversational Commerce, Marketing Automation, and Instagram.


  ManyChat''s developer surface includes authentication, documentation, pricing, signup flow, and 7 more developer resources.'
random_paper: 53
score:
  band: thin
  composite: 28.3
  delta: -2.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 53.4
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/manychat/refs/heads/main/screenshots/manychat-2026-06-20T184935.png
security:
- kind: authentication
  name: Manychat Authentication
  slug: manychat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Manychat Domain Security
  slug: manychat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Manychat Vulnerability Disclosure
  slug: manychat-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: manychat
tags:
- Chat Marketing
- Messenger Marketing
- Conversational Commerce
- Marketing Automation
- Instagram
- WhatsApp
- Facebook Messenger
website: https://manychat.com
---
