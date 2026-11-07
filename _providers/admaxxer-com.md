---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The Admaxxer Pixel API is a JSON API for your website analytics: list your sites, pull the same reports you see in the dashboard, and send server-side goals, payments and events.'
  name: Pixel API
  slug: pixel-api
- description: 'Admaxxer API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: Admaxxer API
  slug: admaxxer-com-api
artifact_total: 9
common:
- group: operate
  href: https://artifacts.apis.io/admaxxer-com/rate-limits/admaxxer-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/admaxxer-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/admaxxer-com/plans/admaxxer-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/admaxxer-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/admaxxer-com/rules/admaxxer-com-rules.yml
  title: ''
  type: Spectral
  url: rules/admaxxer-com-rules.yml
- group: design
  href: https://artifacts.apis.io/admaxxer-com/vocabulary/admaxxer-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/admaxxer-com-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/admaxxer-com/changelog/admaxxer-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/admaxxer-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/admaxxer-com/conventions/admaxxer-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/admaxxer-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/admaxxer-com/conventions/admaxxer-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/admaxxer-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/admaxxer-com/authentication/admaxxer-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/admaxxer-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/admaxxer-com/scopes/admaxxer-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/admaxxer-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/admaxxer-com/conformance/admaxxer-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/admaxxer-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/admaxxer-com/llms/admaxxer-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/admaxxer-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/admaxxer-com/well-known/admaxxer-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/admaxxer-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/admaxxer-com/hosts/admaxxer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/admaxxer-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/admaxxer-com/packages/admaxxer-com-packages.yml
  title: ''
  type: SDKs
  url: packages/admaxxer-com-packages.yml
- group: build
  href: https://artifacts.apis.io/admaxxer-com/packages/admaxxer-com-packages.yml
  title: ''
  type: Packages
  url: packages/admaxxer-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://admaxxer.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://admaxxer.com/changelog
- group: auth
  href: https://artifacts.apis.io/admaxxer-com/security/admaxxer-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/admaxxer-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/admaxxer-com/security/admaxxer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/admaxxer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://admaxxer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://admaxxer.com/documentation/developer
- group: docs
  title: ''
  type: Documentation
  url: https://admaxxer.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://admaxxer.com/documentation/api/pixel/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://admaxxer.com/documentation/getting-started
- group: operate
  title: ''
  type: Support
  url: https://admaxxer.com/support
- group: company
  title: ''
  type: Blog
  url: https://admaxxer.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://admaxxer.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://admaxxer.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://admaxxer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://admaxxer.com/privacy
coverage:
  checked: '2026-10-31'
  detail: Documentation pages list a Base URL but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://admaxxer.com/documentation/api/pixel/overview
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Admaxxer AI Analytics is a marketing analytics and ad‑ops platform that offers first‑party pixel, real‑time visitor and revenue analytics, AI‑driven attribution, and server‑side tracking. It delivers analytics up to 86% cheaper than competitors, with plans starting at $9/mo and a free trial, supporting integration with Claude, ChatGPT, Cursor, Codex and other AI agents. The platform provides blended MER, CPA, and source/medium attribution, multi‑account reporting, role‑based access, and a unified dashboard for Meta and Google ads. Designed for DTC brands and SaaS teams, Admaxxer aims to give honest, transparent data without overage charges.
image: https://admaxxer.com/og-image.png
layout: provider
modified: '2026-10-31'
name: Admaxxer
nav: Providers
network: true
overview: 'Admaxxer is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Attribution, Artificial Intelligence, Server-side-tracking, and Ad-ops.


  The Admaxxer catalog on APIs.io includes 1 Spectral governance ruleset.


  Admaxxer''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 23 more developer resources.'
plans:
- name: Admaxxer Com Plans Pricing
  plan_count: 6
  slug: admaxxer-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Admaxxer Com Rate Limits
  slug: admaxxer-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Admaxxer API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: admaxxer-com-rules
scopes:
- name: Admaxxer Com Scopes
  scope_count: 2
  slug: admaxxer-com-scopes
  summary_line: 2 scopes
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.8
    catalog_earned_first_party: 20.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 41.7
    discoverability: 57.1
    operational_transparency: 34.2
  previous_composite: 48.6
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Admaxxer Com Authentication
  slug: admaxxer-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Admaxxer Com Domain Security
  slug: admaxxer-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Admaxxer Com Vulnerability Disclosure
  slug: admaxxer-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: admaxxer-com
tags:
- Analytics
- Attribution
- Artificial Intelligence
- Server-side-tracking
- Ad-ops
- Direct to Consumer
website: https://admaxxer.com/
---
