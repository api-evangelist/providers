---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.databox.com
  baseurl_source: declared
  description: 'Databox API as documented publicly: 103 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Databox API
  slug: databox-api
artifact_total: 16
common:
- group: auth
  href: https://artifacts.apis.io/databox/well-known/databox-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/databox-status-security.txt
- group: operate
  href: https://artifacts.apis.io/databox/rate-limits/databox-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/databox-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/databox/plans/databox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/databox-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/databox/rules/databox-rules.yml
  title: ''
  type: Spectral
  url: rules/databox-rules.yml
- group: design
  href: https://artifacts.apis.io/databox/json-ld/databox-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/databox-context.jsonld
- group: design
  href: https://artifacts.apis.io/databox/vocabulary/databox-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/databox-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/databox/data-model/databox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/databox-data-model.yml
- group: operate
  href: https://artifacts.apis.io/databox/changelog/databox-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/databox-changelog.yml
- group: design
  href: https://artifacts.apis.io/databox/conventions/databox-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/databox-conventions.yml
- group: design
  href: https://artifacts.apis.io/databox/conventions/databox-conventions.yml
  title: ''
  type: Conventions
  url: conventions/databox-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.databox.com/
- group: auth
  href: https://artifacts.apis.io/databox/security/databox-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/databox-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/databox/authentication/databox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/databox-authentication.yml
- group: design
  href: https://artifacts.apis.io/databox/conformance/databox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/databox-conformance.yml
- group: agent
  href: https://artifacts.apis.io/databox/llms/databox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/databox-llms.txt
- group: other
  href: https://artifacts.apis.io/databox/a2a/databox-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/databox-a2a.yml
- group: agent
  href: https://artifacts.apis.io/databox/mcp/databox-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/databox-mcp.yml
- group: auth
  href: https://artifacts.apis.io/databox/well-known/databox-updates-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/databox-updates-security.txt
- group: auth
  href: https://artifacts.apis.io/databox/well-known/databox-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/databox-security.txt
- group: auth
  href: https://artifacts.apis.io/databox/well-known/databox-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/databox-app-security.txt
- group: auth
  href: https://artifacts.apis.io/databox/well-known/databox-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/databox-api-security.txt
- group: agent
  href: https://artifacts.apis.io/databox/well-known/databox-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/databox-well-known.yml
- group: other
  href: https://artifacts.apis.io/databox/hosts/databox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/databox-hosts.yml
- group: other
  href: https://artifacts.apis.io/databox/vendors/databox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/databox-vendors.yml
- group: build
  href: https://artifacts.apis.io/databox/packages/databox-packages.yml
  title: ''
  type: SDKs
  url: packages/databox-packages.yml
- group: build
  href: https://artifacts.apis.io/databox/packages/databox-packages.yml
  title: ''
  type: Packages
  url: packages/databox-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.databox.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.databox.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.databox.com/docs/api/changelog
- group: company
  title: ''
  type: Blog
  url: https://databox.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/databox
- group: auth
  href: https://artifacts.apis.io/databox/security/databox-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/databox-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/databox/security/databox-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/databox-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/databox/security/databox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/databox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://databox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.databox.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.databox.com/docs/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.databox.com/docs/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://databox.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://databox.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://databox.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://databox.com/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Documentation is available at https://developers.databox.com/docs/api/overview but provides no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract.
  evidence:
  - status: 200
    url: https://developers.databox.com/docs/api/overview
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Databox provides an agentic analytics platform designed for agencies and teams to harness live data with AI-driven insights. The platform offers AI Analyst for natural language queries, automation of recurring analyses, a semantic layer for unified metric definitions, and robust data governance. With integrations to over 130 tools, spreadsheets, databases, and APIs, Databox enables trusted AI analysis, customizable dashboards, and collaborative reporting, empowering businesses to make data‑driven decisions at scale.
image: https://cdnwebsite.databox.com/wp-content/uploads/2026/09/07082959/databox-og-agentic-analytics-platform-2026.png
json_schemas:
- name: GetV2DataSourcesResponse
  property_count: 3
  slug: databox-get-v2-data-sources-response
- name: PostV1DataSourcesRequest
  property_count: 3
  slug: databox-post-v1-data-sources-request
- name: PostV1DatasetsRequest
  property_count: 3
  slug: databox-post-v1-datasets-request
- name: PostV1DatasetsResponse
  property_count: 5
  slug: databox-post-v1-datasets-response
- name: PostV2DatasetsRequest
  property_count: 4
  slug: databox-post-v2-datasets-request
- name: PostV2DatasetsResponse
  property_count: 3
  slug: databox-post-v2-datasets-response
jsonld:
- class_count: 14
  name: Databox Context
  property_count: 13
  slug: databox-context
layout: provider
mcp_servers:
- description: Remote MCP server at developers.databox.com.
  name: Databox MCP Server
  slug: databox-mcp-yml
modified: '2026-10-29'
name: Databox
nav: Providers
network: true
overview: 'Databox is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Artificial Intelligence, Data Integration, and Business Intelligence.


  The Databox catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Databox''s developer surface includes changelog, authentication, support, engineering blog, documentation, getting-started guide, pricing, and 35 more developer resources.'
plans:
- name: Databox Plans Pricing
  plan_count: 6
  slug: databox-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Databox Rate Limits
  slug: databox-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Databox API Rules
  rule_count: 47
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 3
  slug: databox-rules
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.4
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 30.7
    developer_ergonomics: 38.1
    discoverability: 75.0
    operational_transparency: 50.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 58.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/databox/databox-2026-11-03T130131.png
security:
- kind: authentication
  name: Databox Authentication
  slug: databox-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Databox Domain Security
  slug: databox-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Databox Vulnerability Disclosure
  slug: databox-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Databox Trust Center
  slug: databox-trust-center
  summary_line: SOC 2, GDPR
slug: databox
tags:
- Company
- Analytics
- Artificial Intelligence
- Data Integration
- Business Intelligence
website: https://databox.com/
---
