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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Public REST API for Starburst Galaxy, secured with the OAuth2 client-credentials flow. Manages clusters, catalogs, users, roles, privileges, access-control policies, tags, row filters, column masks, d
  name: Starburst Galaxy REST API
  slug: starburst-galaxy-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.starburst.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devcenter.starburst.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.starburst.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.starburst.io/starburst-galaxy/developer-tools/api/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.starburst.io/starburst-galaxy/get-started.html
- group: operate
  title: ''
  type: Support
  url: https://www.starburst.io/learn/support/
- group: company
  title: ''
  type: Blog
  url: https://www.starburst.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/starburstdata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.starburst.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.starburst.io/free-trial/
- group: start
  title: ''
  type: Login
  url: https://galaxy.starburst.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.starburst.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.starburst.io/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.galaxy.starburst.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.starburst.io/
- group: build
  title: ''
  type: Packages
  url: packages/starburst-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/starburst-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/starburst-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/starburst-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/starburst-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/starburst-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/starburst-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/starburst-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/starburst-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starburst-domain-security.yml
created: '2026-07-17'
description: Starburst is an enterprise data analytics and intelligence platform built on Trino, the open-source distributed SQL query engine. It lets organizations access and query data across disparate systems through a unified context layer — federated analytics with no pipelines or data movement required. Its products include Starburst Galaxy (a fully managed cloud service on AWS, GCP, and Azure), Starburst Enterprise (self-managed for hybrid and on-premises), Icehouse (Apache Iceberg plus Trino for the lakehouse), and AIDA, a conversational AI data assistant. Starburst Galaxy exposes a public REST API secured with OAuth2 client credentials for managing clusters, catalogs, users, roles, privileges, access policies, data products, and SQL jobs.
image: https://www.starburst.io/wp-content/uploads/2021/01/starburst-og.jpg
layout: provider
mcp_servers:
- description: ''
  name: starburst-mcp.yml
  slug: starburst-mcpyml
modified: '2026-07-21'
name: Starburst
nav: Providers
network: true
overview: 'Starburst publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Analytics, Data Lakehouse, SQL Query Engine, and Trino.


  Starburst''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 98
score:
  band: thin
  composite: 36.6
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 36.8
  previous_composite: 36.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Starburst Authentication
  slug: starburst-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Starburst Domain Security
  slug: starburst-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Starburst Trust Center
  slug: starburst-trust-center
  summary_line: trust center published
slug: starburst
tags:
- Company
- Data Analytics
- Data Lakehouse
- SQL Query Engine
- Trino
- Federated Query
- Data Governance
- Business Intelligence
website: https://www.starburst.io/
---
