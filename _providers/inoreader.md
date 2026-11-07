---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - rate-limits
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: The Accounts API from Inoreader — 1 operation(s) for accounts.
  name: Inoreader Accounts API
  slug: inoreader-accounts-api
- description: The Oauth2 API from Inoreader — 1 operation(s) for oauth2.
  name: Inoreader Oauth2 API
  slug: inoreader-oauth2-api
- description: The Reader API from Inoreader — 8 operation(s) for reader.
  name: Inoreader Reader API
  slug: inoreader-reader-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/inoreader/rules/inoreader-rules.yml
  title: ''
  type: Spectral
  url: rules/inoreader-rules.yml
- group: design
  href: https://artifacts.apis.io/inoreader/json-ld/inoreader-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/inoreader-context.jsonld
- group: design
  href: https://artifacts.apis.io/inoreader/vocabulary/inoreader-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/inoreader-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/inoreader/data-model/inoreader-data-model.yml
  title: ''
  type: DataModel
  url: data-model/inoreader-data-model.yml
- group: design
  href: https://artifacts.apis.io/inoreader/conformance/inoreader-conformance.yml
  title: ''
  type: Conformance
  url: conformance/inoreader-conformance.yml
- group: operate
  href: https://artifacts.apis.io/inoreader/rate-limits/inoreader-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/inoreader-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/inoreader/plans/inoreader-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/inoreader-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/inoreader/changelog/inoreader-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/inoreader-changelog.yml
- group: agent
  href: https://artifacts.apis.io/inoreader/mcp/inoreader-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/inoreader-mcp.yml
- group: build
  href: https://artifacts.apis.io/inoreader/packages/inoreader-packages.yml
  title: ''
  type: SDKs
  url: packages/inoreader-packages.yml
- group: build
  href: https://artifacts.apis.io/inoreader/packages/inoreader-packages.yml
  title: ''
  type: Packages
  url: packages/inoreader-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.inoreader.com/
- group: other
  title: ''
  type: Leadership
  url: https://www.inoreader.com/discover/topic/business/management
- group: other
  title: ''
  type: x-coverage
  url: ''
- group: auth
  href: https://artifacts.apis.io/inoreader/security/inoreader-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inoreader-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inoreader.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.inoreader.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.inoreader.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://www.inoreader.com/developers/api-endpoint
- group: start
  title: ''
  type: GettingStarted
  url: https://www.inoreader.com/developers/register-app
- group: operate
  title: ''
  type: Support
  url: https://www.inoreader.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.inoreader.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.inoreader.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.inoreader.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.inoreader.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.inoreader.com/privacy_policy
created: '2026-09-21'
description: Inoreader provides a powerful RSS feed reader and content aggregation platform that lets users subscribe to, organize, and share web content. It offers features such as automated tagging, rules for filtering, offline access, and collaborative sharing for teams. The service includes a developer API that enables programmatic access to feed data, article content, and user actions, supporting integration with third‑party applications and custom workflows.
finops:
- has_sources: true
  method: derived
  name: Inoreader Finops
  primary_unit: ''
  service_category: ''
  slug: inoreader-finops
  template: true
image: https://www.inoreader.com/images/landing/v4/og-images/og-image-default.png
json_schemas:
- name: PostAccountsClientloginResponse
  property_count: 3
  slug: inoreader-post-accounts-clientlogin-response
- name: PostOauth2TokenRequest
  property_count: 6
  slug: inoreader-post-oauth2-token-request
- name: PostOauth2TokenResponse
  property_count: 5
  slug: inoreader-post-oauth2-token-response
- name: PostReaderApi0ActiveSearchCreateRequest
  property_count: 7
  slug: inoreader-post-reader-api0-active-search-create-request
- name: PostReaderApi0ActiveSearchCreateResponse
  property_count: 3
  slug: inoreader-post-reader-api0-active-search-create-response
- name: PostReaderApi0RenameTagResponse
  property_count: 1
  slug: inoreader-post-reader-api0-rename-tag-response
jsonld:
- class_count: 9
  name: Inoreader Context
  property_count: 22
  slug: inoreader-context
layout: provider
modified: '2026-09-21'
name: Inoreader
nav: Providers
network: true
overview: 'Inoreader is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Accounts API, Oauth2 API, and Reader API. Tagged areas include Company, RSS, Content Aggregation, and Productivity.


  The Inoreader catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Inoreader''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Inoreader Plans Pricing
  plan_count: 3
  slug: inoreader-plans-pricing
- name: Inoreader Price Estimates
  plan_count: 0
  slug: inoreader-price-estimates
random_paper: 17
rate_limits:
- limit_count: 2
  name: Inoreader Rate Limits
  slug: inoreader-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Inoreader API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: inoreader-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 75.8
    catalog_earned_first_party: 20.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 23.8
    developer_ergonomics: 29.8
    discoverability: 54.5
    operational_transparency: 44.7
  previous_composite: 46.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: unknown
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
screenshot: https://apis.io/screenshots/inoreader/inoreader-2026-10-11T105727.png
security:
- kind: domain-security
  name: Inoreader Domain Security
  slug: inoreader-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: inoreader
tags:
- Company
- RSS
- Content Aggregation
- Productivity
website: https://inoreader.com/
---
