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
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 165
  human_in_the_loop: 8
  name: Coder Agentic Access
  operation_count: 378
  slug: coder-agentic-access
  summary_line: 378 operations · 165 acting · 8 human-in-the-loop
api_count: 32
apis:
- description: Endpoints for creating, retrieving, updating, and managing workspace lifecycle including autostart schedules, time-to-live settings, dormancy controls, ACLs, and real-time monitoring via server-sent e
  name: Coder Workspaces API
  slug: workspaces-api
- description: Endpoints for creating, listing, updating, and archiving workspace templates and template versions within organizations; supports examples, daily active user metrics, and version management.
  name: Coder Templates API
  slug: templates-api
- description: Endpoints for user management including creation, authentication, SSH key management, API token/key lifecycle, role assignment, organization membership, and OIDC/GitHub OAuth integration.
  name: Coder Users API
  slug: users-api
- description: Endpoints for workspace agent lifecycle, authentication (AWS/Azure/GCP instance identity), PTY terminal access, container management, listening-port enumeration, log streaming, and WireGuard/Tailnet c
  name: Coder Workspace Agents API
  slug: agents-api
- description: 'Enterprise-only endpoints covering OAuth2 provider management, licensing and entitlements, group and RBAC management, AI spending budgets, organization-level IdP sync, provisioner key management, and '
  name: Coder Enterprise API
  slug: enterprise-api
- description: The Agents API from Coder — 28 operation(s) for agents.
  name: Coder Agents API
  slug: coder-agents-api
- description: The AI Bridge API from Coder — 4 operation(s) for ai bridge.
  name: Coder AI Bridge API
  slug: coder-ai-bridge-api
- description: The AI Providers API from Coder — 2 operation(s) for ai providers.
  name: Coder AI Providers API
  slug: coder-ai-providers-api
- description: The Applications API from Coder — 2 operation(s) for applications.
  name: Coder Applications API
  slug: coder-applications-api
- description: The Audit API from Coder — 2 operation(s) for audit.
  name: Coder Audit API
  slug: coder-audit-api
- description: The Authorization API from Coder — 7 operation(s) for authorization.
  name: Coder Authorization API
  slug: coder-authorization-api
- description: The Builds API from Coder — 9 operation(s) for builds.
  name: Coder Builds API
  slug: coder-builds-api
- description: The Chats API from Coder — 20 operation(s) for chats.
  name: Coder Chats API
  slug: coder-chats-api
- description: The Debug API from Coder — 14 operation(s) for debug.
  name: Coder Debug API
  slug: coder-debug-api
- description: The Enterprise API from Coder — 67 operation(s) for enterprise.
  name: Coder Enterprise API
  slug: coder-enterprise-api
- description: The Files API from Coder — 2 operation(s) for files.
  name: Coder Files API
  slug: coder-files-api
- description: The General API from Coder — 10 operation(s) for general.
  name: Coder General API
  slug: coder-general-api
- description: The Git API from Coder — 3 operation(s) for git.
  name: Coder Git API
  slug: coder-git-api
- description: The InitScript API from Coder — 1 operation(s) for initscript.
  name: Coder InitScript API
  slug: coder-initscript-api
- description: The Insights API from Coder — 5 operation(s) for insights.
  name: Coder Insights API
  slug: coder-insights-api
- description: The Members API from Coder — 7 operation(s) for members.
  name: Coder Members API
  slug: coder-members-api
- description: The Notifications API from Coder — 13 operation(s) for notifications.
  name: Coder Notifications API
  slug: coder-notifications-api
- description: The Organizations API from Coder — 4 operation(s) for organizations.
  name: Coder Organizations API
  slug: coder-organizations-api
- description: The PortSharing API from Coder — 1 operation(s) for portsharing.
  name: Coder PortSharing API
  slug: coder-portsharing-api
- description: The Prebuilds API from Coder — 1 operation(s) for prebuilds.
  name: Coder Prebuilds API
  slug: coder-prebuilds-api
- description: The Provisioning API from Coder — 1 operation(s) for provisioning.
  name: Coder Provisioning API
  slug: coder-provisioning-api
- description: The Secrets API from Coder — 2 operation(s) for secrets.
  name: Coder Secrets API
  slug: coder-secrets-api
