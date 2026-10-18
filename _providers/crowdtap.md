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
  href: https://raw.githubusercontent.com/api-evangelist/crowdtap/refs/heads/main/hosts/crowdtap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crowdtap-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crowdtap/refs/heads/main/vendors/crowdtap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crowdtap-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crowdtap/refs/heads/main/packages/crowdtap-packages.yml
  title: ''
  type: SDKs
  url: packages/crowdtap-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/crowdtap/refs/heads/main/packages/crowdtap-packages.yml
  title: ''
  type: Packages
  url: packages/crowdtap-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crowdtap
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crowdtap/refs/heads/main/security/crowdtap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crowdtap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crowdtap.com
coverage:
  checked: '2026-10-11'
  detail: No public developer documentation or API reference was found on crowdtap.com or api.crowdtap.com.
  evidence:
  - status: 200
    url: https://crowdtap.com
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Crowdtap is a consumer rewards platform that offers users the ability to earn points by answering surveys, sharing opinions, and completing offers. Users can redeem points for gift cards, product samples, and other rewards. The service operates via a web portal and mobile apps, targeting a broad audience seeking to monetize their feedback. Crowdtap partners with brands to gather market research, providing a marketplace for consumer insights.
layout: provider
modified: '2026-10-11'
name: Crowdtap
nav: Providers
network: true
overview: Crowdtap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include ConsumerRewards, Surveys, Market Research, Mobile App, and Gift Cards.
random_paper: 10
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crowdtap Domain Security
  slug: crowdtap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crowdtap
tags:
- ConsumerRewards
- Surveys
- Market Research
- Mobile App
- Gift Cards
website: https://crowdtap.com
---
