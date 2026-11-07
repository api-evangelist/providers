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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Appfigures API as documented publicly: 32 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Appfigures API
  slug: appfigures-com-api
artifact_total: 11
common:
- group: auth
  href: https://artifacts.apis.io/appfigures-com/well-known/appfigures-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/appfigures-com-status-security.txt
- group: commercial
  href: https://artifacts.apis.io/appfigures-com/plans/appfigures-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appfigures-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/appfigures-com/rules/appfigures-com-rules.yml
  title: ''
  type: Spectral
  url: rules/appfigures-com-rules.yml
- group: design
  href: https://artifacts.apis.io/appfigures-com/json-ld/appfigures-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/appfigures-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/appfigures-com/vocabulary/appfigures-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/appfigures-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/appfigures-com/data-model/appfigures-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appfigures-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/appfigures-com/conformance/appfigures-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appfigures-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/appfigures-com/llms/appfigures-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appfigures-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/appfigures-com/well-known/appfigures-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appfigures-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/appfigures-com/hosts/appfigures-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appfigures-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/appfigures-com/vendors/appfigures-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appfigures-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/appfigures-com/packages/appfigures-com-packages.yml
  title: ''
  type: SDKs
  url: packages/appfigures-com-packages.yml
- group: build
  href: https://artifacts.apis.io/appfigures-com/packages/appfigures-com-packages.yml
  title: ''
  type: Packages
  url: packages/appfigures-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appfigures.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.appfigures.com/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.appfigures.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appfigures.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://appfigures.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://appfigures.com/press
- group: start
  title: ''
  type: Login
  url: https://appfigures.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.appfigures.com/getting-started/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://appfigures.com/developers/keys
- group: company
  title: ''
  type: Blog
  url: http://blog.appfigures.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.appfigures.com/reference/ads/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.appfigures.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appfigures
- group: auth
  href: https://artifacts.apis.io/appfigures-com/security/appfigures-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appfigures-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appfigures.com/
coverage:
  checked: '2026-11-01'
  detail: Cloudflare bot challenge blocks access to developer docs, preventing retrieval of any machine-readable spec.
  evidence:
  - status: 403
    url: https://appfigures.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Appfigures provides app intelligence, ASO tools, and analytics for mobile developers and marketers. Their platform offers universal analytics, ad‑spend consolidation, review monitoring, store performance tracking, market explorer insights, SDK intelligence, and Apple Ads intelligence. Users can access revenue, sales, subscriptions, ads, ratings, and usage reports via a comprehensive API documented at docs.appfigures.com.
json_schemas:
- name: GetFeaturedFullProductidStartdateEnddateResponse
  property_count: 9
  slug: appfigures-com-get-featured-full-productid-startdate-enddate-response
- name: GetReportsAdsResponse
  property_count: 8
  slug: appfigures-com-get-reports-ads-response
- name: GetReportsAdspendResponse
  property_count: 7
  slug: appfigures-com-get-reports-adspend-response
- name: GetReportsRevenueResponse
  property_count: 15
  slug: appfigures-com-get-reports-revenue-response
- name: GetReportsSalesResponse
  property_count: 35
  slug: appfigures-com-get-reports-sales-response
- name: GetUsersEmailOrUserIdResponse
  property_count: 13
  slug: appfigures-com-get-users-email-or-user-id-response
jsonld:
- class_count: 34
  name: Appfigures Com Context
  property_count: 138
  slug: appfigures-com-context
layout: provider
modified: '2026-11-01'
name: Appfigures
nav: Providers
network: true
overview: 'Appfigures is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mobile, Analytics, ASO, Advertising, and Market Data.


  The Appfigures catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Appfigures'' developer surface includes support, pricing, getting-started guide, engineering blog, API reference, documentation, and 22 more developer resources.'
plans:
- name: Appfigures Com Plans Pricing
  plan_count: 5
  slug: appfigures-com-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Appfigures API Rules
  rule_count: 37
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 3
  slug: appfigures-com-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 29.8
    discoverability: 54.5
    operational_transparency: 15.8
  previous_composite: 45.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 19.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appfigures Com Domain Security
  slug: appfigures-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appfigures-com
tags:
- Mobile
- Analytics
- ASO
- Advertising
- Market Data
- Company
website: https://appfigures.com/
---
