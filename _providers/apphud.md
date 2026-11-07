---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    event_surface_described: unknown
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
  score: 16.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Apphud provides a platform for in‑app subscription analytics, revenue optimization, and user retention for iOS and Android apps.
  name: Apphud API
  slug: apphud-api-2
- baseURL: https://api.apphud.com
  baseurl_source: declared
  description: 'Apphud API as documented publicly: 30 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Apphud API
  slug: apphud-api
artifact_total: 12
common:
- group: auth
  href: https://artifacts.apis.io/apphud/well-known/apphud-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apphud-status-security.txt
- group: commercial
  href: https://artifacts.apis.io/apphud/plans/apphud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apphud-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apphud/rules/apphud-rules.yml
  title: ''
  type: Spectral
  url: rules/apphud-rules.yml
- group: design
  href: https://artifacts.apis.io/apphud/json-ld/apphud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apphud-context.jsonld
- group: design
  href: https://artifacts.apis.io/apphud/vocabulary/apphud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apphud-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apphud/data-model/apphud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apphud-data-model.yml
- group: design
  href: https://artifacts.apis.io/apphud/conformance/apphud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apphud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apphud/llms/apphud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apphud-llms.txt
- group: agent
  href: https://artifacts.apis.io/apphud/well-known/apphud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apphud-well-known.yml
- group: other
  href: https://artifacts.apis.io/apphud/hosts/apphud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apphud-hosts.yml
- group: other
  href: https://artifacts.apis.io/apphud/vendors/apphud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apphud-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://apphud.com/integrations/data/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apphud.com/
- group: start
  title: ''
  type: Login
  url: https://dash.apphud.com/sign-in
- group: auth
  href: https://artifacts.apis.io/apphud/security/apphud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apphud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apphud.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dash.apphud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apphud.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apphud.com/docs/what-is-apphud
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apphud.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://apphud.com/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.apphud.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apphud
- group: commercial
  title: ''
  type: Pricing
  url: https://apphud.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apphud.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apphud.com/legal/privacy
coverage:
  checked: '2026-10-26'
  detail: Documentation is served as a JavaScript‑rendered single‑page app, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://docs.apphud.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Apphud provides a platform for in‑app subscription analytics, revenue optimization, and user retention for iOS and Android apps. It offers SDKs, dashboards, A/B testing, paywalls, and integrations with attribution and analytics services, helping developers maximize subscription revenue and understand user behavior across mobile platforms.
image: https://framerusercontent.com/assets/9v1I6RYo9d6ZcU3FkMumpF6Flw.png
json_schemas:
- name: GetV1CustomersResponse
  property_count: 27
  slug: apphud-get-v1-customers-response
- name: PostApiPublicV1ChartListResponse
  property_count: 8
  slug: apphud-post-api-public-v1-chart-list-response
- name: PostApiPublicV1ChartQueryColumnRequest
  property_count: 8
  slug: apphud-post-api-public-v1-chart-query-column-request
- name: PostApiPublicV1OverviewWidgets0123456789AbCdef0123456789Abcd
  property_count: 6
  slug: apphud-post-api-public-v1-overview-widgets0123456789-ab-cdef0123456789-abcd
- name: PostChartQueryColumnRequest
  property_count: 8
  slug: apphud-post-chart-query-column-request
- name: PostV1PromotionsResponse
  property_count: 2
  slug: apphud-post-v1-promotions-response
jsonld:
- class_count: 31
  name: Apphud Context
  property_count: 64
  slug: apphud-context
layout: provider
modified: '2026-10-26'
name: Apphud
nav: Providers
network: true
overview: 'Apphud is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Mobile, Analytics, Subscription, SDK, and Revenue.


  The Apphud catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apphud''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Apphud Plans Pricing
  plan_count: 4
  slug: apphud-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Apphud API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: apphud-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 22.6
    discoverability: 64.3
    operational_transparency: 25.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 45.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/apphud/apphud-2026-11-03T121029.png
security:
- kind: domain-security
  name: Apphud Domain Security
  slug: apphud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apphud
tags:
- Mobile
- Analytics
- Subscription
- SDK
- Revenue
website: https://apphud.com/
---
