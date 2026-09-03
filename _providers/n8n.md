---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 50
  human_in_the_loop: 3
  name: N8N Agentic Access
  operation_count: 73
  slug: n8n-agentic-access
  summary_line: 73 operations · 50 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: /api/v1
  baseurl_source: spec
  description: Build with the precision of code or the speed of drag-n-drop. Host with on-prem control or in-the-cloud convenience. n8n gives you more freedom to implement multi-step AI agents and integrate apps tha
  name: N8n
  slug: n8n
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about security audit
  name: N8n Audit API
  slug: n8n-audit-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about community packages
  name: N8n CommunityPackage API
  slug: n8n-communitypackage-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about credentials
  name: N8n Credential API
  slug: n8n-credential-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about data tables and their rows
  name: N8n DataTable API
  slug: n8n-datatable-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: API capability discovery
  name: N8n Discover API
  slug: n8n-discover-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about executions
  name: N8n Execution API
  slug: n8n-execution-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about folders
  name: N8n Folders API
  slug: n8n-folders-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about insights
  name: N8n Insights API
  slug: n8n-insights-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about projects
  name: N8n Projects API
  slug: n8n-projects-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about source control
  name: N8n SourceControl API
  slug: n8n-sourcecontrol-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about tags
  name: N8n Tags API
  slug: n8n-tags-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about users
  name: N8n User API
  slug: n8n-user-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about variables
  name: N8n Variables API
  slug: n8n-variables-api
- baseURL: https://app.n8n.cloud/api/v1
  baseurl_source: declared
  description: Operations about workflows
  name: N8n Workflow API
  slug: n8n-workflow-api
artifact_total: 59
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: n8n Public Audit API
  slug: open-n8n-audit-api
- collection_type: open
  name: n8n Public Audit CommunityPackage API
  slug: open-n8n-communitypackage-api
- collection_type: open
  name: n8n Public Audit Credential API
  slug: open-n8n-credential-api
- collection_type: open
  name: n8n Public Audit DataTable API
  slug: open-n8n-datatable-api
- collection_type: open
  name: n8n Public Audit Discover API
  slug: open-n8n-discover-api
- collection_type: open
  name: n8n Public Audit Execution API
  slug: open-n8n-execution-api
- collection_type: open
  name: n8n Public Audit Folders API
  slug: open-n8n-folders-api
- collection_type: open
  name: n8n Public Audit Insights API
  slug: open-n8n-insights-api
- collection_type: open
  name: n8n Public Audit Projects API
  slug: open-n8n-projects-api
- collection_type: open
  name: n8n Public Audit SourceControl API
  slug: open-n8n-sourcecontrol-api
- collection_type: open
  name: n8n Public Audit Tags API
  slug: open-n8n-tags-api
- collection_type: open
  name: n8n Public Audit User API
  slug: open-n8n-user-api
- collection_type: open
  name: n8n Public Audit Variables API
  slug: open-n8n-variables-api
- collection_type: open
  name: n8n Public Audit Workflow API
  slug: open-n8n-workflow-api
- collection_type: open
  name: n8n Public API
  slug: open-n8n
common:
- group: company
  title: ''
  type: Website
  url: https://n8n.io
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/n8n-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/n8n-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/n8n-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/n8n-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/n8n-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/n8n
- group: start
  title: ''
  type: Portal
  url: https://n8n.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.n8n.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.n8n.io/try-it-out/quickstart/
- group: start
  title: ''
  type: Login
  url: https://app.n8n.cloud/login
- group: start
  title: ''
  type: Signup
  url: https://app.n8n.cloud/magic-link
- group: commercial
  title: ''
  type: Pricing
  url: https://n8n.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blog.n8n.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.n8n.io/changelog/release-notes
- group: operate
  title: ''
  type: Community
  url: https://community.n8n.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/n8n-io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://n8n.io/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://n8n.io/legal/
