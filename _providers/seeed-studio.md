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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: GraphQL endpoint providing data for Seeed Studio services.
  name: Seeed Studio GraphQL API
  slug: seeed-studio-graphql-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seeed-studio/refs/heads/main/hosts/seeed-studio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seeed-studio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seeed-studio/refs/heads/main/vendors/seeed-studio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seeed-studio-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seeedstudio.com/privacy_policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Seeed-Studio
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seeed-studio/refs/heads/main/security/seeed-studio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seeed-studio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.seeedstudio.com
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.seeedstudio.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://wiki.seeedstudio.com/Getting_Started/
- group: operate
  title: ''
  type: Support
  url: https://www.seeedstudio.com/get_help/
- group: company
  title: ''
  type: Blog
  url: https://www.seeedstudio.com/blog/
created: '2026-10-13'
description: Seeed Studio is a global IoT hardware enabler offering a wide range of open‑source hardware, development boards, sensors, and modules. Founded in 2010, it supports makers, startups, and enterprises with products like the Wio Terminal, Grove system, and reComputer series, plus a comprehensive wiki, community forums, and developer resources. The company emphasizes rapid prototyping, open‑source collaboration, and end‑to‑end solutions from hardware to cloud services.
image: https://www.seeedstudio.com/_pub/images/seeedstudio.png
layout: provider
modified: '2026-10-13'
name: Seeed Studio
nav: Providers
network: true
overview: 'Seeed Studio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Hardware, Open Source, and Community.


  Seeed Studio''s developer surface includes documentation, getting-started guide, support, engineering blog, and 6 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 29.8
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Seeed Studio Domain Security
  slug: seeed-studio-domain-security
  summary_line: TLSv1.3
slug: seeed-studio
tags:
- Company
- IoT
- Hardware
- Open Source
- Community
website: https://www.seeedstudio.com
---
