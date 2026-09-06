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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The ImandraX cloud-native automated reasoning engine, exposed as a protobuf-defined gRPC API. Services include Eval (evaluate code snippets, parse terms/types, manage artifacts), Simple (verify, test,
  name: ImandraX API
  slug: imandrax-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.imandra.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.imandra.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.imandra.ai
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/imandra-ai/imandrax-api/tree/main/src/proto
- group: start
  title: ''
  type: GettingStarted
  url: https://codelogician.dev/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://forum.imandra.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/imandra-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://universe.imandra.ai/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://universe.imandra.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://universe.imandra.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.imandra.ai/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.imandra.ai/legal
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/imandra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/imandra-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/imandra-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/imandra-authentication.yml
- group: build
  title: ''
  type: CLI
  url: cli/imandra-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/imandra-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/imandra-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imandra-domain-security.yml
created: '2026-07-17'
description: Imandra Inc. delivers Reasoning as a Service — combining artificial intelligence with formal verification and automated reasoning. Its neurosymbolic platform builds mathematical models of software so that AI systems can understand, verify, and justify code behavior, prove correctness, and uncover hidden bugs. Core products include ImandraX, a cloud-native automated reasoning engine and theorem prover exposed over a protobuf/gRPC API; CodeLogician, an AI coding agent (with CLI and MCP server) that formalizes source code and reasons about it; IPL (Imandra Protocol Language) for modeling financial messaging protocols; and SpecLogician, which converts natural language into formal models. The tools are delivered through the hosted Imandra Universe platform and target financial infrastructure, autonomous workflows, and regulated industries where trustworthy, explainable AI reasoning is critical.
image: https://www.imandra.ai/images/og-image-default.png
layout: provider
mcp_servers:
- description: The CodeLogician MCP server exposes Imandra's CodeLogician Agent and Server workflows as structured tool calls, letting MCP-compatible agents (Claude, Cursor, Gemini, Codex) build formal models of sou
  name: Imandra MCP Server
  slug: imandra-mcp-server
modified: '2026-07-19'
name: Imandra
nav: Providers
network: true
overview: 'Imandra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automated Reasoning, Formal Verification, and Theorem Proving.


  Imandra''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 14 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 33.9
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imandra/refs/heads/main/screenshots/imandra-2026-07-25T222120.png
security:
- kind: authentication
  name: Imandra Authentication
  slug: imandra-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Imandra Domain Security
  slug: imandra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: imandra
tags:
- Company
- Artificial Intelligence
- Automated Reasoning
- Formal Verification
- Theorem Proving
- Developer Tools
- Code Analysis
- Financial-Services
- gRPC
- MCP
website: https://www.imandra.ai
---
