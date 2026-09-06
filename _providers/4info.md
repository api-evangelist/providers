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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/4info
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4info-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: 4INFO was fully absorbed into Cadent in January 2020 and its domain is now mail-only — 4info.com and www.4info.com publish no A or AAAA record at all, so every HTTP and /.well-known probe fails at DNS resolution rather than returning a page, and the last Internet Archive capture of the site (2023-02) is followed by a 404.
  evidence:
  - status: 0
    url: https://4info.com/
  - status: 0
    url: https://www.4info.com/
  - status: 0
    url: https://4info.com/.well-known/api-catalog
  - status: 404
    url: https://web.archive.org/web/20230528013343/https://4INFO.com/
  - status: 200
    url: https://apitracker.io/a/4info
  - status: 200
    url: https://github.com/4info
  reason: defunct
  state: none
created: '2026-09-05'
description: '4INFO, Inc. was a San Mateo (originally Palo Alto) California advertising-technology company founded in 2004 by Pankaj Shah and Zaw Thet. It began as an SMS content and alerting service — Nielsen called it the largest business-to-consumer SMS content provider in North America in 2008 — then pivoted in 2010 into mobile display advertising with the AdHaven platform, a mobile ad server, audience data-management and analytics stack sold to publishers, aggregators and national advertisers. Its later product was an identity graph: patented technology ("Systems and methods for statistically associating mobile devices to households") that statistically resolved mobile devices, set-top boxes and connected TVs back to a single household so brands could target and measure across screens. mBlox bought the legacy SMS business in 2015, and Cadent acquired the remaining company in January 2020, folding the identity and cross-screen targeting technology into Cadent''s advanced-TV platform.
  4INFO no longer operates as an independent company: 4info.com is retained for email only and publishes no A or AAAA record, so there is no website, developer portal, API reference or machine-readable contract of any kind on any 4Info host, live or archived.'
layout: provider
modified: '2026-09-05'
name: 4Info
nav: Providers
network: true
overview: 4Info is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Mobile Advertising, and Advanced TV.
random_paper: 18
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 4Info Domain Security
  slug: 4info-domain-security
  summary_line: no transport/DNS hardening detected
slug: 4info
tags:
- Company
- Advertising
- AdTech
- Mobile Advertising
- Advanced TV
- Identity Resolution
- Audience Targeting
- Data
- Acquired
- Defunct
---
