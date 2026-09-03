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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: RESTful JSON API for triggering and monitoring pipelines and tasks, managing users/groups, parameters, audit logs, SCM migration, and GitCustodian, authenticated with scoped JWT Personal Access Tokens
  name: Opsera API Platform
  slug: opsera-api-platform
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://opsera.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.opsera.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opsera.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.opsera.io/readme
- group: docs
  title: ''
  type: APIReference
  url: https://docs.opsera.io/api-platform-and-integration
- group: auth
  title: ''
  type: Authentication
  url: authentication/opsera-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/opsera-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opsera-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opsera-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/opsera-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opsera-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/opsera-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opsera-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opsera-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.opsera.io/opsera-release-updates
- group: company
  title: ''
  type: Blog
  url: https://opsera.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://opsera.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://opsera.ai/agents/
- group: start
  title: ''
  type: Login
  url: https://portal.opsera.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opsera.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opsera.ai/privacy/
- group: operate
  title: ''
  type: Support
  url: https://docs.opsera.io/readme/submit-a-support-ticket
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpseraEngineering
created: '2026-07-17'
description: Opsera is an AI-powered unified DevOps platform that helps enterprise software teams orchestrate the full software delivery lifecycle from a single control plane. It combines declarative CI/CD pipeline automation, toolchain integration across 80%+ of common DevOps tools, DevSecOps governance and policy enforcement, and unified insights (DORA, DevEx, and security dashboards) with AI-driven analysis. Developers automate pipelines and tasks programmatically through the Opsera API Platform using scoped JWT Personal Access Tokens, and agents can drive the platform through Opsera's hosted Model Context Protocol (MCP) server. Opsera is backed by Felicis and Trinity Ventures.
image: https://opsera.ai/wp-content/uploads/2025/07/opsera-generic-social.jpg
layout: provider
mcp_servers:
- description: ''
  name: Opsera MCP Server
  slug: opsera-mcp-server
modified: '2026-07-20'
name: Opsera
nav: Providers
network: true
overview: 'Opsera publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, CI/CD, DevSecOps, and Pipeline Orchestration.


  Opsera''s developer surface includes documentation, getting-started guide, API reference, authentication, changelog, engineering blog, pricing, and 16 more developer resources.'
random_paper: 20
scopes:
- name: Opsera Scopes
  scope_count: 2
  slug: opsera-scopes
  summary_line: 2 scopes
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 30.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opsera/refs/heads/main/screenshots/opsera-2026-08-07T190746.png
security:
- kind: authentication
  name: Opsera Authentication
  slug: opsera-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opsera Domain Security
  slug: opsera-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opsera
tags:
- Company
- DevOps
- CI/CD
- DevSecOps
- Pipeline Orchestration
- Developer Tools
- Software Delivery
- Governance
- MCP
- AI Agents
website: https://opsera.ai
---
