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
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accusilicon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accusilicon.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accusilicon.com/cn/accusilicon/terms_conditions
- group: operate
  title: ''
  type: Support
  url: https://accusilicon.com/cn/accusilicon/contact_us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accusilicon-llms.txt
coverage:
  checked: '2026-09-06'
  detail: Accusilicon is a fabless oscillator and mixed-signal chip maker whose only web property is a Chinese-language product marketing site with no developer section — its /en/ locale, /llms.txt, /openapi.json, /apis.json and every /.well-known/ discovery path all 404 at the origin.
  evidence:
  - status: 200
    url: https://accusilicon.com/cn/accusilicon/about_us
  - status: 404
    url: https://accusilicon.com/openapi.json
  - status: 404
    url: https://accusilicon.com/.well-known/api-catalog
  - status: 404
    url: https://accusilicon.com/en/
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'Accusilicon (Guangzhou Ruixin Microelectronics Co., Ltd. / 广州睿芯微电子有限公司) is a fabless mixed-signal semiconductor company founded in July 2014 and headquartered in the Huangpu district of Guangzhou, China, with additional sites in Xi''an and Shanghai. It designs and sells ultra-low phase noise timing silicon and related analog ICs — XO/VCXO/TCXO and OCXO oscillator chips, clock ICs, crystal-oscillator modules, RF and analog switch ICs, mobile-interface protection ICs, ADC/DAC converters, digital audio processor (DSP) and audio ICs, and spectral image sensor chips — alongside clock stability analyzers and other test and measurement instruments, and ASIC/SoC, module, system and clock custom design services. Its parts are used in smartphones, digital communications and high-speed Ethernet, audio/video and professional audiophile equipment, medical, security, payment and measurement systems. The company is a hardware component supplier: it operates a corporate marketing site in Chinese
  only and publishes no developer program, developer portal, API documentation, SDK or machine-readable API description of any kind.'
image: https://accusilicon.com/images/logo.svg
layout: provider
modified: '2026-09-06'
name: Accusilicon
nav: Providers
network: true
overview: 'Accusilicon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Integrated Circuits, Clock Chips, and Oscillators.


  Accusilicon''s developer surface includes support and 4 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.0
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Accusilicon Domain Security
  slug: accusilicon-domain-security
  summary_line: TLSv1.3 · HSTS
slug: accusilicon
tags:
- Company
- Semiconductors
- Integrated Circuits
- Clock Chips
- Oscillators
- Timing
- Audio
- Hardware
- Electronics
website: https://accusilicon.com/
---
