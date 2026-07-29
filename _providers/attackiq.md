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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'REST/JSON API for the AttackIQ Security Optimization Platform. Manage assessments, tests, scenarios, and assets and retrieve execution results. Authenticated with a per-user API token (Authorization: '
  name: AttackIQ Platform API
  slug: attackiq-platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.attackiq.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.attackiq.com/hc/en-us/categories/api
- group: docs
  title: ''
  type: Documentation
  url: https://help.attackiq.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://help.attackiq.com/hc/en-us/categories/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.attackiq.com/academy/
- group: operate
  title: ''
  type: Support
  url: https://help.attackiq.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.attackiq.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AttackIQ
- group: start
  title: ''
  type: SignUp
  url: https://login.attackiq.com/
- group: start
  title: ''
  type: Login
  url: https://login.attackiq.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.attackiq.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.attackiq.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.attackiq.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.attackiq.com/
- group: build
  title: ''
  type: Packages
  url: packages/attackiq-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/attackiq-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/attackiq-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/attackiq-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/attackiq-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/attackiq-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/attackiq-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/attackiq-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/attackiq-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/attackiq-domain-security.yml
created: '2026-07-17'
description: AttackIQ is a cybersecurity company that pioneered Breach and Attack Simulation (BAS) and now delivers a Continuous Threat Exposure Management (CTEM) platform. Its Security Optimization Platform continuously and safely emulates real adversary tactics, techniques, and procedures aligned to the MITRE ATT&CK framework, validating that security controls detect and prevent attacks and measuring control effectiveness over time. The platform exposes a REST/JSON Platform API (firedrill.attackiq.com/v1) for managing assessments, assets, scenarios, tests, and results, authenticated with per-user API tokens, plus an official Python SDK and `aiq` command-line interface. AttackIQ is a portfolio company of Index Ventures.
image: https://www.attackiq.com/wp-content/uploads/2026/05/attackiq-ctem-3.webp
layout: provider
mcp_servers:
- description: ''
  name: attackiq-mcp.yml
  slug: attackiq-mcpyml
modified: '2026-07-18'
name: AttackIQ
nav: Providers
network: true
overview: 'AttackIQ publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Breach and Attack Simulation, and Continuous Threat Exposure Management.


  AttackIQ''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 17 more developer resources.'
random_paper: 40
score:
  band: thin
  composite: 33.7
  delta: -1.5
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 35.2
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/attackiq/refs/heads/main/screenshots/attackiq-2026-07-25T201626.png
security:
- kind: authentication
  name: Attackiq Authentication
  slug: attackiq-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Attackiq Domain Security
  slug: attackiq-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Attackiq Trust Center
  slug: attackiq-trust-center
  summary_line: trust center published
slug: attackiq
tags:
- Company
- Security
- Cybersecurity
- Breach and Attack Simulation
- Continuous Threat Exposure Management
- Security Validation
- MITRE ATT&CK
- Threat Exposure Management
website: https://www.attackiq.com
---
