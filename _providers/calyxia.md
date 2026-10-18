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
  href: https://raw.githubusercontent.com/api-evangelist/calyxia/refs/heads/main/hosts/calyxia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calyxia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/calyxia/refs/heads/main/vendors/calyxia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calyxia-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calyxia.com/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calyxia.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://calyxia.com/news/calyxia-aficep-presentation/
- group: other
  title: ''
  type: Leadership
  url: https://calyxia.com/about-us/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/calyxia/refs/heads/main/security/calyxia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calyxia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calyxia.com
coverage:
  checked: 2026-10-06 'Calyxia designs, manufactures, and sells high‑performing, eco‑engineered microcapsule and microparticle solutions that enable global manufacturers to improve product performance and achieve sustainability goals. Serving leading industrial clients in agriculture, consumer care, and advanced materials, Calyxia leverages over 30 years of emulsion science to deliver customizable, biodegradable encapsulation technologies for a wide range of applications.'
  detail: No public developer program or API documentation was found on the company website.
  evidence:
  - status: 200
    url: https://calyxia.com
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Calyxia designs, manufactures, and sells high‑performing, eco‑engineered microcapsule and microparticle solutions that enable global manufacturers to improve product performance and achieve sustainability goals.
layout: provider
modified: '2026-10-06'
name: Calyxia
nav: Providers
network: true
overview: Calyxia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Microencapsulation, Advanced Materials, Agriculture, Consumer Care, and Home & Beauty.
random_paper: 21
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
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
  name: Calyxia Domain Security
  slug: calyxia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: calyxia
tags:
- Microencapsulation
- Advanced Materials
- Agriculture
- Consumer Care
- Home & Beauty
- Sustainable Chemistry
website: https://calyxia.com
---
