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
api_count: 1
apis:
- description: API reference for Apixio, part of Datavant.
  name: Apixio API
  slug: apixio-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apixio/refs/heads/main/well-known/apixio-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apixio-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apixio/refs/heads/main/well-known/apixio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apixio-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apixio/refs/heads/main/hosts/apixio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apixio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apixio/refs/heads/main/vendors/apixio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apixio-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datavant.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datavant.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.datavant.com/about/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.datavant.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datavant
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apixio/refs/heads/main/security/apixio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apixio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datavant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apixio.relayto.com
- group: docs
  title: ''
  type: APIReference
  url: https://review.apixio.com
- group: start
  title: ''
  type: GettingStarted
  url: https://review.apixio.com/login
coverage:
  checked: 2026-09-25
  detail: Review site renders via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://review.apixio.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Apixio provides AI-powered healthcare data solutions, improving operations, payments, and clinical outcomes for health plans and providers. The company, now part of Datavant, offers a Connected Care Platform that leverages actionable AI technology and flexible services to enable accurate payments, high‑quality patient care, and value‑based reimbursement models.
image: https://www.datavant.com/opengraph.png
layout: provider
modified: '2026-09-25'
name: Apixio
nav: Providers
network: true
overview: 'Apixio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Apixio''s developer surface includes engineering blog, documentation, API reference, getting-started guide, and 10 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 50.0
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apixio Domain Security
  slug: apixio-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: apixio
tags:
- Company
website: https://datavant.com/
---
