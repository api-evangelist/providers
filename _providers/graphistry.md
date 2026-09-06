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
- description: JWT-authenticated REST API on Graphistry Hub for authentication (token obtain/refresh/verify), dataset and file upload, and visualization datasets, powering GPU-accelerated graph rendering and sharing
  name: Graphistry Hub REST API
  slug: graphistry-hub-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.graphistry.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.graphistry.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pygraphistry.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://pygraphistry.readthedocs.io/en/latest/api/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://pygraphistry.readthedocs.io/en/latest/10min.html
- group: start
  title: ''
  type: SignUp
  url: https://www.graphistry.com/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/graphistry
- group: build
  title: ''
  type: Packages
  url: packages/graphistry-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/graphistry-packages.yml
- group: build
  title: ''
  type: CLI
  url: https://github.com/graphistry/graphistry-cli
- group: auth
  title: ''
  type: Authentication
  url: authentication/graphistry-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/graphistry-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/graphistry-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/graphistry-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/graphistry-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/graphistry-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphistry-domain-security.yml
created: '2026-07-17'
description: Graphistry is a GPU-accelerated visual graph analytics platform for exploring, analyzing, and sharing very large graphs and networks directly in the browser. Its open-source PyGraphistry Python client loads, shapes, embeds, and visualizes big graphs from Pandas, Spark, and RAPIDS with end-to-end GPU acceleration, and includes GFQL, a vectorized graph query language. Graphistry Hub is the hosted service exposing a JWT-authenticated REST API for uploading datasets and rendering interactive visualizations, complemented by JavaScript embedding libraries, a CLI for self-hosting, and integrations with Neo4j, Databricks, and RAPIDS. Added to the API Evangelist network from the Bloomberg Beta portfolio.
image: https://github.com/graphistry.png
layout: provider
mcp_servers:
- description: GPU-accelerated graph visualization and analytics for LLMs using Graphistry and MCP. Community-maintained (not a first-party Graphistry product).
  name: Graphistry MCP Server
  slug: graphistry-mcp-server
modified: '2026-07-19'
name: Graphistry
nav: Providers
network: true
overview: 'Graphistry publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Graph Analytics, Graph Visualization, GPU, and Network Analysis.


  Graphistry''s developer surface includes documentation, API reference, getting-started guide, signup flow, CLI, authentication, changelog, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 22.8
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/graphistry/refs/heads/main/screenshots/graphistry-2026-07-25T220239.png
security:
- kind: authentication
  name: Graphistry Authentication
  slug: graphistry-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Graphistry Domain Security
  slug: graphistry-domain-security
  summary_line: TLSv1.3 · DMARC
slug: graphistry
tags:
- Company
- Graph Analytics
- Graph Visualization
- GPU
- Network Analysis
- Data Visualization
- Graph Query
- Machine-Learning
- Cybersecurity
website: https://www.graphistry.com/
---
