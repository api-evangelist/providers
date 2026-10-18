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
  href: https://raw.githubusercontent.com/api-evangelist/carpool-logistics/refs/heads/main/hosts/carpool-logistics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carpool-logistics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carpool-logistics/refs/heads/main/vendors/carpool-logistics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carpool-logistics-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.carpoollogistics.com/
- group: other
  title: ''
  type: Leadership
  url: https://www.carpoollogistics.com/team/?hsLang=en
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carpool-logistics/refs/heads/main/security/carpool-logistics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carpool-logistics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carpoollogistics.com/
- group: company
  title: ''
  type: Blog
  url: https://www.carpoollogistics.com/blog/
- group: company
  title: ''
  type: About
  url: https://www.carpoollogistics.com/team/
- group: operate
  title: ''
  type: Contact
  url: https://www.carpoollogistics.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carpoollogistics.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carpoollogistics.com/terms-conditions/
coverage:
  checked: '2026-10-07'
  detail: Carpool Logistics provides a logistics platform but does not offer a public developer program or API.
  evidence:
  - status: 200
    url: https://www.carpoollogistics.com/
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Carpool Logistics provides end‑to‑end vehicle logistics with a documented chain of custody, moving over 200,000 vehicles annually for dealers, OEMs, fleets and individuals. Their platform offers managed transport, white‑glove home delivery, auction services, and digital tools like a browser extension and CarPass identity‑verified vehicle release, all accessible via a modern web portal.
layout: provider
modified: '2026-10-07'
name: Carpool Logistics
nav: Providers
network: true
overview: 'Carpool Logistics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Vehicles, Transportation, and Supply Chain.


  Carpool Logistics'' developer surface includes engineering blog and 10 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carpool Logistics Domain Security
  slug: carpool-logistics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carpool-logistics
tags:
- Company
- Logistics
- Vehicles
- Transportation
- Supply Chain
website: https://www.carpoollogistics.com/
---
