---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 62
  human_in_the_loop: 13
  name: Anchorbrowser Agentic Access
  operation_count: 98
  slug: anchorbrowser-agentic-access
  summary_line: 98 operations · 62 acting · 13 human-in-the-loop
api_count: 20
apis:
- description: The Anchor Browser REST API exposes cloud browser sessions for AI agents. It covers session lifecycle (create, async create, status, end, list history), batch session creation (up to 5,000 simultaneou
  name: Anchor Browser API
  slug: anchor-browser-api
- description: A Model Context Protocol server (hosted and open-source) that lets MCP-compatible AI clients drive Anchor Browser sessions as tools.
  name: Anchor Browser MCP Server
  slug: anchor-browser-mcp
- description: LangChain-ready tools that wrap Anchor Browser-powered browser actions for use inside LangChain and LangGraph agent workflows.
  name: LangChain Anchor Browser Tools
  slug: anchor-browser-langchain
- description: The Agentic capabilities API from Anchor Browser — 3 operation(s) for agentic capabilities.
  name: Anchor Browser Agentic capabilities API
  slug: anchorbrowser-agentic-capabilities-api
- description: The AI Tools API from Anchor Browser — 2 operation(s) for ai tools.
  name: Anchor Browser AI Tools API
  slug: anchorbrowser-ai-tools-api
- description: The Applications API from Anchor Browser — 6 operation(s) for applications.
  name: Anchor Browser Applications API
  slug: anchorbrowser-applications-api
- description: The Batch Sessions API from Anchor Browser — 3 operation(s) for batch sessions.
  name: Anchor Browser Batch Sessions API
  slug: anchorbrowser-batch-sessions-api
- description: The Billing API from Anchor Browser — 1 operation(s) for billing.
  name: Anchor Browser Billing API
  slug: anchorbrowser-billing-api
- description: The Browser Sessions API from Anchor Browser — 10 operation(s) for browser sessions.
  name: Anchor Browser Browser Sessions API
  slug: anchorbrowser-browser-sessions-api
- description: The Certificates API from Anchor Browser — 2 operation(s) for certificates.
  name: Anchor Browser Certificates API
  slug: anchorbrowser-certificates-api
- description: The Event Coordination API from Anchor Browser — 2 operation(s) for event coordination.
  name: Anchor Browser Event Coordination API
  slug: anchorbrowser-event-coordination-api
- description: The Extensions API from Anchor Browser — 2 operation(s) for extensions.
  name: Anchor Browser Extensions API
  slug: anchorbrowser-extensions-api
- description: The Identities API from Anchor Browser — 2 operation(s) for identities.
  name: Anchor Browser Identities API
  slug: anchorbrowser-identities-api
- description: The Integrations API from Anchor Browser — 2 operation(s) for integrations.
  name: Anchor Browser Integrations API
  slug: anchorbrowser-integrations-api
- description: The OS Level Control API from Anchor Browser — 14 operation(s) for os level control.
  name: Anchor Browser OS Level Control API
  slug: anchorbrowser-os-level-control-api
- description: The Profiles API from Anchor Browser — 2 operation(s) for profiles.
  name: Anchor Browser Profiles API
  slug: anchorbrowser-profiles-api
- description: The Session Recordings API from Anchor Browser — 5 operation(s) for session recordings.
  name: Anchor Browser Session Recordings API
  slug: anchorbrowser-session-recordings-api
- description: The Tasks API from Anchor Browser — 2 operation(s) for tasks.
  name: Anchor Browser Tasks API
  slug: anchorbrowser-tasks-api
- description: The Tasks (Legacy) API from Anchor Browser — 11 operation(s) for tasks (legacy).
  name: Anchor Browser Tasks (Legacy) API
  slug: anchorbrowser-tasks-legacy-api
- description: The Tools API from Anchor Browser — 4 operation(s) for tools.
  name: Anchor Browser Tools API
  slug: anchorbrowser-tools-api
artifact_total: 66
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AnchorBrowser Agentic capabilities API
  slug: open-anchorbrowser-agentic-capabilities-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities AI Tools API
  slug: open-anchorbrowser-ai-tools-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Applications API
  slug: open-anchorbrowser-applications-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Batch Sessions API
  slug: open-anchorbrowser-batch-sessions-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Billing API
  slug: open-anchorbrowser-billing-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Browser Sessions API
  slug: open-anchorbrowser-browser-sessions-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Certificates API
  slug: open-anchorbrowser-certificates-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Event Coordination API
  slug: open-anchorbrowser-event-coordination-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Extensions API
  slug: open-anchorbrowser-extensions-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Identities API
  slug: open-anchorbrowser-identities-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Integrations API
  slug: open-anchorbrowser-integrations-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities OS Level Control API
  slug: open-anchorbrowser-os-level-control-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Profiles API
  slug: open-anchorbrowser-profiles-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Session Recordings API
  slug: open-anchorbrowser-session-recordings-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Tasks API
  slug: open-anchorbrowser-tasks-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Tasks (Legacy) API
  slug: open-anchorbrowser-tasks-legacy-api
- collection_type: open
  name: AnchorBrowser Agentic capabilities Tools API
  slug: open-anchorbrowser-tools-api
- collection_type: open
  name: AnchorBrowser API
  slug: open-anchorbrowser
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/anchorbrowser/langchain-anchorbrowser/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/anchorbrowser/langchain-anchorbrowser/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anchorbrowser-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/anchorbrowser-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anchorbrowser-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anchorbrowser-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://anchorbrowser.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anchorbrowser.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anchorbrowser.io/quickstart/use-via-sdk
- group: auth
  title: ''
  type: Authentication
  url: https://docs.anchorbrowser.io
- group: start
  title: ''
  type: Signup
  url: https://app.anchorbrowser.io
- group: start
  title: ''
  type: Console
  url: https://app.anchorbrowser.io/playground
- group: company
  title: ''
  type: Blog
  url: https://anchorbrowser.io/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anchorbrowser.io
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.anchorbrowser.io
- group: build
  title: ''
  type: SDKs
  url: https://docs.anchorbrowser.io/quickstart/use-via-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/anchorbrowser/langchain-anchorbrowser
- group: agent
  title: ''
  type: MCPServer
  url: https://browsermcp.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.anchorbrowser.io/llms.txt
created: '2026-05-23'
description: Anchor Browser is an AI-native cloud browser infrastructure platform that lets AI agents interact with the web the same way a human would. It provides hosted, isolated Chromium sessions ("Anchor Chromium"), built-in stealth and bot-evasion tuning, an authentication layer (OmniConnect) for managing logged-in user credentials, a built-in enterprise VPN, residential and sticky-IP proxies, a Web Action Cache that hardens flaky workflows into deterministic code, and a REST API plus SDKs for Playwright, Puppeteer, MCP, LangChain, and CrewAI. The platform is positioned as the sandbox runtime for agentic browser automation.
features:
- description: Hosted, isolated Chromium sessions ("Anchor Chromium") allocated on demand and torn down per task, no local browser setup needed.
  name: Cloud Browser Sessions
- description: Humanized Chromium fork tuned to be recognized as legitimate by major bot-protection systems.
  name: Stealth and Bot Evasion
- description: Manages user credentials and authentication lifecycles so agents can operate inside logged-in surfaces.
  name: OmniConnect Authentication
- description: Built-in enterprise VPN for routing browser traffic over trusted networks.
  name: Anchor VPN
- description: Built-in residential proxy rotation, geo-targeting, and dedicated sticky IPs.
  name: Residential and Sticky IPs
- description: Captures repeatable workflows as deterministic code so previously flaky automations become reliable.
  name: Web Action Cache
- description: Natural-language task execution against Claude, Gemini, and OpenAI, plus first-party MCP, LangChain, and CrewAI integrations.
  name: AI Agent Integration
- description: Existing Playwright and Puppeteer code can target Anchor sessions without code changes.
  name: Playwright and Puppeteer Support
- description: Per-session video recording with pause/resume and bidirectional file upload/download.
  name: Recording and File I/O
finops:
- name: Anchorbrowser Finops
  service_category: API
  slug: anchorbrowser-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anchorbrowser.png
integrations:
- description: Hosted and open-source MCP servers let any MCP-compatible client use Anchor Browser as a tool.
  name: Model Context Protocol (MCP)
- description: First-party LangChain tools wrap Anchor actions for use in LangChain and LangGraph agents.
  name: LangChain
- description: Integration for orchestrating multi-agent crews on top of Anchor sessions.
  name: CrewAI
- description: Drop-in target for existing Playwright and Puppeteer automation code.
  name: Playwright and Puppeteer
- description: Integration with Cloudflare's signed-agent / Web Bot Auth scheme so Anchor sessions are recognized as legitimate agent traffic.
  name: Cloudflare Web Bot Auth
- description: Available for procurement via AWS Marketplace.
  name: AWS Marketplace
layout: provider
mcp_servers:
- description: ''
  name: browsermcp.com
  slug: browsermcpcom
modified: '2026-05-23'
name: Anchor Browser
nav: Providers
network: true
overview: 'Anchor Browser publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Agentic capabilities API, AI Tools API, Applications API, and 14 more. Tagged areas include Browser Infrastructure, AI Agents, Cloud Browser, Browser Automation, and Sandbox.


  Anchor Browser''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, developer console, engineering blog, and 12 more developer resources.'
plans:
- name: Anchorbrowser Plans Pricing
  plan_count: 1
  slug: anchorbrowser-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 2
  name: Anchorbrowser Rate Limits
  slug: anchorbrowser-rate-limits
score:
  band: developing
  composite: 49.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.5
    developer_ergonomics: 63.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anchorbrowser/refs/heads/main/screenshots/anchorbrowser-2026-06-20T171955.png
security:
- kind: authentication
  name: Anchorbrowser Authentication
  slug: anchorbrowser-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Anchorbrowser Domain Security
  slug: anchorbrowser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Anchorbrowser Trust Center
  slug: anchorbrowser-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: anchorbrowser
tags:
- Browser Infrastructure
- AI Agents
- Cloud Browser
- Browser Automation
- Sandbox
- Stealth Browser
- MCP
use_cases:
- description: Give AI agents a real browser to navigate sites that lack APIs, submit forms, and extract data.
  name: Agentic Web Automation
- description: Automate operations behind login flows (banking, SaaS dashboards, internal portals) without storing credentials on developer laptops.
  name: Authenticated Workflow Automation
- description: Run up to 5,000 simultaneous sessions with rotating residential IPs and built-in captcha handling.
  name: Web Scraping at Scale
- description: Give frontier model agents a safe, isolated browser to operate in without exposing the user's machine.
  name: AI Agent Sandbox
website: https://anchorbrowser.io
---
