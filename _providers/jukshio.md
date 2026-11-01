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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/jukshio/hosts/jukshio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jukshio-hosts.yml
- group: other
  href: https://artifacts.apis.io/jukshio/vendors/jukshio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jukshio-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.jukshio.com/blog/dfraud
- group: auth
  href: https://artifacts.apis.io/jukshio/security/jukshio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jukshio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jukshio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jukshio.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.jukshio.com/about
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jukshio.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.jukshio.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jukshio.com/privacy-policy
coverage:
  checked: '2026-10-18'
  detail: No machine‑readable API specification was found on the company’s website.
  evidence:
  - status: 200
    url: https://jukshio.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: Jukshio provides AI‑driven identity verification and KYC automation solutions for enterprises. Their platform offers a suite of tools including KYC++, DFraud, video KYC, attendance management, and enterprise access, all designed to secure data, reduce fraud, and optimize AI model performance. Jukshio emphasizes sovereign AI, data ownership, and zero‑hallucination technology, catering to BFSI and other regulated industries.
image: https://cdn.prod.website-files.com/64ce07669d9dd1b58827b206/68ad5990ef124251013741a0_Jukshio-LinkedIn-og-image.jpg
layout: provider
modified: '2026-10-17'
name: Jukshio
nav: Providers
network: true
overview: 'Jukshio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Identity Verification, KYC, and Enterprise.


  Jukshio''s developer surface includes engineering blog, documentation, getting-started guide, pricing, support, and 5 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 13.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Jukshio Domain Security
  slug: jukshio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: jukshio
tags:
- Company
- Artificial Intelligence
- Identity Verification
- KYC
- Enterprise
website: https://jukshio.com/
---
