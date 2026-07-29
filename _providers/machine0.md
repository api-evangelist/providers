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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The machine0 control plane for creating, managing, snapshotting and connecting to persistent cloud VMs. Exposed as a CLI (npm @machine0/cli) and a remote MCP server (Streamable HTTP, OAuth 2.0 + API k
  name: Machine0 Control Plane
  slug: machine0-control-plane
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/machine0-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://machine0.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.machine0.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.machine0.io/introduction/overview
- group: start
  title: ''
  type: Quickstart
  url: https://docs.machine0.io/introduction/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.machine0.io/introduction/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://machine0.io/changelog
- group: start
  title: ''
  type: Login
  url: https://app.machine0.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fdmtl
- group: commercial
  title: ''
  type: TermsOfService
  url: https://machine0.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://machine0.io/privacy
- group: build
  title: ''
  type: Packages
  url: packages/machine0-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/machine0-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/machine0-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/machine0-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Machine0 is a Y Combinator (S26)-backed infrastructure company, operated by Fundamental Software, that provides persistent, on-demand cloud virtual machines driven entirely from the command line and optimized for AI agents. The machine0 CLI ("Cloud VMs from the CLI") and a remote Model Context Protocol (MCP) server let you create, provision, snapshot, suspend and SSH into dedicated VMs — NixOS or Ubuntu, up to 60 vCPU / 240GB RAM with optional GPUs — across five regions (US East/West, UK, EU, Asia) with static IPs, HTTPS endpoints and per-minute billing. Suspend a VM to freeze its state and stop compute charges. Every CLI command supports JSON output and the MCP server exposes the same machine, image, SSH-key and remote-exec operations to agents.
image: https://machine0.io/opengraph-image?d0b124732c7005de
layout: provider
mcp_servers:
- description: ''
  name: machine0-mcp.yml
  slug: machine0-mcpyml
modified: '2026-07-20'
name: Machine0
nav: Providers
network: true
overview: 'Machine0 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Infrastructure, Virtual Machines, and AI Agents.


  Machine0''s developer surface includes documentation, quickstart, pricing, changelog, CLI, and 11 more developer resources.'
random_paper: 44
scopes:
- name: Machine0 Scopes
  scope_count: 0
  slug: machine0-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.1
  delta: -1.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 51.6
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 32.2
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/machine0/refs/heads/main/screenshots/machine0-2026-07-25T225816.png
security:
- kind: authentication
  name: Machine0 Authentication
  slug: machine0-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Machine0 Domain Security
  slug: machine0-domain-security
  summary_line: TLSv1.3 · HSTS
slug: machine0
tags:
- Company
- Cloud
- Infrastructure
- Virtual Machines
- AI Agents
- Developer Tools
- CLI
- MCP
website: https://machine0.io
---
