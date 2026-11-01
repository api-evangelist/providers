---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 10.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 83
  human_in_the_loop: 6
  name: Keba Agentic Access
  operation_count: 150
  slug: keba-agentic-access
  summary_line: 150 operations · 83 acting · 6 human-in-the-loop
api_count: 1
apis:
- description: KEBA API reference as listed on their Swagger UI page.
  name: KEBA API
  slug: keba-api
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/keba/well-known/keba-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/keba-security.txt
- group: auth
  href: https://artifacts.apis.io/keba/well-known/keba-keba-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/keba-keba-security.txt
- group: agent
  href: https://artifacts.apis.io/keba/well-known/keba-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/keba-well-known.yml
- group: other
  href: https://artifacts.apis.io/keba/hosts/keba-hosts.yml
  title: ''
  type: Hosts
  url: hosts/keba-hosts.yml
- group: other
  href: https://artifacts.apis.io/keba/vendors/keba-vendors.yml
  title: ''
  type: Vendors
  url: vendors/keba-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.keba.com/en/banking-automation/why-keba/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.keba.com/en/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.keba.com/de/corporate/newsroom/news/aktuelles
- group: start
  title: ''
  type: Login
  url: https://jobs.keba.com/Login/33?culture=de
- group: docs
  title: ''
  type: APIReference
  url: https://api.keba.com/swagger
- group: auth
  href: https://artifacts.apis.io/keba/security/keba-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/keba-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/keba/security/keba-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keba-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://keba.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.keba.com/en/home
- group: operate
  title: ''
  type: Support
  url: https://www.keba.com/en/corporate/contact/sales-service-network/customer-service
- group: company
  title: ''
  type: Blog
  url: https://www.keba.com/en/corporate/newsroom/calender-of-events/events
coverage:
  detail: Swagger UI page renders via JavaScript and does not expose a raw OpenAPI spec.
  evidence:
  - status: 200
    url: https://api.keba.com/swagger
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: KEBA provides innovative automation solutions across industrial automation, banking, public services, and energy sectors. Their portfolio includes control panels, HMI interfaces, servo controllers, motors, safety technology, and digital services such as AI assistants and e‑charging solutions. The company focuses on integrating hardware and software to enable efficient, secure, and intelligent automation for factories, ATMs, parcel lockers, and more.
image: https://a.storyblok.com/f/keba/downloads/industrial-automation/29_KEBA-Gebaeude_ZOOM.jpg/m/1200x0
layout: provider
modified: '2026-10-28'
name: KEBA
nav: Providers
network: true
overview: 'KEBA publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, Industrial, DigitalSolutions, and Energy.


  The KEBA catalog on APIs.io includes 1 Spectral governance ruleset.


  KEBA''s developer surface includes API reference, documentation, support, engineering blog, and 12 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 0
  name: Keba Rate Limits
  slug: keba-rate-limits
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: KEBA API Rules
  rule_count: 6
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 0
  slug: keba-rules
scopes:
- name: Keba Scopes
  scope_count: 0
  slug: keba-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 15.9
    contract_quality: 6.0
    developer_ergonomics: 23.8
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 64
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Keba Authentication
  slug: keba-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Keba Domain Security
  slug: keba-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Keba Vulnerability Disclosure
  slug: keba-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-applicant
  slug: keba-get-applicant
slug: keba
tags:
- Company
- Automation
- Industrial
- DigitalSolutions
- Energy
website: https://keba.com/
---
