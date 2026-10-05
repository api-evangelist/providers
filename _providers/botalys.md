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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/botalys/refs/heads/main/hosts/botalys-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botalys-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/botalys/refs/heads/main/vendors/botalys-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botalys-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/botalys/refs/heads/main/security/botalys-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botalys-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botalys.com
- group: company
  title: ''
  type: AboutUs
  url: https://botalys.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://botalys.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botalys.com/gdpr
coverage:
  checked: '2026-10-03'
  detail: Botalys website provides no developer documentation or API reference.
  evidence:
  - status: 200
    url: https://botalys.com
  reason: no-developer-program
  state: none
created: '2026-10-03'
description: Botalys develops and supplies premium botanical ingredients through biomimetic indoor farming. The company offers rare botanicals such as Korean Ginseng, Rhodiola, and Sichuan Red Sage for nutraceuticals and cosmetics, emphasizing quality, traceability, and sustainability. It provides a platform for tailored plant development and sample packs, aiming to make sourcing of rare botanicals possible and sustainable for clients.
image: https://botalys.com/share.png
layout: provider
modified: '2026-10-03'
name: Botalys
nav: Providers
network: true
overview: Botalys is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Agriculture, Nutraceuticals, and Cosmetics.
random_paper: 18
score:
  band: minimal
  composite: 6.1
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
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Botalys Domain Security
  slug: botalys-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: botalys
tags:
- Company
- Biotechnology
- Agriculture
- Nutraceuticals
- Cosmetics
website: https://botalys.com
---
