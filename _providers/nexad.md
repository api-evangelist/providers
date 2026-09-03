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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 132
  human_in_the_loop: 124
  name: Nexad Agentic Access
  operation_count: 281
  slug: nexad-agentic-access
  summary_line: 281 operations · 132 acting · 124 human-in-the-loop
api_count: 2
apis:
- description: Java/Kotlin Android SDK for monetizing apps with native, WebView, chat-message, and modal-overlay ad formats — including contextual ads for AI-chat interfaces. Installed via com.nexad:sdk and initiali
  name: Nexad Android Ads SDK
  slug: nexad-android-ads-sdk
- description: 'The Soku AI platform API (identifies as "NexStudio API"). Powers an autonomous marketing agent across ads, analytics (GA4, GSC, PostHog), SEO hosting, and review-gated writes. Authenticated via OAuth '
  name: Soku (NexStudio) API
  slug: soku-nexstudio-api
artifact_total: 10
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/About-Intelligence/soku-cli/blob/main/LICENSE
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
  url: llms/nexad-soku-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nexad-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexad-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/About-Intelligence/soku-cli/blob/main/SECURITY.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nexad-vulnerability-disclosure.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/About-Intelligence
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/About-Intelligence/soku-cli
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nexad-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nexad-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nexad-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nexad-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nexad-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nexad-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nexad-rate-limits.yml
- group: other
  title: ''
  type: Capabilities
  url: cli/nexad-capabilities.json
created: '2026-07-17'
description: 'Nexad (About Intelligence, Inc.) is an AI-native advertising company backed by Andreessen Horowitz, Point72 and Prosus. It ships the Nexad Android Ads SDK — a Java/Kotlin library for embedding contextual, native, WebView, chat-message, and modal-overlay ads directly into mobile and AI-chat applications — and operates Soku AI, an autonomous marketing agent (the NexStudio API at api.soku.ai) that runs and optimizes ad campaigns across Google, Meta, TikTok, and ChatGPT Ads on a 24/7 perceive–decide–act loop with human-in-the-loop approvals. Developers integrate via the Android SDK, the Soku CLI (@soku-ai/cli) for shell-based AI agents such as Claude Code, Codex, and Cursor, an authenticated MCP endpoint at api.soku.ai/mcp, and an open-source marketing skills hub. Nexad publishes no OpenAPI, but it does ship an unusually complete machine-readable substitute: a 281-action capability registry (18 namespaces) in its public MIT-licensed soku-cli repository, where every action declares
  typed inputs, an output shape, a read/write/risk mode and a requires_review flag — 124 of the 281 actions are human-approval-gated at runtime.'
image: https://docs.nex.ad/img/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Nexad MCP Server
  slug: nexad-mcp-server
modified: '2026-08-13'
name: Nexad
nav: Providers
network: true
overview: 'Nexad publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Advertising, Marketing, and Marketing Automation.


  Nexad''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Nexad Plans Pricing
  plan_count: 4
  slug: nexad-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Nexad Rate Limits
  slug: nexad-rate-limits
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 20
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- kind: vulnerability-disclosure
  name: Nexad Vulnerability Disclosure
  slug: nexad-vulnerability-disclosure
  summary_line: Hackerone · contact published
skill_count: 1
skills:
- name: soku
  slug: soku
slug: nexad
tags:
- Company
- Artificial Intelligence
- Advertising
- Marketing
- Marketing Automation
- Contextual Advertising
- Mobile SDK
- Agents
website: https://nex.ad
---
