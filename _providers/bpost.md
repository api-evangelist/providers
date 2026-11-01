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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/bpost/hosts/bpost-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bpost-hosts.yml
- group: other
  href: https://artifacts.apis.io/bpost/vendors/bpost-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bpost-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.bpost.be/en/faqs/faq/registered-mail
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bpost.be/en/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.bpost.be/nl/blog
- group: auth
  href: https://artifacts.apis.io/bpost/security/bpost-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bpost-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bpost.be/
coverage:
  checked: '2026-10-27'
  detail: No machine‑readable API specification was found on the provider’s website or documented hosts.
  evidence:
  - status: 200
    url: https://www.bpost.be/en
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Bpost is the national postal service of Belgium, offering a wide range of mail and parcel delivery services for individuals and businesses. It provides online tools for tracking shipments, calculating rates, managing e‑shop orders, and accessing a customer portal. The company also supports international shipping, customs clearance, and specialized logistics solutions. Bpost’s digital platforms enable users to create shipping labels, schedule pickups, and integrate with e‑commerce systems, reflecting its modern approach to postal services.
layout: provider
modified: '2026-10-27'
name: bpost
nav: Providers
network: true
overview: 'bpost is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Postal, Logistics, Belgium, and Shipping.


  bpost''s developer surface includes signup flow, engineering blog, and 5 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bpost Domain Security
  slug: bpost-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: bpost
tags:
- Company
- Postal
- Logistics
- Belgium
- Shipping
website: https://bpost.be/
---
