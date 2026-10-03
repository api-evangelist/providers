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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API for Believe services as described on the Believe for Artists page.
  name: Believe API
  slug: believe-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/believe/refs/heads/main/conformance/believe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/believe-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/believe/refs/heads/main/llms/believe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/believe-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/believe/refs/heads/main/well-known/believe-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/believe-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/believe/refs/heads/main/hosts/believe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/believe-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/believe/refs/heads/main/vendors/believe-vendors.yml
  title: ''
  type: Vendors
  url: vendors/believe-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.believe.com/newsroom/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/believe/refs/heads/main/security/believe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/believe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.believe.com/
- group: commercial
  title: ''
  type: Legal
  url: https://www.believe.com/legal/
- group: company
  title: ''
  type: Careers
  url: https://careers.believe.com
coverage:
  checked: '2026-09-27'
  detail: Docs are rendered via JavaScript and no OpenAPI spec is publicly available.
  evidence:
  - status: 200
    url: https://www.believe.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Believe is a global artist development company that provides recording, publishing, and distribution services. It works with independent artists, songwriters, record labels, and music publishers to develop careers, protect rights, and collect royalties worldwide. The company operates in more than 50 countries and supports its partners with technology, expertise, and operational support.
layout: provider
modified: '2026-09-27'
name: Believe
nav: Providers
network: true
overview: 'Believe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Artist Development, Songwriters, Record Labels, and Publishers.


  Believe''s developer surface includes legal docs and 9 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Believe Domain Security
  slug: believe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: believe
tags:
- Music
- Artist Development
- Songwriters
- Record Labels
- Publishers
- Distribution
website: https://www.believe.com/
---
