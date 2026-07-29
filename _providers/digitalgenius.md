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
api_count: 1
apis:
- description: HTTP API and flow-execution surface for DigitalGenius AI agents, including generic DG API calls, flow execution, JSON handling, and the hosted MCP server. Region-scoped EU/US hosts, HTTP Basic (encode
  name: DigitalGenius API
  slug: digitalgenius-api
artifact_total: 6
asyncapis:
- description: ''
  name: Digitalgenius Webhooks
  slug: digitalgenius-webhooks
common:
- group: company
  title: ''
  type: Website
  url: http://www.digitalgenius.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.digitalgenius.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.digitalgenius.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.digitalgenius.com/docs/generic-digitalgenius-api-call
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.digitalgenius.com/docs/create-basic-token
- group: operate
  title: ''
  type: Support
  url: https://docs.digitalgenius.com/docs/create-a-ticket-on-support-portal.md
- group: operate
  title: ''
  type: StatusPage
  url: https://status.digitalgenius.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digitalgenius.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digitalgenius.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.digitalgenius.com/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DigitalGenius
- group: agent
  title: ''
  type: MCPServer
  url: mcp/digitalgenius-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/digitalgenius-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/digitalgenius-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/digitalgenius-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/digitalgenius-packages.yml
- group: design
  title: ''
  type: Components
  url: components/digitalgenius-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/digitalgenius-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/digitalgenius-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/digitalgenius-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digitalgenius-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/digitalgenius-trust-center.yml
created: '2026-07-17'
description: DigitalGenius is an AI agent platform purpose-built for ecommerce and retail customer service. It automates pre- and post-purchase support, fully resolving customer issues such as order tracking, returns and exchanges, subscription management, and warranty claims by orchestrating "flows" that deeply integrate with a brand's existing systems (helpdesks like Zendesk, Freshchat, Freshdesk, Kustomer, Gorgias and Salesforce Service Cloud, plus dozens of carriers, WMS/OMS and logistics providers). Developers connect via a documented HTTP API, an embeddable Genius Chat headless SDK (web, iOS, Android, Expo), and an official hosted Model Context Protocol (MCP) server, with region-scoped EU and US hosts and Auth0-backed platform authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digitalgenius.png
layout: provider
mcp_servers:
- description: ''
  name: digitalgenius-mcp.yml
  slug: digitalgenius-mcpyml
modified: '2026-07-18'
name: DigitalGenius
nav: Providers
network: true
overview: 'DigitalGenius publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Service, Ecommerce, Artificial Intelligence, and AI Agents.


  The DigitalGenius catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DigitalGenius'' developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 76
score:
  band: developing
  composite: 45.7
  delta: 5.6
  facets:
    commercial_clarity: 42.1
    contract_quality: 51.6
    developer_ergonomics: 65.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 40.1
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/digitalgenius/refs/heads/main/screenshots/digitalgenius-2026-07-25T212022.png
security:
- kind: authentication
  name: Digitalgenius Authentication
  slug: digitalgenius-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Digitalgenius Domain Security
  slug: digitalgenius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Digitalgenius Trust Center
  slug: digitalgenius-trust-center
  summary_line: trust center published
slug: digitalgenius
tags:
- Company
- Customer Service
- Ecommerce
- Artificial Intelligence
- AI Agents
- Conversational AI
- Customer Support Automation
- Retail
- MCP
website: http://www.digitalgenius.com/
---
