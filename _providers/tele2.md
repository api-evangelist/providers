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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tele2/refs/heads/main/well-known/tele2-tele2-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tele2-tele2-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tele2/refs/heads/main/well-known/tele2-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tele2-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tele2/refs/heads/main/well-known/tele2-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tele2-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tele2/refs/heads/main/hosts/tele2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tele2-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tele2/refs/heads/main/vendors/tele2-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tele2-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tele2.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tele2.com/investors/the-share/privacy-notice/
- group: company
  title: ''
  type: Newsroom
  url: https://www.tele2.com/media
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tele2.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tele2/refs/heads/main/security/tele2-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tele2-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tele2/refs/heads/main/security/tele2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tele2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tele2.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://tele2.com/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Tele2 is a leading European telecommunications operator offering mobile, broadband, and digital services across multiple countries. It focuses on innovative, affordable connectivity solutions for consumers and businesses, emphasizing sustainability and smart network technologies. The company operates in Sweden, the Baltics, and other markets, providing 5G, IoT, and wholesale services, and maintains a corporate website with extensive information about its vision, governance, and offerings.
image: https://www.tele2.com/files/HuvudKVkomprimerad1THUMB.jpg
layout: provider
modified: '2026-10-14'
name: Tele2
nav: Providers
network: true
overview: 'Tele2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Mobile, Broadband, and Europe.


  Tele2''s developer surface includes documentation and 11 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 13.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tele2 Domain Security
  slug: tele2-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tele2 Vulnerability Disclosure
  slug: tele2-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tele2
tags:
- Company
- Telecommunications
- Mobile
- Broadband
- Europe
website: https://tele2.com/
---
