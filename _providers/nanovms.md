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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/nanovms/ops/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/nanovms/ops/blob/master/SECURITY.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/nanovms/ops/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://nanovms.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ops.city/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ops.city/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ops.city/ops/getting_started.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nanovms
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/nanovms/ops
- group: company
  title: ''
  type: Blog
  url: https://nanovms.com/blog
- group: operate
  title: ''
  type: Support
  url: https://forums.nanovms.com
- group: build
  title: ''
  type: PackageRepository
  url: https://repo.ops.city/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/nanovms/ops/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nanovms-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/nanovms-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nanovms-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/nanovms-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nanovms-packages.yml
- group: design
  title: ''
  type: Components
  url: components/nanovms-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nanovms-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nanovms-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nanovms-domain-security.yml
created: '2026-07-17'
description: NanoVMs builds unikernel infrastructure that lets developers run a single application as its own lightweight, secure virtual machine with no operating system and no devops. Its open-source toolchain centers on OPS (the ops CLI, ops.city) for building and deploying unikernels to any cloud in seconds, and Nanos (nanos.org), a kernel designed to run one and only one application in a virtualized environment. The project ships editor extensions, a Terraform provider, a Homebrew tap, a package repository (repo.ops.city), and an official MCP server (ops-mcp) for driving the toolchain from AI agents. NanoVMs is a Bloomberg Beta and Initialized Capital portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nanovms.png
layout: provider
mcp_servers:
- description: Official Model Context Protocol server for working with unikernels using the nanos/ops toolchain. Lets an MCP client (e.g. Claude Desktop) list and create unikernel instances and images through the lo
  name: NanoVMs MCP Server
  slug: nanovms-mcp-server
modified: '2026-07-20'
name: NanoVMs
nav: Providers
network: true
overview: 'NanoVMs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Unikernels, Virtualization, Cloud Infrastructure, and DevOps.


  NanoVMs'' developer surface includes documentation, getting-started guide, engineering blog, support, changelog, CLI, and 16 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 85.0
  previous_composite: 26.5
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nanovms/refs/heads/main/screenshots/nanovms-2026-08-07T184622.png
security:
- kind: domain-security
  name: Nanovms Domain Security
  slug: nanovms-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: nanovms
tags:
- Company
- Unikernels
- Virtualization
- Cloud Infrastructure
- DevOps
- Open-Source
- Developer Tools
- CLI
website: https://nanovms.com/
---
