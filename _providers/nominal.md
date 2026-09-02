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
    agent_skills: false
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Nominal Core REST API (Conjure-generated) for test data storage, ingest, streaming, compute, and asset/run/checklist management.
  name: Nominal Core API
  slug: nominal-core-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.nominal.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nominal.io/home
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nominal.io/home
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nominal.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nominal.io/python/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nominal-io
- group: company
  title: ''
  type: Blog
  url: https://nominal.io/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.gov.nominal.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nominal.io
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.nominal.io
- group: auth
  title: ''
  type: Compliance
  url: https://trust.nominal.io
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nominal-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nominal-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/nominal-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nominal-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nominal-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nominal-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nominal-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nominal-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nominal-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nominal-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nominal-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nominal-domain-security.yml
created: '2026-07-17'
description: Nominal is the unified software suite for testing and operating advanced hardware — flight systems, satellites, robotics, energy, and other mission-critical engineering programs. Nominal Core is a collaborative workspace that captures, monitors, and analyzes multimodal test data (telemetry, logs, video, and simulation results) across datasets, runs, assets, channels, workbooks, and checklists, while Nominal Connect runs at the edge to read from and write to instruments in real time from Python. Nominal exposes an open Conjure-based REST API at api.gov.nominal.io/api, with first-party SDKs for Python, Rust (and the nom CLI), Go, and LabVIEW, plus a documentation MCP server for AI clients. Backed by Founders Fund, General Catalyst, Lightspeed Venture Partners, and Lux Capital.
image: https://nominal.io/favicon.ico
layout: provider
mcp_servers:
- description: Nominal's hosted documentation MCP server for AI clients (Claude Code, Cursor, etc.). Serves the Nominal docs corpus over MCP so agents can retrieve product, SDK, and API-reference guidance. This is a
  name: Nominal MCP Server
  slug: nominal-mcp-server
modified: '2026-07-20'
name: Nominal
nav: Providers
network: true
overview: 'Nominal publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Deep Tech, Test and Measurement, Hardware, and Aerospace.


  Nominal''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, CLI, authentication, and 16 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 31.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nominal/refs/heads/main/screenshots/nominal-2026-08-07T185449.png
security:
- kind: authentication
  name: Nominal Authentication
  slug: nominal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nominal Domain Security
  slug: nominal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Nominal Trust Center
  slug: nominal-trust-center
  summary_line: SOC 2 Type II, CMMC Level 1, CMMC Level 2 Self-Assessment, NIST 800-171 (SPRS submission)
slug: nominal
tags:
- Company
- Deep Tech
- Test and Measurement
- Hardware
- Aerospace
- Telemetry
- Observability
- Industrial Data
- Data Platform
- SDK
website: https://www.nominal.io
---
