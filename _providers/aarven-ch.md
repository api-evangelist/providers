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
  - scopes
  - rate-limits
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: A simple REST API for creating bookings and reading your chart of accounts and company data.
  name: Aarven API
  slug: aarven-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/aarven-ch/rate-limits/aarven-ch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aarven-ch-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aarven-ch/plans/aarven-ch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aarven-ch-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aarven-ch/conventions/aarven-ch-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aarven-ch-conventions.yml
- group: design
  href: https://artifacts.apis.io/aarven-ch/conventions/aarven-ch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aarven-ch-conventions.yml
- group: auth
  href: https://artifacts.apis.io/aarven-ch/authentication/aarven-ch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aarven-ch-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aarven-ch/scopes/aarven-ch-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aarven-ch-scopes.yml
- group: design
  href: https://artifacts.apis.io/aarven-ch/errors/aarven-ch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aarven-ch-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aarven-ch/conformance/aarven-ch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aarven-ch-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aarven-ch/llms/aarven-ch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aarven-ch-llms.txt
- group: agent
  href: https://artifacts.apis.io/aarven-ch/well-known/aarven-ch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aarven-ch-well-known.yml
- group: other
  href: https://artifacts.apis.io/aarven-ch/hosts/aarven-ch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aarven-ch-hosts.yml
- group: other
  href: https://artifacts.apis.io/aarven-ch/vendors/aarven-ch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aarven-ch-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aarven-ch/security/aarven-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aarven-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aarven.ch/
- group: docs
  title: ''
  type: Documentation
  url: https://aarven.ch/ki-buchhaltung
- group: docs
  title: ''
  type: APIReference
  url: https://aarven.ch/Api
- group: start
  title: ''
  type: GettingStarted
  url: https://aarven.ch/Anleitung
- group: commercial
  title: ''
  type: Pricing
  url: https://aarven.ch/Pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aarven.ch/Agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aarven.ch/Privacy
- group: start
  title: ''
  type: SignUp
  url: https://aarven.ch/Demo
coverage:
  checked: '2026-10-31'
  detail: API documentation is rendered via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://aarven.ch/Api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Aarven provides AI-powered bookkeeping solutions tailored for Swiss small and medium-sized enterprises (KMU) and trustees. Leveraging artificial intelligence, the platform automatically captures receipts, records transactions, generates balance sheets, profit & loss statements, and monitors VAT. Users can connect the system directly with large language models such as Claude, ChatGPT, and others to enhance workflow. The service offers a free starter tier and integrates with popular tools via Zapier, aiming to streamline accounting for the Swiss market.
image: https://aarven.ch/android-chrome-512x512.png
layout: provider
modified: '2026-10-31'
name: Aarven
nav: Providers
network: true
overview: 'Aarven is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Artificial Intelligence, Bookkeeping, Swiss, and Finance.


  Aarven''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Aarven Ch Plans Pricing
  plan_count: 6
  slug: aarven-ch-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Aarven Ch Rate Limits
  slug: aarven-ch-rate-limits
scopes:
- name: Aarven Ch Scopes
  scope_count: 4
  slug: aarven-ch-scopes
  summary_line: 4 scopes
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 37.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aarven Ch Authentication
  slug: aarven-ch-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aarven Ch Domain Security
  slug: aarven-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aarven-ch
tags:
- Accounting
- Artificial Intelligence
- Bookkeeping
- Swiss
- Finance
- Automation
website: https://aarven.ch/
---
