---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: REST API for the D-Tools Cloud platform. Read, create and update Clients, Products, Opportunities, Quotes, Projects, Change Orders, Purchase Orders, Service Contracts, Files and Time Entries. Requests
  name: D-Tools Cloud API
  slug: d-tools-cloud-api
- description: 'Cloud middleware API that bridges the on-premises or hosted D-Tools System Integrator application to third-party systems. It is a queue, not a live database: publishers POST projects, change orders, t'
  name: D-Tools System Integrator (SI) API
  slug: d-tools-system-integrator-si-api
artifact_total: 7
asyncapis:
- description: ''
  name: D Tools Cloud Webhooks
  slug: d-tools-cloud-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/d-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.d-tools.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.d-tools.cloud/en/collections/7640732-cloud-api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://dtcloudapi.d-tools.cloud/apidocs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.d-tools.cloud/en/articles/9344578-best-practices-for-developing-api-integrations
- group: operate
  title: ''
  type: Support
  url: https://www.d-tools.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.d-tools.cloud/en/
- group: company
  title: ''
  type: Blog
  url: https://www.d-tools.com/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://feedback.d-tools.cloud/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.d-tools.com/cloud-pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.d-tools.com/cloud-free-trial
- group: start
  title: ''
  type: Login
  url: https://d-tools.cloud/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.d-tools.com/d-tools-software-terms-of-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.d-tools.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.d-tools.cloud/
- group: build
  title: ''
  type: Postman
  url: https://docs.d-tools.cloud/en/articles/8756124-using-postman-to-test-api-responses
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/d-tools-cloud-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/d-tools-cloud-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/d-tools-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/d-tools-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/d-tools-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/d-tools-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/d-tools-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/d-tools-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/d-tools-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/d-tools-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/d-tools-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-11'
description: 'D-Tools Inc. builds estimation, system design, project management and field-service software for audio-visual, low-voltage, security and systems-integration contractors. Two products carry two distinct public APIs. D-Tools Cloud is the web-native platform, and its REST API (dtcloudapi.d-tools.cloud) exposes Clients, Products, Opportunities, Quotes, Projects, Change Orders, Purchase Orders, Service Contracts, Files and Time Entries with documented rate limits, webhooks and a downloadable Postman collection. D-Tools System Integrator (SI) is the on-premises/hosted Windows product; because SI itself has no directly reachable API, D-Tools operates a cloud middleware queue at api.d-tools.com/si where third parties publish projects, change orders, tasks, service orders, purchase orders, time sheets, product catalogs, clients and vendors to an SI user and subscribe to what that SI user exports. Both APIs publish machine-readable specifications: OpenAPI 3.1.1 for SI and OpenAPI 3.0.4
  for Cloud.'
image: https://www.d-tools.com/hubfs/D__only_PNG.png
layout: provider
modified: '2026-08-11'
name: D-Tools
nav: Providers
network: true
overview: 'D-Tools publishes 2 APIs on the [APIs.io](https://apis.io/) network: Cloud API and System Integrator (SI) API. Tagged areas include av-integration, systems-integration, project-management, estimation, and quoting.


  The D-Tools catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  D-Tools'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: D Tools Plans Pricing
  plan_count: 6
  slug: d-tools-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 2
  name: D Tools Rate Limits
  slug: d-tools-rate-limits
score:
  band: strong
  composite: 57.8
  facets:
    commercial_clarity: 76.3
    contract_quality: 52.2
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 65.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: D Tools Authentication
  slug: d-tools-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: D Tools Domain Security
  slug: d-tools-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: d-tools
tags:
- av-integration
- systems-integration
- project-management
- estimation
- quoting
- field-service-management
- construction-tech
- low-voltage
- product-catalog
- erp-integration
- vertical-saas
website: https://www.d-tools.com/
---
