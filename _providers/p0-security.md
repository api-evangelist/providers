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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: P0 Security Agentic Access
  operation_count: 4
  slug: p0-security-agentic-access
  summary_line: 4 operations · 4 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Submit commands that trigger access workflows.
  name: P0 Security Command API
  slug: p0-security-command-api
- description: Approve, deny, or revoke just-in-time access requests.
  name: P0 Security Permission Requests API
  slug: p0-security-permission-requests-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/p0-security-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/p0-security-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.p0.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.p0.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.p0.dev/access-management/just-in-time-access/just-in-time-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.p0.dev/getting-started/p0-security-onboarding
- group: operate
  title: ''
  type: Support
  url: https://support.p0.dev/
- group: company
  title: ''
  type: Blog
  url: https://p0.dev/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/p0-security
- group: start
  title: ''
  type: SignUp
  url: https://p0.app/
- group: start
  title: ''
  type: Login
  url: https://p0.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://p0.app/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://p0.app/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://p0.dev/trust-center/
- group: auth
  title: ''
  type: Compliance
  url: security/p0-security-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/p0-security-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/p0-security-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/p0-security-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/p0-security-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/p0-security-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/p0-security-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/p0-security-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/p0-security-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/p0-security-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/p0-security-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/p0-security-jit-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: P0 Security is a cloud-native Privileged Access Management (PAM) platform that governs runtime authorization for human users, machine/service accounts, and AI agents across hybrid and multi-cloud environments. Its AuthZ Control Plane enforces just-in-time (JIT), least-privilege access to AWS, Google Cloud, Azure, Oracle Cloud, Kubernetes, databases, SSH hosts, Okta, and Google Workspace — provisioning short-lived credentials on request, routing approvals through Slack, Microsoft Teams, the web app, or the CLI, and automatically revoking access when it expires. P0 also provides an access inventory and identity graph, posture scanning for over-privileged and stale access, service-account key rotation, and an agentic authorization control plane with a self-hosted MCP Gateway that enforces least-privilege policy on every MCP tool call. Developers integrate P0 through the official p0 CLI, a Terraform provider, and a bearer-authenticated Just-in-Time Access API (Command, Permission
  Request, and Access Policies).
image: https://p0.dev/p0.jpg
layout: provider
mcp_servers:
- description: ''
  name: p0-security-mcp.yml
  slug: p0-security-mcpyml
modified: '2026-07-20'
name: P0 Security
nav: Providers
network: true
overview: 'P0 Security publishes 2 APIs on the [APIs.io](https://apis.io/) network: Command API and Permission Requests API. Tagged areas include Company, Security, Privileged Access Management, Identity and Access Management, and Just-in-Time Access.


  P0 Security''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 20 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 50.6
  delta: 1.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.2
    developer_ergonomics: 58.2
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: P0 Security Authentication
  slug: p0-security-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: P0 Security Domain Security
  slug: p0-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: P0 Security Trust Center
  slug: p0-security-trust-center
  summary_line: SOC 2 Type II
slug: p0-security
tags:
- Company
- Security
- Privileged Access Management
- Identity and Access Management
- Just-in-Time Access
- Cloud Security
- Authorization
- Zero Trust
- Agentic Access
- MCP
website: https://docs.p0.dev/
---
