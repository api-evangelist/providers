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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-04'
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
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/klaus-ai-mcp.yml
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


  Klaus AI''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, CLI, and 17 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 35.7
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
- Integration
- Webhook
- Command Line
- Messaging
- Y Combinator
website: https://klausai.com/
---
