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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beeyond-media/refs/heads/main/hosts/beeyond-media-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beeyond-media-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beeyondmedia.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.beeyondmedia.com/news
- group: company
  title: ''
  type: Blog
  url: https://beeyondmedia.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beeyond-media/refs/heads/main/security/beeyond-media-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beeyond-media-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beeyondmedia.com
coverage:
  checked: '2026-09-27'
  detail: The site provides no developer documentation or API endpoints, only a marketing website.
  evidence:
  - status: 200
    url: https://beeyondmedia.com
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Beeyond Media provides a programmatic digital out‑of‑home (DOOH) advertising platform that connects brands and agencies with over 2.1 million billboards and screens worldwide. Their solution enables premium, data‑driven campaigns, real‑time inventory management, and detailed performance analytics for elite advertisers.
image: https://beeyondmedia.com/images/beeyond.jpg
layout: provider
modified: '2026-09-27'
name: Beeyond Media
nav: Providers
network: true
overview: 'Beeyond Media is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Digital Out Of Home, Programmatic, MediaTech, and Company.


  Beeyond Media''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beeyond Media Domain Security
  slug: beeyond-media-domain-security
  summary_line: TLSv1.3 · DMARC
slug: beeyond-media
tags:
- Advertising
- Digital Out Of Home
- Programmatic
- MediaTech
- Company
website: https://beeyondmedia.com
---
