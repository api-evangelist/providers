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
    error_semantics: documented
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
  score: 24.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Corridor Agentic Access
  operation_count: 27
  slug: corridor-agentic-access
  summary_line: 27 operations · 9 acting
api_count: 1
apis:
- baseURL: https://app.corridor.dev/api
  baseurl_source: declared
  description: Access dashboard metrics and AI usage data.
  name: Corridor Dashboard API
  slug: corridor-dashboard-api
- baseURL: https://app.corridor.dev/api
  baseurl_source: declared
  description: Retrieve and manage security findings across projects.
  name: Corridor Findings API
  slug: corridor-findings-api
- baseURL: https://app.corridor.dev/api
  baseurl_source: declared
  description: Manage per-project security guardrails (reports) and packs.
  name: Corridor Guardrails API
  slug: corridor-guardrails-api
- baseURL: https://app.corridor.dev/api
  baseurl_source: declared
  description: Access pull request review results and AI analysis.
  name: Corridor PR Reviews API
  slug: corridor-pr-reviews-api
- baseURL: https://app.corridor.dev/api
  baseurl_source: declared
  description: List and inspect projects (connected repositories).
  name: Corridor Projects API
  slug: corridor-projects-api
- baseURL: https://app.corridor.dev/api
  baseurl_source: declared
  description: Manage team configuration, members, and permissions.
  name: Corridor Teams API
  slug: corridor-teams-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Corridor Dashboard API
  slug: open-corridor-dashboard-api
- collection_type: open
  name: Corridor Dashboard Findings API
  slug: open-corridor-findings-api
- collection_type: open
  name: Corridor Dashboard Guardrails API
  slug: open-corridor-guardrails-api
- collection_type: open
  name: Corridor Dashboard Projects API
  slug: open-corridor-projects-api
- collection_type: open
  name: Corridor Dashboard Teams API
  slug: open-corridor-teams-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/corridor-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://corridor.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.corridor.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.corridor.dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.corridor.dev/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.corridor.dev/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://corridor.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://corridor.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.corridor.dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corridor.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corridor.dev/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@corridor.dev
- group: operate
  title: ''
  type: StatusPage
  url: https://status.corridor.dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.corridor.dev/changelog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/corridor-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/corridor-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/corridor-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/corridor-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/corridor-security.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/corridor-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.corridor.dev
- group: auth
  title: ''
  type: Security
  url: https://corridor.dev/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/corridor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corridor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/corridor-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/corridor-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/corridor-triage-findings.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/corridor-manage-guardrails.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/corridor-pr-review-lookup.md
created: '2026-07-17'
description: 'Corridor is a security company building the security layer for AI coding. Founded by Jack Cable (former CISA) and backed by Felicis, Corridor secures AI-generated code at the source: it plugs into AI coding assistants and IDEs (Claude Code, Cursor, VS Code, Codex, Devin, Factory) to deliver real-time security guardrails as code is generated, automated security PR reviews on GitHub and GitLab, pre-commit scanning, findings management, and MCP compliance enforcement. Corridor exposes a REST API and an official hosted Model Context Protocol (MCP) server so agents and CI/CD pipelines can query findings, manage guardrails, look up PR reviews, and read dashboard data.'
image: https://www.corridor.dev/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Corridor MCP Server
  slug: corridor-mcp-server
modified: '2026-07-18'
name: Corridor
nav: Providers
network: true
overview: 'Corridor publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Dashboard API, Findings API, Guardrails API, and 3 more. Tagged areas include Company, Security, Application Security, AI Coding, and Code Security.


  Corridor''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 22 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 13.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/corridor/refs/heads/main/screenshots/corridor-2026-07-25T210442.png
security:
- kind: authentication
  name: Corridor Authentication
  slug: corridor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Corridor Domain Security
  slug: corridor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Corridor Vulnerability Disclosure
  slug: corridor-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Corridor Trust Center
  slug: corridor-trust-center
  summary_line: trust center published
slug: corridor
tags:
- Company
- Security
- Application Security
- AI Coding
- Code Security
- Developer Tools
- Guardrails
- MCP
- Static Analysis
- DevSecOps
website: https://corridor.dev
---
