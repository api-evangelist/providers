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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 35.6
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Hosted Model Context Protocol server that pipes a Jam's recording, console logs, network requests, user events, transcript, and metadata into AI coding tools (Claude, Cursor, VS Code). OAuth2 (PKCE) o
  name: Jam MCP Server
  slug: jam-mcp-server
artifact_total: 8
asyncapis:
- description: ''
  name: Jam Webhooks
  slug: jam-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://jam.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://jam.dev/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://jam.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://jam.dev/docs/cli
- group: start
  title: ''
  type: GettingStarted
  url: https://jam.dev/docs/introduction
- group: operate
  title: ''
  type: Support
  url: https://jam.dev/help
- group: company
  title: ''
  type: Blog
  url: https://jam.dev/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jamdotdev
- group: commercial
  title: ''
  type: Pricing
  url: https://jam.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://jam.dev/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jam.dev/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jam.dev/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://jam.instatus.com/
- group: auth
  title: ''
  type: Security
  url: https://jam.dev/docs/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/jam-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.jam.dev/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jam-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jam-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jam-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/jam-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/jam-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/jam-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jam-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jam-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jam-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/jam-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jam-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jam-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jam-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jam-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/jam-bug-to-fix.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/jam-collect-recordings.md
created: '2026-07-17'
description: Jam is a bug-reporting and debugging-telemetry tool for software teams. Its Chrome extension and iOS app capture one-click bug reports that bundle a screen recording or screenshot together with console logs, network requests, user events, and device metadata, so engineers can reproduce and fix issues without chasing repro steps. Jam adds Instant Replay (the last two minutes of activity), Recording Links for collecting captures from anyone with no install, and routes reports into GitHub, GitLab, Jira, Linear, Slack, Notion, Sentry and other tools. For developers and AI agents Jam exposes a hosted MCP server, a first-party CLI, a JavaScript SDK (jam.metadata()), and Standard Webhooks. Used by 200,000+ people across QA, product, engineering, and support.
image: https://storage.googleapis.com/jam-assets/jam-og-image.png
layout: provider
mcp_servers:
- description: ''
  name: jam-mcp.yml
  slug: jam-mcpyml
modified: '2026-07-19'
name: Jam
nav: Providers
network: true
overview: 'Jam publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Bug Reporting, Debugging, and Quality Assurance.


  The Jam catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Jam''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, CLI, and 25 more developer resources.'
random_paper: 6
scopes:
- name: Jam Scopes
  scope_count: 2
  slug: jam-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 48.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 22.6
    developer_ergonomics: 80.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 48.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Jam Authentication
  slug: jam-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Jam Domain Security
  slug: jam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jam Vulnerability Disclosure
  slug: jam-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Jam Trust Center
  slug: jam-trust-center
  summary_line: SOC 2, ISO 27001
slug: jam
tags:
- Company
- Developer Tools
- Bug Reporting
- Debugging
- Quality Assurance
- Observability
- Screen Recording
- Model Context Protocol
website: https://jam.dev/
---
