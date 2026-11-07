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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CollBox provides an API for law firms to integrate invoice recovery services. Documentation is available at the website but no machine‑readable contract was found.
  name: CollBox API
  slug: collbox-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/collbox/plans/collbox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/collbox-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/collbox/hosts/collbox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/collbox-hosts.yml
- group: other
  href: https://artifacts.apis.io/collbox/vendors/collbox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/collbox-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://collbox.co/get-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/collbox
- group: auth
  href: https://artifacts.apis.io/collbox/security/collbox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/collbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://collbox.co/
- group: company
  title: ''
  type: Blog
  url: https://collbox.co/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://collbox.co/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://collbox.co/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://collbox.co/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://collbox.notion.site/CollBox-Help-Center-a1c62d34f7a646b7b5fb9d8ede11f168
- group: start
  title: ''
  type: SignUp
  url: https://collbox.co/sign-up/
- group: company
  title: ''
  type: Website
  url: https://collbox.co/
coverage:
  checked: '2026-10-28'
  detail: Provider's documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec could be retrieved.
  evidence:
  - status: 200
    url: https://collbox.co/get-started/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: CollBox provides a service that helps law firms recover past‑due invoices by integrating with practice‑management and accounting systems such as Clio, QuickBooks, Xero and others. It offers both one‑time clean‑up and ongoing receivables support, delivering up to 40% faster payments and handling client communications on behalf of firms. The platform is built for North‑American law practices and emphasizes preserving client relationships while automating follow‑up.
image: https://collbox.co/wp-content/uploads/2025/03/collbox-logo.svg
layout: provider
modified: '2026-10-28'
name: CollBox
nav: Providers
network: true
overview: 'CollBox is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Law, Finance, Software-as-a-Service, and Invoicing.


  CollBox''s developer surface includes getting-started guide, engineering blog, pricing, support, signup flow, and 9 more developer resources.'
plans:
- name: Collbox Plans Pricing
  plan_count: 2
  slug: collbox-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/collbox/collbox-2026-11-03T124850.png
security:
- kind: domain-security
  name: Collbox Domain Security
  slug: collbox-domain-security
  summary_line: TLSv1.3 · DMARC
slug: collbox
tags:
- Company
- Law
- Finance
- Software-as-a-Service
- Invoicing
website: https://collbox.co/
---
