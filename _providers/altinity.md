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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://acm.altinity.cloud/api/
  baseurl_source: declared
  description: The Auth API from Altinity — 8 operation(s) for auth.
  name: Altinity Auth API
  slug: altinity-auth-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Altinity Cloud Manager Auth API
  slug: open-altinity-auth-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/altinity-acm-overlay.yaml
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
- description: Official Altinity Model Context Protocol (MCP) server for using ClickHouse databases in AI agents. Written in Go, Apache-2.0. Exposes SQL query execution and dynamically generates tools and resource t
  name: Altinity MCP Server
  slug: altinity-mcp-server
modified: '2026-07-17'
name: Altinity
nav: Providers
network: true
overview: 'Altinity publishes 1 API on the [APIs.io](https://apis.io/) network: Auth API. Tagged areas include Company, Big Data, ClickHouse, Analytics, and Database.


  Altinity''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 17 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 46.9
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 41.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Open-Source
website: https://altinity.com/
---
