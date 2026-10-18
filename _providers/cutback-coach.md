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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cutback-coach/refs/heads/main/llms/cutback-coach-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cutback-coach-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cutback-coach/refs/heads/main/hosts/cutback-coach-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cutback-coach-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cutback-coach/refs/heads/main/vendors/cutback-coach-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cutback-coach-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sunnyside.co/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sunnyside.co/privacy/
- group: start
  title: ''
  type: Login
  url: https://app.sunnyside.co/login/phone
- group: company
  title: ''
  type: Blog
  url: https://www.sunnyside.co/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.sunnyside.co/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cutback-coach/refs/heads/main/security/cutback-coach-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cutback-coach-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sunnyside.co/
coverage:
  checked: '2026-10-12'
  detail: Help site provides markdown docs but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://help.sunnyside.co/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Sunnyside, formerly known as Cutback Coach, is a digital health company that helps people develop healthier relationships with alcohol. It offers behavior‑change tools, medication‑assisted programs, and a supportive online community, claiming to have helped over 600,000 users reduce their drinking by an average of 33%.
layout: provider
modified: '2026-10-12'
name: Cutback Coach
nav: Providers
network: true
overview: 'Cutback Coach is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Alcohol, and Wellness.


  Cutback Coach''s developer surface includes engineering blog, documentation, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cutback Coach Domain Security
  slug: cutback-coach-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cutback-coach
tags:
- Company
- Health
- Digital Health
- Alcohol
- Wellness
website: https://www.sunnyside.co/
---
