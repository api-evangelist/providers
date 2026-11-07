---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 148
  human_in_the_loop: 21
  name: Monacloud Agentic Access
  operation_count: 258
  slug: monacloud-agentic-access
  summary_line: 258 operations · 148 acting · 21 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.monacloud.vn
  baseurl_source: declared
  description: Deploy app từ git hoặc thư mục local và quản lý app host / Deploy git or local source and manage Dokploy hosts.
  name: The MONA Group Apps API
  slug: monacloud-apps-api
- baseURL: https://api.monacloud.vn
  baseurl_source: declared
  description: Đăng nhập, token và tài khoản.
  name: The MONA Group Auth API
  slug: monacloud-auth-api
- baseURL: https://api.monacloud.vn
  baseurl_source: declared
  description: Thanh toán, số dư và hạn mức.
  name: The MONA Group Billing API
  slug: monacloud-billing-api
- baseURL: https://api.monacloud.vn
  baseurl_source: declared
  description: Tạo và quản lý database.
  name: The MONA Group Databases API
  slug: monacloud-databases-api
- baseURL: https://api.monacloud.vn
  baseurl_source: declared
  description: Theo dõi tác vụ bất đồng bộ.
  name: The MONA Group Jobs API
  slug: monacloud-jobs-api
- baseURL: https://api.monacloud.vn
  baseurl_source: declared
  description: Tạo và quản lý VPS LXC.
  name: The MONA Group Lxc API
  slug: monacloud-lxc-api
- baseURL: https://api.monacloud.vn
  baseurl_source: declared
  description: Bảng giá và gói tài nguyên.
  name: The MONA Group Prices API
  slug: monacloud-prices-api
- baseURL: https://api.monacloud.vn
  baseurl_source: declared
  description: Thử API miễn phí, không tạo hạ tầng thật.
  name: The MONA Group Sandbox API
  slug: monacloud-sandbox-api
- baseURL: https://api.monacloud.vn
  baseurl_source: declared
  description: Dịch vụ và dữ liệu vận hành.
  name: The MONA Group Services API
  slug: monacloud-services-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/monacloud/agentic-access/monacloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/monacloud-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/monacloud/rate-limits/monacloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/monacloud-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/monacloud/plans/monacloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/monacloud-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/monacloud/rules/monacloud-rules.yml
  title: ''
  type: Spectral
  url: rules/monacloud-rules.yml
- group: design
  href: https://artifacts.apis.io/monacloud/json-ld/monacloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/monacloud-context.jsonld
- group: design
  href: https://artifacts.apis.io/monacloud/vocabulary/monacloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/monacloud-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/monacloud/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/monacloud/data-model/monacloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/monacloud-data-model.yml
- group: build
  href: https://artifacts.apis.io/monacloud/cli/monacloud-cli.yml
  title: ''
  type: CLI
  url: cli/monacloud-cli.yml
- group: operate
  href: https://artifacts.apis.io/monacloud/changelog/monacloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/monacloud-changelog.yml
- group: start
  href: https://artifacts.apis.io/monacloud/sandbox/monacloud-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/monacloud-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://monacloud.vn/bao-mat/cam-on
- group: auth
  href: https://artifacts.apis.io/monacloud/authentication/monacloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/monacloud-authentication.yml
- group: design
  href: https://artifacts.apis.io/monacloud/errors/monacloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/monacloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/monacloud/conformance/monacloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/monacloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/monacloud/llms/monacloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/monacloud-llms.txt
- group: auth
  href: https://artifacts.apis.io/monacloud/well-known/monacloud-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/monacloud-security.txt
- group: auth
  href: https://artifacts.apis.io/monacloud/well-known/monacloud-beta-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/monacloud-beta-security.txt
- group: agent
  href: https://artifacts.apis.io/monacloud/well-known/monacloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/monacloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/monacloud/hosts/monacloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/monacloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/monacloud/vendors/monacloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/monacloud-vendors.yml
- group: build
  href: https://artifacts.apis.io/monacloud/packages/monacloud-packages.yml
  title: ''
  type: SDKs
  url: packages/monacloud-packages.yml
