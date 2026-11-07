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
  href: https://artifacts.apis.io/simplefin/hosts/simplefin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/simplefin-hosts.yml
- group: other
  href: https://artifacts.apis.io/simplefin/vendors/simplefin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/simplefin-vendors.yml
- group: build
  href: https://artifacts.apis.io/simplefin/packages/simplefin-packages.yml
  title: ''
  type: SDKs
  url: packages/simplefin-packages.yml
- group: build
  href: https://artifacts.apis.io/simplefin/packages/simplefin-packages.yml
  title: ''
  type: Packages
  url: packages/simplefin-packages.yml
- group: auth
  href: https://artifacts.apis.io/simplefin/security/simplefin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simplefin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.simplefin.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.simplefin.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.simplefin.org/
- group: docs
  title: ''
  type: APIReference
  url: https://www.simplefin.org/protocol.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.simplefin.org/ecosystem.html
- group: operate
  title: ''
  type: Support
  url: https://www.simplefin.org/
- group: company
  title: ''
  type: Blog
  url: https://www.simplefin.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/simplefin
- group: operate
  title: ''
  type: Roadmap
  url: https://www.simplefin.org/CHANGELOG.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.simplefin.org/CHANGELOG.html
created: '2026-10-26'
description: SimpleFIN Bridge provides a read‑only financial data interchange protocol that enables applications to access banking information without requiring users to share credentials. Acting as a “window on a safe,” SimpleFIN lets users grant view‑only access to their financial accounts, supporting both Protocol v1 and v2. The service is open, free to use, and aims to become an RSS‑style standard for financial data aggregation, promoting security and user control across the banking ecosystem.
layout: provider
modified: '2026-10-26'
name: SimpleFIN Bridge
nav: Providers
network: true
overview: 'SimpleFIN Bridge is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Open Source, and Data.


  SimpleFIN Bridge''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 9 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 35.7
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.0
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
screenshot: https://apis.io/screenshots/simplefin/simplefin-2026-11-03T143218.png
security:
- kind: domain-security
  name: Simplefin Domain Security
  slug: simplefin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: simplefin
tags:
- Company
- Finance
- Open Source
- Data
website: https://www.simplefin.org/
---
