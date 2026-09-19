---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-09-18'
api_count: 0
artifact_total: 3
common:
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiperofficial/refs/heads/main/packages/aiperofficial-packages.yml
  title: ''
  type: Packages
  url: packages/aiperofficial-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiperofficial/refs/heads/main/llms/aiperofficial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiperofficial-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiperofficial/refs/heads/main/security/aiperofficial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiperofficial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiper.com/us/home
- group: operate
  title: ''
  type: Support
  url: https://aiper.com/us/support
- group: company
  title: ''
  type: Blog
  url: https://poolblog.aiper.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiper.com/us/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiper.com/us/privacy-notice
coverage:
  checked: '2026-09-14'
  detail: Aiper sells consumer pool-cleaning robots controlled only by its own mobile app - there is no developer portal, API reference, SDK or GitHub organization anywhere, and its real regional app-cloud hosts (apiamerica/apieurope/apiasia.aiper.com) answer EVERY path, /.well-known/* included, with HTTP 200 carrying the JSON body {"code":"401","message":"Your login has expired"}, so there is no anonymous contract surface to read.
  evidence:
  - status: 200
    url: https://apiamerica.aiper.com/openapi.json
  - status: 200
    url: https://apiamerica.aiper.com/.well-known/api-catalog
  - status: 200
    url: https://www.aiper.com/llms.txt
  - status: 404
    url: https://aiper.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/aiper
  reason: no-developer-program
  state: none
created: '2026-09-14'
description: 'Aiper is a consumer robotics company that designs and sells cordless robotic pool cleaners, solar-powered pool skimmers and smart yard-care hardware (the Scuba, Surfer/EcoSurfer, Pilot and IrriSense lines), sold in more than 7,000 stores across 50+ countries with a US base in The Woodlands, Texas. Its devices are paired to the Aiper mobile app, which talks to a regional cloud control plane at apiamerica/apieurope/apiasia.aiper.com plus an AWS IoT MQTT layer. That cloud surface is a private first-party app backend: Aiper publishes no developer portal, no API reference, no SDK and no machine-readable contract, and every anonymous request to those hosts is answered with an authentication error. The only clients that speak it are unofficial, community reverse-engineered Home Assistant and Homebridge integrations.'
image: https://d1274tx8ixnt7d.cloudfront.net/20250611/17496348246021749634730323_lQDPJxtgagiJ-NPNAyDNAyCw5tV7PWNRyTEIKTTbrt39AA_800_800.jpg
layout: provider
modified: '2026-09-14'
name: Aiper
nav: Providers
network: true
overview: 'Aiper is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Consumer Electronics, IoT, and Smart Home.


  Aiper''s developer surface includes support, engineering blog, and 6 more developer resources.'
plans:
- name: Aiperofficial Plans Pricing
  plan_count: 0
  slug: aiperofficial-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Aiperofficial Rate Limits
  slug: aiperofficial-rate-limits
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 10.6
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiperofficial Domain Security
  slug: aiperofficial-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aiperofficial
tags:
- Company
- Robotics
- Consumer Electronics
- IoT
- Smart Home
- Home & Garden
- Hardware
- Artificial Intelligence
- Pool Care
website: https://aiper.com/us/home
---
