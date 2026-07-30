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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Jinba Agentic Access
  operation_count: 39
  slug: jinba-agentic-access
  summary_line: 39 operations · 23 acting
api_count: 14
apis:
- description: The API Keys API from Jinba — 2 operation(s) for api keys.
  name: Jinba API Keys API
  slug: jinba-api-keys-api
- description: The Credits API from Jinba — 1 operation(s) for credits.
  name: Jinba Credits API
  slug: jinba-credits-api
- description: The Execution API from Jinba — 2 operation(s) for execution.
  name: Jinba Execution API
  slug: jinba-execution-api
- description: The Explore API from Jinba — 2 operation(s) for explore.
  name: Jinba Explore API
  slug: jinba-explore-api
- description: The Flows API from Jinba — 1 operation(s) for flows.
  name: Jinba Flows API
  slug: jinba-flows-api
- description: The MCP API from Jinba — 2 operation(s) for mcp.
  name: Jinba MCP API
  slug: jinba-mcp-api
- description: The Members API from Jinba — 1 operation(s) for members.
  name: Jinba Members API
  slug: jinba-members-api
- description: The Organizations API from Jinba — 2 operation(s) for organizations.
  name: Jinba Organizations API
  slug: jinba-organizations-api
- description: The Public API from Jinba — 2 operation(s) for public.
  name: Jinba Public API
  slug: jinba-public-api
- description: The Runs API from Jinba — 2 operation(s) for runs.
  name: Jinba Runs API
  slug: jinba-runs-api
- description: The Tools API from Jinba — 2 operation(s) for tools.
  name: Jinba Tools API
  slug: jinba-tools-api
- description: The ToolSets API from Jinba — 2 operation(s) for toolsets.
  name: Jinba ToolSets API
  slug: jinba-toolsets-api
- description: The Versions API from Jinba — 3 operation(s) for versions.
  name: Jinba Versions API
  slug: jinba-versions-api
- description: The Webhooks API from Jinba — 3 operation(s) for webhooks.
  name: Jinba Webhooks API
  slug: jinba-webhooks-api
artifact_total: 19
asyncapis:
- description: ''
  name: Jinba Toolbox Webhooks
  slug: jinba-toolbox-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://jinba.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jinba.io/en/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jinba.io/en/pages/basics/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jinba.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.jinba.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jinba.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jinba.io/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.jinba.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.jinba.io/contact-sales
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jinba.io
- group: company
  title: ''
  type: Twitter
  url: https://x.com/jinbaflow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jinba
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jinba-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jinba-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jinba-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jinba-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jinba-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jinba-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/jinba-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/jinba-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jinba-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.jinba.io/en/pages/security/index
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jinba-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/jinba-toolbox-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jinba-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jinba-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Jinba is an enterprise-grade platform for building, running, and deploying AI-powered workflows and agents using natural language. Business teams describe a process in plain language, refine it in a visual graph editor or a YAML manifest, and deploy it to production as an API or an MCP server. The product spans Jinba Flow (the workflow builder), Jinba App / App Neo (the execution and agent environment), and Jinba Toolbox (a centralized tool management and execution platform for AI agents that runs tools in isolated E2B or Daytona sandboxes). For developers, Jinba exposes two REST APIs — the Flow External API for invoking published workflows synchronously or asynchronously, and the Toolbox API for managing organizations, toolsets, tools, versions, runs, webhooks, and API keys — plus a TypeScript SDK, native Model Context Protocol (MCP) endpoints, webhooks with HMAC-signed payloads, and RFC 9457 error semantics. Jinba is SOC 2 Type 2 audited, supports SSO and RBAC, and offers
  on-premises or private-cloud (AWS/GCP/Azure) deployment. Founded by Shoya Matsumori and Takuya Norisugi; Y Combinator (Winter 2026).
image: https://jinba.io/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: jinba-mcp.yml
  slug: jinba-mcpyml
modified: '2026-07-19'
name: Jinba
nav: Providers
network: true
overview: 'Jinba publishes 14 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Credits API, Execution API, and 11 more. Tagged areas include Company, AI, Agents, Workflow Automation, and Enterprise.


  The Jinba catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Jinba''s developer surface includes documentation, getting-started guide, pricing, signup flow, engineering blog, support, authentication, and 20 more developer resources.'
random_paper: 24
score:
  band: developing
  composite: 54.4
  delta: 0.9
  facets:
    commercial_clarity: 52.6
    contract_quality: 66.2
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jinba/refs/heads/main/screenshots/jinba-2026-07-25T223154.png
security:
- kind: authentication
  name: Jinba Authentication
  slug: jinba-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Jinba Domain Security
  slug: jinba-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: jinba
tags:
- Company
- AI
- Agents
- Workflow Automation
- Enterprise
- MCP
- Low-Code
- Developer Tools
- Tools
- Automation
website: https://jinba.io
---
