---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 74.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 81
  human_in_the_loop: 0
  name: Doit Agentic Access
  operation_count: 166
  slug: doit-agentic-access
  summary_line: 166 operations · 81 acting
api_count: 2
apis:
- description: 'Programmatic access to the DoiT Cloud Intelligence platform: Cloud Analytics reports and queries, allocations, dimensions, budgets, alerts, annotations, labels, anomalies, invoices, assets, contracts,'
  name: DoiT API
  slug: doit-api
- description: Official DoiT Model Context Protocol server. A remote Streamable HTTP endpoint at https://mcp.doit.com/mcp authenticated with OAuth 2.0 against console.doit.com, plus a local stdio server published to
  name: DoiT MCP Server
  slug: doit-mcp-server
artifact_total: 12
asyncapis:
- description: ''
  name: Doit Events
  slug: doit-events
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doit-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/doit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/doit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.doit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.doit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.doit.com/docs/start
- group: docs
  title: ''
  type: APIReference
  url: https://developer.doit.com/reference/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.doit.com/docs/start
- group: operate
  title: ''
  type: Support
  url: https://help.doit.com/
- group: company
  title: ''
  type: Blog
  url: https://www.doit.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.doit.com/blog/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doitintl
- group: commercial
  title: ''
  type: Pricing
  url: https://www.doit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.doit.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doit.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.doit.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.doit.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.doit.com/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doit-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/doit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/doit-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/doit-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/doit-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/doit-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/doit-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/doit-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.doit.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/doit-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/doit-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.doit.com/docs/availability-matrix
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/doit-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doit-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://help.doit.com/docs/vendor-information/bug-bounty-program
- group: design
  title: ''
  type: Conventions
  url: conventions/doit-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/doit-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/doit-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/doit-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/doit-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/doit-events.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/doit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doit-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/doit-mcp-setup.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/doit-mcp-reporting.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/doit-mcp-anomaly-investigation.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/doit-mcp-api.md
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/doitintl
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/doit-openapi-original.yml
- group: operate
  title: ''
  type: ChangeLogRSS
  url: https://developer.doit.com/changelog.rss
created: '2026-08-12'
description: DoiT International is a cloud and FinOps technology company behind DoiT Cloud Intelligence, an intent-aware FinOps platform that unifies cost, usage and savings data across AWS, Google Cloud, Azure, Kubernetes and 40+ other clouds and SaaS providers. The DoiT Platform API at api.doit.com gives programmatic access to Cloud Analytics reports, allocations, budgets, alerts, anomalies, invoices, assets, DataHub ingestion, CloudFlow automation, cloud incidents, support requests, insights and its Ava AI assistant, published as a single OpenAPI 3.0.1 contract. DoiT also ships an official remote MCP server at mcp.doit.com, a generated dci CLI, a Terraform provider, a Grafana plugin, and an open-source Agent Skills plugin for agentic FinOps workflows.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: DoiT MCP Server
  slug: doit-mcp-server
modified: '2026-08-12'
name: DoiT
nav: Providers
network: true
overview: 'DoiT publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinOps, Cloud Cost Management, Cloud Intelligence, and Cost Optimization.


  The DoiT catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DoiT''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 44 more developer resources.'
plans:
- name: Doit Plans Pricing
  plan_count: 6
  slug: doit-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Doit Rate Limits
  slug: doit-rate-limits
scopes:
- name: Doit Scopes
  scope_count: 4
  slug: doit-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 65.1
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 69.0
    developer_ergonomics: 64.3
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 69.7
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doit/refs/heads/main/screenshots/doit-2026-08-17T080051.png
security:
- kind: authentication
  name: Doit Authentication
  slug: doit-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Doit Domain Security
  slug: doit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Doit Vulnerability Disclosure
  slug: doit-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Doit Trust Center
  slug: doit-trust-center
  summary_line: SOC 2 Type 2, SOC 3, ISO 27001, ISO 27001:2022, GDPR, CCPA, ICO registered, EU-US Data Privacy Framework
slug: doit
tags:
- Company
- FinOps
- Cloud Cost Management
- Cloud Intelligence
- Cost Optimization
- Multi-Cloud
- Kubernetes
- Analytics
- MCP
- Artificial Intelligence
website: https://www.doit.com/
---
