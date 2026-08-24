---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: The Kuaishou Open Platform (快手开放平台) exposes a JSON HTTP API for third-party applications, mini programs and merchant tools built on Kuaishou. Access is granted through a standard OAuth 2.0 authorizati
  name: Kuaishou Open Platform API
  slug: open-platform
- description: Kwai for Business is Kuaishou's international advertising and marketing platform for the Kwai app. Its developer portal at developers.kwai.com documents a marketing API served from the /rest/n/mapi pa
  name: Kwai for Business Marketing API
  slug: kwai-for-business
- description: Kling AI (可灵) is Kuaishou Technology's generative video and image platform, launched in June 2024 and, by the company's own account, responsible for over 600 million generated videos and 30,000+ enter
  name: Kling AI API
  slug: kling-ai
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kuaishou-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kuaishou.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.kuaishou.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kwai
- group: operate
  title: ''
  type: Support
  url: https://www.kuaishou.com/about/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.kuaishou.com/help/feedback
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kuaishou.com/about/policy?tab=protocol
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kuaishou.com/about/policy?tab=privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/kuaishou-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kuaishou-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kuaishou-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kuaishou-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kuaishou-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kuaishou-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kuaishou-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kuaishou-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kuaishou-kling-mcp.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kuaishou-scopes.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: CLI
  url: cli/kuaishou-cli.yml
- group: design
  title: ''
  type: Components
  url: components/kuaishou-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kuaishou-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kuaishou-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kuaishou-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kuaishou-changelog.yml
- group: docs
  title: ''
  type: Documentation
  url: https://open.kuaishou.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://open.kuaishou.com/docs/develop/server/code2Session.html
- group: start
  title: ''
  type: GettingStarted
  url: https://open.kuaishou.com/docs/introduction/quickStartGuide/quickStart.html
- group: commercial
  title: ''
  type: Pricing
  url: https://kling.ai/dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://kling.ai/blog
created: '2026-07-17'
description: 'Kuaishou Technology (快手) is a Beijing-based short-video and live-streaming platform operating Kuaishou in mainland China and Kwai internationally, spanning short video, live commerce, local services and online marketing. Its developer surface is split across two public properties: the Kuaishou Open Platform (open.kuaishou.com), which exposes an OAuth 2.0 authorization-code flow and a JSON Open API for third-party apps, mini programs and merchant integrations; and Kwai for Business (developers.kwai.com), the international marketing/advertising API used by advertisers and measurement partners. A third and markedly more open surface is Kling AI (kling.ai), Kuaishou''s generative video and image platform, which ships an asynchronous REST API, an official CLI, a hosted MCP server with published OAuth scopes, and the only llms.txt Kuaishou serves anywhere. Kuaishou also publishes open source under the Kwai GitHub organization. The Open Platform console and the Kwai for Business portal
  are JavaScript single-page applications, largely Chinese-language and gated behind developer registration, but the mini-program documentation subtree at open.kuaishou.com/docs is server-rendered and publicly readable, so this profile records endpoints and pages verified by live HTTP probe or read from that subtree.'
image: https://s2-11031.kwimgs.com/kos/nlav11031/assets/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Kling AI MCP Server
  slug: kling-ai-mcp-server
modified: '2026-08-12'
name: Kuaishou
nav: Providers
network: true
overview: 'Kuaishou publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Social, Video, and Short Video.


  Kuaishou''s developer surface includes support, authentication, CLI, changelog, documentation, API reference, getting-started guide, and 23 more developer resources.'
plans:
- name: Kuaishou Plans Pricing
  plan_count: 0
  slug: kuaishou-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Kuaishou Rate Limits
  slug: kuaishou-rate-limits
scopes:
- name: Kuaishou Scopes
  scope_count: 0
  slug: kuaishou-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.2
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 63.7
    discoverability: 92.6
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 29.2
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kuaishou/refs/heads/main/screenshots/kuaishou-2026-07-25T224317.png
security:
- kind: authentication
  name: Kuaishou Authentication
  slug: kuaishou-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kuaishou Domain Security
  slug: kuaishou-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: kuaishou
tags:
- Company
- Consumer
- Social
- Video
- Short Video
- Live Streaming
- Advertising
- Marketing
- Social-Media
- Content
- China
- Artificial Intelligence
- Generative AI
- Machine-Learning
- MCP
website: https://www.kuaishou.com/
---