- group: auth
  title: ''
  type: Security
  url: https://n8n.io/legal/security/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/n8n-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/n8n-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/n8n-security.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/n8n-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/n8n-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/n8n-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/n8n-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/n8n-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/n8n-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/n8n-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.n8n.cloud/
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/n8n-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/n8n-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/n8n-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/n8n-cli.yml
- group: design
  title: ''
  type: Components
  url: components/n8n-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/n8n-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/n8n-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/n8n-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/n8n-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/n8n-public-overlay.yaml
- group: auth
  title: ''
  type: Compliance
  url: security/n8n-trust-center.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.n8n.io/connect/n8n-api/api-reference
created: '2025-06-06'
description: n8n is a fair-code workflow automation and iPaaS platform with AI-agent tooling. It exposes an instance-scoped REST API (public OpenAPI 3.0 contract), MCP server/client capabilities via built-in nodes, and an llms.txt documentation index.
features:
- 'Starter €20/mo: 2,500 executions, unlimited users, 1 project'
- 'Pro €50/mo: 10K executions, 3 projects, admin roles, 7-day insights'
- 'Business €667/mo: 40K executions, SSO/SAML/LDAP, git, self-hosted'
- 'Enterprise custom: unlimited projects, 200+ concurrent, 365-day insights'
- 'REST API: 60 req/min/workspace'
- Webhook trigger and concurrent execution scale with tier
- 1,200+ pre-built integrations
- Visual node-based workflow editor
- Code nodes (JavaScript, Python via Pyodide)
- AI Workflow Builder for natural-language workflow creation
- AI Agent nodes (LangChain integration)
- Self-hosted Community Edition (free)
- Self-hosted Enterprise Edition (paid Business+)
- Webhooks (in/out), schedule triggers, manual triggers
- Multi-environment (dev/stage/prod) on Business+
- Git-based version control on Business+
finops:
- name: N8N Finops
  service_category: Workflow Automation
  slug: n8n-finops
graphqls:
- description: n8n does not currently expose a public GraphQL API. The primary programmatic interface is a REST API documented at [https://docs.n8n.io/api/api-reference/](https://docs.n8n.io/api/api-reference/). How
  name: n8n GraphQL Schema
  slug: n8n-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/n8n.png
json_structures:
- name: N8N Structure
  property_count: 0
  slug: n8n-structure
layout: provider
mcp_servers:
- description: 'n8n ships an official instance-level MCP server built into every n8n instance (Cloud and self-hosted, minimum n8n 2.2.0). MCP clients connect over streamable HTTP to build, edit, publish, and execute '
  name: MCP Server
  slug: mcp-server
modified: '2026-09-03'
name: n8n
nav: Providers
network: true
overview: 'n8n publishes 15 APIs on the [APIs.io](https://apis.io/) network, including N8n, Audit API, CommunityPackage API, and 12 more. Tagged areas include Agents, Artificial Intelligence, Integration, Workflows, and Automation.


  n8n''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 37 more developer resources.'
plans:
- name: N8N Plans Pricing
  plan_count: 4
  slug: n8n-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: N8N Rate Limits
  slug: n8n-rate-limits
scopes:
- name: N8N Scopes
  scope_count: 67
  slug: n8n-scopes
  summary_line: 67 scopes
score:
  band: strong
  composite: 62.3
  coverage:
    artifact_dirs: 31
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 12.5
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 58.4
    developer_ergonomics: 85.7
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 55.3
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/n8n/refs/heads/main/screenshots/n8n-2026-06-20T185922.png
security:
- kind: authentication
  name: N8N Authentication
  slug: n8n-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: N8N Domain Security
  slug: n8n-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: N8N Vulnerability Disclosure
  slug: n8n-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: N8N Trust Center
  slug: n8n-trust-center
  summary_line: SOC 2, GDPR
slug: n8n
tags:
- Agents
- Artificial Intelligence
- Integration
- Workflows
- Automation
- Low Code
website: https://n8n.io
---
