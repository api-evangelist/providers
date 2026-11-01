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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/hatch-co/hosts/hatch-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hatch-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/hatch-co/vendors/hatch-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hatch-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hatch.co/terms
- group: operate
  title: ''
  type: Support
  url: https://help.hatch.co/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hatch.co/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.hatch.co/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.hatch.co/
- group: auth
  href: https://artifacts.apis.io/hatch-co/security/hatch-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hatch-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hatch.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hatch.co/learn/hatch-sleep-clock
coverage:
  checked: '2026-10-29'
  detail: Hatch provides smart sleep devices and does not offer a public developer API.
  evidence:
  - status: 200
    url: https://www.hatch.co/
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: Hatch offers a variety of smart sleep devices to help you sleep better night after night. Create healthy sleeping habits for the whole family with Hatch. Their flagship Hatch Sleep Clock is a sleep tracker designed to get you to sleep without relying on scores, offering customizable light and sound routines.
image: https://www.hatch.co/img/logos/hatch-logo.svg
layout: provider
modified: '2026-10-29'
name: Hatch
nav: Providers
network: true
overview: 'Hatch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include sleep, health, smart-home, iot, and family.


  Hatch''s developer surface includes support, engineering blog, documentation, getting-started guide, and 6 more developer resources.'
plans:
- name: Hatch Co Plans Pricing
  plan_count: 0
  slug: hatch-co-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Hatch Co Rate Limits
  slug: hatch-co-rate-limits
scopes:
- name: Hatch Co Scopes
  scope_count: 0
  slug: hatch-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 24.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hatch Co Authentication
  slug: hatch-co-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hatch Co Domain Security
  slug: hatch-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hatch-co
tags:
- sleep
- health
- smart-home
- iot
- family
- wellness
website: https://www.hatch.co/
---
