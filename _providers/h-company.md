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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 43
  human_in_the_loop: 4
  name: H Company Agentic Access
  operation_count: 69
  slug: h-company-agentic-access
  summary_line: 69 operations · 43 acting · 4 human-in-the-loop
api_count: 10
apis:
- description: OpenAI-compatible inference API serving the Holo3 and Holo3.1 vision-language models for computer use — chat completions with structured outputs, reasoning, and image inputs, plus runtime model discov
  name: H Company Holo Models API
  slug: h-company-holo-models
- description: The Agents API from H Company — 2 operation(s) for agents.
  name: H Company Agents API
  slug: h-company-agents-api
- description: The Browser Profiles API from H Company — 6 operation(s) for browser profiles.
  name: H Company Browser Profiles API
  slug: h-company-browser-profiles-api
- description: The Environments API from H Company — 2 operation(s) for environments.
  name: H Company Environments API
  slug: h-company-environments-api
- description: The quota API from H Company — 1 operation(s) for quota.
  name: H Company quota API
  slug: h-company-quota-api
- description: The Schedules API from H Company — 6 operation(s) for schedules.
  name: H Company Schedules API
  slug: h-company-schedules-api
- description: The Sessions API from H Company — 15 operation(s) for sessions.
  name: H Company Sessions API
  slug: h-company-sessions-api
- description: The Skills API from H Company — 2 operation(s) for skills.
  name: H Company Skills API
  slug: h-company-skills-api
- description: The Vaults API from H Company — 4 operation(s) for vaults.
  name: H Company Vaults API
  slug: h-company-vaults-api
- description: The Webhooks API from H Company — 5 operation(s) for webhooks.
  name: H Company Webhooks API
  slug: h-company-webhooks-api
artifact_total: 15
asyncapis:
- description: ''
  name: H Company Webhooks
  slug: h-company-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.hcompany.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.hcompany.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://hub.hcompany.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://agp.hcompany.ai/share/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://hub.hcompany.ai/computer-use-agents/quickstart
- group: company
  title: ''
  type: Blog
  url: https://hcompany.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hcompai
- group: operate
  title: ''
  type: Support
  url: https://hcompany.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://hcompany.ai/holo-models-api
- group: start
  title: ''
  type: SignUp
  url: https://portal.hcompany.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hcompany.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hcompany.ai/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/h-company-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/h-company-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/h-company-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/h-company-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/h-company-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/h-company-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/h-company-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/h-company-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/h-company-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/h-company-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/h-company-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/h-company-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://hub.hcompany.ai/models
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/h-company-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/h-company-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/h-company-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/h-company-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'H Company (hcompany.ai) is a Paris-based AI lab, backed by Accel and Creandum, that builds the Holo family of vision-language models and a Computer-Use Agents platform for automating work on browsers and desktops. It ships two public APIs: the Computer-Use Agents API (agp, /api/v2) for launching, steering, scheduling, and observing autonomous agent sessions — with reusable agents, skills, environments, browser profiles, vaults, and signed webhooks — and the OpenAI-compatible Holo Models API (/v1) serving the Holo3 and Holo3.1 models. Typed Python and TypeScript SDKs (hai-agents), a hai CLI, an official MCP server, and idempotent, region-isolated (EU/US) REST round out an agent-native developer surface.'
image: https://framerusercontent.com/assets/Xk8HZOz0eejLsPdcyokpuQJa3c.png
layout: provider
mcp_servers:
- description: ''
  name: h-company-mcp.yml
  slug: h-company-mcpyml
modified: '2026-07-19'
name: H Company
nav: Providers
network: true
overview: 'H Company publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Browser Profiles API, Environments API, and 6 more. Tagged areas include Artificial Intelligence, Agents, Computer Use, Automation, and Machine Learning.


  The H Company catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  H Company''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 23 more developer resources.'
random_paper: 61
score:
  band: strong
  composite: 56.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 67.9
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 56.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/h-company/refs/heads/main/screenshots/h-company-2026-07-25T220500.png
security:
- kind: authentication
  name: H Company Authentication
  slug: h-company-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: H Company Domain Security
  slug: h-company-domain-security
  summary_line: TLSv1.2 · DMARC
slug: h-company
tags:
- Artificial Intelligence
- Agents
- Computer Use
- Automation
- Machine Learning
- Browser Automation
- LLMs
- MCP
- Developer Tools
website: https://www.hcompany.ai/
---
