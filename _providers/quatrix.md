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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/quatrix/plans/quatrix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quatrix-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/quatrix/hosts/quatrix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quatrix-hosts.yml
- group: other
  href: https://artifacts.apis.io/quatrix/vendors/quatrix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quatrix-vendors.yml
- group: build
  href: https://artifacts.apis.io/quatrix/packages/quatrix-packages.yml
  title: ''
  type: SDKs
  url: packages/quatrix-packages.yml
- group: build
  href: https://artifacts.apis.io/quatrix/packages/quatrix-packages.yml
  title: ''
  type: Packages
  url: packages/quatrix-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.maytech.net/blog/category/security
- group: commercial
  title: ''
  type: Pricing
  url: https://www.maytech.net/plans-pricing
- group: start
  title: ''
  type: Login
  url: https://www.maytech.net/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maytech
- group: auth
  href: https://artifacts.apis.io/quatrix/security/quatrix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quatrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://maytech.net/
- group: company
  title: ''
  type: Blog
  url: https://www.maytech.net/blog
- group: operate
  title: ''
  type: Support
  url: https://www.maytech.net/product-support
- group: docs
  title: ''
  type: Documentation
  url: https://www.maytech.net/product-support
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.maytech.net/product-support
coverage:
  checked: '2026-10-28'
  detail: Developer pages return 404 and the site relies heavily on JavaScript without machine‑readable API documentation.
  evidence:
  - status: 404
    url: https://www.maytech.net/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Quatrix, operating under the Maytech brand, provides secure file transfer, automated data acquisition, and compliant data sharing solutions for enterprises across industries such as finance, healthcare, and media. Their platform offers SFTP hosting, secure file sharing, large‑file transfers, and data rooms, emphasizing PCI compliance and robust security features.
image: https://www.maytech.net/wp-content/uploads/2019/08/banner-homepage@2x.png
layout: provider
modified: '2026-10-28'
name: Quatrix (Maytech)
nav: Providers
network: true
overview: 'Quatrix (Maytech) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, File Transfer, SecureData, Enterprise, and Compliance.


  Quatrix (Maytech)''s developer surface includes pricing, engineering blog, support, documentation, and 11 more developer resources.'
plans:
- name: Quatrix Plans Pricing
  plan_count: 9
  slug: quatrix-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 48.2
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/quatrix/quatrix-2026-11-03T141820.png
security:
- kind: domain-security
  name: Quatrix Domain Security
  slug: quatrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quatrix
tags:
- Company
- File Transfer
- SecureData
- Enterprise
- Compliance
- Cloud
website: https://maytech.net/
---
