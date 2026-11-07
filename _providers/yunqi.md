---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.clickzetta.com
  baseurl_source: declared
  description: 数据源连接管理
  name: Yunqi (ClickZetta / Singdata Lakehouse) Data Source API
  slug: yunqi-datasource-api
- baseURL: https://api.clickzetta.com
  baseurl_source: declared
  description: 数据质量规则管理
  name: Yunqi (ClickZetta / Singdata Lakehouse) Dqc API
  slug: yunqi-dqc-api
- baseURL: https://api.clickzetta.com
  baseurl_source: declared
  description: 实例管理
  name: Yunqi (ClickZetta / Singdata Lakehouse) Instance API
  slug: yunqi-instance-api
- baseURL: https://api.clickzetta.com
  baseurl_source: declared
  description: 库表同步任务管理
  name: Yunqi (ClickZetta / Singdata Lakehouse) Multi Realtime Di Task API
  slug: yunqi-multirealtimeditask-api
- baseURL: https://api.clickzetta.com
  baseurl_source: declared
  description: 实时任务管理
  name: Yunqi (ClickZetta / Singdata Lakehouse) Realtime Task API
  slug: yunqi-realtimetask-api
- baseURL: https://api.clickzetta.com
  baseurl_source: declared
  description: 调度任务与组合任务管理
  name: Yunqi (ClickZetta / Singdata Lakehouse) Schedule Task API
  slug: yunqi-scheduletask-api
- baseURL: https://api.clickzetta.com
  baseurl_source: declared
  description: 用户管理
  name: Yunqi (ClickZetta / Singdata Lakehouse) User Management API
  slug: yunqi-user-management-api
- baseURL: https://api.clickzetta.com
  baseurl_source: declared
  description: 虚拟集群管理
  name: Yunqi (ClickZetta / Singdata Lakehouse) Virtual Cluster API
  slug: yunqi-virtualcluster-api
- baseURL: https://api.clickzetta.com
  baseurl_source: declared
  description: 工作空间管理
  name: Yunqi (ClickZetta / Singdata Lakehouse) Workspace API
  slug: yunqi-workspace-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/yunqi/plans/yunqi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yunqi-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.yunqi.tech
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.yunqi.tech/documents
- group: docs
  title: ''
  type: Documentation
  url: https://www.singdata.com/documents
- group: docs
  title: ''
  type: APIReference
  url: https://www.yunqi.tech/documents/python_reference/connector
- group: start
  title: ''
  type: GettingStarted
  url: https://www.singdata.com/documents/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yunqi.tech/documents/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.yunqi.tech/resource/blogs
- group: start
  title: ''
  type: SignUp
  url: https://accounts.clickzetta.com/register
- group: start
  title: ''
  type: Login
  url: https://accounts.clickzetta.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.singdata.com/documents/service-aggrement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.singdata.com/documents/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clickzetta
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.yunqi.tech/documents/releasenotes
- group: build
  href: https://artifacts.apis.io/yunqi/packages/yunqi-packages.yml
  title: ''
  type: Packages
  url: packages/yunqi-packages.yml
- group: build
  href: https://artifacts.apis.io/yunqi/packages/yunqi-packages.yml
  title: ''
  type: SDKs
  url: packages/yunqi-packages.yml
- group: build
  href: https://artifacts.apis.io/yunqi/cli/yunqi-cli.yml
  title: ''
  type: CLI
  url: cli/yunqi-cli.yml
- group: agent
  href: https://artifacts.apis.io/yunqi/mcp/yunqi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/yunqi-mcp.yml
- group: agent
  href: https://artifacts.apis.io/yunqi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/yunqi/llms/yunqi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yunqi-llms.txt
- group: auth
  href: https://artifacts.apis.io/yunqi/authentication/yunqi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yunqi-authentication.yml
- group: design
  href: https://artifacts.apis.io/yunqi/lifecycle/yunqi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/yunqi-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/yunqi/changelog/yunqi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/yunqi-changelog.yml
- group: design
  href: https://artifacts.apis.io/yunqi/conformance/yunqi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yunqi-conformance.yml
- group: auth
  href: https://artifacts.apis.io/yunqi/security/yunqi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yunqi-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://cn-shanghai-alicloud-mcp.api.clickzetta.com/mcp
created: '2026-07-17'
description: Yunqi (云器科技, English brands ClickZetta and Singdata) is a cloud-native AI Lakehouse company that unifies structured, semi-structured, and unstructured data on Apache Iceberg behind a single vectorized SQL engine. Its proprietary Generic Incremental Computation (GIC) model powers Dynamic Table pipelines, compute-storage separation, and native AI capabilities such as vector search, LLM functions, and Semantic Views. The platform is consumed programmatically through JDBC, an official Python connector (PEP 249), a Java SDK, the ZettaPark DataFrame API, a dbt adapter, a SQLAlchemy dialect, a Go client, and an AI-agent-friendly CLI, delivered as a fully managed SaaS on Alibaba Cloud, Tencent Cloud, and AWS. Backed by Qiming Venture Partners.
image: https://www.yunqi.tech/favicon.ico
layout: provider
mcp_servers:
- description: Model Context Protocol server for ClickZetta Lakehouse. Lets AI assistants (Claude Desktop, Trae) run SQL queries against a ClickZetta Lakehouse and manage a memo of data insights exposed as an MCP re
  name: Yunqi (ClickZetta / Singdata Lakehouse) MCP Server
  slug: mcp-clickzetta-server
- description: 'Official Studio-managed MCP server (Streamable HTTP; X-Lakehouse-Token PAT). Setup: https://yunqi.tech/documents/studio-mcp-setup-guide'
  name: Yunqi (ClickZetta / Singdata Lakehouse) MCP Server
  slug: mcp
modified: '2026-07-21'
name: Yunqi (ClickZetta / Singdata Lakehouse)
nav: Providers
network: true
overview: 'Yunqi (ClickZetta / Singdata Lakehouse) publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data Source API, Dqc API, Instance API, and 6 more. Tagged areas include Company, Data, Lakehouse, Analytics, and SQL.


  Yunqi (ClickZetta / Singdata Lakehouse)''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, changelog, and 19 more developer resources.'
plans:
- name: Yunqi Plans Pricing
  plan_count: 0
  slug: yunqi-plans-pricing
random_paper: 14
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.6
  facets:
    access_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 47.1
    developer_ergonomics: 73.8
    discoverability: 73.2
    operational_transparency: 18.4
  previous_composite: 32.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/yunqi/yunqi-2026-09-02T171409.png
security:
- kind: authentication
  name: Yunqi Authentication
  slug: yunqi-authentication
  summary_line: username-password/key-pair/oauth2 · 3 schemes
- kind: domain-security
  name: Yunqi Domain Security
  slug: yunqi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yunqi
tags:
- Company
- Data
- Lakehouse
- Analytics
- SQL
- Cloud
- Data Engineering
- Artificial Intelligence
- Apache Iceberg
- Database
website: https://www.yunqi.tech
---
