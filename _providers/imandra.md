---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The ImandraX cloud-native automated reasoning engine, exposed as a protobuf-defined gRPC API. Services include Eval (evaluate code snippets, parse terms/types, manage artifacts), Simple (verify, test,
  name: ImandraX API
  slug: imandrax-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/imandra/plans/imandra-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/imandra-plans-pricing.yml
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
  href: https://artifacts.apis.io/imandra/grpc/_index.yml
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: build
  href: https://artifacts.apis.io/imandra/packages/imandra-packages.yml
  title: ''
  type: Packages
  url: packages/imandra-packages.yml
- group: build
  href: https://artifacts.apis.io/imandra/packages/imandra-packages.yml
  title: ''
  type: SDKs
  url: packages/imandra-packages.yml
- group: agent
  href: https://artifacts.apis.io/imandra/mcp/imandra-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/imandra-mcp.yml
- group: auth
  href: https://artifacts.apis.io/imandra/authentication/imandra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/imandra-authentication.yml
- group: build
  href: https://artifacts.apis.io/imandra/cli/imandra-cli.yml
  title: ''
  type: CLI
  url: cli/imandra-cli.yml
- group: design
  href: https://artifacts.apis.io/imandra/conventions/imandra-conventions.yml
  title: ''
  type: Conventions
  url: conventions/imandra-conventions.yml
- group: agent
  href: https://artifacts.apis.io/imandra/llms/imandra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/imandra-llms.txt
- group: auth
  href: https://artifacts.apis.io/imandra/security/imandra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/imandra-domain-security.yml
created: '2026-07-17'
description: Imandra Inc. delivers Reasoning as a Service — combining artificial intelligence with formal verification and automated reasoning. Its neurosymbolic platform builds mathematical models of software so that AI systems can understand, verify, and justify code behavior, prove correctness, and uncover hidden bugs. Core products include ImandraX, a cloud-native automated reasoning engine and theorem prover exposed over a protobuf/gRPC API; CodeLogician, an AI coding agent (with CLI and MCP server) that formalizes source code and reasons about it; IPL (Imandra Protocol Language) for modeling financial messaging protocols; and SpecLogician, which converts natural language into formal models. The tools are delivered through the hosted Imandra Universe platform and target financial infrastructure, autonomous workflows, and regulated industries where trustworthy, explainable AI reasoning is critical.
finops:
- has_sources: true
  method: derived
  name: Imandra Finops
  primary_unit: subscription
  service_category: ''
  slug: imandra-finops
  template: false
image: https://www.imandra.ai/images/og-image-default.png
layout: provider
mcp_servers:
- description: The CodeLogician MCP server exposes Imandra's CodeLogician Agent and Server workflows as structured tool calls, letting MCP-compatible agents (Claude, Cursor, Gemini, Codex) build formal models of sou
  name: Imandra MCP Server
  slug: code-logician
modified: '2026-07-19'
name: Imandra
nav: Providers
network: true
overview: 'Imandra is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automated Reasoning, Formal Verification, and Theorem Proving.


  Imandra''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 15 more developer resources.'
plans:
- name: Imandra Plans Pricing
  plan_count: 3
  slug: imandra-plans-pricing
- name: Imandra Price Estimates
  plan_count: 0
  slug: imandra-price-estimates
random_paper: 12
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 67.1
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 69.0
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 41.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/imandra/imandra-2026-07-25T222120.png
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
- Financial Services
- gRPC
- MCP
website: https://www.imandra.ai
---
