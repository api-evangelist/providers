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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Line Agentic Access
  operation_count: 8
  slug: line-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 4
apis:
- description: The Channel API from LINE — 1 operation(s) for channel.
  name: LINE Channel API
  slug: line-channel-api
- description: The Info API from LINE — 1 operation(s) for info.
  name: LINE Info API
  slug: line-info-api
- description: The Message API from LINE — 4 operation(s) for message.
  name: LINE Message API
  slug: line-message-api
- description: The Profile API from LINE — 1 operation(s) for profile.
  name: LINE Profile API
  slug: line-profile-api
artifact_total: 12
asyncapis:
- description: 'AsyncAPI description of the webhook event surface published by the LINE Messaging API to bot servers. The Messaging API delivers webhook events as HTTPS POST requests to the configured webhook URL of '
  name: LINE Messaging Webhook Event Surface
  slug: line-messaging-webhook
collections:
- collection_type: open
  name: LINE Messaging API
  slug: open-line
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/line-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/line-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/line-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/line-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/linecorp
- group: company
  title: ''
  type: Website
  url: https://line.me
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.line.biz/en/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.line.biz/en/docs/
- group: docs
  title: ''
  type: OpenAPI Repository
  url: https://github.com/line/line-openapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/line
- group: start
  title: ''
  type: Signup
  url: https://developers.line.biz/console/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.linebiz.com/jp-en/service/line-account-connect/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/line/line-bot-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.line.biz/llms.txt
created: '2026-05-11'
description: LINE is a Japan-based messaging platform with over 200 million monthly active users across Japan, Taiwan, Thailand, and Indonesia, offering messaging, payments, news, and a broad ecosystem of services. The LINE Developers platform exposes public APIs for building chatbots, mini-apps, social login, and audience marketing, all documented as OpenAPI specifications. APIs use Bearer token authentication with channel access tokens issued per LINE channel.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/line.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-29'
name: LINE
nav: Providers
network: true
overview: 'LINE publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Channel API, Info API, Message API, and 1 more. Tagged areas include Messaging, Chatbots, Social Login, Mini Apps, and Marketing.


  The LINE catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  LINE''s developer surface includes authentication, documentation, signup flow, pricing, and 10 more developer resources.'
random_paper: 76
rules:
- name: LINE API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 2
  slug: line-asyncapi-spectral-rules
score:
  band: thin
  composite: 41.3
  delta: 4.8
  facets:
    commercial_clarity: 23.7
    contract_quality: 68.3
    developer_ergonomics: 37.0
    discoverability: 81.5
    governance: 27.1
    operational_transparency: 5.3
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/line/refs/heads/main/screenshots/line-2026-06-20T184539.png
security:
- kind: authentication
  name: Line Authentication
  slug: line-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Line Domain Security
  slug: line-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Line Vulnerability Disclosure
  slug: line-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: line
tags:
- Messaging
- Chatbots
- Social Login
- Mini Apps
- Marketing
- Japan
website: https://line.me
---
