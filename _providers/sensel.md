---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  - '{''url'': ''https://sensel.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.cirque.com/sensel — a different registrable domain (sensel.com -> cirque.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The Sensel API is a C library for communicating with Sensel devices (Morph and Sensel sensor boards). It is a LOCAL DEVICE API, not an HTTP service: an application links LibSensel and LibSenselDecompr'
  name: Sensel API (LibSensel)
  slug: sensel-api-libsensel
artifact_total: 4
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/sensel/sensel-api/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sensel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sensel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://guide.sensel.com/
- group: docs
  title: ''
  type: APIReference
  url: https://guide.sensel.com/sensel_h.html
- group: start
  title: ''
  type: GettingStarted
  url: https://guide.sensel.com/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sensel
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/sensel/sensel-api
- group: operate
  title: ''
  type: Support
  url: https://github.com/sensel/sensel-api/issues
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cirque.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/sensel-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sensel-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sensel-status-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sensel-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sensel-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/sensel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sensel-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Sensel's API is a local MIT-licensed C library (LibSensel) that talks to Morph/sensor hardware over USB/serial — guide.sensel.com and the sensel.h header on GitHub are fully readable by a human, but the provider publishes no OpenAPI, AsyncAPI, GraphQL SDL, Postman collection or JSON Schema anywhere, and there is no HTTP endpoint for one to describe.
  evidence:
  - status: 200
    url: https://guide.sensel.com/
  - status: 404
    url: https://guide.sensel.com/openapi.json
  - status: 404
    url: https://sensel.com/openapi.json
  - status: 404
    url: https://sensel.com/.well-known/agent-card.json
  - status: 301
    url: https://sensel.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-08-26'
description: 'Sensel is a Sunnyvale, California touch-input company founded in 2013 by Ilya Rosenberg and Aaron Zarraga, building high-resolution force-sensing hardware — the Morph pressure-sensitive input device and the force-sensing touchpad technology shipped in laptops such as Lenovo''s ThinkPad X1 Titanium Yoga. Its developer surface is not a web API: the Sensel API is an open-source, MIT-licensed C library (LibSensel) that talks to Sensel devices over USB/serial, published at github.com/sensel/sensel-api with C, C#, Python, Arduino, Processing, Max and Pure Data bindings and documented at guide.sensel.com. Sensel''s intellectual property, physical assets and trademarks were acquired by Cirque Corporation (an Alps Alpine company), and sensel.com now 301-redirects to cirque.com/sensel.'
image: https://guide.sensel.com/img/sensel-logo-blue.svg
layout: provider
modified: '2026-08-26'
name: Sensel
nav: Providers
network: true
overview: 'Sensel publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Touch Input, Haptics, Sensors, and Hardware.


  Sensel''s developer surface includes documentation, API reference, getting-started guide, support, and 13 more developer resources.'
plans:
- name: Sensel Plans Pricing
  plan_count: 0
  slug: sensel-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Sensel Rate Limits
  slug: sensel-rate-limits
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 17.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sensel/refs/heads/main/screenshots/sensel-2026-09-02T154902.png
security:
- kind: domain-security
  name: Sensel Domain Security
  slug: sensel-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sensel
tags:
- Company
- Touch Input
- Haptics
- Sensors
- Hardware
- Human Interface Devices
- Embedded
- Open-Source
- Device SDK
- Music Technology
website: https://sensel.com/
---
