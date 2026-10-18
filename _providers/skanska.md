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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/skanska/refs/heads/main/hosts/skanska-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skanska-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/skanska/refs/heads/main/vendors/skanska-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skanska-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skanska.com/us/en/privacy-policy/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skanska.com/us/en/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/skanska/refs/heads/main/security/skanska-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skanska-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.skanska.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.skanska.com/us/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.skanska.com/us/en
- group: start
  title: ''
  type: GettingStarted
  url: https://www.skanska.com/us/en
- group: company
  title: ''
  type: Blog
  url: https://www.skanska.com/us/en/media
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://skanska.com/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Skanska is a global construction and development company delivering complex building and infrastructure projects across diverse market sectors. With a focus on sustainability, innovation, and community impact, Skanska builds for a better society, offering services in commercial development, transportation infrastructure, and building construction worldwide.
image: https://edit.skanska.com/en/site-settings/contentassets/skanska-orig-logo-rgb-534.png?v=2026-09-09T07:05:20Z
layout: provider
modified: '2026-10-14'
name: Skanska
nav: Providers
network: true
overview: 'Skanska is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Infrastructure, Sustainability, Global, and Engineering.


  Skanska''s developer surface includes documentation, getting-started guide, engineering blog, and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Skanska Domain Security
  slug: skanska-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skanska
tags:
- Construction
- Infrastructure
- Sustainability
- Global
- Engineering
website: https://www.skanska.com/
---
