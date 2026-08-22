---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://hyperprobe.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hyperprobe.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hyperprobe.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hyperprobe.co/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.hyperprobe.co
- group: build
  title: ''
  type: SDKs
  url: packages/hyperprobe-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/hyperprobe-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hyperprobe-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/hyperprobe-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hyperprobe-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hyperprobe-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hyperprobe-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperprobe-domain-security.yml
created: '2026-07-17'
description: Hyperprobe is a runtime data platform for AI-native software development, built by a San Francisco team in Y Combinator's Summer 2026 batch. It lets developers and coding agents (Cursor, Claude Code, Codex, opencode, Windsurf) set live, non-breaking breakpoints in running production services directly from the IDE — capturing exact variable snapshots, injecting logs, and tracing call stacks without pausing threads, redeploying, or changing source code. Probes are read-only and non-blocking with under 1% overhead, and PII is redacted in-process before any data leaves the container's memory boundary (password, secret, token, authorization, cookie, key, signature, ssn and creditCard patterns are masked by default). Hyperprobe ships in-process SDKs for Node.js (@hyperprobe/node-sdk), Java (a bytecode-instrumentation agent), and Python (hyperprobe-agent), a VS Code extension, and an official Model Context Protocol (MCP) server (@hyperprobe/mcp-server) that lets AI assistants autonomously
  register conditional probes and read real runtime evidence instead of flat logs. The platform can run fully self-hosted via Docker Compose. Originally added to the API Evangelist network as a Y Combinator portfolio lead, this profile has been enriched from Hyperprobe's public developer surface.
image: https://hyperprobe.co/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: hyperprobe-mcp.yml
  slug: hyperprobe-mcpyml
modified: '2026-07-19'
name: Hyperprobe
nav: Providers
network: true
overview: 'Hyperprobe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Observability, Debugging, Developer Tools, and Runtime.


  Hyperprobe''s developer surface includes documentation, getting-started guide, signup flow, CLI, and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 19.6
  delta: -0.3
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperprobe/refs/heads/main/screenshots/hyperprobe-2026-07-25T221912.png
security:
- kind: domain-security
  name: Hyperprobe Domain Security
  slug: hyperprobe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hyperprobe
tags:
- Company
- Observability
- Debugging
- Developer Tools
- Runtime
- AI
- MCP
- SDK
- Production Debugging
website: https://hyperprobe.co/
---
