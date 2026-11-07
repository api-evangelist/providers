---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://dashboard.chartsy.app
  baseurl_source: declared
  description: 'Chartsy API as documented publicly: 68 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Chartsy API
  slug: chartsy-app-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/chartsy-app/plans/chartsy-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chartsy-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chartsy-app/rules/chartsy-app-rules.yml
  title: ''
  type: Spectral
  url: rules/chartsy-app-rules.yml
- group: design
  href: https://artifacts.apis.io/chartsy-app/json-ld/chartsy-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chartsy-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/chartsy-app/vocabulary/chartsy-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chartsy-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chartsy-app/data-model/chartsy-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chartsy-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/chartsy-app/conformance/chartsy-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chartsy-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chartsy-app/llms/chartsy-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chartsy-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/chartsy-app/well-known/chartsy-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chartsy-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/chartsy-app/hosts/chartsy-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chartsy-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/chartsy-app/vendors/chartsy-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chartsy-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chartsy.app/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chartsy.app/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://dashboard.chartsy.app/login
- group: start
  title: ''
  type: GettingStarted
  url: https://chartsy.app/getting-started/saas
- group: docs
  title: ''
  type: Documentation
  url: https://help.chartsy.app/
- group: auth
  href: https://artifacts.apis.io/chartsy-app/security/chartsy-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chartsy-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chartsy.app/
- group: company
  title: ''
  type: Blog
  url: https://chartsy.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://chartsy.app/saas/pricing
- group: company
  title: ''
  type: About
  url: https://chartsy.app/about
- group: operate
  title: ''
  type: Support
  url: https://chartsy.app/ai-policy
coverage:
  checked: '2026-11-03'
  detail: The provider's website renders pages via JavaScript, preventing machine‑readable extraction of an API contract.
  evidence:
  - status: 200
    url: https://chartsy.app/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Chartsy provides an easy MRR dashboard for SaaS founders, integrating with Stripe, Paddle and other payment platforms. It helps track revenue, subscription analytics, churn, and marketing attribution, offering clear insights from first visit to paid customer.
image: https://chartsy.app/images/chartsy_og_image.png
json_schemas:
- name: GetEventsCancellationsRecentResponse
  property_count: 14
  slug: chartsy-app-get-events-cancellations-recent-response
- name: GetEventsDailySnapshotsOneResponse
  property_count: 27
  slug: chartsy-app-get-events-daily-snapshots-one-response
- name: GetEventsDailySummariesTheResponse
  property_count: 27
  slug: chartsy-app-get-events-daily-summaries-the-response
- name: GetEventsGoalsReachedTheResponse
  property_count: 12
  slug: chartsy-app-get-events-goals-reached-the-response
- name: GetReportsDailySummaryOneResponse
  property_count: 27
  slug: chartsy-app-get-reports-daily-summary-one-response
- name: PostTransactionsRequest
  property_count: 26
  slug: chartsy-app-post-transactions-request
jsonld:
- class_count: 61
  name: Chartsy App Context
  property_count: 156
  slug: chartsy-app-context
layout: provider
modified: '2026-11-03'
name: Chartsy
nav: Providers
network: true
overview: 'Chartsy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Software-as-a-Service, Analytics, Revenue, MRR, and Marketing.


  The Chartsy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chartsy''s developer surface includes getting-started guide, documentation, engineering blog, pricing, support, and 16 more developer resources.'
plans:
- name: Chartsy App Plans Pricing
  plan_count: 4
  slug: chartsy-app-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Chartsy API Rules
  rule_count: 44
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 2
  slug: chartsy-app-rules
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 26.3
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 0.0
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
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chartsy App Domain Security
  slug: chartsy-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chartsy-app
tags:
- Software-as-a-Service
- Analytics
- Revenue
- MRR
- Marketing
website: https://chartsy.app/
---
