---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-10-04'
api_count: 4
apis:
- description: Coralogix is an observability platform providing log analytics, metrics, tracing, and AI-powered insights.
  name: Coralogix
  slug: coralogix
- baseURL: https://api.eu2.coralogix.com
  baseurl_source: declared
  description: The Dashboards API from Coralogix — 7 operation(s) for dashboards.
  name: Coralogix Dashboards API
  slug: coralogix-dashboards-api
- baseURL: https://api.eu2.coralogix.com
  baseurl_source: declared
  description: The Dataprime API from Coralogix — 2 operation(s) for dataprime.
  name: Coralogix Dataprime API
  slug: coralogix-dataprime-api
- baseURL: https://api.eu2.coralogix.com
  baseurl_source: declared
  description: The Mgmt API from Coralogix — 1 operation(s) for mgmt.
  name: Coralogix Mgmt API
  slug: coralogix-mgmt-api
artifact_total: 19
asyncapis:
- description: AsyncAPI description of Coralogix's publicly documented streaming and event-driven surfaces. This document covers only what Coralogix publishes in https://coralogix.com/docs/ and does not enumerate un
  name: Coralogix Streaming Surfaces
  slug: coralogix-asyncapi
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/finops/coralogix-finops.yml
  title: ''
  type: FinOps
  url: finops/coralogix-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/rate-limits/coralogix-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coralogix-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/plans/coralogix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coralogix-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/rules/coralogix-rules.yml
  title: ''
  type: Spectral
  url: rules/coralogix-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/rules/coralogix-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/coralogix-asyncapi-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/json-ld/coralogix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coralogix-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/vocabulary/coralogix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coralogix-vocabulary.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/asyncapi/coralogix-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/coralogix-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/data-model/coralogix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coralogix-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/changelog/coralogix-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/coralogix-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.coralogix.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/conformance/coralogix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coralogix-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/llms/coralogix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coralogix-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/a2a/coralogix-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/coralogix-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/well-known/coralogix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coralogix-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/hosts/coralogix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coralogix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/vendors/coralogix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coralogix-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/packages/coralogix-packages.yml
  title: ''
  type: SDKs
  url: packages/coralogix-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/packages/coralogix-packages.yml
  title: ''
  type: Packages
  url: packages/coralogix-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://coralogix.com/newsroom/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://coralogix.com/developers/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/security/coralogix-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/coralogix-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/security/coralogix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coralogix-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coralogix
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coralogix
- group: company
  title: ''
  type: Website
  url: https://coralogix.com
- group: docs
  title: ''
  type: Documentation
  url: https://coralogix.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://coralogix.com/docs/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://coralogix.com/docs/user-guides/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://coralogix.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://coralogix.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://signup.coralogix.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coralogix.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coralogix.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://coralogix.com/feed/
created: '2026-03-27'
description: Coralogix is a comprehensive observability platform that delivers real‑time log analytics, metrics, tracing, and AI‑driven insights. It enables developers, DevOps, and SRE teams to monitor applications, infrastructure, and services across cloud, on‑premise, and hybrid environments. Features include infinite data retention, customizable dashboards, alerting, OpenTelemetry support, and integrations with major cloud providers and third‑party tools, helping organizations ensure performance, reliability, and security at scale.
finops:
- name: Coralogix Finops
  service_category: API
  slug: coralogix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coralogix.png
json_schemas:
- name: GetDashboardsDashboardsV1DashboardidResponse
  property_count: 14
  slug: coralogix-get-dashboards-dashboards-v1-dashboardid-response
- name: GetDashboardsDashboardsV1SlugsSlugResponse
  property_count: 14
  slug: coralogix-get-dashboards-dashboards-v1-slugs-slug-response
- name: PostDashboardsDashboardsV1Request
  property_count: 14
  slug: coralogix-post-dashboards-dashboards-v1-request
- name: PostDashboardsDashboardsV1Response
  property_count: 14
  slug: coralogix-post-dashboards-dashboards-v1-response
- name: PostMgmtOpenapi5Request
  property_count: 9
  slug: coralogix-post-mgmt-openapi5-request
- name: PutDashboardsDashboardsV1Request
  property_count: 14
  slug: coralogix-put-dashboards-dashboards-v1-request
jsonld:
- class_count: 15
  name: Coralogix Context
  property_count: 29
  slug: coralogix-context
layout: provider
modified: '2026-05-29'
name: Coralogix
nav: Providers
network: true
overview: 'Coralogix publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Coralogix, Dashboards API, Dataprime API, and 1 more. Tagged areas include AIOps, Observability, Monitoring, Cloud, and DevOps.


  The Coralogix catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Coralogix''s developer surface includes changelog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Coralogix Plans Pricing
  plan_count: 3
  slug: coralogix-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Coralogix Rate Limits
  slug: coralogix-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Coralogix API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: coralogix-asyncapi-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Coralogix API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: coralogix-rules
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 69.8
    catalog_earned_first_party: 0.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 27.7
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 35.1
    developer_ergonomics: 52.4
    discoverability: 71.4
    operational_transparency: 26.3
  previous_composite: 23.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/coralogix/refs/heads/main/screenshots/coralogix-2026-06-20T175022.png
security:
- kind: domain-security
  name: Coralogix Domain Security
  slug: coralogix-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Coralogix Trust Center
  slug: coralogix-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR
slug: coralogix
tags:
- AIOps
- Observability
- Monitoring
- Cloud
- DevOps
website: https://coralogix.com
---
