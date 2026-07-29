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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: verified
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 63.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 111
  human_in_the_loop: 19
  name: Tesslio Agentic Access
  operation_count: 225
  slug: tesslio-agentic-access
  summary_line: 225 operations · 111 acting · 19 human-in-the-loop
api_count: 35
apis:
- description: Admin-scoped API keys for support tooling.
  name: tessl.io Admin Keys API
  slug: tesslio-admin-keys-api
- description: Agent and hosted-execution log uploads.
  name: tessl.io Agent Logs API
  slug: tesslio-agent-logs-api
- description: Workspace and organization API keys.
  name: tessl.io API Keys API
  slug: tesslio-api-keys-api
- description: Workspace badge generation.
  name: tessl.io Badges API
  slug: tesslio-badges-api
- description: The Billing API from tessl.io — 4 operation(s) for billing.
  name: tessl.io Billing API
  slug: tesslio-billing-api
- description: Sandbox and capacity-lease scheduling.
  name: tessl.io Capacity API
  slug: tesslio-capacity-api
- description: Endpoints used by the Tessl CLI.
  name: tessl.io CLI API
  slug: tesslio-cli-api
- description: The Context API from tessl.io — 3 operation(s) for context.
  name: tessl.io Context API
  slug: tesslio-context-api
- description: Curated tile lists and items.
  name: tessl.io Curated Lists API
  slug: tesslio-curated-lists-api
- description: The Environments API from tessl.io — 2 operation(s) for environments.
  name: tessl.io Environments API
  slug: tesslio-environments-api
- description: Eval runs, scenarios, and solution scoring.
  name: tessl.io Evals API
  slug: tesslio-evals-api
- description: The Fix Runs API from tessl.io — 4 operation(s) for fix runs.
  name: tessl.io Fix Runs API
  slug: tesslio-fix-runs-api
- description: Eval scenario generation runs.
  name: tessl.io Generation API
  slug: tesslio-generation-api
- description: The InstallPolicy API from tessl.io — 2 operation(s) for installpolicy.
  name: tessl.io InstallPolicy API
  slug: tesslio-installpolicy-api
- description: Third-party integrations (GitHub, GitLab, etc).
  name: tessl.io Integrations API
  slug: tesslio-integrations-api
- description: The Launch Runs API from tessl.io — 4 operation(s) for launch runs.
  name: tessl.io Launch Runs API
  slug: tesslio-launch-runs-api
- description: The LLM API from tessl.io — 2 operation(s) for llm.
  name: tessl.io LLM API
  slug: tesslio-llm-api
- description: The ManagedProjectPolicy API from tessl.io — 1 operation(s) for managedprojectpolicy.
  name: tessl.io ManagedProjectPolicy API
  slug: tesslio-managedprojectpolicy-api
- description: The MCP API from tessl.io — 4 operation(s) for mcp.
  name: tessl.io MCP API
  slug: tesslio-mcp-api
- description: Organizations, members, and invitations.
  name: tessl.io Orgs API
  slug: tesslio-orgs-api
- description: The Policy API from tessl.io — 3 operation(s) for policy.
  name: tessl.io Policy API
  slug: tesslio-policy-api
- description: Workspace projects.
  name: tessl.io Projects API
  slug: tesslio-projects-api
- description: The PublishPolicy API from tessl.io — 1 operation(s) for publishpolicy.
  name: tessl.io PublishPolicy API
  slug: tesslio-publishpolicy-api
- description: Source-control repository helpers.
  name: tessl.io Repos API
  slug: tesslio-repos-api
- description: The Review Runs API from tessl.io — 3 operation(s) for review runs.
  name: tessl.io Review Runs API
  slug: tesslio-review-runs-api
- description: The Reviews API from tessl.io — 3 operation(s) for reviews.
  name: tessl.io Reviews API
  slug: tesslio-reviews-api
- description: Search across tiles, skills, and repos.
  name: tessl.io Search API
  slug: tesslio-search-api