- group: build
  href: https://artifacts.apis.io/monacloud/packages/monacloud-packages.yml
  title: ''
  type: Packages
  url: packages/monacloud-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://monacloud.vn/status
- group: operate
  title: ''
  type: Roadmap
  url: https://monacloud.vn/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monacloud.vn/en/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://monacloud.vn/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.monacloud.vn&quot;
- group: auth
  href: https://artifacts.apis.io/monacloud/security/monacloud-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/monacloud-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/monacloud/security/monacloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monacloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://monacloud.vn/
- group: docs
  title: ''
  type: Documentation
  url: https://monacloud.vn/docs
- group: docs
  title: ''
  type: APIReference
  url: https://monacloud.vn/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://monacloud.vn/docs/bat-dau-nhanh
- group: commercial
  title: ''
  type: Pricing
  url: https://monacloud.vn/bang-gia
created: '2026-10-18'
description: The MONA Group, operating under the brand MONA Cloud, provides a suite of cloud services and developer tools for Vietnamese developers. It offers VPS hosting, managed databases, AI‑assisted deployment agents, and a Marketplace Cloud Platform (MCP) with CLI and API access. The platform targets VibeCoder and other local developers, delivering pay‑as‑you‑go pricing, AI‑driven project estimation, and integrations for popular frameworks. Documentation is available in Vietnamese, covering quick‑start guides, API reference, pricing, and sandbox environments.
image: https://monacloud.vn/assets/og/home.jpg?v=10
json_schemas:
- name: AdminPlanUpsertRequest
  property_count: 11
  slug: monacloud-admin-plan-upsert-request
- name: AppCreateRequest
  property_count: 9
  slug: monacloud-app-create-request
- name: AppResponse
  property_count: 16
  slug: monacloud-app-response
- name: DomainRegistrant
  property_count: 14
  slug: monacloud-domain-registrant
- name: DomainReserveRequest
  property_count: 8
  slug: monacloud-domain-reserve-request
- name: JobResponse
  property_count: 12
  slug: monacloud-job-response
- name: LxcCreateRequest
  property_count: 9
  slug: monacloud-lxc-create-request
- name: ServiceResponse
  property_count: 25
  slug: monacloud-service-response
jsonld:
- class_count: 76
  name: Monacloud Context
  property_count: 189
  slug: monacloud-context
layout: provider
modified: '2026-10-18'
name: The MONA Group
nav: Providers
network: true
overview: 'The MONA Group publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, Auth API, Billing API, and 6 more. Tagged areas include Cloud, Hosting, Developer Tools, Vietnamese, and Artificial Intelligence.


  The The MONA Group catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The MONA Group''s developer surface includes CLI, changelog, sandbox, authentication, documentation, API reference, getting-started guide, and 28 more developer resources.'
plans:
- name: Monacloud Plans Pricing
  plan_count: 4
  slug: monacloud-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Monacloud Rate Limits
  slug: monacloud-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: The MONA Group API Rules
  rule_count: 58
  severity_counts:
    error: 46
    hint: 0
    info: 3
    warn: 9
  slug: monacloud-rules
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 65.4
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 44.7
  previous_composite: 63.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/monacloud/monacloud-2026-11-03T135820.png
security:
- kind: authentication
  name: Monacloud Authentication
  slug: monacloud-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Monacloud Domain Security
  slug: monacloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Monacloud Vulnerability Disclosure
  slug: monacloud-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: monacloud-billing-create-and-check-vietqr-payment
  slug: monacloud-billing-create-and-check-vietqr-payment
- name: monacloud-create-and-deploy-app
  slug: monacloud-create-and-deploy-app
- name: monacloud-databases-provision
  slug: monacloud-databases-provision
- name: monacloud-manage-service
  slug: monacloud-manage-service
- name: monacloud-monitor-job-status
  slug: monacloud-monitor-job-status
slug: monacloud
tags:
- Cloud
- Hosting
- Developer Tools
- Vietnamese
- Artificial Intelligence
website: https://monacloud.vn/
---
