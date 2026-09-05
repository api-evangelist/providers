---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: A remote Model Context Protocol server published by Plotly that lets AI agents search and read the Dash documentation directly. Exposes list_pages, search_pages and get_page_as_markdown. Authenticated
  name: Dash Docs MCP Server
  slug: dash-docs-mcp-server
- description: The first-party GraphQL management API for Dash Enterprise, served from each customer's own Dash Enterprise host at /Manager/graphql. Covers app lifecycle, collaborators, environment variables, linked
  name: Dash Enterprise GraphQL API
  slug: dash-enterprise-graphql-api
artifact_total: 10
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/plotly/dds-client/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plotly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plotly.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dash.plotly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dash.plotly.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dash.plotly.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dash.plotly.com/installation
- group: operate
  title: ''
  type: Support
  url: https://dash.plotly.com/support
- group: operate
  title: ''
  type: Community
  url: https://community.plotly.com/
- group: company
  title: ''
  type: Blog
  url: https://plotly.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plotly
- group: commercial
  title: ''
  type: Pricing
  url: https://plotly.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://signin.cloud.plotly.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plotly.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plotly.com/privacy/
- group: auth
  title: ''
  type: Security
  url: https://plotly.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.plotly.com/
- group: auth
  title: ''
  type: Compliance
  url: https://plotly.com/security/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/plotly-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/plotly-mcp.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/plotly-dash-enterprise-graphql.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plotly-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/plotly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/plotly-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/plotly-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/plotly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/plotly-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plotly-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/plotly-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plotly-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plotly-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/plotly-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/plotly-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plotly-error-codes.yml
- group: design
  title: ''
  type: Components
  url: components/plotly-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/plotly-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/plotly-vulnerability-disclosure.yml
created: '2026-08-26'
description: Plotly is a Montreal-based data visualization and analytics company behind the open-source Plotly graphing libraries (plotly.js, plotly.py, Plotly.R, Plotly.NET, plotly.rs, Dash.jl) and the Dash framework for building interactive analytical web applications in Python. Its commercial products are Plotly Studio, an AI-native desktop application that generates Dash data apps from a dataset; Plotly Cloud, the hosted publishing and sharing platform for Dash and Studio apps; and Dash Enterprise, the self-hosted data app platform used by financial services, healthcare and life sciences, energy, and retail organizations. Plotly's machine-readable surfaces are a remote Dash Docs MCP server, an OAuth 2.1/OIDC authorization server for Plotly Cloud, and a first-party GraphQL management API for Dash Enterprise. The legacy Chart Studio Cloud REST API was retired on 2025-10-31.
image: https://plotly.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Plotly MCP Server
  slug: plotly-mcp-server
modified: '2026-08-26'
name: Plotly
nav: Providers
network: true
overview: 'Plotly publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Visualization, Analytics, Data Apps, and Business Intelligence.


  Plotly''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Plotly Plans Pricing
  plan_count: 3
  slug: plotly-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Plotly Rate Limits
  slug: plotly-rate-limits
scopes:
- name: Plotly Scopes
  scope_count: 0
  slug: plotly-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 44.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plotly/refs/heads/main/screenshots/plotly-2026-09-02T151532.png
security:
- kind: authentication
  name: Plotly Authentication
  slug: plotly-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Plotly Domain Security
  slug: plotly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Plotly Vulnerability Disclosure
  slug: plotly-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Plotly Trust Center
  slug: plotly-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 42001
slug: plotly
tags:
- Company
- Data Visualization
- Analytics
- Data Apps
- Business Intelligence
- Open-Source
- Python
- JavaScript
- Charts
- Dashboards
- Developer Tools
- MCP
website: https://plotly.com
---