- description: The Security Review Runs API from tessl.io — 2 operation(s) for security review runs.
  name: tessl.io Security Review Runs API
  slug: tesslio-security-review-runs-api
- description: The SkillInventory API from tessl.io — 24 operation(s) for skillinventory.
  name: tessl.io SkillInventory API
  slug: tesslio-skillinventory-api
- description: Skill discovery, reviews, and security checks.
  name: tessl.io Skills API
  slug: tesslio-skills-api
- description: The Tasks API from tessl.io — 8 operation(s) for tasks.
  name: tessl.io Tasks API
  slug: tesslio-tasks-api
- description: Tile catalog, versions, and metadata.
  name: tessl.io Tiles API
  slug: tesslio-tiles-api
- description: User accounts and identity.
  name: tessl.io Users API
  slug: tesslio-users-api
- description: Background workflow executions and repository workflow configs.
  name: tessl.io Workflows API
  slug: tesslio-workflows-api
- description: Workspaces and workspace membership.
  name: tessl.io Workspaces API
  slug: tesslio-workspaces-api
artifact_total: 41
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/tesslio-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/tesslio-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tesslio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tesslio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tesslio-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tesslio-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tesslio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tesslio-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tessl.io
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.tessl.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tesslio-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/tesslio-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/tesslio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tesslio-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tesslio-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tesslio-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tesslio-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tesslio-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tesslio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://tessl.io/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tesslio-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.tessl.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tessl.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tessl.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.tessl.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tessl.io/introduction-to-tessl/set-up-tessl
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tesslio-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://docs.tessl.io/support/faqs
- group: company
  title: ''
  type: Blog
  url: https://tessl.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tesslio
- group: commercial
  title: ''
  type: Pricing
  url: https://tessl.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.tessl.io
- group: start
  title: ''
  type: Registry
  url: https://tessl.io/registry
- group: company
  title: ''
  type: Website
  url: https://tessl.io
created: '2026-07-17'
description: Tessl is an agent-enablement platform for spec-driven and agentic software development. It provides a registry of versioned "tiles"/plugins (10,000+ library docs) and 3,000+ searchable Agent Skills, a CLI for authoring, linting, reviewing, and publishing skills and plugins, server-side quality reviews and Snyk-powered security scanning, eval/scenario tooling to prove a skill changes agent behavior, org/workspace governance with install policies, and a first-party Model Context Protocol (MCP) server plus a workspace MCP gateway so AI coding agents can discover and install the right context. Backed by Index Ventures. The public REST API (api.tessl.io) exposes 225 operations across tiles, skills, workspaces, orgs, projects, evals, and integrations.
image: https://cdn.sanity.io/images/ojuglg5y/production/fa12cfb35dd51f280b764adf7122a6c0f7911e12-2400x1260.png?w=1200&fit=max&auto=format
layout: provider
mcp_servers:
- description: ''
  name: tesslio-mcp.yml
  slug: tesslio-mcpyml
modified: '2026-07-21'
name: tessl.io
nav: Providers
network: true
overview: 'tessl.io publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Admin Keys API, Agent Logs API, API Keys API, and 32 more. Tagged areas include Company, Ai Ml, Agent Enablement, Agentic Development, and Developer Tools.


  tessl.io''s developer surface includes authentication, changelog, CLI, documentation, API reference, getting-started guide, support, and 28 more developer resources.'
random_paper: 60
score:
  band: developing
  composite: 50.9
  delta: 0.2
  facets:
    commercial_clarity: 31.6
    contract_quality: 46.5
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Tesslio Authentication
  slug: tesslio-authentication
  summary_line: http-bearer/apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Tesslio Domain Security
  slug: tesslio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tesslio Vulnerability Disclosure
  slug: tesslio-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Tesslio Trust Center
  slug: tesslio-trust-center
  summary_line: trust center published
slug: tesslio
tags:
- Company
- Ai Ml
- Agent Enablement
- Agentic Development
- Developer Tools
- Skills Registry
- Model Context Protocol
- Spec-Driven Development
- Code Review
- CLI
website: https://tessl.io
---
