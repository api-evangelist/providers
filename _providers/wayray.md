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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://wayray.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wayray.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wayray.com/policy/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@WayRay
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wayray-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wayray-llms.txt
coverage:
  checked: '2026-09-04'
  detail: WayRay AG was declared bankrupt by the Zurich probate court effective 2023-08-14 and is in liquidation; the static wayray.com archive is still served, but the True AR SDK download the company's own 2018 press release names at wayray.com/sdk now 404s, and no API, spec, or /.well-known document survives on any WayRay host.
  evidence:
  - status: 404
    url: https://wayray.com/sdk
  - status: 200
    url: https://wayray.com/press-releases/SDKlaunch/
  - status: 404
    url: https://wayray.com/openapi.json
  - status: 404
    url: https://wayray.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/wayray
  reason: defunct
  state: none
created: '2026-09-04'
description: WayRay AG was a Swiss deep-tech company, founded in 2012 by Vitaly Ponomarev and headquartered in Zurich, that developed holographic augmented-reality displays for the automotive industry — the Deep Reality Display, an embedded holographic optical element laminated into a vehicle windshield, paired with an AR rendering engine and the True AR SDK for building in-vehicle AR applications. The company raised roughly $140M from Porsche, Hyundai, Alibaba and others and shipped concept integrations with Pininfarina and Karma Automotive, but the Zurich probate court declared its bankruptcy effective 14 August 2023 and its assets have been in liquidation since. The marketing site at wayray.com remains standing as a static archive; the developer surface it once advertised (the True AR SDK download at wayray.com/sdk, a C++ toolkit with an emulator, simulator, docs and samples) now returns 404, and no public web API, OpenAPI, developer portal or package registry presence survives.
image: https://wayray.com/static/2908924d420a329dc51630aa0f385af1/d344a/meta_hero_d259289d3e.jpg
layout: provider
modified: '2026-09-04'
name: WayRay
nav: Providers
network: true
overview: 'WayRay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Augmented Reality, Holographic Display, and Deep Tech.


  WayRay''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: domain-security
  name: Wayray Domain Security
  slug: wayray-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: wayray
tags:
- Company
- Automotive
- Augmented Reality
- Holographic Display
- Deep Tech
- Head-Up Display
- Switzerland
- Defunct
website: https://wayray.com/
---
