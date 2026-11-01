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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for accessing subtitle data.
  name: OpenSubtitles API
  slug: opensubtitles-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/opensubtitles/hosts/opensubtitles-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opensubtitles-hosts.yml
- group: other
  href: https://artifacts.apis.io/opensubtitles/vendors/opensubtitles-vendors.yml
  title: ''
  type: Vendors
  url: vendors/opensubtitles-vendors.yml
- group: auth
  href: https://artifacts.apis.io/opensubtitles/security/opensubtitles-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opensubtitles-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opensubtitles.com/
created: '2026-10-28'
description: OpenSubtitles is a website dedicated to the aggregation of subtitles for audiovisual works. In 2022, OpenSubtitles was one of the 5,000 most accessed websites from the internet. OpenSubtitles was created in 2005 by the Slovak programmer Braňo. In 2018, the Federal Court of Australia issued an injunction demanding the blockage of 181 sites linked to online piracy, including OpenSubtitles. The case was filed by companies such as Village Roadshow, Disney, Twentieth Century Fox, Paramount Pictures, Columbia Pictures, Universal Pictures and Warner Bros.
image: https://www.opensubtitles.com/n/img/opensubtitles-beta_banner_black.png
layout: provider
modified: '2026-10-28'
name: OpenSubtitles
nav: Providers
network: true
overview: OpenSubtitles is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, subtitles, video, media, and API.
random_paper: 9
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Opensubtitles Domain Security
  slug: opensubtitles-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: opensubtitles
tags:
- Company
- subtitles
- video
- media
- API
website: https://opensubtitles.com/
---
