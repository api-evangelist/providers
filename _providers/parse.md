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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'HTTP+JSON REST API for the Parse Platform: object CRUD and queries, users and sessions, roles, files, analytics and push. Parse Server is self-hosted, so the base URL is the operator''s own Parse Serve'
  name: Parse REST API
  slug: parse-rest-api
artifact_total: 6
asyncapis:
- description: ''
  name: Parse Webhooks
  slug: parse-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://parseplatform.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.parseplatform.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.parseplatform.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.parseplatform.org/rest/guide/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.parseplatform.org/parse-server/guide/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parse-community
- group: company
  title: ''
  type: Blog
  url: https://blog.parseplatform.org/
- group: operate
  title: ''
  type: Support
  url: https://community.parseplatform.org/
- group: build
  title: ''
  type: Packages
  url: packages/parse-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/parse-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parse-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parse-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/parse-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/parse-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/parse-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parse-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/parse-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/parse-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/parse-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/parse-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parse-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/parse-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/parse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/parse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parse-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/parse-conformance.yml
created: '2026-07-17'
description: Parse is an open-source Backend-as-a-Service (BaaS). Originally the mobile backend company founded in 2011, backed by GV and DCVC, and acquired by Facebook in 2013 before the hosted parse.com service was shut down in 2017, Parse now lives on as the community-maintained Parse Platform. It centers on Parse Server, a self-hostable Node.js/Express backend, paired with first-party client SDKs for JavaScript, Apple (iOS/macOS), Android, Flutter/Dart, PHP, .NET, Swift and Arduino. Parse exposes a documented REST API over HTTP+JSON providing a schemaless object store, user authentication and sessions, roles and ACL/class-level permissions, file storage, rich queries, Cloud Code, Cloud Code Webhooks, LiveQuery real-time subscriptions, analytics and push notifications.
image: https://raw.githubusercontent.com/parse-community/parse-server/alpha/.github/parse-server-logo.png
layout: provider
mcp_servers:
- description: ''
  name: parse-mcp.yml
  slug: parse-mcpyml
modified: '2026-07-20'
name: Parse
nav: Providers
network: true
overview: 'Parse publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Backend as a Service, BaaS, Mobile, and Open Source.


  The Parse catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Parse''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 19 more developer resources.'
random_paper: 92
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 47.4
  previous_composite: 39.2
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parse/refs/heads/main/screenshots/parse-2026-08-07T191458.png
security:
- kind: authentication
  name: Parse Authentication
  slug: parse-authentication
  summary_line: apiKey · 5 schemes
- kind: domain-security
  name: Parse Domain Security
  slug: parse-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Parse Vulnerability Disclosure
  slug: parse-vulnerability-disclosure
  summary_line: contact published
slug: parse
tags:
- Company
- Backend as a Service
- BaaS
- Mobile
- Open Source
- REST API
- Database
- Authentication
- Push Notifications
- Real Time
website: https://parseplatform.org
---
