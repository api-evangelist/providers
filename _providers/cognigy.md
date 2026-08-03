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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The Cognigy.AI REST API for managing AI Agents throughout their lifecycle — deployment and snapshots, flow configuration and interaction, endpoints, resource monitoring, administration and user manage
  name: Cognigy.AI API
  slug: cognigyai-api
artifact_total: 5
asyncapis:
- description: ''
  name: Cognigy Webhooks
  slug: cognigy-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cognigy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cognigy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cognigy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cognigy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cognigy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cognigy.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cognigy.com/ai/for-developers/developers/api-and-cli/
- group: operate
  title: ''
  type: Support
  url: https://support.cognigy.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.cognigy.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cognigy
- group: start
  title: ''
  type: SignUp
  url: https://www.cognigy.com/get-demo
- group: start
  title: ''
  type: Login
  url: https://app.cognigy.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cognigy.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cognigy.com/release-notes/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cognigy.com/
- group: build
  title: ''
  type: Packages
  url: packages/cognigy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cognigy-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cognigy-cli.yml
- group: design
  title: ''
  type: Components
  url: components/cognigy-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cognigy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cognigy-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cognigy-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cognigy-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cognigy-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cognigy-sandbox.yml
created: '2026-07-17'
description: Cognigy (now NiCE Cognigy, following NICE's 2024 acquisition) is an enterprise conversational and agentic AI platform for building, deploying, and operating AI Agents across voice, chat, and messaging channels. Cognigy.AI lets teams design conversational flows, connect large language models and knowledge bases, orchestrate omnichannel customer service automation, and augment human contact center agents with real-time Agent Copilot assistance. The platform exposes a comprehensive REST API (the Cognigy.AI API) for managing agents, snapshots, flows, endpoints, users, and organizations, an OData analytics endpoint, webhook and REST endpoints for real-time interactions, a Socket client for webchat, an embeddable Webchat widget, and a first-party command-line interface for managing local copies of virtual agent projects.
image: https://www.cognigy.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Cognigy
nav: Providers
network: true
overview: 'Cognigy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Conversational AI, Agentic AI, Contact Center, and Customer Service Automation.


  The Cognigy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cognigy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 18 more developer resources.'
random_paper: 87
score:
  band: developing
  composite: 49.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.6
    developer_ergonomics: 71.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 49.1
  provenance:
    conformance: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cognigy/refs/heads/main/screenshots/cognigy-2026-07-25T210022.png
security:
- kind: authentication
  name: Cognigy Authentication
  slug: cognigy-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Cognigy Domain Security
  slug: cognigy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cognigy Trust Center
  slug: cognigy-trust-center
  summary_line: SOC 2, ISO 27001
slug: cognigy
tags:
- Company
- Conversational AI
- Agentic AI
- Contact Center
- Customer Service Automation
- Chatbots
- Voice AI
- Virtual Agents
- Enterprise AI
- Omnichannel
website: https://www.cognigy.com/
---
