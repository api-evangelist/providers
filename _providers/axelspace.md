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
  href: https://raw.githubusercontent.com/api-evangelist/axelspace/refs/heads/main/hosts/axelspace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axelspace-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.axelspace.com/privacypolicy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.axelspace.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axelspace
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axelspace/refs/heads/main/security/axelspace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axelspace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.axelspace.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/axelspace
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Axelspace has been leading the space business industry as a pioneer of microsatellite technology since 2008. With the vision of “Space within Your Reach,” Axelspace is determined to demonstrate its continued leadership in the realization of an advanced society, offering satellite imagery, data services, and innovative space solutions to customers worldwide.
image: https://www.axelspace.com/assets/img/ogp/ogp.png
layout: provider
modified: '2026-09-27'
name: Axelspace
nav: Providers
network: true
overview: Axelspace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Space, Satellite, Imagery, Data Services, and Innovation.
random_paper: 4
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 5.3
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
  name: Axelspace Domain Security
  slug: axelspace-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: axelspace
tags:
- Space
- Satellite
- Imagery
- Data Services
- Innovation
website: https://www.axelspace.com
---
