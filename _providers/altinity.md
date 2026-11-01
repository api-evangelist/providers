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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://acm.altinity.cloud/api/
  baseurl_source: declared
  description: The Auth API from Altinity — 8 operation(s) for auth.
  name: Altinity Auth API
  slug: altinity-auth-api
artifact_total: 10
collections:
- collection_type: open
  name: Altinity Cloud Manager Auth API
  slug: open-altinity-auth-api
common:
- group: commercial
  href: https://artifacts.apis.io/altinity/plans/altinity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/altinity-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://altinity.com/feed/
- group: other
  href: https://artifacts.apis.io/altinity/overlays/altinity-acm-overlay.yaml
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
  href: https://artifacts.apis.io/altinity/authentication/altinity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/altinity-authentication.yml
- group: build
  href: https://artifacts.apis.io/altinity/packages/altinity-packages.yml
  title: ''
  type: Packages
  url: packages/altinity-packages.yml
- group: build
  href: https://artifacts.apis.io/altinity/packages/altinity-packages.yml
  title: ''
  type: SDKs
  url: packages/altinity-packages.yml
- group: agent
  href: https://artifacts.apis.io/altinity/mcp/altinity-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/altinity-mcp.yml
- group: agent
  href: https://artifacts.apis.io/altinity/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/altinity/llms/altinity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/altinity-llms.txt
- group: design
  href: https://artifacts.apis.io/altinity/lifecycle/altinity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/altinity-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/altinity/changelog/altinity-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/altinity-changelog.yml
- group: design
  href: https://artifacts.apis.io/altinity/conventions/altinity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/altinity-conventions.yml
- group: design
  href: https://artifacts.apis.io/altinity/conformance/altinity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/altinity-conformance.yml
- group: auth
  href: https://artifacts.apis.io/altinity/security/altinity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altinity-domain-security.yml
created: '2026-07-17'
description: Altinity is the enterprise provider for open-source ClickHouse, the real-time analytical database. It builds and operates Altinity.Cloud, a fully managed ClickHouse service available on AWS, GCP, Azure and Hetzner, plus a bring-your-own-cloud (BYOC) option, and delivers 24/7 expert support, performance tuning, and training. Altinity is a leading ClickHouse contributor and maintains widely used open-source tooling including the Altinity Kubernetes Operator for ClickHouse, clickhouse-backup, the clickhouse-sink-connector, a Grafana datasource plugin, Altinity Stable Builds, and an official MCP server for AI agents. Its Altinity Cloud Manager (ACM) exposes a REST API for managing environments and ClickHouse clusters programmatically.
finops:
- has_sources: true
  method: derived
  name: Altinity Finops
  primary_unit: vcpu
  service_category: ''
  slug: altinity-finops
  template: false
image: https://altinity.com/wp-content/uploads/2025/06/sharing-icon.png
layout: provider
mcp_servers:
- description: Official Altinity Model Context Protocol (MCP) server for using ClickHouse databases in AI agents. Written in Go, Apache-2.0. Exposes SQL query execution and dynamically generates tools and resource t
  name: Altinity MCP Server
  slug: altinity-mcp
modified: '2026-10-06'
name: Altinity
nav: Providers
network: true
overview: 'Altinity publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Auth API. Tagged areas include Company, Big Data, ClickHouse, Analytics, and Database.


  Altinity''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Altinity Plans Pricing
  plan_count: 7
  slug: altinity-plans-pricing
- name: Altinity Price Estimates
  plan_count: 0
  slug: altinity-price-estimates
random_paper: 14
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 42.2
    developer_ergonomics: 66.1
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 43.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/altinity/altinity-2026-07-25T195834.png
security:
- kind: authentication
  name: Altinity Authentication
  slug: altinity-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Altinity Domain Security
  slug: altinity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Authenticate to the Altinity Cloud Manager API
  slug: altinity-authenticate
- name: Create an Altinity.Cloud trial account
  slug: altinity-signup-trial
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
