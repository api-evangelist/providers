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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Signadot Agentic Access
  operation_count: 21
  slug: signadot-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.signadot.com/api/v2
  baseurl_source: declared
  description: The Cluster API from Signadot — 5 operation(s) for cluster.
  name: Signadot Cluster API
  slug: signadot-cluster-api
- baseURL: https://api.signadot.com/api/v2
  baseurl_source: declared
  description: The Orgs API from Signadot — 1 operation(s) for orgs.
  name: Signadot Orgs API
  slug: signadot-orgs-api
- baseURL: https://api.signadot.com/api/v2
  baseurl_source: declared
  description: The ResourcePlugins API from Signadot — 2 operation(s) for resourceplugins.
  name: Signadot ResourcePlugins API
  slug: signadot-resourceplugins-api
- baseURL: https://api.signadot.com/api/v2
  baseurl_source: declared
  description: The RouteGroups API from Signadot — 2 operation(s) for routegroups.
  name: Signadot RouteGroups API
  slug: signadot-routegroups-api
- baseURL: https://api.signadot.com/api/v2
  baseurl_source: declared
  description: The Sandboxes API from Signadot — 2 operation(s) for sandboxes.
  name: Signadot Sandboxes API
  slug: signadot-sandboxes-api
arazzos:
- description: Create a sandbox, poll it until ready to read its preview endpoints, then delete it.
  name: Create and inspect a Signadot sandbox
  slug: signadot-create-and-inspect-sandbox
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Signadot Cluster API
  slug: open-signadot-cluster-api
- collection_type: open
  name: Signadot Cluster Orgs API
  slug: open-signadot-orgs-api
- collection_type: open
  name: Signadot Cluster ResourcePlugins API
  slug: open-signadot-resourceplugins-api
- collection_type: open
  name: Signadot Cluster RouteGroups API
  slug: open-signadot-routegroups-api
- collection_type: open
  name: Signadot Cluster Sandboxes API
  slug: open-signadot-sandboxes-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/signadot-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.signadot.com/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://www.signadot.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://www.signadot.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.signadot.com/docs/getting-started/installation
- group: operate
  title: ''
  type: Support
  url: https://signadotcommunity.slack.com
- group: company
  title: ''
  type: Blog
  url: https://www.signadot.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signadot
- group: commercial
  title: ''
  type: Pricing
  url: https://www.signadot.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.signadot.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.signadot.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.signadot.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.signadot.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/signadot-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/signadot-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/signadot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/signadot-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/signadot-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/signadot-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/signadot-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/signadot-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/signadot-conformance.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/signadot-create-and-inspect-sandbox.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/signadot-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/signadot-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signadot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://signadot.com/
created: '2026-07-17'
description: 'Signadot is a Kubernetes-native platform for validating microservices and AI-generated code changes against real dependencies before merge. Its core is environment virtualization: large numbers of lightweight ephemeral "sandboxes" spin up in seconds by routing request-level traffic to only the changed services on a shared cluster, without duplicating the whole stack. Testing capabilities — Jobs (Playwright/Cypress/k6 runners), Smart Tests (AI regression detection), and Plans (reusable validation workflows) — layer on top, and a bundled MCP server plus installable Agent Skills let coding agents (Cursor, Claude Code, Codex) provision environments and validate their own work. Signadot installs as a Kubernetes operator, integrates with service meshes and CI/CD, and exposes a REST control-plane API, a CLI, and a Go SDK.'
image: https://www.signadot.com/images/og-image.png
layout: provider
mcp_servers:
- description: 'Signadot''s Model Context Protocol server, bundled with the Signadot CLI. Exposes control-plane operations as MCP tools so MCP-compatible coding agents (Cursor, Claude Code, VS Code, Codex) can create '
  name: Signadot MCP Server
  slug: signadot-mcp-server
modified: '2026-07-21'
name: Signadot
nav: Providers
network: true
overview: 'Signadot publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cluster API, Orgs API, ResourcePlugins API, and 2 more. Tagged areas include Company, Developer Tools, Kubernetes, Testing, and Ephemeral Environments.


  Signadot''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 56.5
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/signadot/refs/heads/main/screenshots/signadot-2026-08-17T081851.png
security:
- kind: authentication
  name: Signadot Authentication
  slug: signadot-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Signadot Domain Security
  slug: signadot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: signadot
tags:
- Company
- Developer Tools
- Kubernetes
- Testing
- Ephemeral Environments
- Microservices
- Preview Environments
- Agentic Development
- Continuous Integration
- Developer Experience
website: https://signadot.com/
---
