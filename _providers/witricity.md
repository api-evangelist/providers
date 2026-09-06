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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.witricity.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.witricity.com/terms.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.witricity.com/privacy-policy.php
- group: company
  title: ''
  type: Blog
  url: https://www.witricity.com/blog-and-newsroom.php
- group: operate
  title: ''
  type: Support
  url: https://www.witricity.com/contact.php
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/witricity-aitechllc
- group: auth
  title: ''
  type: DomainSecurity
  url: security/witricity-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/witricity-llms.txt
coverage:
  checked: '2026-09-04'
  detail: WiTricity AI Tech, LLC is an EV wireless-power IP licensor whose entire public site is 30 static .php marketing pages with no developer, API or documentation section; api./developer./docs./dev./portal.witricity.com are all NXDOMAIN and github.com/witricity does not exist, so integration is delivered through licensee engineering services rather than any API.
  evidence:
  - status: 200
    url: https://www.witricity.com/
  - status: 404
    url: https://www.witricity.com/openapi.json
  - status: 404
    url: https://www.witricity.com/.well-known/api-catalog
  - status: 404
    url: https://www.witricity.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/witricity
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: 'WiTricity AI Tech, LLC is a wireless power transfer company founded on the highly resonant magnetic-resonance research published by an MIT team led by Marin Soljacic in 2007. The company holds the foundational patent portfolio for wireless power transfer over distance and commercializes it by licensing intellectual property, reference designs and engineering services to automakers, Tier 1 suppliers and charging hardware manufacturers rather than by selling software. Its product surface is hardware and IP: the MR/1 charging system, light-, medium- and heavy-duty EV wireless charging, smart-city and transit infrastructure, autonomous-vehicle and ground-support-equipment fleets, and bidirectional V2G energy arbitrage. WiTricity chairs several SAE J2954 working groups, the interoperability standard for wireless EV and PHEV charging. As of a probe on 2026-09-04 the company publishes no developer program, no API documentation, no machine-readable contract and no public code repositories;
  its integration story is delivered through licensee engineering support, not a public API.'
image: https://www.witricity.com/images/logo-for-social.jpg
layout: provider
modified: '2026-09-04'
name: WiTricity
nav: Providers
network: true
overview: 'WiTricity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wireless Power, Electric Vehicles, EV Charging, and Automotive.


  WiTricity''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: Witricity Plans Pricing
  plan_count: 0
  slug: witricity-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Witricity Rate Limits
  slug: witricity-rate-limits
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Witricity Domain Security
  slug: witricity-domain-security
  summary_line: TLSv1.3 · DMARC
slug: witricity
tags:
- Company
- Wireless Power
- Electric Vehicles
- EV Charging
- Automotive
- Energy
- Hardware
- Intellectual Property Licensing
- Smart Cities
- Vehicle to Grid
website: https://www.witricity.com/
---
