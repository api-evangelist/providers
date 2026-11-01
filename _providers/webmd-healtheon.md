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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/webmd-healtheon/security/webmd-healtheon-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/webmd-healtheon-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/webmd-healtheon/well-known/webmd-healtheon-symptoms-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/webmd-healtheon-symptoms-security.txt
- group: auth
  href: https://artifacts.apis.io/webmd-healtheon/well-known/webmd-healtheon-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/webmd-healtheon-security.txt
- group: auth
  href: https://artifacts.apis.io/webmd-healtheon/well-known/webmd-healtheon-member-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/webmd-healtheon-member-security.txt
- group: auth
  href: https://artifacts.apis.io/webmd-healtheon/well-known/webmd-healtheon-doctor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/webmd-healtheon-doctor-security.txt
- group: auth
  href: https://artifacts.apis.io/webmd-healtheon/well-known/webmd-healtheon-blogs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/webmd-healtheon-blogs-security.txt
- group: agent
  href: https://artifacts.apis.io/webmd-healtheon/well-known/webmd-healtheon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/webmd-healtheon-well-known.yml
- group: other
  href: https://artifacts.apis.io/webmd-healtheon/hosts/webmd-healtheon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/webmd-healtheon-hosts.yml
- group: other
  href: https://artifacts.apis.io/webmd-healtheon/vendors/webmd-healtheon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/webmd-healtheon-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.webmd.com/news/default.htm
- group: auth
  href: https://artifacts.apis.io/webmd-healtheon/security/webmd-healtheon-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/webmd-healtheon-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/webmd-healtheon/security/webmd-healtheon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/webmd-healtheon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.webmd.com/
coverage:
  checked: '2026-10-26'
  detail: WebMD does not provide a public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.webmd.com/robots.txt
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: WebMD (Healtheon) provides health information, tools and services through its extensive online platform. It offers medical content, symptom checkers, drug information, and personalized health resources to consumers and professionals. The company integrates various APIs for content delivery, user personalization, and data analytics, supporting developers in building health‑focused applications and services.
image: https://img.lb.wbmdstatic.com/vim/live/webmd/consumer_assets/site_images/logos/webmd/web/webmd-logo-fb.jpg
layout: provider
modified: '2026-10-26'
name: WebMD (Healtheon)
nav: Providers
network: true
overview: WebMD (Healtheon) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Information, API, and Consumer.
random_paper: 12
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Webmd Healtheon Domain Security
  slug: webmd-healtheon-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Webmd Healtheon Vulnerability Disclosure
  slug: webmd-healtheon-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: webmd-healtheon
tags:
- Company
- Health
- Information
- API
- Consumer
- Professional
website: https://www.webmd.com/
---
