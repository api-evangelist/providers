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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Microsoft Power Virtual Agents Agentic Access
  operation_count: 6
  slug: microsoft-power-virtual-agents-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 4
apis:
- description: The Copilot Studio Direct Line API enables custom applications to communicate with bots built in Microsoft Copilot Studio (formerly Power Virtual Agents). It provides REST endpoints for starting conve
  name: Copilot Studio Direct Line API
  slug: direct-line-api
- description: The Copilot Studio management capabilities enable programmatic configuration and deployment of conversational AI agents. Developers can manage topics, entities, authentication settings, and channel co
  name: Copilot Studio Bot Management API
  slug: bot-management-api
- description: The Conversations API from Microsoft Power Virtual Agents — 3 operation(s) for conversations.
  name: Microsoft Power Virtual Agents Conversations API
  slug: microsoft-power-virtual-agents-conversations-api
- description: The Tokens API from Microsoft Power Virtual Agents — 2 operation(s) for tokens.
  name: Microsoft Power Virtual Agents Tokens API
  slug: microsoft-power-virtual-agents-tokens-api
artifact_total: 12
collections:
- collection_type: open
  name: Microsoft Copilot Studio Direct Line API
  slug: open-microsoft-power-virtual-agents
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-power-virtual-agents-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-power-virtual-agents-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-power-virtual-agents-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-power-virtual-agents-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://copilotstudio.microsoft.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: Community
  url: https://community.powerplatform.com/forums/thread/?threadid=7de87c01-da4e-ef11-9f89-7c1e52206d8b
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=copilot-studio-blog
created: '2024-01-01'
description: Microsoft Power Virtual Agents (now Copilot Studio) enables building AI-powered conversational chatbots without coding. It provides APIs for integrating bots with custom applications and managing bot configurations programmatically.
finops:
- name: Microsoft Power Virtual Agents Finops
  service_category: API
  slug: microsoft-power-virtual-agents-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-power-virtual-agents.png
layout: provider
modified: '2026-04-28'
name: Microsoft Power Virtual Agents
nav: Providers
network: true
overview: 'Microsoft Power Virtual Agents publishes 2 APIs on the [APIs.io](https://apis.io/) network: Conversations API and Tokens API. Tagged areas include Chatbots, Conversational AI, Copilot Studio, and Microsoft.


  Microsoft Power Virtual Agents'' developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, and 8 more developer resources.'
plans:
- name: Microsoft Power Virtual Agents Plans Pricing
  plan_count: 3
  slug: microsoft-power-virtual-agents-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 5
  name: Microsoft Power Virtual Agents Rate Limits
  slug: microsoft-power-virtual-agents-rate-limits
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 54.3
    developer_ergonomics: 45.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-power-virtual-agents/refs/heads/main/screenshots/microsoft-power-virtual-agents-2026-06-20T185526.png
security:
- kind: authentication
  name: Microsoft Power Virtual Agents Authentication
  slug: microsoft-power-virtual-agents-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Power Virtual Agents Domain Security
  slug: microsoft-power-virtual-agents-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Power Virtual Agents Vulnerability Disclosure
  slug: microsoft-power-virtual-agents-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-power-virtual-agents
tags:
- Chatbots
- Conversational AI
- Copilot Studio
- Microsoft
website: https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
---
