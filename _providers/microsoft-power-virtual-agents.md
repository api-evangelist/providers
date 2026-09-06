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
- baseURL: https://directline.botframework.com/
  baseurl_source: declared
  description: The Conversations API from Microsoft Power Virtual Agents — 3 operation(s) for conversations.
  name: Microsoft Power Virtual Agents Conversations API
  slug: microsoft-power-virtual-agents-conversations-api
- baseURL: https://directline.botframework.com/
  baseurl_source: declared
  description: The Tokens API from Microsoft Power Virtual Agents — 2 operation(s) for tokens.
  name: Microsoft Power Virtual Agents Tokens API
  slug: microsoft-power-virtual-agents-tokens-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Copilot Studio Direct Line Conversations API
  slug: open-microsoft-power-virtual-agents-conversations-api
- collection_type: open
  name: Microsoft Copilot Studio Direct Line Conversations Tokens API
  slug: open-microsoft-power-virtual-agents-tokens-api
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
random_paper: 4
rate_limits:
- limit_count: 5
  name: Microsoft Power Virtual Agents Rate Limits
  slug: microsoft-power-virtual-agents-rate-limits
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 50.0
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
