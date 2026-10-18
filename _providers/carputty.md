---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Carputty provides a flexible auto financing API for loan pre‑qualification and management.
  name: Carputty API
  slug: carputty-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/carputty/refs/heads/main/plans/carputty-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carputty-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carputty/refs/heads/main/conformance/carputty-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carputty-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carputty/refs/heads/main/hosts/carputty-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carputty-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carputty/refs/heads/main/vendors/carputty-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carputty-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.carputty.com/support-categories/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carputty
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carputty/refs/heads/main/security/carputty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carputty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carputty.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.carputty.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.carputty.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.carputty.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.carputty.com/landing/flexloan
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://api.carputty.com/mcp
  - status: 200
    url: https://www.carputty.com
  - status: 403
    url: https://equityzen.com/company/carputty
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Carputty provides flexible auto financing solutions, offering consumers real-time, transparent lines of credit for vehicle purchases. Their platform enables users to pre‑qualify for loans without impacting credit scores, choose financing terms, and manage the process online. Carputty aims to simplify car ownership by delivering clear, fast, and user‑friendly financing options, backed by proprietary valuation tools and a mission to rewrite industry rules.
layout: provider
modified: '2026-10-07'
name: Carputty
nav: Providers
network: true
overview: 'Carputty is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AutoFinance, Fintech, Loans, and ConsumerCredit.


  Carputty''s developer surface includes getting-started guide, documentation, engineering blog, support, pricing, and 7 more developer resources.'
plans:
- name: Carputty Plans Pricing
  plan_count: 2
  slug: carputty-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 62.5
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carputty Domain Security
  slug: carputty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carputty
tags:
- Company
- AutoFinance
- Fintech
- Loans
- ConsumerCredit
- Technology
website: https://www.carputty.com
---
