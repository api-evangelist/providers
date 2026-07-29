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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Auth API from Altinity — 8 operation(s) for auth.
  name: Altinity Auth API
  slug: altinity-auth-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://altinity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.altinity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.altinity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://acm.altinity.cloud/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.altinity.com/altinitycloud/altinity-cloud-101/
- group: company
  title: ''
  type: Blog
  url: https://altinity.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/altinity
- group: operate
  title: ''
  type: Support
  url: https://docs.altinity.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://altinity.com/clickhouse-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://acm.altinity.cloud/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altinity.com/wp-content/uploads/2022/09/Altinity.Cloud-Terms-of-Service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altinity.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/altinity-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/altinity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/altinity-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/altinity-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/altinity-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/altinity-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/altinity-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/altinity-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/altinity-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/altinity-domain-security.yml
created: '2026-07-17'
description: Altinity is the enterprise provider for open-source ClickHouse, the real-time analytical database. It builds and operates Altinity.Cloud, a fully managed ClickHouse service available on AWS, GCP, Azure and Hetzner, plus a bring-your-own-cloud (BYOC) option, and delivers 24/7 expert support, performance tuning, and training. Altinity is a leading ClickHouse contributor and maintains widely used open-source tooling including the Altinity Kubernetes Operator for ClickHouse, clickhouse-backup, the clickhouse-sink-connector, a Grafana datasource plugin, Altinity Stable Builds, and an official MCP server for AI agents. Its Altinity Cloud Manager (ACM) exposes a REST API for managing environments and ClickHouse clusters programmatically.
image: https://altinity.com/wp-content/uploads/2025/06/sharing-icon.png
layout: provider
mcp_servers:
- description: ''
  name: altinity-mcp.yml
  slug: altinity-mcpyml
modified: '2026-07-17'
name: Altinity
nav: Providers
network: true
overview: 'Altinity publishes 1 API on the [APIs.io](https://apis.io/) network: Auth API. Tagged areas include Company, Big Data, ClickHouse, Analytics, and Database.


  Altinity''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 16 more developer resources.'
random_paper: 78
score:
  band: developing
  composite: 46.8
  delta: -0.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 49.2
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/altinity/refs/heads/main/screenshots/altinity-2026-07-25T195834.png
security:
- kind: authentication
  name: Altinity Authentication
  slug: altinity-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Altinity Domain Security
  slug: altinity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: altinity
tags:
- Company
- Big Data
- ClickHouse
- Analytics
- Database
- Managed Cloud
- Kubernetes
- Real-Time Analytics
- Open Source
website: https://altinity.com/
---
