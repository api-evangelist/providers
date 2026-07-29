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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Anysphere Agentic Access
  operation_count: 18
  slug: anysphere-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 5
apis:
- description: The Agents API from Anysphere — 11 operation(s) for agents.
  name: Anysphere Agents API
  slug: anysphere-agents-api
- description: The Me API from Anysphere — 1 operation(s) for me.
  name: Anysphere Me API
  slug: anysphere-me-api
- description: The Models API from Anysphere — 1 operation(s) for models.
  name: Anysphere Models API
  slug: anysphere-models-api
- description: The Repositories API from Anysphere — 1 operation(s) for repositories.
  name: Anysphere Repositories API
  slug: anysphere-repositories-api
- description: The Sub Tokens API from Anysphere — 1 operation(s) for sub tokens.
  name: Anysphere Sub Tokens API
  slug: anysphere-sub-tokens-api
artifact_total: 17
collections:
- collection_type: postman
  name: Cursor Cloud Agents API
  slug: postman-anysphere-agents-api
- collection_type: postman
  name: Cursor Cloud Agents Me API
  slug: postman-anysphere-me-api
- collection_type: postman
  name: Cursor Cloud Agents Models API
  slug: postman-anysphere-models-api
- collection_type: postman
  name: Cursor Cloud Agents Repositories API
  slug: postman-anysphere-repositories-api
- collection_type: postman
  name: Cursor Cloud Agents Sub Tokens API
  slug: postman-anysphere-sub-tokens-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/anysphere/overview
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anysphere-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://cursor.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anysphere-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/anysphere-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cursor.com/security
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anysphere-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anysphere-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anysphere-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anysphere-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anysphere-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/anysphere-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/anysphere-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anysphere-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cursor.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/anysphere-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anysphere-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/anysphere-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/anysphere-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/anysphere-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anysphere-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anysphere-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/anysphere-cloud-agents-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cursor.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://cursor.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cursor.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://cursor.com/docs/get-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://forum.cursor.com
- group: company
  title: ''
  type: Blog
  url: https://cursor.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cursor
- group: commercial
  title: ''
  type: Pricing
  url: https://cursor.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cursor.com/dashboard/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cursor.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cursor.com/privacy
- group: company
  title: ''
  type: Website
  url: https://anysphere.inc
created: '2026-07-17'
description: Anysphere is the applied-research company behind Cursor, the AI-native code editor and agent platform. Beyond the desktop app, Cursor ships a public Cloud Agents REST API (https://api.cursor.com) that lets developers programmatically create autonomous coding agents, submit prompt runs, stream run events over SSE, and retrieve produced artifacts, plus an Admin API for team member/usage/spend management and a first-party terminal CLI (the `agent` binary). Authentication is a dashboard-issued API key over HTTP Basic/Bearer. This profile was surfaced as a Thrive Capital portfolio company and enriched from Cursor's public developer surface.
image: https://cursor.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: anysphere-mcp.yml
  slug: anysphere-mcpyml
modified: '2026-07-17'
name: Anysphere
nav: Providers
network: true
overview: 'Anysphere publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Me API, Models API, and 2 more. Tagged areas include Company, Developer Tools, Artificial Intelligence, Code Editor, and Coding Agents.


  Anysphere''s developer surface includes authentication, changelog, CLI, documentation, API reference, getting-started guide, support, and 29 more developer resources.'
random_paper: 27
rate_limits:
- limit_count: 7
  name: Anysphere Rate Limits
  slug: anysphere-rate-limits
score:
  band: strong
  composite: 61.6
  delta: -1.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.0
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 78.9
  previous_composite: 62.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anysphere/refs/heads/main/screenshots/anysphere-2026-07-25T200524.png
security:
- kind: authentication
  name: Anysphere Authentication
  slug: anysphere-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Anysphere Domain Security
  slug: anysphere-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anysphere Vulnerability Disclosure
  slug: anysphere-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Anysphere Trust Center
  slug: anysphere-trust-center
  summary_line: SOC 2 Type II
slug: anysphere
tags:
- Company
- Developer Tools
- Artificial Intelligence
- Code Editor
- Coding Agents
- Cloud Agents
- Developer Productivity
- IDE
website: https://anysphere.inc
---
