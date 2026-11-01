---
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
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Rent GPU servers via REST API, supports ruble and dollar billing, includes endpoints for catalog, instances, keys, and account management.
  name: gpu.nz API
  slug: gpu-nz-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/gpu-nz/vocabulary/gpu-nz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gpu-nz-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/gpu-nz/cli/gpu-nz-cli.yml
  title: ''
  type: CLI
  url: cli/gpu-nz-cli.yml
- group: design
  href: https://artifacts.apis.io/gpu-nz/conventions/gpu-nz-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/gpu-nz-conventions.yml
- group: design
  href: https://artifacts.apis.io/gpu-nz/conventions/gpu-nz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gpu-nz-conventions.yml
- group: auth
  href: https://artifacts.apis.io/gpu-nz/authentication/gpu-nz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gpu-nz-authentication.yml
- group: design
  href: https://artifacts.apis.io/gpu-nz/conformance/gpu-nz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gpu-nz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gpu-nz/llms/gpu-nz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gpu-nz-llms.txt
- group: agent
  href: https://artifacts.apis.io/gpu-nz/mcp/gpu-nz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gpu-nz-mcp.yml
- group: other
  href: https://artifacts.apis.io/gpu-nz/hosts/gpu-nz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gpu-nz-hosts.yml
- group: start
  title: ''
  type: Sandbox
  url: https://gpu.nz/en/console/keys
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gpu.nz/en/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://gpu.nz/en/pricing
- group: start
  title: ''
  type: Login
  url: https://gpu.nz/en/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gpunz
- group: docs
  title: ''
  type: APIReference
  url: https://gpu.nz/en/docs
- group: auth
  href: https://artifacts.apis.io/gpu-nz/security/gpu-nz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gpu-nz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gpu.nz/en
- group: docs
  title: ''
  type: Documentation
  url: https://gpu.nz/en/docs/api
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://gpu.nz/mcp
  - status: 200
    url: https://gpu.nz/en
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: gpu.nz provides on-demand GPU server rentals and graphics card access via a RESTful API. Users can browse available GPU models, pricing, and regions, then rent servers by the minute for workloads such as AI model training, rendering, and inference. The platform offers a command‑line interface and a streamable MCP endpoint for AI agents, supporting both ruble and dollar billing. Documentation includes quickstart guides, API reference, CLI usage, and integration examples for developers and AI agents.
image: https://gpu.nz/en/og?kind=home
layout: provider
mcp_servers:
- description: Remote MCP server at gpu.nz requiring an API key.
  name: gpu.nz MCP Server
  slug: gpu-nz-mcp-yml
modified: '2026-10-22'
name: gpu.nz
nav: Providers
network: true
overview: 'gpu.nz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, GPU, Rentals, Artificial Intelligence, and Compute.


  gpu.nz''s developer surface includes CLI, authentication, sandbox, pricing, API reference, documentation, and 12 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gpu Nz Authentication
  slug: gpu-nz-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Gpu Nz Domain Security
  slug: gpu-nz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gpu-nz
tags:
- Cloud
- GPU
- Rentals
- Artificial Intelligence
- Compute
website: https://gpu.nz/en
---
