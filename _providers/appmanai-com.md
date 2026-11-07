---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Appmanai Com Agentic Access
  operation_count: 7
  slug: appmanai-com-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://appmanai.com/api/v1
  baseurl_source: declared
  description: An app's store listing — title, developer, category, ratings, metadata.
  name: AppManAi App Metadata API
  slug: appmanai-com-app-metadata-api
- baseURL: https://appmanai.com/api/v1
  baseurl_source: declared
  description: Measurements of an app over time. Ratings today; more metrics later.
  name: AppManAi App Metrics API
  slug: appmanai-com-app-metrics-api
- baseURL: https://appmanai.com/api/v1
  baseurl_source: declared
  description: User reviews of an app.
  name: AppManAi App Reviews API
  slug: appmanai-com-app-reviews-api
- baseURL: https://appmanai.com/api/v1
  baseurl_source: declared
  description: Finding an app by name, and the apps a store considers similar to it.
  name: AppManAi App Search API
  slug: appmanai-com-app-search-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/appmanai-com/agentic-access/appmanai-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/appmanai-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/appmanai-com/rate-limits/appmanai-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/appmanai-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/appmanai-com/plans/appmanai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appmanai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/appmanai-com/rules/appmanai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/appmanai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/appmanai-com/vocabulary/appmanai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/appmanai-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/appmanai-com/authentication/appmanai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appmanai-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/appmanai-com/errors/appmanai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appmanai-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/appmanai-com/conformance/appmanai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appmanai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/appmanai-com/well-known/appmanai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appmanai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/appmanai-com/hosts/appmanai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appmanai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/appmanai-com/vendors/appmanai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appmanai-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://appmanai.com/status
- group: docs
  title: ''
  type: APIReference
  url: https://appmanai.com/docs/reference/
- group: auth
  href: https://artifacts.apis.io/appmanai-com/security/appmanai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appmanai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appmanai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://appmanai.com/docs/guide/quickstart.html
- group: commercial
  title: ''
  type: Pricing
  url: https://appmanai.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appmanai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appmanai.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://appmanai.com/app/login?mode=signup
created: '2026-11-01'
description: AppManAi provides AI agents and development teams with real App Store and Google Play data through a Model Context Protocol (MCP) connector. The service offers searchable app metadata, keyword intelligence, performance metrics, reviews, and competitor insights for over 6 million apps and 15 million keywords across 100+ countries. Pricing is per‑request with a free starter tier and monthly credit plans, and the connector works with Claude, ChatGPT, Cursor and other MCP‑compatible clients.
image: https://appmanai.com/_og/s/c_Default,title_~R2l2ZSB5b3VyIEFJIHJlYWwgQXBwIFN0b3JlICYgR29vZ2xlIFBsYXkgZGF0YQ,description_~Q29ubmVjdCB0aGUgTUNQIHNlcnZlciB0byBDbGF1ZGUsIEN1cnNvciBvciBhbnkgYWdlbnQgYW5kIGFzayBpbiBwbGFpbiBFbmdsaXNoLg.png
layout: provider
modified: '2026-11-01'
name: AppManAi
nav: Providers
network: true
overview: 'AppManAi publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including App Metadata API, App Metrics API, App Reviews API, and 1 more. Tagged areas include App Store Data, Google Play Data, ASO, Data API, and App Intelligence.


  The AppManAi catalog on APIs.io includes 1 Spectral governance ruleset.


  AppManAi''s developer surface includes authentication, API reference, documentation, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Appmanai Com Plans Pricing
  plan_count: 5
  slug: appmanai-com-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Appmanai Com Rate Limits
  slug: appmanai-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: AppManAi API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: appmanai-com-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 20.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 43.3
    developer_ergonomics: 20.2
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Appmanai Com Authentication
  slug: appmanai-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Appmanai Com Domain Security
  slug: appmanai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appmanai-com
tags:
- App Store Data
- Google Play Data
- ASO
- Data API
- App Intelligence
website: https://appmanai.com/
---
