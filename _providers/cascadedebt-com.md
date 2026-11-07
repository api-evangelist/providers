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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cascadedebt-com/hosts/cascadedebt-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cascadedebt-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cascadedebt-com/vendors/cascadedebt-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cascadedebt-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cascadedebt.com/tos
- group: auth
  title: ''
  type: Security
  url: https://www.cascadedebt.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cascadedebt.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cascadedebt
- group: auth
  href: https://artifacts.apis.io/cascadedebt-com/security/cascadedebt-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cascadedebt-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cascadedebt.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cascadedebt.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://support.cascadedebt.com/tickets
- group: company
  title: ''
  type: Blog
  url: https://www.cascadedebt.com/insights
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cascadedebt.com
coverage:
  checked: '2026-10-22'
  detail: The Cascade website serves HTML with JavaScript rendering and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.cascadedebt.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Cascade Debt provides a precision asset‑based finance platform that streamlines institutional debt access. The web‑based solution simplifies lending processes, offering faster onboarding, transparent terms, and automated workflows for both lenders and borrowers. By leveraging modern technology, Cascade aims to reduce friction in capital markets and empower businesses to secure financing efficiently.
image: https://cdn.prod.website-files.com/66a2515470d3ed7f7117dbea/66c497613fa009537a4c63a0_Cascade%20-%20Rebrand.png
layout: provider
modified: '2026-10-21'
name: Cascade
nav: Providers
network: true
overview: 'Cascade is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, AssetBased, Lending, and Platform.


  Cascade''s developer surface includes documentation, support, engineering blog, and 9 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.3
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
screenshot: https://apis.io/screenshots/cascadedebt-com/cascadedebt-com-2026-11-03T123439.png
security:
- kind: domain-security
  name: Cascadedebt Com Domain Security
  slug: cascadedebt-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cascadedebt-com
tags:
- Company
- Finance
- AssetBased
- Lending
- Platform
website: https://cascadedebt.com
---
