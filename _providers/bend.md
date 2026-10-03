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
  href: https://raw.githubusercontent.com/api-evangelist/bend/refs/heads/main/hosts/bend-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bend-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bend/refs/heads/main/vendors/bend-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bend-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bend.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.bend.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bend.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bend/refs/heads/main/security/bend-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bend-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bend.com
coverage:
  checked: '2026-09-27'
  detail: Bend provides a mobile app but does not offer a public developer program or API.
  evidence:
  - status: 200
    url: https://bend.com
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Bend is a mobile application company offering a daily stretching and movement platform. The Bend app provides guided routines, video demonstrations, and progress tracking to help users improve flexibility, reduce pain, and maintain an active lifestyle. With millions of downloads, Bend targets a broad audience from beginners to athletes, emphasizing simplicity, affordability, and personalized workout plans.
image: https://bend.com/images/bend-preview.png
layout: provider
modified: '2026-09-27'
name: Bend
nav: Providers
network: true
overview: 'Bend is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Fitness, Mobile App, and Wellness.


  Bend''s developer surface includes support and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bend Domain Security
  slug: bend-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bend
tags:
- Company
- Health
- Fitness
- Mobile App
- Wellness
website: https://bend.com
---
