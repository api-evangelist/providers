---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Payment gateway API providing endpoints for payments, disbursements, and transaction management.
  name: Duitku API
  slug: duitku-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/duitku/plans/duitku-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/duitku-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/duitku/changelog/duitku-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/duitku-changelog.yml
- group: other
  href: https://artifacts.apis.io/duitku/hosts/duitku-hosts.yml
  title: ''
  type: Hosts
  url: hosts/duitku-hosts.yml
- group: other
  href: https://artifacts.apis.io/duitku/vendors/duitku-vendors.yml
  title: ''
  type: Vendors
  url: vendors/duitku-vendors.yml
- group: build
  href: https://artifacts.apis.io/duitku/packages/duitku-packages.yml
  title: ''
  type: SDKs
  url: packages/duitku-packages.yml
- group: build
  href: https://artifacts.apis.io/duitku/packages/duitku-packages.yml
  title: ''
  type: Packages
  url: packages/duitku-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.duitku.com/en/news/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.duitku.com/changelog/
- group: auth
  href: https://artifacts.apis.io/duitku/security/duitku-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duitku-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.duitku.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.duitku.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.duitku.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.duitku.com/
- group: operate
  title: ''
  type: Support
  url: https://www.duitku.com/kontak/
- group: company
  title: ''
  type: Blog
  url: https://www.duitku.com/berita/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.duitku.com/harga/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.duitku.com/Account/Register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.duitku.com/kebijakan-privasi/
- group: company
  title: ''
  type: Website
  url: https://duitku.com/
coverage:
  checked: '2026-10-27'
  detail: Documentation site renders via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.duitku.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Duitku provides a payment gateway platform in Indonesia, enabling merchants to accept online payments via various methods such as credit cards, bank transfers, e‑wallets, and QR codes. It offers APIs for payment processing, disbursements, and transaction management, with features like real‑time monitoring, fraud protection, and multi‑currency support. The service is tailored for the Indonesian market, emphasizing ease of integration and comprehensive documentation for developers.
image: https://www.duitku.com/wp-content/uploads/2025/02/Duitku-rounded-transparent-1-1.png
layout: provider
modified: '2026-10-27'
name: Duitku
nav: Providers
network: true
overview: 'Duitku is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, and Indonesia.


  Duitku''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Duitku Plans Pricing
  plan_count: 4
  slug: duitku-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 49.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 7.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/duitku/duitku-2026-11-03T131119.png
security:
- kind: domain-security
  name: Duitku Domain Security
  slug: duitku-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: duitku
tags:
- Company
- Payments
- Fintech
- Indonesia
website: https://duitku.com/
---
