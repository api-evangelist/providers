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
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Dapta Webhooks
  slug: dapta-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://dapta.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dapta.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dapta.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dapta.ai/fundamentals/how-to-create-an-account-in-dapta
- group: company
  title: ''
  type: Blog
  url: https://dapta.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://dapta.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://auth.dapta.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.dapta.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dapta.ai/dapta-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dapta.ai/dapta-privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://dapta.ai/contact-us-2/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dapta.ai
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dapta-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dapta-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dapta-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dapta-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dapta-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dapta-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dapta-domain-security.yml
created: '2026-07-17'
description: Dapta is a no-code AI voice and text agent platform for small and medium businesses, letting teams build AI phone agents, SMS and WhatsApp bots, meeting notetakers, and workflow automations in minutes without writing code. Voice agents answer inbound and place outbound calls in 20+ languages, qualify leads, book appointments, and handle support 24/7; text agents automate SMS and WhatsApp conversations; Flow Studio wires no-code automations across 1000+ tools with CRM connectors for HubSpot, Salesforce, and GoHighLevel. Dapta exposes a hosted, workspace-scoped Model Context Protocol (MCP) server at mcp.dapta.ai so AI clients such as Claude and Codex can drive a workspace, plus an outbound webhook surface for call, meeting, flow, and campaign events. The company is backed by 500 Global and says it serves 50,000+ businesses.
image: https://dapta.ai/wp-content/uploads/2025/02/og-tag.jpg
layout: provider
mcp_servers:
- description: ''
  name: Dapta MCP Server
  slug: dapta-mcp-server
modified: '2026-07-18'
name: Dapta
nav: Providers
network: true
overview: 'Dapta is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Voice AI, Conversational AI, and Automation.


  The Dapta catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dapta''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, authentication, and 12 more developer resources.'
random_paper: 42
score:
  band: thin
  composite: 41.5
  delta: 6.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 54.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.3
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/dapta/refs/heads/main/screenshots/dapta-2026-07-25T211214.png
security:
- kind: authentication
  name: Dapta Authentication
  slug: dapta-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dapta Domain Security
  slug: dapta-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dapta
tags:
- Company
- AI Agents
- Voice AI
- Conversational AI
- Automation
- No-Code
- Model Context Protocol
- Webhooks
- CRM
- SMB
website: https://dapta.ai
---
