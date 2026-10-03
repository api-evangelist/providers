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
  href: https://raw.githubusercontent.com/api-evangelist/biddingx/refs/heads/main/hosts/biddingx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biddingx-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.biddingx.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.biddingx.com/introduction/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biddingx/refs/heads/main/security/biddingx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biddingx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biddingx.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.biddingx.com/en/about
- group: docs
  title: ''
  type: APIReference
  url: https://www.biddingx.com/en/platform
- group: start
  title: ''
  type: GettingStarted
  url: https://www.biddingx.com/en/services
- group: operate
  title: ''
  type: Support
  url: https://www.biddingx.com/en/contact_us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.biddingx.com/en/terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.biddingx.com/en/data_protection_policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/biddingx
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://equityzen.com/company/biddingx
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: BiddingX is China’s award‑winning and advanced marketing technology platform with a performance‑driven AI algorithm. It empowers global marketers to effectively advertise in China, handling 50 billion bid requests per day and reaching 99 % of Chinese netizens, with 1 billion unique users.
layout: provider
modified: '2026-09-28'
name: Biddingx
nav: Providers
network: true
overview: 'Biddingx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Programmatic, DSP, and Artificial Intelligence.


  Biddingx''s developer surface includes documentation, API reference, getting-started guide, support, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biddingx Domain Security
  slug: biddingx-domain-security
  summary_line: TLSv1.3 · HSTS
slug: biddingx
tags:
- Company
- Marketing
- Programmatic
- DSP
- Artificial Intelligence
website: https://www.biddingx.com
---
