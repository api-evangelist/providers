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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.7
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://codspeed.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.codspeed.io/
- group: docs
  title: ''
  type: Documentation
  url: https://codspeed.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://codspeed.io/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://codspeed.io/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://codspeed.io/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@codspeed.io
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/MxpaCfKSqF
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CodSpeedHQ
- group: commercial
  title: ''
  type: Pricing
  url: https://codspeed.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.codspeed.io/login?flow=get-started
- group: start
  title: ''
  type: Login
  url: https://app.codspeed.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codspeed.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codspeed.io/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://codspeed.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/codspeed-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/codspeed-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/codspeed-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/codspeed-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/codspeed-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codspeed-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/codspeed-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/codspeed-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.codspeed.io
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.codspeed.io
- group: auth
  title: ''
  type: Security
  url: https://codspeed.io/docs/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/codspeed-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codspeed-domain-security.yml
created: '2026-07-17'
description: CodSpeed is a continuous performance testing and optimization platform that automatically detects performance regressions in pull requests and proposes autonomous optimizations. It runs benchmarks with sub-1% variance inside CI (GitHub Actions, GitLab CI, Buildkite), generates differential flamegraphs to pinpoint the exact lines that degraded, and gates PRs that fail performance standards. CodSpeed supports Rust, C++, Go, Java, Python, and Node.js via first-party harnesses (pytest-codspeed, cargo-codspeed / codspeed-rust, google_benchmark, JMH, vitest, tinybench, benchmark.js), CPU-simulation, walltime, and memory instruments, plus MongoDB database instrumentation. It ships an open-source CLI, a GitHub Action, a hosted MCP server, and packaged Agent Skills so AI coding assistants can investigate regressions and optimize code directly. CodSpeed is a Techstars-backed company.
image: https://codspeed.io/logo.svg
layout: provider
mcp_servers:
- description: Hosted, remote MCP server that gives AI-powered coding tools direct access to CodSpeed performance data (benchmark runs, comparisons, flamegraphs) so agents can investigate regressions and optimize co
  name: CodSpeed MCP Server
  slug: codspeed-mcp-server
modified: '2026-07-18'
name: CodSpeed
nav: Providers
network: true
overview: 'CodSpeed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Performance, Benchmarking, Continuous Integration, and Developer Tools.


  CodSpeed''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 22 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 33.5
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 33.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codspeed/refs/heads/main/screenshots/codspeed-2026-07-25T205952.png
security:
- kind: authentication
  name: Codspeed Authentication
  slug: codspeed-authentication
  summary_line: oauth2/oidc/token/github-app · 4 schemes
- kind: domain-security
  name: Codspeed Domain Security
  slug: codspeed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Codspeed Vulnerability Disclosure
  slug: codspeed-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Codspeed Trust Center
  slug: codspeed-trust-center
  summary_line: SOC 2 Type II
slug: codspeed
tags:
- Company
- Performance
- Benchmarking
- Continuous Integration
- Developer Tools
- Observability
- Testing
- DevOps
- Artificial Intelligence
- MCP
website: https://codspeed.io/
---
