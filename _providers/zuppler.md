---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/zuppler/hosts/zuppler-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zuppler-hosts.yml
- group: other
  href: https://artifacts.apis.io/zuppler/vendors/zuppler-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zuppler-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.zuppler.com/blog/tag/Security
- group: auth
  href: https://artifacts.apis.io/zuppler/security/zuppler-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zuppler-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zuppler.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zuppler.com/online-food-ordering-system
- group: start
  title: ''
  type: DeveloperPortal
  url: https://order.zuppler.com
- group: company
  title: ''
  type: Blog
  url: https://www.zuppler.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zuppler.com/connect
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zuppler.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zuppler.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.zuppler.com/portal/en/home
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zuppler
coverage:
  checked: '2026-10-27'
  detail: The developer portal at https://order.zuppler.com loads a JavaScript‑rendered interface with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://order.zuppler.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Zuppler provides online ordering and restaurant revenue solutions, offering a platform for restaurants to manage orders, catering, multi‑brand operations, and marketplace integrations. Their services include white‑label solutions, mobile apps, loyalty programs, marketing automation, gift cards, AI‑driven upselling, and analytics, helping restaurants increase sales and streamline operations.
image: http://static1.squarespace.com/static/5a8d9d13d55b413a6330e9f0/t/5ad08616575d1fe016cbf3ed/1523615255551/zuppler-logo-dark.png?format=1500w
layout: provider
modified: '2026-10-27'
name: Zuppler
nav: Providers
network: true
overview: 'Zuppler is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Online Ordering, RestaurantTech, and Software-as-a-Service.


  Zuppler''s developer surface includes documentation, engineering blog, pricing, support, and 9 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 39.3
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.2
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/zuppler/zuppler-2026-11-03T150556.png
security:
- kind: domain-security
  name: Zuppler Domain Security
  slug: zuppler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zuppler
tags:
- Company
- Online Ordering
- RestaurantTech
- Software-as-a-Service
website: https://www.zuppler.com/
---
