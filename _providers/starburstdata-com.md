---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/starburstdata-com/plans/starburstdata-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/starburstdata-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/starburstdata-com/hosts/starburstdata-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/starburstdata-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/starburstdata-com/vendors/starburstdata-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/starburstdata-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/starburstdata-com/packages/starburstdata-com-packages.yml
  title: ''
  type: SDKs
  url: packages/starburstdata-com-packages.yml
- group: build
  href: https://artifacts.apis.io/starburstdata-com/packages/starburstdata-com-packages.yml
  title: ''
  type: Packages
  url: packages/starburstdata-com-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.starburst.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.starburst.io/terms/
- group: operate
  title: ''
  type: Support
  url: https://www.starburst.io/learn/support/
- group: auth
  title: ''
  type: Security
  url: https://www.starburst.io/about/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.starburst.io/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.starburst.io/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.starburst.io/about/newsroom/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.starburst.io/starburst-enterprise/releases/
- group: company
  title: ''
  type: Blog
  url: https://www.starburst.io/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.starburst.io/info/starburst-galaxy-onboarding/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.starburstdata.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/starburstdata
- group: auth
  href: https://artifacts.apis.io/starburstdata-com/security/starburstdata-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/starburstdata-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.starburstdata.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://docs.starburstdata.com/mcp
  - status: 200
    url: https://www.starburstdata.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Starburst provides an enterprise‑grade data platform that enables query across multiple sources using data federation, Trino, and Apache Iceberg. It helps organizations unify analytics, reduce data movement, and accelerate insights while offering robust security, governance, and performance features for modern data workloads.
image: https://www.starburst.io/wp-content/uploads/2026/09/brand-starburst-feature-image.png
layout: provider
modified: '2026-10-22'
name: Starburst
nav: Providers
network: true
overview: 'Starburst is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Platform, Analytics, Trino, and Apache Iceberg.


  Starburst''s developer surface includes support, pricing, changelog, engineering blog, getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Starburstdata Com Plans Pricing
  plan_count: 4
  slug: starburstdata-com-plans-pricing
random_paper: 0
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 50.0
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Starburstdata Com Domain Security
  slug: starburstdata-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: starburstdata-com
tags:
- Company
- Data Platform
- Analytics
- Trino
- Apache Iceberg
website: https://www.starburstdata.com
---
