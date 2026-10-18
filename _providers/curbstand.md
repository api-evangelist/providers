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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curbstand/refs/heads/main/hosts/curbstand-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curbstand-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CurbStand
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curbstand/refs/heads/main/security/curbstand-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curbstand-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://curbstand.com/
- group: company
  title: ''
  type: AboutUs
  url: https://curbstand.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://curbstand.com/blog/
- group: operate
  title: ''
  type: Contact
  url: https://curbstand.com/get-in-touch/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://curbstand.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://curbstand.com/privacy-policy/
coverage:
  checked: '2026-10-12'
  detail: No public API documentation or developer program is available; attempts to fetch https://api.curbstand.com failed.
  evidence:
  - status: fail
    url: https://api.curbstand.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: CurbStand provides valet, monthly parking, and mobile car wash services in Los Angeles. Founded in 2013, it offers a mobile app for locating, paying, and tipping for valet services, as well as subscription-based monthly parking and on-demand car wash. The company emphasizes convenience, safety, and flexible pricing, targeting both individual drivers and event organizers.
image: https://curbstand.com/wp-content/uploads/2023/03/Logo-1x.png
layout: provider
modified: '2026-10-12'
name: CurbStand
nav: Providers
network: true
overview: 'CurbStand is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Valet, Parking, CarWash, and LosAngeles.


  CurbStand''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Curbstand Domain Security
  slug: curbstand-domain-security
  summary_line: TLSv1.3 · DMARC
slug: curbstand
tags:
- Company
- Valet
- Parking
- CarWash
- LosAngeles
website: https://curbstand.com/
---
