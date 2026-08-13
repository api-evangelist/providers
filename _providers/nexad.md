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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: Java/Kotlin Android SDK for monetizing apps with native, WebView, chat-message, and modal-overlay ad formats — including contextual ads for AI-chat interfaces. Installed via com.nexad:sdk and initiali
  name: Nexad Android Ads SDK
  slug: nexad-android-ads-sdk
- description: 'The Soku AI platform API (identifies as "NexStudio API"). Powers an autonomous marketing agent across ads, analytics (GA4, GSC, PostHog), SEO hosting, and review-gated writes. Authenticated via OAuth '
  name: Soku (NexStudio) API
  slug: soku-nexstudio-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://nex.ad
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nex.ad
- group: docs
  title: ''
  type: Documentation
  url: https://soku.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nex.ad/docs/android/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nex.ad/docs/android/getting-started
- group: company
  title: ''
  type: Blog
  url: https://soku.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://soku.ai/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://soku.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://soku.ai/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://soku.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://soku.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://join.slack.com/t/soku-talk/shared_invite/zt-3s9i1a4w7-AWlkU3GAiar3wJM4ToYLEg
- group: build
  title: ''
  type: Packages
  url: packages/nexad-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nexad-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nexad-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nexad-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nexad-authentication.yml
- group: design
  title: ''
  type: Components
  url: components/nexad-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nexad-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nexad-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nexad-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexad-domain-security.yml
created: '2026-07-17'
description: Nexad (About Intelligence, Inc.) is an AI-native advertising company backed by Prosus Ventures. It ships the Nexad Android Ads SDK — a Java/Kotlin library for embedding contextual, native, WebView, chat-message, and modal-overlay ads directly into mobile and AI-chat applications — and operates Soku AI, an autonomous marketing agent (the NexStudio API at api.soku.ai) that runs and optimizes ad campaigns across Google, Meta, TikTok, and ChatGPT Ads on a 24/7 perceive–decide–act loop with human-in-the-loop approvals. Developers integrate via the Android SDK, the Soku CLI (@soku-ai/cli) for shell-based AI agents such as Claude Code, Codex, and Cursor, an authenticated MCP endpoint, and a hub of 100+ open-source marketing skills.
image: https://docs.nex.ad/img/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: nexad-mcp.yml
  slug: nexad-mcpyml
modified: '2026-07-20'
name: Nexad
nav: Providers
network: true
overview: 'Nexad publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Advertising, Marketing, and Marketing Automation.


  Nexad''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, pricing, signup flow, and 16 more developer resources.'
random_paper: 48
score:
  band: thin
  composite: 33.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 33.7
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nexad/refs/heads/main/screenshots/nexad-2026-08-07T185142.png
security:
- kind: authentication
  name: Nexad Authentication
  slug: nexad-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Nexad Domain Security
  slug: nexad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nexad
tags:
- Company
- Artificial Intelligence
- Advertising
- Marketing
- Marketing Automation
- Contextual Advertising
- Mobile SDK
- Agent
website: https://nex.ad
---
