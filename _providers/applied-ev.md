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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/applied-ev/refs/heads/main/well-known/applied-ev-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/applied-ev-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/applied-ev/refs/heads/main/well-known/applied-ev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/applied-ev-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/applied-ev/refs/heads/main/hosts/applied-ev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applied-ev-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/applied-ev/refs/heads/main/vendors/applied-ev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/applied-ev-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/applied-ev/refs/heads/main/security/applied-ev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/applied-ev-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/applied-ev/refs/heads/main/security/applied-ev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applied-ev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.appliedev.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.appliedev.com/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appliedev.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appliedev.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.appliedev.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.appliedev.com/news
coverage:
  checked: 2026-09-25
  detail: Applied EV does not publish any developer program or public API documentation.
  evidence:
  - status: 200
    url: https://www.appliedev.com
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: Applied EV is a Melbourne‑based mobility technology company developing autonomous electric freight and industrial vehicles. It offers a software‑defined platform with a proprietary Digital Backbone control system, enabling scalable autonomy for logistics, warehouse, and factory transport. The company provides hardware such as the Blanc Robot cabin‑less vehicle and a suite of power and control products, and partners with firms like Siemens, NXP, and Oxbotica to deliver end‑to‑end autonomous solutions.
image: https://www.appliedev.com/api/assets/5146586c-032d-4b18-90fc-2edeffc24a30
layout: provider
modified: '2026-09-25'
name: Applied Ev
nav: Providers
network: true
overview: 'Applied Ev is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobility, Autonomous Vehicles, Electric, and Logistics.


  Applied Ev''s developer surface includes documentation, support, engineering blog, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 14.3
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
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Applied Ev Domain Security
  slug: applied-ev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Applied Ev Vulnerability Disclosure
  slug: applied-ev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: applied-ev
tags:
- Company
- Mobility
- Autonomous Vehicles
- Electric
- Logistics
- Technology
website: https://www.appliedev.com/
---
