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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Versioned REST API for the CodeNOW platform covering applications, components, containers, libraries, builds, releases, triggers, deployments, environments, clusters, managed services, labels, teams a
  name: CodeNOW API
  slug: codenow-api
artifact_total: 5
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.codenow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codenow.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.codenow.com/category/application/vnd.codenow.v1+json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.codenow.com/manuals
- group: auth
  title: ''
  type: Authentication
  url: authentication/codenow-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/codenow-mcp.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/codenow-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/codenow-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.codenow.com/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.codenow.com/en/product/roadmap
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/codenow-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/codenow-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/codenow-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/codenow-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codenow-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codenow-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.codenow.com/en/blog
- group: operate
  title: ''
  type: Support
  url: https://support.codenow.com/
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/mjtQeHYFvJ
- group: start
  title: ''
  type: SignUp
  url: https://cloud.codenow.com
- group: start
  title: ''
  type: Login
  url: https://cloud.codenow.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.codenow.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.codenow.com/privacy-policy
created: '2026-07-17'
description: CodeNOW is a Prague-based governance and execution platform for AI-scale software delivery — a control plane that determines how software moves through the SDLC regardless of whether a human or an AI agent wrote it. Founded by an ex-IBM team, CodeNOW provides a governed execution layer that enforces organizational policies and standards across human and non-human actors, making every action auditable, stoppable, and structurally controlled. The platform manages applications, components, containers, libraries, builds, releases, deployments, environments and Kubernetes clusters, and is available in cloud, on-premises, and air-gapped deployments. It exposes a versioned REST API (media-type versioning) authenticated with an API key, plus an official Model Context Protocol (MCP) server that wraps the API so AI assistants and agents can operate the platform directly.
image: https://www.codenow.com/img/CN-icon-40x42px-dark-forwhite-bg.png
layout: provider
mcp_servers:
- description: ''
  name: codenow-mcp.yml
  slug: codenow-mcpyml
modified: '2026-07-18'
name: CodeNOW
nav: Providers
network: true
overview: 'CodeNOW publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, Software Delivery, Platform Engineering, and Governance.


  CodeNOW''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 16 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 1
  name: Codenow Rate Limits
  slug: codenow-rate-limits
score:
  band: thin
  composite: 28.7
  delta: -6.9
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 35.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/codenow/refs/heads/main/screenshots/codenow-2026-07-25T205923.png
security:
- kind: authentication
  name: Codenow Authentication
  slug: codenow-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Codenow Domain Security
  slug: codenow-domain-security
  summary_line: TLSv1.3 · DMARC
slug: codenow
tags:
- Company
- DevOps
- Software Delivery
- Platform Engineering
- Governance
- AI Agents
- CI/CD
- Deployment
- Kubernetes
- Model Context Protocol
website: https://docs.codenow.com/
---
