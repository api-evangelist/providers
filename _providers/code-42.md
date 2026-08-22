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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Code42 Incydr's public REST API for insider risk management — actors, agents, alert rules, audit log, cases, departments, directory groups, file events, sessions, trusted activities, users, and watchl
  name: Code42 Incydr API
  slug: code42-incydr-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/code-42-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.code42.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.code42.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.code42.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.code42.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.code42.com/sdk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/code42
- group: company
  title: ''
  type: Blog
  url: https://www.code42.com/blog/
- group: start
  title: ''
  type: Login
  url: https://console.us.code42.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.code42.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/code-42-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/code-42-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/code-42-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/code-42-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/code-42-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/code-42-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/code-42-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/code-42-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/code-42-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/code-42-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/code-42-llms.txt
created: '2026-07-17'
description: Code42 (now part of Mimecast) is a security software company whose Incydr product is a SaaS Insider Risk Management (IRM) platform that detects, and responds to data exfiltration and insider threats across endpoints, cloud, email, and browsers. Code42 exposes a public OAuth 2.0 REST API through its regional API gateways (api.us.code42.com and other regions) covering actors, agents, alert rules, audit log, cases, file events, sessions, users, and watchlists. Developers integrate via the official Incydr Python SDK, the incydr command-line interface, and the legacy py42 SDK. This profile was added to the API Evangelist network as a portfolio-company lead (backed by Accel) and has been enriched from Code42's public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/code-42.png
layout: provider
modified: '2026-07-18'
name: Code 42
nav: Providers
network: true
overview: 'Code 42 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Insider Risk Management, Data Loss Prevention, and Data Security.


  Code 42''s developer surface includes documentation, API reference, getting-started guide, engineering blog, CLI, authentication, changelog, and 14 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 29.4
  delta: -0.3
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 29.7
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/code-42/refs/heads/main/screenshots/code-42-2026-07-25T205903.png
security:
- kind: authentication
  name: Code 42 Authentication
  slug: code-42-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Code 42 Domain Security
  slug: code-42-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: code-42
tags:
- Company
- Security
- Insider Risk Management
- Data Loss Prevention
- Data Security
- Endpoint Security
- Cybersecurity
- SaaS
website: https://www.code42.com
---
