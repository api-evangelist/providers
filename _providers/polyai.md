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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Build, run and observe PolyAI voice and chat agents from your own systems. Three REST API families (Agents, Conversations, Webhooks & Alerts) plus Chat, SMS, Outbound Calling, Handoff, DNI, External E
  name: PolyAI Platform API
  slug: polyai-platform-api
artifact_total: 4
asyncapis:
- description: ''
  name: Polyai Webhooks
  slug: polyai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.polyai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.poly.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.poly.ai/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.poly.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.poly.ai/api-reference/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PolyAI-LDN
- group: auth
  title: ''
  type: Compliance
  url: https://docs.poly.ai/legal/compliance
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/polyai-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/polyai-error-codes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/polyai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/polyai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/polyai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/polyai-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/polyai-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/polyai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/polyai-cli.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/polyai-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polyai-domain-security.yml
created: '2026-07-17'
description: PolyAI builds enterprise-grade voice and chat AI agents that handle real customer service conversations across 24+ languages, with 99.994% production uptime. The PolyAI Platform exposes three REST API families — an Agents API to create, branch, configure and deploy agents through environments; a Conversations API to retrieve transcripts, audio, metrics and session data; and a Webhooks & Alerts surface for real-time event notifications — plus Chat, SMS, Outbound Calling, Handoff, DNI, External Events, Messaging (WebSocket) and a WebRTC Gateway. Authentication is header-based (x-api-key) with region-scoped keys, and a Python Agent Development Kit (ADK) offers a Git-like local build-pull-push workflow. Backed by Khosla Ventures and profiled in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/polyai.png
layout: provider
modified: '2026-07-20'
name: Polyai
nav: Providers
network: true
overview: 'Polyai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Conversational AI, Voice AI, Customer Service, and Contact Center.


  The Polyai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Polyai''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, and 13 more developer resources.'
random_paper: 74
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 37.9
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Polyai Authentication
  slug: polyai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Polyai Domain Security
  slug: polyai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: polyai
tags:
- Company
- Conversational AI
- Voice AI
- Customer Service
- Contact Center
- Agents
- Speech Recognition
- Text to Speech
- Webhooks
- Enterprise
website: https://www.polyai.com/
---
