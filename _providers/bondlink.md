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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/bondlink/hosts/bondlink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bondlink-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.bondlink.com/resources/news
- group: start
  title: ''
  type: Login
  url: https://www.bondlink.com/login
- group: auth
  href: https://artifacts.apis.io/bondlink/security/bondlink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bondlink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bondlink.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bondlink.com/platform
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bondlink.com/platform
- group: operate
  title: ''
  type: Support
  url: https://www.bondlink.com/about-us/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bondlink.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bondlink.com/privacy
created: '2026-10-22'
description: BondLink provides a trusted software platform for municipal bond issuers, offering tools for bond sale marketing, investor relations, debt management, and analytics. The service includes modern deal pages, printing, distribution, and dedicated support, helping finance teams bring every bond sale to market with confidence.
image: https://www.bondlink.com/assets/img/logos/bondlink-social-share.png
layout: provider
modified: '2026-10-22'
name: BondLink
nav: Providers
network: true
overview: 'BondLink is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Software, Municipal Bonds, and Platform.


  BondLink''s developer surface includes documentation, getting-started guide, support, and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bondlink Domain Security
  slug: bondlink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bondlink
tags:
- Company
- Finance
- Software
- Municipal Bonds
- Platform
website: https://www.bondlink.com/
---
