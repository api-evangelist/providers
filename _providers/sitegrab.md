---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Sitegrab Agentic Access
  operation_count: 10
  slug: sitegrab-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.sitegrab.dev
  baseurl_source: declared
  description: Capture pixel-perfect screenshots of any webpage via a simple REST API.
  name: SiteGrab Screenshot API
  slug: sitegrab-screenshot-api
- baseURL: https://api.sitegrab.dev
  baseurl_source: declared
  description: The Checkout API from SiteGrab Screenshot API (LaminarForge) — 1 operation(s) for checkout.
  name: SiteGrab Screenshot API (LaminarForge) Checkout API
  slug: sitegrab-checkout-api
- baseURL: https://api.sitegrab.dev
  baseurl_source: declared
  description: The Docs API from SiteGrab Screenshot API (LaminarForge) — 1 operation(s) for docs.
  name: SiteGrab Screenshot API (LaminarForge) Docs API
  slug: sitegrab-docs-api
- baseURL: https://api.sitegrab.dev
  baseurl_source: declared
  description: The Health API from SiteGrab Screenshot API (LaminarForge) — 1 operation(s) for health.
  name: SiteGrab Screenshot API (LaminarForge) Health API
  slug: sitegrab-health-api
- baseURL: https://api.sitegrab.dev
  baseurl_source: declared
  description: The Keys API from SiteGrab Screenshot API (LaminarForge) — 1 operation(s) for keys.
  name: SiteGrab Screenshot API (LaminarForge) Keys API
  slug: sitegrab-keys-api
- baseURL: https://api.sitegrab.dev
  baseurl_source: declared
  description: The Screenshot API from SiteGrab Screenshot API (LaminarForge) — 1 operation(s) for screenshot.
  name: SiteGrab Screenshot API (LaminarForge) Screenshot API
  slug: sitegrab-screenshot-api
- baseURL: https://api.sitegrab.dev
  baseurl_source: declared
  description: The Signup API from SiteGrab Screenshot API (LaminarForge) — 1 operation(s) for signup.
  name: SiteGrab Screenshot API (LaminarForge) Signup API
  slug: sitegrab-signup-api
- baseURL: https://api.sitegrab.dev
  baseurl_source: declared
  description: The SiteGrab Screenshot API API from SiteGrab Screenshot API (LaminarForge) — 1 operation(s) for sitegrab screenshot api.
  name: SiteGrab Screenshot API (LaminarForge) SiteGrab Screenshot API
  slug: sitegrab-sitegrab-screenshot-api-api
- baseURL: https://api.sitegrab.dev
  baseurl_source: declared
  description: The Usage API from SiteGrab Screenshot API (LaminarForge) — 1 operation(s) for usage.
  name: SiteGrab Screenshot API (LaminarForge) Usage API
  slug: sitegrab-usage-api
- baseURL: https://api.sitegrab.dev
  baseurl_source: declared
  description: The Webhook API from SiteGrab Screenshot API (LaminarForge) — 1 operation(s) for webhook.
  name: SiteGrab Screenshot API (LaminarForge) Webhook API
  slug: sitegrab-webhook-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/sitegrab/agentic-access/sitegrab-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sitegrab-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/sitegrab/rules/sitegrab-rules.yml
  title: ''
  type: Spectral
  url: rules/sitegrab-rules.yml
- group: design
  href: https://artifacts.apis.io/sitegrab/vocabulary/sitegrab-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sitegrab-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sitegrab/errors/sitegrab-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sitegrab-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/sitegrab/authentication/sitegrab-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sitegrab-authentication.yml
- group: design
  href: https://artifacts.apis.io/sitegrab/conformance/sitegrab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sitegrab-conformance.yml
- group: other
  href: https://artifacts.apis.io/sitegrab/hosts/sitegrab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sitegrab-hosts.yml
- group: other
  href: https://artifacts.apis.io/sitegrab/vendors/sitegrab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sitegrab-vendors.yml
- group: auth
  href: https://artifacts.apis.io/sitegrab/security/sitegrab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sitegrab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sitegrab.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://api.sitegrab.dev/v1/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sitegrab.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://api.sitegrab.dev/v1/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://sitegrab.dev/signup
- group: operate
  title: ''
  type: Support
  url: https://sitegrab.dev/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sitegrab.dev/terms
created: '2026-10-17'
description: SiteGrab Screenshot API, built by LaminarForge, provides a simple REST interface to capture full-page, responsive screenshots of any website. It supports JPEG, PNG, and PDF formats, custom viewport sizes, and offers a free tier of 50 screenshots per month with no credit card required. The service is powered by Playwright on dedicated VPS for pixel‑perfect results, includes detailed usage statistics, rate limits, and tiered pricing plans for higher usage, and is designed for developers needing reliable, high‑quality visual snapshots of web pages.
layout: provider
modified: '2026-10-17'
name: SiteGrab Screenshot API (LaminarForge)
nav: Providers
network: true
overview: 'SiteGrab Screenshot API (LaminarForge) publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including SiteGrab Screenshot API, Checkout API, Docs API, and 7 more. Tagged areas include Screenshots, Automation, Image, and Web.


  The SiteGrab Screenshot API (LaminarForge) catalog on APIs.io includes 1 Spectral governance ruleset.


  SiteGrab Screenshot API (LaminarForge)''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 11 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: SiteGrab Screenshot API (LaminarForge) API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: sitegrab-rules
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 46.0
    developer_ergonomics: 33.3
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sitegrab/sitegrab-2026-11-03T143244.png
security:
- kind: authentication
  name: Sitegrab Authentication
  slug: sitegrab-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sitegrab Domain Security
  slug: sitegrab-domain-security
  summary_line: TLSv1.3
slug: sitegrab
tags:
- Screenshots
- Automation
- Image
- Web
website: https://sitegrab.dev/
---
