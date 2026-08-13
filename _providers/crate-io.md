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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: The CrateDB Cloud REST API manages CrateDB Cloud resources — organizations, regions, projects, clusters, products, users, roles, subscriptions, and audit logs. Authentication uses HTTP Basic auth with
  name: CrateDB Cloud API
  slug: cratedb-cloud-api
- description: 'CrateDB''s native developer interface: a JSON-over-HTTP SQL endpoint. Clients POST a JSON body ({"stmt": "...", "args": [...], "bulk_args": [[...]]}) to /_sql (default port 4200) and receive cols/rows/'
  name: CrateDB HTTP SQL Endpoint
  slug: cratedb-http-sql-endpoint
artifact_total: 7
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.cratedb.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://cratedb.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cratedb.com/docs/cloud/en/latest/reference/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://cratedb.com/docs/guide/
- group: operate
  title: ''
  type: Support
  url: https://cratedb.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.cratedb.com/
- group: company
  title: ''
  type: Blog
  url: https://cratedb.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crate
- group: commercial
  title: ''
  type: Pricing
  url: https://cratedb.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.cratedb.cloud/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cratedb.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cratedb.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://cratedb.statuspage.io/
- group: build
  title: ''
  type: Packages
  url: packages/crate-io-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crate-io-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/crate-io-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crate-io-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crate-io-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/crate-io-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crate-io-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crate-io-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crate-io-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crate-io-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crate-io-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cratedb.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crate-io-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crate-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/crate/crate/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/crate-io-trust-center.yml
created: '2026-07-17'
description: Crate.io is the company behind CrateDB, a distributed SQL database engineered for real-time analytics on large volumes of operational data. CrateDB unifies time-series, JSON/document, full-text search, vector, geospatial, and relational data behind standard SQL, is PostgreSQL wire-protocol compatible, and is built on Lucene for horizontal scalability and sub-second queries over billions of rows. Developers interact with CrateDB through an HTTP SQL endpoint (POST /_sql on port 4200) and with the managed CrateDB Cloud service through the CrateDB Cloud REST API (https://console.cratedb.cloud/api/v2), which manages organizations, projects, clusters, users, roles, subscriptions, and audit logs. Crate.io is a Speedinvest portfolio company; CrateDB Cloud is certified to ISO 27001 and SOC 2 Type II.
image: https://cratedb.com/hubfs/cr-featured-image-23.jpg
layout: provider
mcp_servers:
- description: ''
  name: crate-io-mcp.yml
  slug: crate-io-mcpyml
modified: '2026-07-18'
name: Crate Io
nav: Providers
network: true
overview: 'Crate Io publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Database, SQL, Distributed Database, and Analytics.


  Crate Io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 68
score:
  band: developing
  composite: 42.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 73.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 47.4
  previous_composite: 42.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crate-io/refs/heads/main/screenshots/crate-io-2026-07-25T210645.png
security:
- kind: authentication
  name: Crate Io Authentication
  slug: crate-io-authentication
  summary_line: http-basic/http-basic-apikey/jwt · 3 schemes
- kind: domain-security
  name: Crate Io Domain Security
  slug: crate-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crate Io Vulnerability Disclosure
  slug: crate-io-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Crate Io Trust Center
  slug: crate-io-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: crate-io
tags:
- Company
- Database
- SQL
- Distributed Database
- Analytics
- Time Series
- Vector Database
- IoT
- Cloud
- Developer Tools
website: https://console.cratedb.cloud/
---
