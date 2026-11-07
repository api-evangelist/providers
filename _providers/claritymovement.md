---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://clarity-data-api.clarity.io
  baseurl_source: spec
  description: Claritymovement provides air quality monitoring hardware and cloud data services.
  name: Claritymovement API
  slug: claritymovement-api
- baseURL: https://clarity-data-api.clarity.io
  baseurl_source: declared
  description: The Report Requests API from Claritymovement — 2 operation(s) for report requests.
  name: Claritymovement Report Requests API
  slug: claritymovement-report-requests-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/claritymovement/rules/claritymovement-rules.yml
  title: ''
  type: Spectral
  url: rules/claritymovement-rules.yml
- group: design
  href: https://artifacts.apis.io/claritymovement/json-ld/claritymovement-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/claritymovement-context.jsonld
- group: design
  href: https://artifacts.apis.io/claritymovement/vocabulary/claritymovement-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/claritymovement-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/claritymovement/data-model/claritymovement-data-model.yml
  title: ''
  type: DataModel
  url: data-model/claritymovement-data-model.yml
- group: operate
  href: https://artifacts.apis.io/claritymovement/changelog/claritymovement-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/claritymovement-changelog.yml
- group: operate
  href: https://artifacts.apis.io/claritymovement/lifecycle/claritymovement-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/claritymovement-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/claritymovement/lifecycle/claritymovement-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/claritymovement-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/claritymovement/conformance/claritymovement-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claritymovement-conformance.yml
- group: agent
  href: https://artifacts.apis.io/claritymovement/llms/claritymovement-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claritymovement-llms.txt
- group: agent
  href: https://artifacts.apis.io/claritymovement/well-known/claritymovement-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claritymovement-well-known.yml
- group: other
  href: https://artifacts.apis.io/claritymovement/hosts/claritymovement-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claritymovement-hosts.yml
- group: other
  href: https://artifacts.apis.io/claritymovement/vendors/claritymovement-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claritymovement-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.clarity.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clarity.io/
- group: start
  title: ''
  type: SignUp
  url: https://www.clarity.io/landing-pages/register-for-awma-panel-best-practices-for-the-use-of-low-cost-sensors-to-expand-air-quality-monitoring-coverage-in-the-urban-environment
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clarity.io/privacy-consent-pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.clarity.io/media
- group: company
  title: ''
  type: Blog
  url: https://www.clarity.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.clarity.io/getting-started.html
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.clarity.io/
- group: auth
  href: https://artifacts.apis.io/claritymovement/security/claritymovement-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claritymovement-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clarity.io
coverage:
  checked: '2026-10-08'
  detail: Homepage loads content via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.clarity.io
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Claritymovement (Clarity Movement Co.) provides low‑cost air quality monitoring hardware and cloud‑based data services. Leveraging IoT sensors, data analytics, and a global network, they enable governments, businesses, and communities to measure and improve air quality. Their solutions include multi‑gas modules, wind modules, black‑carbon and dust sensors, and a SaaS platform for real‑time monitoring, reporting, and compliance across 85+ countries.
image: https://cdn.prod.website-files.com/5f64f95d58facb3cb9ddca5b/695f2817eef260d75a742c0a_Crop_Chicago_Node_Installed_Blue_Sky.avif
json_schemas:
- name: GetV2ReportRequestsReportidResponse
  property_count: 6
  slug: claritymovement-get-v2-report-requests-reportid-response
jsonld:
- class_count: 1
  name: Claritymovement Context
  property_count: 6
  slug: claritymovement-context
layout: provider
modified: '2026-10-08'
name: Claritymovement
nav: Providers
network: true
overview: 'Claritymovement is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Report Requests API, and 1 more. Tagged areas include Company, Air Quality, IoT, Sensors, and Data Analytics.


  The Claritymovement catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Claritymovement''s developer surface includes changelog, support, signup flow, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Claritymovement API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: claritymovement-rules
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 14.3
    discoverability: 65.2
    operational_transparency: 31.6
  previous_composite: 28.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/claritymovement/claritymovement-2026-11-03T124316.png
security:
- kind: domain-security
  name: Claritymovement Domain Security
  slug: claritymovement-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: claritymovement
tags:
- Company
- Air Quality
- IoT
- Sensors
- Data Analytics
website: https://www.clarity.io
---
