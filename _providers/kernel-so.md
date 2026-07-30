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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 82
  human_in_the_loop: 13
  name: Kernel So Agentic Access
  operation_count: 133
  slug: kernel-so-agentic-access
  summary_line: 133 operations · 82 acting · 13 human-in-the-loop
api_count: 22
apis:
- description: Hosted Model Context Protocol server at mcp.onkernel.com that exposes Kernel resources (browsers, profiles, proxies, apps) as MCP tools and bundles four standalone tools — computer actions, Playwright
  name: Kernel MCP Server
  slug: kernel-mcp-server
- description: Create and manage API keys for organization and project-scoped access.
  name: Kernel API Keys API
  slug: kernel-so-api-keys-api
- description: List applications and versions.
  name: Kernel Apps API
  slug: kernel-so-apps-api
- description: The Auth Connections API from Kernel — 6 operation(s) for auth connections.
  name: Kernel Auth Connections API
  slug: kernel-so-auth-connections-api
- description: Control mouse, keyboard, and screen on the browser instance.
  name: Kernel Browser Computer Controls API
  slug: kernel-so-browser-computer-controls-api
- description: Read, write, and manage files on the browser instance.
  name: Kernel Browser Filesystem API
  slug: kernel-so-browser-filesystem-api
- description: Stream logs from the browser instance.
  name: Kernel Browser Logs API
  slug: kernel-so-browser-logs-api
- description: Execute Playwright code against the browser instance.
  name: Kernel Browser Playwright API
  slug: kernel-so-browser-playwright-api
- description: Create and manage browser pools for acquiring and releasing browsers.
  name: Kernel Browser Pools API
  slug: kernel-so-browser-pools-api
- description: Execute and manage processes on the browser instance.
  name: Kernel Browser Processes API
  slug: kernel-so-browser-processes-api
- description: Record and manage browser session video replays.
  name: Kernel Browser Replays API
  slug: kernel-so-browser-replays-api
- description: Stream live telemetry events from a browser session.
  name: Kernel Browser Telemetry API
  slug: kernel-so-browser-telemetry-api
- description: Create and manage browser sessions.
  name: Kernel Browsers API
  slug: kernel-so-browsers-api
- description: Configure external credential providers like 1Password.
  name: Kernel Credential Providers API
  slug: kernel-so-credential-providers-api
- description: Create and manage credentials for authentication.
  name: Kernel Credentials API
  slug: kernel-so-credentials-api
- description: Create and manage app deployments and stream deployment events.
  name: Kernel Deployments API
  slug: kernel-so-deployments-api
- description: Create, list, retrieve, and delete browser extensions.
  name: Kernel Extensions API
  slug: kernel-so-extensions-api
- description: Invoke actions and stream or query invocation status and events.
  name: Kernel Invocations API
  slug: kernel-so-invocations-api
- description: Create and manage auth connections for automated credential capture and login.
  name: Kernel Managed Auth API
  slug: kernel-so-managed-auth-api
- description: Create, list, retrieve, and delete browser profiles.
  name: Kernel Profiles API
  slug: kernel-so-profiles-api
- description: Create and manage projects for resource isolation within an organization.
  name: Kernel Projects API
  slug: kernel-so-projects-api
- description: Create and manage proxy configurations for routing browser traffic.
  name: Kernel Proxies API
  slug: kernel-so-proxies-api
artifact_total: 28
collections:
- collection_type: open
  name: Kernel API
  slug: open-kernel
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kernel-so-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kernel-so-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kernel-so-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kernel-so-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.kernel.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://www.kernel.sh/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.kernel.sh/docs/api-reference/
- group: agent
  title: ''
  type: LlmsText
  url: https://www.kernel.sh/docs/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kernel.sh/docs/info/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.kernel.sh/changelog
- group: operate
  title: ''
  type: Support
  url: https://www.kernel.sh/docs/info/support
- group: operate
  title: ''
  type: Community
  url: https://www.kernel.sh/docs/community/discord
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/onkernel
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/onkernel/kernel-images
- group: build
  title: ''
  type: SDKs
  url: https://github.com/onkernel/kernel-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/onkernel/kernel-node-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/onkernel/kernel-go-sdk
- group: build
  title: ''
  type: CLI
  url: https://github.com/onkernel/cli
- group: build
  title: ''
  type: CLI
  url: https://github.com/onkernel/homebrew-tap
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/onkernel/kernel-mcp-server
- group: build
  title: ''
  type: SDKs
  url: https://github.com/onkernel/cu-playwright-ts
- group: build
  title: ''
  type: SDKs
  url: https://github.com/onkernel/cu-playwright-python
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/onkernel/hypeman
- group: operate
  title: ''
  type: Migration
  url: https://www.kernel.sh/docs/migrations/scrapybara
- group: other
  title: ''
  type: Funding
  url: https://www.ycombinator.com/companies/kernel
- group: company
  title: ''
  type: Blog
  url: https://www.kernel.sh/api/blog/rss
created: '2026-05-25'
description: Kernel is browser infrastructure for AI agents and web automations. Founded in 2025 by Catherine Jue (CEO) and Rafael Garcia (CTO) and backed by Accel and Y Combinator (S25), Kernel runs sandboxed Chromium browsers on a unikernel platform with sub-150ms cold starts, built-in stealth mode, residential proxies, CAPTCHA solving, session recording, live view, persistent profiles, and a serverless app platform that co-locates agent code with browsers. Kernel works with Playwright, Puppeteer, Browser Use, Stagehand, Magnitude, Notte, and the Anthropic/OpenAI/Gemini computer-use loops. The REST API at api.onkernel.com exposes browsers, browser pools, profiles, proxies, replays, extensions, computer controls, filesystem, processes, Playwright execution, managed auth, credentials, apps, deployments, invocations, and projects.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kernel-so.png
layout: provider
mcp_servers:
- description: ''
  name: Kernel MCP Server (source)
  slug: kernel-mcp-server-source
modified: '2026-05-25'
name: Kernel
nav: Providers
network: true
overview: 'Kernel publishes 21 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Apps API, Auth Connections API, and 18 more. Tagged areas include Agents, AI, Artificial Intelligence, Browser Automation, and Browsers.


  Kernel''s developer surface includes authentication, developer portal, documentation, pricing, changelog, support, CLI, and 19 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 40.5
  delta: -3.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 57.4
    developer_ergonomics: 65.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kernel-so/refs/heads/main/screenshots/kernel-so-2026-06-20T183954.png
security:
- kind: authentication
  name: Kernel So Authentication
  slug: kernel-so-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kernel So Domain Security
  slug: kernel-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kernel So Trust Center
  slug: kernel-so-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: kernel-so
tags:
- Agents
- AI
- Artificial Intelligence
- Browser Automation
- Browsers
- Computer Use
- Headless Browsers
- MCP
- Playwright
- Web Agents
website: https://www.kernel.sh/
---
