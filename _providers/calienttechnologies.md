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
  href: https://raw.githubusercontent.com/api-evangelist/calienttechnologies/refs/heads/main/hosts/calienttechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calienttechnologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/calienttechnologies/refs/heads/main/vendors/calienttechnologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calienttechnologies-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.calient.net/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.calient.net/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/calienttechnologies/refs/heads/main/security/calienttechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calienttechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.calient.net
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.calient.net
  - status: 403
    url: https://equityzen.com/company/calienttechnologies
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Calient Technologies (Calient.AI) is a leading provider of pure photonic optical circuit switching solutions. The company offers high‑bandwidth, scalable optical circuit switches for network service providers and data center operators, reducing costs and enabling flexible network architectures. Their portfolio includes the S320 optical circuit switch and related products, with extensive documentation and support resources available online.
layout: provider
modified: '2026-10-06'
name: Calienttechnologies
nav: Providers
network: true
overview: 'Calienttechnologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Optical, Networking, Photonics, and Enterprise.


  Calienttechnologies'' developer surface includes support and 5 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calienttechnologies Domain Security
  slug: calienttechnologies-domain-security
  summary_line: TLSv1.3
slug: calienttechnologies
tags:
- Company
- Optical
- Networking
- Photonics
- Enterprise
website: https://www.calient.net
---
