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
  score: 13.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: DISA provides compliance, background check, drug testing, and occupational health services via its platform.
  name: DISA API
  slug: disa-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/disa/well-known/disa-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/disa-well-known.yml
- group: other
  href: https://artifacts.apis.io/disa/hosts/disa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/disa-hosts.yml
- group: other
  href: https://artifacts.apis.io/disa/vendors/disa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/disa-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://disa.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://disa.com/news/
- group: start
  title: ''
  type: Login
  url: https://auth.disa.com/account/login
- group: other
  title: ''
  type: Leadership
  url: https://disa.com/disa-difference/team/
- group: auth
  href: https://artifacts.apis.io/disa/security/disa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/disa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://disa.com/
coverage:
  checked: '2026-10-23'
  detail: The DISA website returns HTML but provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://disa.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: DISA Global Solutions provides comprehensive compliance, background check, drug testing, and occupational health services to enterprises worldwide. With over 40 years of experience, DISA serves more than 30% of Fortune 500 companies across industries such as healthcare, entertainment, transportation, and retail. Their solutions cover the full employee lifecycle, from pre‑hire screening to ongoing monitoring, helping clients mitigate risk and ensure regulatory compliance.
image: https://disa.com/assets/DISA-article-card-2.png?fit=contain&height=630&width=1200&s=oH_Zesk7PchRr_3GZd6_Evj_9cP5BsUaj7elysf6PuQ
layout: provider
modified: '2026-10-23'
name: DISA
nav: Providers
network: true
overview: DISA is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Compliance, Background Checks, HR Technology, and Enterprise Services.
random_paper: 9
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Disa Domain Security
  slug: disa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: disa
tags:
- Company
- Compliance
- Background Checks
- HR Technology
- Enterprise Services
website: https://disa.com/
---
