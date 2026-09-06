---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The developer interfaces to the HEAVY.AI platform: native SQL against the GPU-accelerated HeavyDB engine, an Apache Thrift API, JDBC/ODBC drivers, the heavysql CLI console, a Python client (heavyai) a'
  name: HEAVY.AI Platform APIs
  slug: heavyai-platform-apis
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.heavy.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nvidia.com/heavyai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nvidia.com/heavyai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nvidia.com/heavyai/apis-and-interfaces
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nvidia.com/heavyai/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heavyai
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.nvidia.com/heavyai/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/heavyai-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/heavyai-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/heavyai-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/heavyai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/heavyai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/heavyai-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/heavyai-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/heavyai-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/heavyai-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heavyai-domain-security.yml
created: '2026-07-17'
description: HEAVY.AI is a GPU-accelerated analytics platform (formerly OmniSci / MapD, now part of NVIDIA) built to interactively query and visualize very large, often geospatial and time-series, datasets. It pairs an open-source, GPU-accelerated SQL database (HeavyDB) with a server-side rendering engine (HeavyRender) and a web-based visual analytics application (Heavy Immerse). Developers interact with the platform through native SQL, an Apache Thrift API, JDBC/ODBC drivers, the heavysql command-line console, a Python data-science client (heavyai) and a JavaScript connector (@heavyai/connector), plus a Vega-based rendering API. The documentation is published on the NVIDIA docs site and exposes an llms.txt index and a hosted MCP server for AI agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heavyai.png
layout: provider
mcp_servers:
- description: ''
  name: HEAVY.AI MCP Server
  slug: heavyai-mcp-server
modified: '2026-07-19'
name: HEAVY.AI
nav: Providers
network: true
overview: 'HEAVY.AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Analytics, Database, and GPU.


  HEAVY.AI''s developer surface includes documentation, API reference, getting-started guide, changelog, CLI, authentication, and 11 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 21.9
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heavyai/refs/heads/main/screenshots/heavyai-2026-07-25T220902.png
security:
- kind: authentication
  name: Heavyai Authentication
  slug: heavyai-authentication
  summary_line: username-password/tls · 2 schemes
- kind: domain-security
  name: Heavyai Domain Security
  slug: heavyai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: heavyai
tags:
- Company
- Artificial Intelligence
- Analytics
- Database
- GPU
- SQL
- Geospatial
- Data Visualization
- Data Science
- Business Intelligence
website: https://www.heavy.ai
---
