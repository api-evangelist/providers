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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/mediaredefined-com/hosts/mediaredefined-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mediaredefined-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/mediaredefined-com/vendors/mediaredefined-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mediaredefined-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://redef.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/REDEF
- group: auth
  href: https://artifacts.apis.io/mediaredefined-com/security/mediaredefined-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mediaredefined-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://redef.com/
- group: docs
  title: ''
  type: Documentation
  url: https://redef.com/info/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redef.com/info/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redef.com/info/terms
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://redef.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: ReDEF (formerly Media Redefined) is a digital media curation platform that aggregates newsletters, podcasts, and articles across topics like tech, fashion, sports, and culture. It offers a personalized feed, original content, and community-driven mixes, aiming to move minds through curated stories and ideas. The service provides public channels, subscription options, and a public API for accessing its content catalog.
image: https://redef.com/static/assets/images/global/redef-placeholder-square.png
layout: provider
modified: '2026-10-21'
name: ReDEF
nav: Providers
network: true
overview: 'ReDEF is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Curation, Newsletter, and Podcast.


  ReDEF''s developer surface includes documentation and 8 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mediaredefined Com Domain Security
  slug: mediaredefined-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mediaredefined-com
tags:
- Company
- Media
- Curation
- Newsletter
- Podcast
website: https://redef.com/
---
