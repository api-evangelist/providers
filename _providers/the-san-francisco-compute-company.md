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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 31
  human_in_the_loop: 2
  name: The San Francisco Compute Company Agentic Access
  operation_count: 65
  slug: the-san-francisco-compute-company-agentic-access
  summary_line: 65 operations · 31 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: The authenticated account and logged-in user.
  name: The San Francisco Compute Company Account API
  slug: the-san-francisco-compute-company-account-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: Deployment automations that maintain a fleet of instances, including spot deployments that buy capacity up to a maximum price.
  name: The San Francisco Compute Company Deployments API
  slug: the-san-francisco-compute-company-deployments-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: The Feature Flags API from The San Francisco Compute Company — 2 operation(s) for feature flags.
  name: The San Francisco Compute Company Feature Flags API
  slug: the-san-francisco-compute-company-feature-flags-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: Custom machine images for instances.
  name: The San Francisco Compute Company Images API
  slug: the-san-francisco-compute-company-images-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: Browse available instance SKU property definitions.
  name: The San Francisco Compute Company Instance SKU Catalog API
  slug: the-san-francisco-compute-company-instance-sku-catalog-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: The Instance SKUs API from The San Francisco Compute Company — 4 operation(s) for instance skus.
  name: The San Francisco Compute Company Instance SKUs API
  slug: the-san-francisco-compute-company-instance-skus-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: Reusable instance configuration.
  name: The San Francisco Compute Company Instance Templates API
  slug: the-san-francisco-compute-company-instance-templates-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: Spin up instances in a capacity to use your available compute.
  name: The San Francisco Compute Company Instances API
  slug: the-san-francisco-compute-company-instances-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: 'Read-only orderbook visibility: bid/ask spread, depth, open and filled orders, and historical fills, keyed on hardware requirements + delivery window.'
  name: The San Francisco Compute Company Orderbook API
  slug: the-san-francisco-compute-company-orderbook-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: 'Estimate an order before placing it: filled price, fee, and operational notices.'
  name: The San Francisco Compute Company Orders API
  slug: the-san-francisco-compute-company-orders-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: A bucket of owned compute balance over time.
  name: The San Francisco Compute Company Pools API
  slug: the-san-francisco-compute-company-pools-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: Market automations that maintain capacity by placing buy/sell orders.
  name: The San Francisco Compute Company Procurements API
  slug: the-san-francisco-compute-company-procurements-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: Read-only access to users within the caller's organization.
  name: The San Francisco Compute Company Users API
  slug: the-san-francisco-compute-company-users-api
- baseURL: https://api.sfcompute.com/preview/v2
  baseurl_source: declared
  description: Resource containers scoped to an account.
  name: The San Francisco Compute Company Workspaces API
  slug: the-san-francisco-compute-company-workspaces-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: sfc-api Account API
  slug: open-the-san-francisco-compute-company-account-api
- collection_type: open
  name: sfc-api Account Deployments API
  slug: open-the-san-francisco-compute-company-deployments-api
- collection_type: open
  name: sfc-api Account Feature Flags API
  slug: open-the-san-francisco-compute-company-feature-flags-api
- collection_type: open
  name: sfc-api Account Images API
  slug: open-the-san-francisco-compute-company-images-api
- collection_type: open
  name: sfc-api Account Instance SKU Catalog API
  slug: open-the-san-francisco-compute-company-instance-sku-catalog-api
- collection_type: open
  name: sfc-api Account Instance SKUs API
  slug: open-the-san-francisco-compute-company-instance-skus-api
- collection_type: open
  name: sfc-api Account Instance Templates API
  slug: open-the-san-francisco-compute-company-instance-templates-api
- collection_type: open
  name: sfc-api Account Instances API
  slug: open-the-san-francisco-compute-company-instances-api
- collection_type: open
  name: sfc-api Account Orderbook API
  slug: open-the-san-francisco-compute-company-orderbook-api
- collection_type: open
  name: sfc-api Account Orders API
  slug: open-the-san-francisco-compute-company-orders-api
