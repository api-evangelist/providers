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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 53
  human_in_the_loop: 4
  name: Border0 Agentic Access
  operation_count: 89
  slug: border0-agentic-access
  summary_line: 89 operations · 53 acting · 4 human-in-the-loop
api_count: 15
apis:
- description: The Audit Actions API from Border0 — 2 operation(s) for audit actions.
  name: Border0 Audit Actions API
  slug: border0-audit-actions-api
- description: The Client API from Border0 — 6 operation(s) for client.
  name: Border0 Client API
  slug: border0-client-api
- description: The Connect API from Border0 — 1 operation(s) for connect.
  name: Border0 Connect API
  slug: border0-connect-api
- description: The Login API from Border0 — 2 operation(s) for login.
  name: Border0 Login API
  slug: border0-login-api
- description: The Mtls-Ca API from Border0 — 3 operation(s) for mtls-ca.
  name: Border0 Mtls-Ca API
  slug: border0-mtls-ca-api
- description: The Organization API from Border0 — 4 operation(s) for organization.
  name: Border0 Organization API
  slug: border0-organization-api
- description: The Organizations API from Border0 — 15 operation(s) for organizations.
  name: Border0 Organizations API
  slug: border0-organizations-api
- description: The Policies API from Border0 — 2 operation(s) for policies.
  name: Border0 Policies API
  slug: border0-policies-api
- description: The Policy API from Border0 — 1 operation(s) for policy.
  name: Border0 Policy API
  slug: border0-policy-api
- description: The Session API from Border0 — 3 operation(s) for session.
  name: Border0 Session API
  slug: border0-session-api
- description: The Sessions API from Border0 — 2 operation(s) for sessions.
  name: Border0 Sessions API
  slug: border0-sessions-api
- description: The Socket API from Border0 — 10 operation(s) for socket.
  name: Border0 Socket API
  slug: border0-socket-api
- description: The Stats API from Border0 — 2 operation(s) for stats.
  name: Border0 Stats API
  slug: border0-stats-api
- description: The User API from Border0 — 4 operation(s) for user.
  name: Border0 User API
  slug: border0-user-api
- description: The Users API from Border0 — 5 operation(s) for users.
  name: Border0 Users API
  slug: border0-users-api
artifact_total: 20
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/border0-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.border0.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.border0.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.border0.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.border0.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.border0.com/docs/quick-start-copy
- group: operate
  title: ''
  type: Support
  url: https://docs.border0.com/docs/getting-help
- group: company
  title: ''
  type: Blog
  url: https://www.border0.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/borderzero
- group: start
  title: ''
  type: SignUp
  url: https://portal.border0.com/register
- group: start
  title: ''
  type: Login
  url: https://portal.border0.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.border0.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.border0.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.border0.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/border0-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.border0.com/docs/security-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/border0-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/border0-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/border0-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/border0-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/border0-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/border0-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/border0-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/border0-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/border0-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/border0-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/border0-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/border0-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/border0-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/border0-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Border0 is an identity-aware Zero Trust network access platform for securing access to infrastructure — SSH and RDP servers, PostgreSQL/MySQL/MSSQL/MongoDB/Elasticsearch databases, Kubernetes clusters, AWS consoles and S3 buckets, and any internal HTTP or TCP service. Instead of VPNs and shared credentials, Border0 publishes each resource as a policy-gated "socket," authenticates users through their existing SSO/identity provider, and records every session for audit. Its REST admin API (api.border0.com/api/v1) manages sockets, access policies, connectors, organizations, identity providers, service accounts, tokens, sessions, and audit logs, and is complemented by an official Go SDK, a Terraform provider, a CLI, and GitHub Actions. Border0 was acquired by Tailscale in March 2026.
image: https://cdn.prod.website-files.com/6329655518c5f56d63ac0eb8/673ac517dcc68218bae5a42d_img-border0-opengraph.png
layout: provider
mcp_servers:
- description: ''
  name: border0-mcp.yml
  slug: border0-mcpyml
modified: '2026-07-18'
name: Border0
nav: Providers
network: true
overview: 'Border0 publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Audit Actions API, Client API, Connect API, and 12 more. Tagged areas include Zero Trust, Network Access, Security, Identity and Access Management, and Infrastructure.


  Border0''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 24 more developer resources.'
random_paper: 86
score:
  band: developing
  composite: 50.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 56.1
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/border0/refs/heads/main/screenshots/border0-2026-07-25T203633.png
security:
- kind: authentication
  name: Border0 Authentication
  slug: border0-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Border0 Domain Security
  slug: border0-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Border0 Vulnerability Disclosure
  slug: border0-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: border0
tags:
- Zero Trust
- Network Access
- Security
- Identity and Access Management
- Infrastructure
- VPN
- SSH
- Databases
- Kubernetes
- Company
website: https://www.border0.com
---
