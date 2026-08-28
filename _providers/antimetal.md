---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
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
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Antimetal Agentic Access
  operation_count: 9
  slug: antimetal-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 5
apis:
- description: Remote Model Context Protocol server exposing Antimetal's investigation, root-cause analysis and remediation capabilities to MCP-compatible clients such as Claude Code, Cursor, VS Code, Windsurf and C
  name: Antimetal MCP Server
  slug: antimetal-mcp-server
- description: Public protobuf/Connect definitions for the Antimetal system agent — the component that connects customer infrastructure to the Antimetal platform. Covers agent config and instance, hardware and Linux
  name: Antimetal Agent APIs (Protobuf)
  slug: antimetal-agent-apis
- description: The Artifacts API from Antimetal — 1 operation(s) for artifacts.
  name: Antimetal Artifacts API
  slug: antimetal-artifacts-api
- description: The Issues API from Antimetal — 4 operation(s) for issues.
  name: Antimetal Issues API
  slug: antimetal-issues-api
- description: The Query API from Antimetal — 1 operation(s) for query.
  name: Antimetal Query API
  slug: antimetal-query-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Antimetal External Artifacts API
  slug: open-antimetal-artifacts-api
- collection_type: open
  name: Antimetal External Issues API
  slug: open-antimetal-issues-api
- collection_type: open
  name: Antimetal External Query API
  slug: open-antimetal-query-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/antimetal-external-api-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/antimetal/apis/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/antimetal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/antimetal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/antimetal-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.antimetal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.antimetal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.antimetal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.antimetal.com/api-reference/issues/fetch-issues-for-an-organization
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.antimetal.com/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://overlook.antimetal.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@antimetal.com
- group: company
  title: ''
  type: Blog
  url: https://antimetal.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/antimetal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://antimetal.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://antimetal.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.antimetal.com/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.antimetal.com/admin/security
- group: auth
  title: ''
  type: Security
  url: https://docs.antimetal.com/admin/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/antimetal-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/antimetal-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/antimetal-api-catalog.json
- group: other
  title: ''
  type: AgentCard
  url: a2a/antimetal-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/antimetal-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/antimetal-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/antimetal-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/antimetal-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/antimetal-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/antimetal-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/antimetal-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/antimetal-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/antimetal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/antimetal-trust-center.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/antimetal-scopes.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/antimetal
created: '2026-08-06'
description: Antimetal is a New York based software company building an autonomous production-management platform for engineering teams — "everything that happens after you deploy". It maintains a continuously updated world model of a customer's production stack and runs specialized AI agents that patrol for risk and drift, triage noisy signals into structured issues, investigate incidents down to a root cause, and generate production-ready fixes tied back to the underlying evidence. It connects to more than ninety cloud, observability, CI/CD, incident and code tools — AWS, Google Cloud, Azure, Kubernetes, Datadog, Grafana, Prometheus, Sentry, Splunk, New Relic, Honeycomb, PagerDuty, incident.io, GitHub, Vercel and Slack among them. Antimetal publishes a public REST API (the Antimetal External API, at bff.antimetal.com/api/v2) covering issues, investigation results, evidential artifacts and a natural-language query endpoint, a remote MCP server at mcp.antimetal.com with OAuth 2.1 and API-key
  auth, an official TypeScript SDK, published Agent Skills for Claude Code and Cursor, open protobuf definitions for its infrastructure agent, and a Terraform provider and Helm charts.
image: https://avatars.githubusercontent.com/antimetal
layout: provider
mcp_servers:
- description: ''
  name: Antimetal MCP Server
  slug: antimetal-mcp-server
modified: '2026-08-06'
name: Antimetal
nav: Providers
network: true
overview: 'Antimetal publishes 3 APIs on the [APIs.io](https://apis.io/) network: Artifacts API, Issues API, and Query API. Tagged areas include Company, Observability, Incident Management, Site Reliability Engineering, and Artificial Intelligence.


  Antimetal''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 29 more developer resources.'
random_paper: 14
scopes:
- name: Antimetal Scopes
  scope_count: 4
  slug: antimetal-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode/refreshToken
score:
  band: developing
  composite: 52.7
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 30.3
    contract_quality: 57.8
    developer_ergonomics: 71.4
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 28.9
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/antimetal/refs/heads/main/screenshots/antimetal-2026-08-07T161424.png
security:
- kind: authentication
  name: Antimetal Authentication
  slug: antimetal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Antimetal Domain Security
  slug: antimetal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Antimetal Vulnerability Disclosure
  slug: antimetal-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Antimetal Trust Center
  slug: antimetal-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: antimetal
tags:
- Company
- Observability
- Incident Management
- Site Reliability Engineering
- Artificial Intelligence
- Agents
- DevOps
- Cloud Infrastructure
- Kubernetes
- Root Cause Analysis
- MCP
website: https://www.antimetal.com/
---
