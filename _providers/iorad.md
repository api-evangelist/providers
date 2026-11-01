---
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/iorad/vendors/iorad-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iorad-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/iorad/plans/iorad-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iorad-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/iorad/well-known/iorad-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/iorad-well-known.yml
- group: other
  href: https://artifacts.apis.io/iorad/hosts/iorad-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iorad-hosts.yml
- group: build
  href: https://artifacts.apis.io/iorad/packages/iorad-packages.yml
  title: ''
  type: SDKs
  url: packages/iorad-packages.yml
- group: build
  href: https://artifacts.apis.io/iorad/packages/iorad-packages.yml
  title: ''
  type: Packages
  url: packages/iorad-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.iorad.com/resources/help-center
- group: operate
  title: ''
  type: StatusPage
  url: https://status.iorad.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iorad.com/privacypolicy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iorad.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.iorad.com/login
- group: other
  title: ''
  type: Leadership
  url: https://www.iorad.com/leadership
- group: start
  title: ''
  type: GettingStarted
  url: https://www.iorad.com/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iorad.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iorad
- group: auth
  href: https://artifacts.apis.io/iorad/security/iorad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iorad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iorad.com/
coverage:
  checked: '2026-10-27'
  detail: The iorad website provides only HTML FAQ pages with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.iorad.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: iorad is an interactive tutorial builder that automatically captures step‑by‑step workflows and converts them into customer training materials, onboarding guides, and SOP documentation. Teams use iorad to quickly scale software adoption, self‑service learning, and internal training, creating interactive step‑by‑step tutorials in seconds for web applications.
image: https://www.iorad.com/logo.png
layout: provider
modified: '2026-10-27'
name: iorad
nav: Providers
network: true
overview: 'iorad is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tutorial, Training, Software Adoption, and Interactive.


  iorad''s developer surface includes support, pricing, getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Iorad Plans Pricing
  plan_count: 5
  slug: iorad-plans-pricing
random_paper: 23
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 50.0
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Iorad Domain Security
  slug: iorad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iorad
tags:
- Company
- Tutorial
- Training
- Software Adoption
- Interactive
website: https://www.iorad.com/
---
