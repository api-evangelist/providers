---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'Reforge Launch delivers feature flags, live configuration, dynamic log levels, and experiments through first-party SDKs and a CLI. SDKs fetch configuration from a global delivery network and evaluate '
  name: Reforge Launch
  slug: reforge-launch
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reforge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reforge.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.reforge.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reforge.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reforge.com/docs/tutorials/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ReforgeHQ
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reforge.com/
- group: company
  title: ''
  type: Blog
  url: https://www.reforge.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reforge.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.reforge.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reforge.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reforge.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/reforge-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reforge-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/reforge-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reforge-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reforge-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reforge-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reforge-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reforge-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reforge-llms.txt
created: '2026-07-17'
description: Reforge is the company behind Reforge Launch, a developer platform for feature flags, live configuration, dynamic log levels, and experimentation delivered as a service (the product formerly known as Prefab). Applications integrate Reforge through first-party SDKs for Node, JavaScript, React, Python, Ruby, Go, and Java plus a command-line interface, evaluating flags and configuration against user context with server- and client-side SDK keys. Configuration is delivered over a global content network (primary/secondary.reforge.com) with server-sent events and polling for real-time updates, while telemetry flows to api.reforge.com. Reforge is backed by a16z and Insight Partners.
image: https://avatars.githubusercontent.com/u/24498216?v=4
layout: provider
mcp_servers:
- description: 'The Reforge CLI ships an MCP server that connects an AI assistant to a Reforge workspace. `reforge mcp` configures the server for a supported editor/assistant (e.g. Claude Code, Codeium), letting the '
  name: Reforge MCP Server
  slug: reforge-mcp-server
modified: '2026-07-21'
name: Reforge
nav: Providers
network: true
overview: 'Reforge publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Feature Flags, Feature Management, Dynamic Configuration, and Live Config.


  Reforge''s developer surface includes documentation, getting-started guide, engineering blog, pricing, CLI, authentication, and 15 more developer resources.'
random_paper: 11
screenshot: https://raw.githubusercontent.com/api-evangelist/reforge/refs/heads/main/screenshots/reforge-2026-09-02T153231.png
security:
- kind: authentication
  name: Reforge Authentication
  slug: reforge-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Reforge Domain Security
  slug: reforge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reforge
tags:
- Company
- Feature Flags
- Feature Management
- Dynamic Configuration
- Live Config
- Experimentation
- Developer Tools
- SDK
- Observability
website: https://www.reforge.com/
---
