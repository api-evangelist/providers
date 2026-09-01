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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Expanso Agentic Access
  operation_count: 20
  slug: expanso-agentic-access
  summary_line: 20 operations · 5 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Ops API from Expanso — 6 operation(s) for ops.
  name: Expanso Ops API
  slug: expanso-ops-api
- description: The Orchestrator API from Expanso — 11 operation(s) for orchestrator.
  name: Expanso Orchestrator API
  slug: expanso-orchestrator-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bacalhau Ops API
  slug: open-expanso-ops-api
- collection_type: open
  name: Bacalhau Ops Orchestrator API
  slug: open-expanso-orchestrator-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/bacalhau-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.expanso.io
- group: docs
  title: ''
  type: Documentation
  url: https://bacalhau.org/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://bacalhau.org/docs/cli-api/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.expanso.io/getting-started/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://expanso.io/blog/
- group: operate
  title: ''
  type: Support
  url: https://expanso.io/help-center/
- group: operate
  title: ''
  type: HelpCenter
  url: https://expanso.io/help-center/
- group: commercial
  title: ''
  type: Pricing
  url: https://expanso.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://cloud.expanso.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://expanso.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://expanso.io/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bacalhau-project
- group: operate
  title: ''
  type: StatusPage
  url: https://status.expanso.io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/expanso-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/expanso-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/expanso-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/expanso-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/expanso-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/expanso-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/expanso-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/expanso-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/expanso-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Expanso is the company behind Bacalhau, an open-source distributed compute orchestration framework that brings compute to the data by running jobs close to where data is generated across edge, on-premise, and cloud environments. Expanso Cloud is the managed platform for deploying intelligent data pipelines at the edge - filtering, transforming, and governing data (PII/GDPR compliance, lineage) before it reaches downstream platforms like Snowflake and Databricks. The Bacalhau Orchestrator API exposes job submission, execution history, results, log streaming, and node/agent management over a versioned REST interface. Expanso is backed by General Catalyst and was named Edge AI Startup of the Year 2026.
image: https://expanso.io/favicon.ico
layout: provider
mcp_servers:
- description: 'Candidate MCP tool surface derived one-per-operation from the Bacalhau Orchestrator API OpenAPI. No official hosted Expanso/Bacalhau MCP server was located at time of enrichment; this is a governance '
  name: Expanso MCP Server
  slug: expanso-mcp-server
modified: '2026-07-19'
name: Expanso
nav: Providers
network: true
overview: 'Expanso publishes 2 APIs on the [APIs.io](https://apis.io/) network: Ops API and Orchestrator API. Tagged areas include Company, Distributed Computing, Edge Computing, Compute Orchestration, and Data Pipeline.


  Expanso''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 17 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 37.8
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/expanso/refs/heads/main/screenshots/expanso-2026-07-25T213913.png
security:
- kind: domain-security
  name: Expanso Domain Security
  slug: expanso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: expanso
tags:
- Company
- Distributed Computing
- Edge Computing
- Compute Orchestration
- Data Pipeline
- Data Governance
- Open-Source
- Artificial Intelligence
- Job Orchestration
website: https://docs.expanso.io
---
