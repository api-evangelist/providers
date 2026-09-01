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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Token-authenticated REST API over data.thinknum.com for querying Thinknum's alternative datasets. Endpoints cover dataset query (filter/group/sort/ function), historical daily and monthly feeds, compa
  name: Thinknum Data API
  slug: thinknum-data-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://thinknum.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.thinknum.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thinknum.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thinknum.com/docs/query-api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thinknum.com/docs/getting-started.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/thinknum-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.thinknum.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.thinknum.com/status
- group: operate
  title: ''
  type: Support
  url: mailto:support@thinknum.com
- group: start
  title: ''
  type: Login
  url: https://www.thinknum.com/creator/account/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thinknum.com/tos
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thinknum
- group: build
  title: ''
  type: Packages
  url: packages/thinknum-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/thinknum-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thinknum-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/thinknum-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thinknum-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thinknum-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thinknum-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/thinknum-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/thinknum-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/thinknum-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thinknum-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thinknum-domain-security.yml
created: '2026-07-17'
description: Thinknum is an alternative data platform that collects and structures web-sourced datasets to power investment and business intelligence. It tracks metrics such as job listings, store locations, product pricing, web traffic, app reviews, and social engagement across hundreds of thousands of companies, keyed by exchange ticker. The Thinknum Data API (data.thinknum.com) exposes these datasets over a token-authenticated REST interface with Query, Historical, Company, and Upload endpoints, plus embeddable widgets and an official Python client. Backed by 500 Global.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thinknum.png
layout: provider
mcp_servers:
- description: Candidate MCP tool surface derived from the published Thinknum Data API operations. Not an official Thinknum MCP server — a starting point for wrapping the token-authenticated REST API as MCP tools.
  name: Thinknum MCP Server
  slug: thinknum-mcp-server
modified: '2026-07-21'
name: Thinknum
nav: Providers
network: true
overview: 'Thinknum publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Alternative Data, Financial Data, Investment Research, and Market Intelligence.


  Thinknum''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, changelog, and 17 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Thinknum Rate Limits
  slug: thinknum-rate-limits
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 12
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 27.2
  provenance:
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Thinknum Authentication
  slug: thinknum-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Thinknum Domain Security
  slug: thinknum-domain-security
  summary_line: TLSv1.3
slug: thinknum
tags:
- Company
- Alternative Data
- Financial Data
- Investment Research
- Market Intelligence
- Web Data
- Datasets
website: https://thinknum.com
---
