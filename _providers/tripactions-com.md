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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: RESTful API for partners and integrators to retrieve and update Navan expense data, including card transactions, reimbursements, fees, and more.
  name: Navan Expense API
  slug: navan-expense-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/tripactions-com/plans/tripactions-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tripactions-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://navan.com/security
- group: agent
  href: https://artifacts.apis.io/tripactions-com/llms/tripactions-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tripactions-com-llms.txt
- group: other
  href: https://artifacts.apis.io/tripactions-com/hosts/tripactions-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tripactions-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/tripactions-com/vendors/tripactions-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tripactions-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://navan.com/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.navan.com/
- group: auth
  title: ''
  type: Security
  url: https://navan.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://navan.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://navan.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://navan.com/press/news
- group: start
  title: ''
  type: Login
  url: https://navan.com/signin
- group: other
  title: ''
  type: Leadership
  url: https://navan.com/de/management
- group: start
  title: ''
  type: GettingStarted
  url: https://navan.com/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://navan.com/resources/guides
- group: operate
  title: ''
  type: ChangeLog
  url: https://navan.com/press/releases
- group: company
  title: ''
  type: Blog
  url: https://navan.com/blog
- group: auth
  href: https://artifacts.apis.io/tripactions-com/security/tripactions-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tripactions-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tripactions-com/security/tripactions-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tripactions-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tripactions-com/security/tripactions-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tripactions-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tripactions.com
coverage:
  checked: '2026-10-25'
  detail: Developer portal provides HTML docs but no machine‑readable OpenAPI spec; openapi.json returns HTML page.
  evidence:
  - status: 200
    url: https://developer.navan.com/api/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Navan (formerly TripActions) provides a corporate travel management platform that enables businesses to book, manage, and expense travel in one place. The service offers features such as travel policy enforcement, advanced analytics, sustainability options, integrated expense management, and a suite of tools for travelers, finance teams, and administrators. Navan aims to simplify corporate travel, improve compliance, and deliver cost savings through a unified, user‑friendly experience.
image: https://images.ctfassets.net/r49k2skuorjz/6FIv7ITxTTSkfATgwmVUN6/d991df51e415434ccd32ca0c609a6a3d/Share-image.webp
layout: provider
modified: '2026-10-25'
name: Navan
nav: Providers
network: true
overview: 'Navan is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Expense Management, Software-as-a-Service, and Corporate.


  Navan''s developer surface includes pricing, getting-started guide, documentation, changelog, engineering blog, and 16 more developer resources.'
plans:
- name: Tripactions Com Plans Pricing
  plan_count: 2
  slug: tripactions-com-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.5
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.0
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tripactions-com/tripactions-com-2026-11-03T145103.png
security:
- kind: domain-security
  name: Tripactions Com Domain Security
  slug: tripactions-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tripactions Com Vulnerability Disclosure
  slug: tripactions-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Tripactions Com Trust Center
  slug: tripactions-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: tripactions-com
tags:
- Company
- Travel
- Expense Management
- Software-as-a-Service
- Corporate
website: https://tripactions.com
---
