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
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The Klaus platform API at api.klausai.com is a tRPC RPC surface used by the first-party @klausai/cli command-line client to manage OpenClaw instances, agents, integrations, models, and chat sessions, '
  name: Klaus Platform API
  slug: klaus-ai-platform-api
artifact_total: 4
asyncapis:
- description: ''
  name: Klaus Ai Webhooks
  slug: klaus-ai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://klausai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://klausai.com/faq/
- group: docs
  title: ''
  type: Documentation
  url: https://klausai.com/faq/
- group: start
  title: ''
  type: GettingStarted
  url: https://klausai.com/blog/how-to-set-up-openclaw-complete-getting-started-guide/
- group: operate
  title: ''
  type: Support
  url: https://klausai.com/support
- group: company
  title: ''
  type: Blog
  url: https://klausai.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://klausai.com/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://klausai.com/klaus/subscribe
- group: start
  title: ''
  type: SignUp
  url: https://klausai.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://klausai.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://klausai.com/privacy/
- group: build
  title: ''
  type: Packages
  url: packages/klaus-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/klaus-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/klaus-ai-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/klaus-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/klaus-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/klaus-ai-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/klaus-ai-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klaus-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/klaus-ai-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/klaus-ai-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klaus-ai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klaus-ai-llms.txt
created: '2026-07-17'
description: Klaus is a managed cloud hosting platform for OpenClaw AI agents, built by Usebits Inc (Y Combinator W26, San Francisco) and founded by Bailey Wickham and Robbie Thompson. Klaus provisions an isolated, pre-configured OpenClaw instance on dedicated AWS ARM compute in about five minutes, with messaging channels (Slack, Telegram, WhatsApp, iMessage, Discord), Google Workspace, browser automation via Chromium and a Chrome Browser Relay extension, AgentMail email, GitHub backup, Tailscale SSH, scheduled cron tasks, semantic memory backed by OpenRouter embeddings, and instance webhooks that let external services trigger the agent over authenticated HTTP. Model access is brokered through OpenRouter with bring-your-own-key and ChatGPT-subscription options. The platform is operated through the Klaus web dashboard and a first-party command-line client published to npm as @klausai/cli, which talks to a tRPC API at api.klausai.com and proxies an OpenAI-compatible chat-completions endpoint.
  Authentication is by API key or an OAuth 2.0 Device Authorization Grant (RFC 8628).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/klaus-ai.png
layout: provider
modified: '2026-07-19'
name: Klaus AI
nav: Providers
network: true
overview: 'Klaus AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, AI Agents, Agent Hosting, OpenClaw, and Personal Assistant.


  The Klaus AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Klaus AI''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, CLI, and 16 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 42.3
  delta: 5.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 7.9
  previous_composite: 36.6
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/klaus-ai/refs/heads/main/screenshots/klaus-ai-2026-07-25T223940.png
security:
- kind: authentication
  name: Klaus Ai Authentication
  slug: klaus-ai-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Klaus Ai Domain Security
  slug: klaus-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: klaus-ai
tags:
- Artificial Intelligence
- AI Agents
- Agent Hosting
- OpenClaw
- Personal Assistant
- Automation
- Managed Hosting
- Integrations
- Webhooks
- Command Line
- Messaging
- Y Combinator
website: https://klausai.com/
---
