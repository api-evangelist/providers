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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'EquateAPI is a partner API exposed by EquatePlus, Computershare''s employee share plan platform, that supports real-time data loads of participant information from a company''s HR platform with instant '
  name: Computershare EquateAPI
  slug: computershare-equateapi
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/computershare/hosts/computershare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/computershare-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://www.computershare.com/
- group: auth
  href: https://artifacts.apis.io/computershare/security/computershare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/computershare-domain-security.yml
- group: other
  title: ''
  type: APIOverview
  url: https://www.computershare.com/us/business/employee-share-plans/equateapi
- group: company
  title: ''
  type: About
  url: https://www.computershare.com/corporate/about-us/our-company
- group: operate
  title: ''
  type: Support
  url: https://www.computershare.com/us/contact-us
- group: company
  title: ''
  type: Newsroom
  url: https://www.computershare.com/us/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.computershare.com/us/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.computershare.com/ca/en/governance/terms-and-conditions
- group: start
  title: ''
  type: Login
  url: https://www-us.computershare.com/AdvisorPortal/Login
- group: company
  title: ''
  type: Careers
  url: http://careers.computershare.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/computershare
- group: other
  title: ''
  type: X
  url: https://x.com/computershare
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/COMPUTERSHARE
created: '2026-10-21'
description: Computershare is a global financial administration company providing transfer agency and share registry services, employee equity plans (EquatePlus), proxy solicitation (Georgeson), entity compliance (GEMS), corporate trust, stakeholder communications and other diversified financial and governance services. Its public web presence documents EquateAPI, a partner API exposed by EquatePlus that supports real-time loads of participant data from HR systems as an alternative to SFTP file exchange; no public developer portal or API reference was found.
image: https://www.computershare.com/img/new-img/og-image-cpu.jpg
layout: provider
modified: '2026-10-21'
name: Computershare
nav: Providers
network: true
overview: 'Computershare is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Transfer Agent, Share Registry, and Employee Equity Plans.


  Computershare''s developer surface includes support, YouTube channel, and 12 more developer resources.'
plans:
- name: Computershare Plans Pricing
  plan_count: 0
  slug: computershare-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Computershare Rate Limits
  slug: computershare-rate-limits
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.9
    operational_transparency: 0.0
  previous_composite: 15.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Computershare Domain Security
  slug: computershare-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: computershare
tags:
- Company
- Financial Services
- Transfer Agent
- Share Registry
- Employee Equity Plans
- Proxy Solicitation
- Corporate Trust
- Governance
website: https://www.computershare.com/
---
