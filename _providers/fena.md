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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/fena/hosts/fena-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fena-hosts.yml
- group: other
  href: https://artifacts.apis.io/fena/vendors/fena-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fena-vendors.yml
- group: build
  href: https://artifacts.apis.io/fena/packages/fena-packages.yml
  title: ''
  type: SDKs
  url: packages/fena-packages.yml
- group: build
  href: https://artifacts.apis.io/fena/packages/fena-packages.yml
  title: ''
  type: Packages
  url: packages/fena-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fena.co/useful/security
- group: auth
  href: https://artifacts.apis.io/fena/security/fena-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fena-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fena.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://toolkit-docs.fena.co/
- group: docs
  title: ''
  type: Documentation
  url: https://toolkit-docs.fena.co/
- group: operate
  title: ''
  type: Support
  url: https://help.fena.co/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.fena.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fena-co
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fena.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fena.co/useful/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fena.co/useful/privacy-policy
created: '2026-10-20'
description: Fena Labs Ltd provides Open Banking payment solutions, enabling merchants to accept bank‑to‑bank transfers, instant payments, and recurring payments via APIs, plugins, and a mobile app. Their platform offers transparent pricing, real‑time transaction monitoring, and tools for finance teams, serving over 2,500 UK merchants with high‑speed, low‑cost payments.
image: https://framerusercontent.com/images/MOvni85FmOjGqmlH2HcEhN80eeY.png
layout: provider
modified: '2026-10-20'
name: Fena Labs Ltd
nav: Providers
network: true
overview: 'Fena Labs Ltd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, OpenBanking, FinTech, and API.


  Fena Labs Ltd''s developer surface includes documentation, support, engineering blog, pricing, and 11 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fena Domain Security
  slug: fena-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fena
tags:
- Company
- Payments
- OpenBanking
- FinTech
- API
website: https://fena.co/
---
