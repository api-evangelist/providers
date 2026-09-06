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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://908devices.com/
- group: company
  title: ''
  type: Blog
  url: https://908devices.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://908devices.com/blog/feed/
- group: company
  title: ''
  type: Newsroom
  url: https://908devices.com/news/
- group: company
  title: ''
  type: x-NewsRSS
  url: https://908devices.com/news/feed/
- group: company
  title: ''
  type: About
  url: https://908devices.com/about/
- group: company
  title: ''
  type: Careers
  url: https://908devices.com/careers/
- group: operate
  title: ''
  type: Support
  url: https://908devices.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://908devices.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://908devices.com/privacy-policy/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.908devices.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/908-devices
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@908devices
- group: company
  title: ''
  type: Twitter
  url: https://x.com/908devices
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/908-devices-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/908-devices-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/908-devices-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/908-devices-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: 'FIELDLAB — the one developer-facing product in the 908 Devices portfolio, marketed at "app developers and chemists" to build custom mobile NIR spectroscopy applications on the NIRLAB platform 908 Devices acquired in May 2026 — publishes no reference, endpoint or spec: the page''s only call to action is a contact-sales form, the NIRLAB cloud console at app.nirlab.com redirects straight to a login, and on the core instrument line the published integration mechanism is an RS232 serial port rather than a network API.'
  evidence:
  - status: 200
    url: https://www.nirlab.com/fieldlab/
  - status: 200
    url: https://app.nirlab.com/
  - status: 404
    url: https://908devices.com/openapi.json
  - status: 404
    url: https://908devices.com/.well-known/api-catalog
  - status: 200
    url: https://908devices.com/news/908-devices-announces-mx908-integration-capabilities/
  reason: sales-gate
  state: gated
created: '2026-09-05'
description: '908 Devices Inc. (Nasdaq: MASS) is a Burlington, Massachusetts maker of purpose-built handheld chemical analysis devices for public safety, defense, customs and forensic teams. Its flagship MX908 is a handheld high-pressure mass spectrometer that identifies narcotics, explosives and hazardous materials at trace level in about 30 seconds; the portfolio also includes the VipIR, XplorIR, ProtectIR and InterceptIR FTIR/Raman analyzers and, since the May 2026 acquisition of NIRLAB AG of Lausanne, a cloud-connected NIR spectroscopy platform. As of this profile the company publishes no public developer program, API reference, OpenAPI or SDK: MX908 integration ships as an RS232 serial port, field data moves over Bluetooth via the MX908 Remote and Team Leader mobile apps, and the NIRLAB cloud console at app.nirlab.com is login-gated. NIRLAB''s FIELDLAB is marketed to app developers, but its reference sits behind a contact-sales form.'
image: https://908devices.com/wp-content/uploads/2022/08/908Devices_Logo_Primary.jpg
layout: provider
modified: '2026-09-05'
name: 908 Devices
nav: Providers
network: true
overview: '908 Devices is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chemical Analysis, Mass Spectrometry, Spectroscopy, and Scientific Instruments.


  908 Devices'' developer surface includes engineering blog, support, YouTube channel, changelog, and 14 more developer resources.'
plans:
- name: 908 Devices Plans Pricing
  plan_count: 0
  slug: 908-devices-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 908 Devices Domain Security
  slug: 908-devices-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 908-devices
tags:
- Company
- Chemical Analysis
- Mass Spectrometry
- Spectroscopy
- Scientific Instruments
- Public Safety
- Defense
- Narcotics Detection
- Hazmat
- Hardware
- Life Sciences
website: https://908devices.com/
---
