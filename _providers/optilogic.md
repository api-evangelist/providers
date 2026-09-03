---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.7
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Optilogic operates a hosted, remote Model Context Protocol server that backs the Ada connector for Claude. An MCP client points at https://mcp.optilogic.app/mcp and authenticates over OAuth 2.1 agains
  name: Optilogic MCP Server (Ada Connector)
  slug: optilogic-mcp-server-ada-connector
- baseURL: https://api.optilogic.app/v0
  baseurl_source: declared
  description: Get authentication keys and client credentials
  name: Optilogic Authentication API
  slug: optilogic-authentication-api
- baseURL: https://api.optilogic.app/v0
  baseurl_source: declared
  description: Get information about Andromeda jobs
  name: Optilogic Job API
  slug: optilogic-job-api
- baseURL: https://api.optilogic.app/v0
  baseurl_source: declared
  description: Get storage information
  name: Optilogic Storage API
  slug: optilogic-storage-api
- baseURL: https://api.optilogic.app/v0
  baseurl_source: declared
  description: Manage database custom columns
  name: 'Optilogic storage : custom columns API'
  slug: optilogic-storage-custom-columns-api
- baseURL: https://api.optilogic.app/v0
  baseurl_source: declared
  description: Manage database custom tables
  name: 'Optilogic storage : custom tables API'
  slug: optilogic-storage-custom-tables-api
- baseURL: https://api.optilogic.app/v0
  baseurl_source: declared
  description: Manage custom key/value attributes on a storage record
  name: 'Optilogic storage : labels API'
  slug: optilogic-storage-labels-api
- baseURL: https://api.optilogic.app/v0
  baseurl_source: declared
  description: Share, send, and clone databases
  name: 'Optilogic storage : sharing API'
  slug: optilogic-storage-sharing-api
- baseURL: https://api.optilogic.app/v0
  baseurl_source: declared
  description: Manage custom tags on a storage record
  name: 'Optilogic storage : tags API'
  slug: optilogic-storage-tags-api
- baseURL: https://api.optilogic.app/v0
  baseurl_source: declared
  description: Get database template information
  name: 'Optilogic storage : templates API'
  slug: optilogic-storage-templates-api
- baseURL: https://api.optilogic.app/v0
  baseurl_source: declared
  description: A library of tools that solve specific problems
  name: Optilogic Utility API
  slug: optilogic-utility-api
- baseURL: https://api.optilogic.app/v0
  baseurl_source: declared
  description: Get information about a workspace, including job and file information
  name: Optilogic Workspace API
  slug: optilogic-workspace-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/optilogic-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optilogic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://optilogic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.optilogic.app/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.optilogic.app/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.optilogic.app/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://optilogic.com/help-center/connecting-via-api
- group: operate
  title: ''
  type: Support
  url: https://optilogic.com/help-center/
- group: operate
  title: ''
  type: HelpCenter
  url: https://optilogic.com/help-center/
- group: company
  title: ''
  type: Blog
  url: https://optilogic.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/optilogic
- group: start
  title: ''
  type: SignUp
  url: https://www.optilogic.com/create-an-account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://optilogic.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://optilogic.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://optilogic.com/resources/latest-updates
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/optilogic-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/optilogic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/optilogic-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/optilogic-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/optilogic-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/optilogic-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/optilogic-rest-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/optilogic-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/optilogic-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/optilogic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/optilogic-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/optilogic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/optilogic-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/optilogic-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/optilogic-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/optilogic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/optilogic-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/optilogic-rest-api-openapi.json
created: '2026-08-26'
description: Optilogic is a cloud-native supply chain design company headquartered in Ann Arbor, Michigan, whose Cosmic Frog platform lets teams model, optimize, simulate and risk-score supply chain networks in one environment, alongside DataStar for AI-assisted data preparation, Ada agentic AI, the Lumina Tariff Optimizer and the Atlas Python coding workspace. Its developer surface is the Optilogic REST API (Swagger 2.0, 67 operations across authentication, workspace, job, storage and utility) served from api.optilogic.app/v0 with X-API-KEY authentication, an OptiPy Python client and an OptiJS browser client, plus an OAuth-protected remote MCP server at mcp.optilogic.app/mcp that powers the Ada connector for Claude.
image: https://cdn.prod.website-files.com/682c88de65bdb86ec53f8277/687fd1599d7415ecd00e4908_Optilogic_logo_2025.svg
layout: provider
mcp_servers:
- description: ''
  name: Optilogic MCP Server (Ada Connector)
  slug: optilogic-mcp-server-ada-connector
modified: '2026-08-26'
name: Optilogic
nav: Providers
network: true
overview: 'Optilogic publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Job API, Storage API, and 8 more. Tagged areas include Supply Chain, Supply Chain Design, Network Optimization, Simulation, and Optimization.


  Optilogic''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 27 more developer resources.'
plans:
- name: Optilogic Plans Pricing
  plan_count: 0
  slug: optilogic-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Optilogic Rate Limits
  slug: optilogic-rate-limits
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 49.2
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 47.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optilogic/refs/heads/main/screenshots/optilogic-2026-09-02T150852.png
security:
- kind: authentication
  name: Optilogic Authentication
  slug: optilogic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Optilogic Domain Security
  slug: optilogic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Optilogic Trust Center
  slug: optilogic-trust-center
  summary_line: SOC 2 Type II, CMMC Level 1
slug: optilogic
tags:
- Supply Chain
- Supply Chain Design
- Network Optimization
- Simulation
- Optimization
- Logistics
- Analytics
- Artificial Intelligence
- Job
- Cloud
website: https://optilogic.com/
---
