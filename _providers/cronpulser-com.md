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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: CronPulser provides a REST API for managing scheduled jobs and execution logs.
  name: CronPulser API
  slug: cronpulser-api
- baseURL: https://api.cronpulser.com
  baseurl_source: declared
  description: 'CronPulser API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: CronPulser API
  slug: cronpulser-com-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/cronpulser-com/rate-limits/cronpulser-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cronpulser-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cronpulser-com/plans/cronpulser-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cronpulser-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cronpulser-com/rules/cronpulser-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cronpulser-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cronpulser-com/json-ld/cronpulser-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cronpulser-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cronpulser-com/vocabulary/cronpulser-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cronpulser-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cronpulser-com/data-model/cronpulser-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cronpulser-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cronpulser-com/conventions/cronpulser-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cronpulser-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cronpulser.com/security/
- group: auth
  href: https://artifacts.apis.io/cronpulser-com/authentication/cronpulser-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cronpulser-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/cronpulser-com/conformance/cronpulser-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cronpulser-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cronpulser-com/llms/cronpulser-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cronpulser-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cronpulser-com/well-known/cronpulser-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cronpulser-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cronpulser-com/hosts/cronpulser-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cronpulser-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cronpulser-com/vendors/cronpulser-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cronpulser-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cronpulser.com/terms/
- group: auth
  title: ''
  type: Security
  url: https://cronpulser.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cronpulser.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cronpulser
- group: start
  title: ''
  type: GettingStarted
  url: https://cronpulser.com/docs/runner/
- group: auth
  href: https://artifacts.apis.io/cronpulser-com/security/cronpulser-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cronpulser-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cronpulser-com/security/cronpulser-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cronpulser-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cronpulser-com/security/cronpulser-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cronpulser-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cronpulser.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cronpulser.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://cronpulser.com/docs/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://cronpulser.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://cronpulser.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://app.cronpulser.com/register
- group: other
  title: ''
  type: SignIn
  url: https://app.cronpulser.com/login
coverage:
  checked: '2026-11-04'
  detail: API requires an API key and authentication, no public contract discovered.
  evidence:
  - status: 404
    url: https://api.cronpulser.com/openapi.json
  reason: auth-required
  state: gated
created: '2026-11-04'
description: 'cronpulser-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://cronpulser.com/cronpulser-social-card.png
json_schemas:
- name: GetJobsIdLogsExecutionidResponse
  property_count: 11
  slug: cronpulser-com-get-jobs-id-logs-executionid-response
- name: GetJobsIdLogsResponse
  property_count: 4
  slug: cronpulser-com-get-jobs-id-logs-response
- name: GetJobsIdResponse
  property_count: 15
  slug: cronpulser-com-get-jobs-id-response
- name: PostJobsRequest
  property_count: 8
  slug: cronpulser-com-post-jobs-request
- name: PostJobsResponse
  property_count: 15
  slug: cronpulser-com-post-jobs-response
- name: PutJobsIdRequest
  property_count: 11
  slug: cronpulser-com-put-jobs-id-request
jsonld:
- class_count: 11
  name: Cronpulser Com Context
  property_count: 32
  slug: cronpulser-com-context
layout: provider
modified: '2026-11-04'
name: CronPulser
nav: Providers
network: true
overview: 'CronPulser is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include HTTP Scheduler, API Scheduling, runner, and TLS Monitoring.


  The CronPulser catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CronPulser''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, engineering blog, signup flow, and 22 more developer resources.'
plans:
- name: Cronpulser Com Plans Pricing
  plan_count: 3
  slug: cronpulser-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Cronpulser Com Rate Limits
  slug: cronpulser-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: CronPulser API Rules
  rule_count: 46
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 3
  slug: cronpulser-com-rules
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 67.8
    catalog_earned_first_party: 20.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 26.1
    developer_ergonomics: 42.9
    discoverability: 39.3
    operational_transparency: 36.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cronpulser Com Authentication
  slug: cronpulser-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cronpulser Com Domain Security
  slug: cronpulser-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cronpulser Com Vulnerability Disclosure
  slug: cronpulser-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cronpulser Com Trust Center
  slug: cronpulser-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: cronpulser-com
tags:
- HTTP Scheduler
- API Scheduling
- runner
- TLS Monitoring
website: https://cronpulser.com/
---