- collection_type: open
  name: sfc-api Account Pools API
  slug: open-the-san-francisco-compute-company-pools-api
- collection_type: open
  name: sfc-api Account Procurements API
  slug: open-the-san-francisco-compute-company-procurements-api
- collection_type: open
  name: sfc-api Account Users API
  slug: open-the-san-francisco-compute-company-users-api
- collection_type: open
  name: sfc-api Account Workspaces API
  slug: open-the-san-francisco-compute-company-workspaces-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/the-san-francisco-compute-company-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sfcompute.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sfcompute.com/preview/using-the-api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sfcompute.com/preview/api-reference/account/get-the-authenticated-account-and-logged-in-user
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sfcompute.com/preview/quick-start
- group: company
  title: ''
  type: Blog
  url: https://sfcompute.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://sfcompute.com/changelog
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.sfcompute.com/preview/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sfcompute
- group: operate
  title: ''
  type: Support
  url: mailto:support@sfcompute.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sfcompute.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://sfcompute.com/prices
- group: start
  title: ''
  type: SignUp
  url: https://sfcompute.com/auth/sign-up
- group: start
  title: ''
  type: Login
  url: https://sfcompute.com/auth/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sfcompute.com/legal
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sfcompute.com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sfcompute
- group: build
  title: ''
  type: Packages
  url: packages/the-san-francisco-compute-company-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/the-san-francisco-compute-company-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/the-san-francisco-compute-company-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/the-san-francisco-compute-company-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-san-francisco-compute-company-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-san-francisco-compute-company-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-san-francisco-compute-company-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-san-francisco-compute-company-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/the-san-francisco-compute-company-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/the-san-francisco-compute-company-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/the-san-francisco-compute-company-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.sfcompute.com/preview/roadmap
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/the-san-francisco-compute-company-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/the-san-francisco-compute-company-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-san-francisco-compute-company-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/the-san-francisco-compute-company-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-san-francisco-compute-company-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/the-san-francisco-compute-company-sf-cli.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-san-francisco-compute-company-agentic-access.yml
created: '2026-07-17'
description: The San Francisco Compute Company (SF Compute) runs large-scale, vetted GPU clusters and operates a compute marketplace where buyers reserve H100/H200 capacity by the hour and sellers resell unused compute back into the market with no long-term lock-in. Its public preview REST API (api.sfcompute.com, base path /preview/v2) and the `sf` CLI let developers buy and sell compute via orders and an orderbook, manage pools of reserved balance, launch and operate GPU instances from images and templates, run procurements and deployments, and organize resources across workspaces with roles, grants, and tags. Authentication is a Bearer token (sk_live_ API key). The API is documented on a Mintlify docs site with a per-operation OpenAPI reference, an llms.txt index, and an official agent skill.
image: https://sfcompute.com/icon.svg
layout: provider
mcp_servers:
- description: SF Compute publishes a hosted MCP server for its documentation (served by the Mintlify docs platform). It exposes documentation search to MCP-capable agents. There is no first-party MCP server for the
  name: The San Francisco Compute Company MCP Server
  slug: the-san-francisco-compute-company-mcp-server
modified: '2026-07-21'
name: The San Francisco Compute Company
nav: Providers
network: true
overview: 'The San Francisco Compute Company publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Account API, Deployments API, Feature Flags API, and 11 more. Tagged areas include Company, GPU, Compute, Cloud Infrastructure, and Artificial Intelligence.


  The San Francisco Compute Company''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, support, pricing, and 29 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 60.0
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 14
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-san-francisco-compute-company/refs/heads/main/screenshots/the-san-francisco-compute-company-2026-08-17T082343.png
security:
- kind: authentication
  name: The San Francisco Compute Company Authentication
  slug: the-san-francisco-compute-company-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: The San Francisco Compute Company Domain Security
  slug: the-san-francisco-compute-company-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-san-francisco-compute-company
tags:
- Company
- GPU
- Compute
- Cloud Infrastructure
- Artificial Intelligence
- Machine-Learning
- Compute Marketplace
- Reselling
- Infrastructure
website: https://docs.sfcompute.com
---
