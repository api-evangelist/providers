---
access_model:
  confidence: medium
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
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Browser Forest API provides REST endpoints for creating and managing browser sessions, contexts, and cookies. Base URL: https://browserforest.com/api/v1 as documented.'
  name: Browser Forest API
  slug: browser-forest-api
- description: 'Browser Forest API as documented publicly: 64 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Browser Forest API
  slug: browserforest-com-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/browserforest-com/plans/browserforest-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/browserforest-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/browserforest-com/rules/browserforest-com-rules.yml
  title: ''
  type: Spectral
  url: rules/browserforest-com-rules.yml
- group: design
  href: https://artifacts.apis.io/browserforest-com/json-ld/browserforest-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/browserforest-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/browserforest-com/vocabulary/browserforest-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/browserforest-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/browserforest-com/data-model/browserforest-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/browserforest-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/browserforest-com/authentication/browserforest-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/browserforest-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/browserforest-com/conformance/browserforest-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/browserforest-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/browserforest-com/hosts/browserforest-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/browserforest-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/browserforest-com/vendors/browserforest-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/browserforest-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://browserforest.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://browserforest.com/legal/privacy
- group: auth
  href: https://artifacts.apis.io/browserforest-com/security/browserforest-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/browserforest-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://browserforest.com/
- group: docs
  title: ''
  type: Documentation
  url: https://browserforest.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://browserforest.com/api/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://browserforest.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://browserforest.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://browserforest.com/login
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are rendered HTML with no machine‑readable OpenAPI spec available.
  evidence:
  - status: 200
    url: https://browserforest.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Browser Forest provides cloud‑based Chromium browsers designed for AI agents and automation. Users can create undetectable browser sessions via CDP (Playwright/Puppeteer) with built‑in captcha solving and anti‑detection patches. The service offers a free tier with no credit‑card required, 300 minutes of usage and up to three concurrent sessions, plus paid plans for higher concurrency. It targets developers needing scalable, stealthy browsing for scraping, testing, or AI‑driven web interactions.
json_schemas:
- name: PostApiV1ScrapeResponse
  property_count: 4
  slug: browserforest-com-post-api-v1-scrape-response
- name: PostV1AuthLoginRequest
  property_count: 1
  slug: browserforest-com-post-v1-auth-login-request
- name: PostV1CaptchaSolveInteractRequest
  property_count: 1
  slug: browserforest-com-post-v1-captcha-solve-interact-request
- name: PostV1CaptchaSolveRequest
  property_count: 1
  slug: browserforest-com-post-v1-captcha-solve-request
- name: PutApiV1SessionsSesXxxxCookiesRequest
  property_count: 1
  slug: browserforest-com-put-api-v1-sessions-ses-xxxx-cookies-request
- name: PutApiV1SessionsSesXxxxxxxxCookiesRequest
  property_count: 1
  slug: browserforest-com-put-api-v1-sessions-ses-xxxxxxxx-cookies-request
jsonld:
- class_count: 14
  name: Browserforest Com Context
  property_count: 13
  slug: browserforest-com-context
layout: provider
modified: '2026-11-03'
name: Browser Forest
nav: Providers
network: true
overview: 'Browser Forest is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Browser, AI Agents, Automation, Chromium, and Free Tier.


  The Browser Forest catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Browser Forest''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, signup flow, and 12 more developer resources.'
plans:
- name: Browserforest Com Plans Pricing
  plan_count: 4
  slug: browserforest-com-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Browser Forest API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: browserforest-com-rules
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 21.4
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
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
- kind: authentication
  name: Browserforest Com Authentication
  slug: browserforest-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Browserforest Com Domain Security
  slug: browserforest-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: browserforest-com
tags:
- Cloud Browser
- AI Agents
- Automation
- Chromium
- Free Tier
website: https://browserforest.com/
---
