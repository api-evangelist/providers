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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baozhunniu/refs/heads/main/hosts/baozhunniu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baozhunniu-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://facade.bznins.com/user/register?service=https://www.bznins.com/index
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bznpgi.bznins.com/file/api/out/show?filePath=/data/template/Documents/privacy.pdf
- group: company
  title: ''
  type: Newsroom
  url: https://www.bznins.com/news/list
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/baozhunniu/refs/heads/main/security/baozhunniu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baozhunniu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bznins.com/
coverage:
  checked: '2026-09-27'
  detail: No public developer program or API documentation is available on the company's website.
  evidence:
  - status: 200
    url: https://www.bznins.com/
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Baozhunniu (保准牛) is a Chinese insurance technology platform offering customized insurance solutions for enterprises and individuals. It provides a range of products such as group insurance, study abroad insurance, sports event coverage, and corporate risk management services. The platform integrates with major insurers, offers digital enrollment, claims assistance, and a user‑friendly portal for policy management, aiming to simplify insurance procurement and improve risk mitigation for businesses across various sectors.
layout: provider
modified: '2026-09-27'
name: Baozhunniu
nav: Providers
network: true
overview: 'Baozhunniu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Technology, Platform, China, and B2B.


  Baozhunniu''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 8.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Baozhunniu Domain Security
  slug: baozhunniu-domain-security
  summary_line: TLSv1.2
slug: baozhunniu
tags:
- Insurance
- Technology
- Platform
- China
- B2B
- Consumer
website: https://www.bznins.com/
---
