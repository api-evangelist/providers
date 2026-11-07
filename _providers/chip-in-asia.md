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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/chip-in-asia/vendors/chip-in-asia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chip-in-asia-vendors.yml
- group: operate
  href: https://artifacts.apis.io/chip-in-asia/rate-limits/chip-in-asia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chip-in-asia-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chip-in-asia/plans/chip-in-asia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chip-in-asia-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/chip-in-asia/authentication/chip-in-asia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chip-in-asia-authentication.yml
- group: agent
  href: https://artifacts.apis.io/chip-in-asia/llms/chip-in-asia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chip-in-asia-llms.txt
- group: other
  href: https://artifacts.apis.io/chip-in-asia/a2a/chip-in-asia-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/chip-in-asia-a2a.yml
- group: other
  href: https://artifacts.apis.io/chip-in-asia/hosts/chip-in-asia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chip-in-asia-hosts.yml
- group: build
  href: https://artifacts.apis.io/chip-in-asia/packages/chip-in-asia-packages.yml
  title: ''
  type: SDKs
  url: packages/chip-in-asia-packages.yml
- group: build
  href: https://artifacts.apis.io/chip-in-asia/packages/chip-in-asia-packages.yml
  title: ''
  type: Packages
  url: packages/chip-in-asia-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chip-in.asia/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chip-in.asia/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://chip-in.asia/pricing
- group: start
  title: ''
  type: Login
  url: https://referrer.chip-in.asia/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CHIPAsia
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chip-in.asia/chip-collect/overview/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.chip-in.asia/chip-collect/overview/changelog
- group: company
  title: ''
  type: Blog
  url: https://blog.chip-in.asia
- group: docs
  title: ''
  type: Documentation
  url: https://developer.chip-in.asia/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.whatsapp.com/send?phone=60149362105&text=Hi%20CHIP%20Team%2C%20I%27m%20interested%20to%20activate%20the%20plugins%20sponsored%20by%20CHIP
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chip-in.asia/llms.txt
- group: auth
  href: https://artifacts.apis.io/chip-in-asia/security/chip-in-asia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chip-in-asia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chip-in.asia/
coverage:
  checked: '2026-10-26'
  detail: The developer documentation pages are rendered via JavaScript and no machine‑readable OpenAPI or other contract could be retrieved.
  evidence:
  - status: 404
    url: https://www.chip-in.asia/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: CHIP is a Digital Finance Platform for Malaysian businesses, offering services to collect payments, manage cashflow, control expenses, send payouts, and access financing. The platform provides APIs to integrate payment processing, cash management, expense tracking, and payout automation, enabling businesses to streamline financial operations and improve liquidity. CHIP aims to empower SMEs with modern digital finance tools tailored to the Malaysian market, supporting growth and operational efficiency.
image: https://cdn.prod.website-files.com/69d899d232bb80d7f1280cfb/69e20b76b75f63633ff36d37_75706778d66c2dfa1cc3e8aead851e6d_CHIP-OG.avif
layout: provider
modified: '2026-10-26'
name: CHIP
nav: Providers
network: true
overview: 'CHIP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Payments, Small Business, and Malaysia.


  CHIP''s developer surface includes authentication, pricing, getting-started guide, changelog, engineering blog, documentation, API reference, and 15 more developer resources.'
plans:
- name: Chip In Asia Plans Pricing
  plan_count: 3
  slug: chip-in-asia-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Chip In Asia Rate Limits
  slug: chip-in-asia-rate-limits
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 47.0
    catalog_earned_first_party: 20.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 39.3
    discoverability: 62.5
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - malaysia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 38.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 14.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chip-in-asia/chip-in-asia-2026-11-03T124042.png
security:
- kind: authentication
  name: Chip In Asia Authentication
  slug: chip-in-asia-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Chip In Asia Domain Security
  slug: chip-in-asia-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: chip-in-asia
tags:
- Company
- Finance
- Payments
- Small Business
- Malaysia
website: https://chip-in.asia/
---
