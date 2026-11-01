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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/qworum/plans/qworum-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qworum-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/qworum/security/qworum-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/qworum-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/qworum/well-known/qworum-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/qworum-security.txt
- group: agent
  href: https://artifacts.apis.io/qworum/well-known/qworum-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qworum-well-known.yml
- group: other
  href: https://artifacts.apis.io/qworum/hosts/qworum-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qworum-hosts.yml
- group: other
  href: https://artifacts.apis.io/qworum/vendors/qworum-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qworum-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://qworum.net/en/plans/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://qworum.net/en/developers/
- group: auth
  href: https://artifacts.apis.io/qworum/security/qworum-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/qworum-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/qworum/security/qworum-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qworum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qworum.net/
coverage:
  checked: '2026-10-21'
  detail: The domain qworum.com redirects to a parked domain with no API documentation.
  evidence:
  - status: 200
    url: http://qworum.com
  reason: defunct
  state: none
created: '2026-10-21'
description: Qworum builds distributed web applications using micro‑frontends and micro‑services architecture. The platform enables developers to compose modular front‑end components that run independently yet integrate seamlessly, offering scalable, maintainable solutions for complex web ecosystems. Qworum provides tooling, runtime support, and APIs to orchestrate these components, targeting modern web development teams seeking flexibility and performance.
layout: provider
modified: '2026-10-21'
name: Qworum
nav: Providers
network: true
overview: 'Qworum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Distributed, Web, Micro‑frontends, and Micro‑services.


  Qworum''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Qworum Plans Pricing
  plan_count: 2
  slug: qworum-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Qworum Domain Security
  slug: qworum-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Qworum Vulnerability Disclosure
  slug: qworum-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: qworum
tags:
- Company
- Distributed
- Web
- Micro‑frontends
- Micro‑services
website: https://qworum.net/
---
