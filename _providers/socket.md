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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 61.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 44
  human_in_the_loop: 1
  name: Socket Agentic Access
  operation_count: 96
  slug: socket-agentic-access
  summary_line: 96 operations · 44 acting · 1 human-in-the-loop
api_count: 20
apis:
- description: The alerts API from Socket — 6 operation(s) for alerts.
  name: Socket alerts API
  slug: socket-alerts-api
- description: The api-tokens API from Socket — 6 operation(s) for api-tokens.
  name: Socket api-tokens API
  slug: socket-api-tokens-api
- description: The audit-log API from Socket — 1 operation(s) for audit-log.
  name: Socket audit-log API
  slug: socket-audit-log-api
- description: The dependencies API from Socket — 2 operation(s) for dependencies.
  name: Socket dependencies API
  slug: socket-dependencies-api
- description: The deprecated API from Socket — 17 operation(s) for deprecated.
  name: Socket deprecated API
  slug: socket-deprecated-api
- description: The diff-scans API from Socket — 7 operation(s) for diff-scans.
  name: Socket diff-scans API
  slug: socket-diff-scans-api
- description: The fixes API from Socket — 1 operation(s) for fixes.
  name: Socket fixes API
  slug: socket-fixes-api
- description: The full-scans API from Socket — 13 operation(s) for full-scans.
  name: Socket full-scans API
  slug: socket-full-scans-api
- description: The license-policy API from Socket — 4 operation(s) for license-policy.
  name: Socket license-policy API
  slug: socket-license-policy-api
- description: The metadata API from Socket — 5 operation(s) for metadata.
  name: Socket metadata API
  slug: socket-metadata-api
- description: The org-settings API from Socket — 2 operation(s) for org-settings.
  name: Socket org-settings API
  slug: socket-org-settings-api
- description: The org-snapshots API from Socket — 1 operation(s) for org-snapshots.
  name: Socket org-snapshots API
  slug: socket-org-snapshots-api
- description: The packages API from Socket — 2 operation(s) for packages.
  name: Socket packages API
  slug: socket-packages-api
- description: The repo-labels API from Socket — 5 operation(s) for repo-labels.
  name: Socket repo-labels API
  slug: socket-repo-labels-api
- description: The repos API from Socket — 2 operation(s) for repos.
  name: Socket repos API
  slug: socket-repos-api
- description: The security-policy API from Socket — 1 operation(s) for security-policy.
  name: Socket security-policy API
  slug: socket-security-policy-api
- description: The telemetry API from Socket — 1 operation(s) for telemetry.
  name: Socket telemetry API
  slug: socket-telemetry-api
- description: The threat-feed API from Socket — 1 operation(s) for threat-feed.
  name: Socket threat-feed API
  slug: socket-threat-feed-api
- description: The triage API from Socket — 2 operation(s) for triage.
  name: Socket triage API
  slug: socket-triage-api
- description: The webhooks API from Socket — 2 operation(s) for webhooks.
  name: Socket webhooks API
  slug: socket-webhooks-api
artifact_total: 28
asyncapis:
- description: ''
  name: Socket Webhooks
  slug: socket-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/socket-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/socket-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/socket-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://socket.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.socket.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.socket.dev/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.socket.dev/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.socket.dev/reference/authentication
- group: operate
  title: ''
  type: Support
  url: https://docs.socket.dev/docs/contact-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SocketDev
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/socket-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/socket-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/socket-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/socket-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/socket-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/socket-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/socket-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/socket-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/socket-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.socket.dev/reference/api-lifecycle-and-deprecation-process
- group: operate
  title: ''
  type: StatusPage
  url: https://status.socket.dev
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/socket-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/socket-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/socket-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/socket-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.socket.dev/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/socket-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/socket-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/socket-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://socket.dev/security/disclosure
- group: company
  title: ''
  type: Blog
  url: https://socket.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://socket.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://socket.dev/login
created: '2026-07-17'
description: Socket is a developer-first software supply chain security platform that protects applications from supply chain attacks by deeply inspecting open source dependencies across npm, PyPI, Maven, Go, NuGet, RubyGems, Cargo and more. Socket detects malware, hidden code, typosquats, install scripts, protestware, and risky capabilities in packages, scores their quality and risk, and enforces security and license policies across repositories through a REST API, CLI, GitHub App, MCP server, and static reachability analysis. Founded by Feross Aboukhadijeh and backed by a16z, Socket is used by engineering teams at organizations including Vercel, Replit, and Brave.
image: https://socket.dev/favicon.ico
layout: provider
mcp_servers:
- description: Socket's official MCP server exposes the depscore tool so AI assistants can query dependency scores from the Socket API; hosted at https://mcp.socket.dev/ or run locally.
  name: Socket MCP Server
  slug: socket-mcp-server
modified: '2026-07-21'
name: Socket
nav: Providers
network: true
overview: 'Socket publishes 20 APIs on the [APIs.io](https://apis.io/) network, including alerts API, api-tokens API, audit-log API, and 17 more. Tagged areas include Company, Security, Software Supply Chain Security, Dependency Scanning, and Software Composition Analysis.


  The Socket catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Socket''s developer surface includes documentation, getting-started guide, API reference, support, authentication, changelog, CLI, and 27 more developer resources.'
random_paper: 69
rate_limits:
- limit_count: 0
  name: Socket Rate Limits
  slug: socket-rate-limits
scopes:
- name: Socket Scopes
  scope_count: 34
  slug: socket-scopes
  summary_line: 34 scopes
score:
  band: strong
  composite: 56.1
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 69.8
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 63.2
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Socket Authentication
  slug: socket-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Socket Domain Security
  slug: socket-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Socket Vulnerability Disclosure
  slug: socket-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: socket
tags:
- Company
- Security
- Software Supply Chain Security
- Dependency Scanning
- Software Composition Analysis
- Vulnerability Management
- Open Source Security
- DevSecOps
- SBOM
- Package Analysis
website: https://socket.dev
---
