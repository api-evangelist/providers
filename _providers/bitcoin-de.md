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
- group: operate
  href: https://artifacts.apis.io/bitcoin-de/changelog/bitcoin-de-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bitcoin-de-changelog.yml
- group: other
  href: https://artifacts.apis.io/bitcoin-de/hosts/bitcoin-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitcoin-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitcoin-de/vendors/bitcoin-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitcoin-de-vendors.yml
- group: build
  href: https://artifacts.apis.io/bitcoin-de/packages/bitcoin-de-packages.yml
  title: ''
  type: SDKs
  url: packages/bitcoin-de-packages.yml
- group: build
  href: https://artifacts.apis.io/bitcoin-de/packages/bitcoin-de-packages.yml
  title: ''
  type: Packages
  url: packages/bitcoin-de-packages.yml
- group: start
  title: ''
  type: Login
  url: https://www.bitcoin.de/de/login
- group: auth
  href: https://artifacts.apis.io/bitcoin-de/security/bitcoin-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitcoin-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bitcoin.de/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bitcoin.de/de/api/tapi/doc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitcoin.de/de/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitcoin.de/de/datenschutzerklaerung
- group: commercial
  title: ''
  type: Legal
  url: https://www.bitcoin.de/de/impressum
- group: operate
  title: ''
  type: Support
  url: https://www.bitcoin.de/de/kontakt
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.bitcoin.de/de/faq
- group: company
  title: ''
  type: Blog
  url: https://www.bitcoin.de/de/presse
- group: auth
  title: ''
  type: Security
  url: https://www.bitcoin.de/de/bug-bounty
created: '2026-10-27'
description: Bitcoin.de is a German cryptocurrency exchange and marketplace offering buying, selling, and trading of Bitcoin and other digital assets. It provides a platform for users to manage crypto portfolios, access price data, and utilize P2P trading services. The company operates under regulatory oversight in Germany and aims to make cryptocurrency accessible to a broad audience.
layout: provider
modified: '2026-10-27'
name: Bitcoin.de
nav: Providers
network: true
overview: 'Bitcoin.de is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Bitcoin.de''s developer surface includes changelog, documentation, legal docs, support, engineering blog, and 11 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 35.7
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitcoin De Domain Security
  slug: bitcoin-de-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitcoin-de
tags:
- Company
website: https://www.bitcoin.de/
---
