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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Microsoft Bot Framework Agentic Access
  operation_count: 15
  slug: microsoft-bot-framework-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 6
apis:
- description: Custom applications communicate directly with bots through REST and WebSocket connections.
  name: Direct Line API
  slug: direct-line
- description: Libraries for building conversational AI bots in C#, JavaScript, Python, and Java.
  name: Bot Builder SDK
  slug: bot-builder-sdk
- description: The Activities API from Microsoft Bot Framework — 3 operation(s) for activities.
  name: Microsoft Bot Framework Activities API
  slug: microsoft-bot-framework-activities-api
- description: The Attachments API from Microsoft Bot Framework — 3 operation(s) for attachments.
  name: Microsoft Bot Framework Attachments API
  slug: microsoft-bot-framework-attachments-api
- description: The Conversations API from Microsoft Bot Framework — 1 operation(s) for conversations.
  name: Microsoft Bot Framework Conversations API
  slug: microsoft-bot-framework-conversations-api
- description: The Members API from Microsoft Bot Framework — 4 operation(s) for members.
  name: Microsoft Bot Framework Members API
  slug: microsoft-bot-framework-members-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Bot Framework Connector REST Activities API
  slug: open-microsoft-bot-framework-activities-api
- collection_type: open
  name: Microsoft Bot Framework Connector REST Activities Attachments API
  slug: open-microsoft-bot-framework-attachments-api
- collection_type: open
  name: Microsoft Bot Framework Connector REST Activities Conversations API
  slug: open-microsoft-bot-framework-conversations-api
- collection_type: open
  name: Microsoft Bot Framework Connector REST Activities Members API
  slug: open-microsoft-bot-framework-members-api
- collection_type: open
  name: Microsoft Bot Framework Connector REST API
  slug: open-microsoft-bot-framework
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-bot-framework-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-bot-framework-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-bot-framework-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://dev.botframework.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/botframework-sdk
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/bot-services/
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
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/microsoft/ignite25-LAB513-build-a2a-and-mcp-systems-using-swe-agents-and-agent-framework
- group: agent
  title: ''
  type: LlmsText
  url: https://dev.botframework.com/llms.txt
created: '2026-03-13'
description: Microsoft Bot Framework provides APIs and SDKs for building conversational AI bots that work across multiple channels including Teams, Slack, and custom applications.
finops:
- name: Microsoft Bot Framework Finops
  service_category: API
  slug: microsoft-bot-framework-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-bot-framework.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Microsoft Bot Framework
nav: Providers
network: true
overview: 'Microsoft Bot Framework publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Attachments API, Conversations API, and 1 more. Tagged areas include Bots, Conversational AI, Messaging, Bot Framework, and Direct Line.


  Microsoft Bot Framework''s developer surface includes authentication, developer portal, pricing, support, and 7 more developer resources.'
plans:
- name: Microsoft Bot Framework Plans Pricing
  plan_count: 3
  slug: microsoft-bot-framework-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Microsoft Bot Framework Rate Limits
  slug: microsoft-bot-framework-rate-limits
score:
  band: thin
  composite: 35.4
  delta: 1.9
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 35.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-bot-framework/refs/heads/main/screenshots/microsoft-bot-framework-2026-06-20T185445.png
security:
- kind: authentication
  name: Microsoft Bot Framework Authentication
  slug: microsoft-bot-framework-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Bot Framework Domain Security
  slug: microsoft-bot-framework-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-bot-framework
tags:
- Bots
- Conversational AI
- Messaging
- Bot Framework
- Direct Line
website: https://dev.botframework.com/
---