- description: The Tasks API from Coder — 9 operation(s) for tasks.
  name: Coder Tasks API
  slug: coder-tasks-api
- description: The Templates API from Coder — 33 operation(s) for templates.
  name: Coder Templates API
  slug: coder-templates-api
- description: The Users API from Coder — 28 operation(s) for users.
  name: Coder Users API
  slug: coder-users-api
- description: The WorkspaceProxies API from Coder — 1 operation(s) for workspaceproxies.
  name: Coder WorkspaceProxies API
  slug: coder-workspaceproxies-api
- description: The Workspaces API from Coder — 20 operation(s) for workspaces.
  name: Coder Workspaces API
  slug: coder-workspaces-api
artifact_total: 55
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coder-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/coder-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coder-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coder-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coder-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://coder.com
- group: docs
  title: ''
  type: Documentation
  url: https://coder.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coder
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coderhq
- group: other
  title: ''
  type: X
  url: https://x.com/coderhq
- group: company
  title: ''
  type: Blog
  url: https://coder.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://coder.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://coder.com/pricing
- group: build
  title: ''
  type: CLI
  url: https://coder.com/docs/reference/cli
- group: commercial
  title: ''
  type: Plans
  url: plans/coder-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coder-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/coder-finops.yml
created: '2026-06-12'
description: Coder is a self-hosted and cloud platform for remote cloud development environments (CDEs) and AI coding agents, where workspaces are defined using Terraform and connected via a secure WireGuard tunnel. It serves individual developers and enterprises in industries such as automotive, finance, government, and technology, providing governed, reproducible workspaces with IDE integrations for VS Code, JetBrains, Cursor, and others. Coder exposes a comprehensive REST API (v2) covering workspaces, templates, users, organizations, agents, and enterprise management, with a published Swagger 2.0 specification. SDKs include a built-in Go client (codersdk) and a Terraform provider; a CLI with 40+ subcommands is also available for full programmatic control.
examples:
- key_count: 7
  name: Coder Create Workspace Example
  slug: coder-create-workspace-example
- key_count: 27
  name: Coder Get Template Example
  slug: coder-get-template-example
- key_count: 13
  name: Coder Get User Example
  slug: coder-get-user-example
- key_count: 26
  name: Coder Get Workspace Example
  slug: coder-get-workspace-example
- key_count: 2
  name: Coder List Workspaces Example
  slug: coder-list-workspaces-example
finops:
- name: Coder Finops
  service_category: Developer Tools
  slug: coder-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coder.png
json_schemas:
- name: AuditLog
  property_count: 19
  slug: coder-auditlog
- name: Organization
  property_count: 9
  slug: coder-organization
- name: Template
  property_count: 35
  slug: coder-template
- name: TemplateVersion
  property_count: 14
  slug: coder-templateversion
- name: User
  property_count: 15
  slug: coder-user
- name: Workspace
  property_count: 33
  slug: coder-workspace
- name: WorkspaceAgent
  property_count: 33
  slug: coder-workspaceagent
- name: WorkspaceBuild
  property_count: 25
  slug: coder-workspacebuild
jsonld:
- class_count: 40
  name: Coder Context
  property_count: 48
  slug: coder-context
layout: provider
modified: '2026-06-12'
name: Coder
nav: Providers
network: true
overview: 'Coder publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Agents API, AI Bridge API, AI Providers API, and 24 more. Tagged areas include Developer Tools, Remote Development, Cloud Development Environments, AI Agents, and Infrastructure.


  The Coder catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Coder''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, CLI, and 11 more developer resources.'
plans:
- name: Coder Plans Pricing
  plan_count: 2
  slug: coder-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 4
  name: Coder Rate Limits
  slug: coder-rate-limits
rules:
- name: Coder API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: coder-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.3
  delta: -4.9
  facets:
    commercial_clarity: 47.4
    contract_quality: 55.4
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coder/refs/heads/main/screenshots/coder-2026-06-20T174705.png
security:
- kind: authentication
  name: Coder Authentication
  slug: coder-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Coder Domain Security
  slug: coder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coder Vulnerability Disclosure
  slug: coder-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Coder Trust Center
  slug: coder-trust-center
  summary_line: SOC 2
slug: coder
tags:
- Developer Tools
- Remote Development
- Cloud Development Environments
- AI Agents
- Infrastructure
- Workspaces
website: https://coder.com
---
