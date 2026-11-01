---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/mosaicmanufacturing-com/llms/mosaicmanufacturing-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mosaicmanufacturing-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/mosaicmanufacturing-com/well-known/mosaicmanufacturing-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mosaicmanufacturing-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/mosaicmanufacturing-com/hosts/mosaicmanufacturing-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mosaicmanufacturing-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mosaicmfg.com/terms-conditions/
- group: operate
  title: ''
  type: Support
  url: https://mosaicmfg.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mosaicmfg.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/mosaicmanufacturing-com/security/mosaicmanufacturing-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mosaicmanufacturing-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mosaicmanufacturing.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://mosaicmanufacturing.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Mosaic Manufacturing is a 3D printing solutions provider that expands manufacturing horizons with advanced additive manufacturing technologies. The company offers a range of services including custom part production, material expertise, and integration support for industrial clients. Based on its website, Mosaic focuses on delivering high‑quality printed components, rapid prototyping, and scalable production capabilities to serve various sectors such as aerospace, automotive, and medical devices. Their platform emphasizes ease of use, reliability, and innovative material options, positioning them as a modern manufacturing partner for complex engineering challenges.
layout: provider
modified: '2026-10-24'
name: Mosaic Manufacturing
nav: Providers
network: true
overview: 'Mosaic Manufacturing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D Printing, Manufacturing, Additive Manufacturing, and Industrial.


  Mosaic Manufacturing''s developer surface includes support and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
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
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mosaicmanufacturing Com Domain Security
  slug: mosaicmanufacturing-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mosaicmanufacturing-com
tags:
- Company
- 3D Printing
- Manufacturing
- Additive Manufacturing
- Industrial
website: https://mosaicmanufacturing.com/
---
