---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bmi/refs/heads/main/well-known/bmi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bmi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bmi/refs/heads/main/hosts/bmi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bmi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bmi/refs/heads/main/vendors/bmi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bmi-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bmi/refs/heads/main/security/bmi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bmi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bmi.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bmi.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bmi.com/legal/terms-and-conditions-of-use
- group: operate
  title: ''
  type: Contact
  url: https://www.bmi.com/contact-us
- group: company
  title: ''
  type: About
  url: https://www.bmi.com/about
coverage:
  checked: 2026-09-23
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found at the API host or documentation pages.
  evidence:
  - status: 0
    url: https://api.bmi.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-23'
description: Broadcast Music, Inc. (BMI) is the largest performing rights organization in the United States, representing songwriters, composers and music publishers. It collects and distributes royalties for public performances of music, offers licensing services to businesses, and provides resources, advocacy, and career development for music creators. BMI also runs programs like Health Connect, Spark, and AI & Copyright initiatives to support its members.
layout: provider
modified: '2026-09-23'
name: BMI
nav: Providers
network: true
overview: BMI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Royalties, Licensing, and Advocacy.
random_paper: 4
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 8.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bmi Domain Security
  slug: bmi-domain-security
  summary_line: TLSv1.2 · DMARC
slug: bmi
tags:
- Company
- Music
- Royalties
- Licensing
- Advocacy
website: https://bmi.com/
---
