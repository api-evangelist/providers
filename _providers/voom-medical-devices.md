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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voom-medical-devices-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.voommedicaldevices.com/
- group: company
  title: ''
  type: About
  url: https://www.voommedicaldevices.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.voommedicaldevices.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voommedicaldevices.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.voommedicaldevices.com/terms-of-use
- group: auth
  title: ''
  type: Compliance
  url: https://www.voommedicaldevices.com/compliance
- group: company
  title: ''
  type: Newsroom
  url: https://www.voommedicaldevices.com/about-us/news-events
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voomdevices
- group: design
  title: ''
  type: Conformance
  url: conformance/voom-medical-devices-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voom-medical-devices-llms.txt
coverage:
  checked: '2026-09-04'
  detail: Voom manufactures bunion-surgery implants and instrument kits; its entire public site is 22 URLs of product, training and compliance pages, with no api./developer./docs. subdomain resolving and every /.well-known/, /openapi.json and /llms.txt path returning 404.
  evidence:
  - status: 404
    url: https://www.voommedicaldevices.com/openapi.json
  - status: 404
    url: https://www.voommedicaldevices.com/.well-known/agent-card.json
  - status: 404
    url: https://www.voommedicaldevices.com/llms.txt
  - status: 200
    url: https://www.voommedicaldevices.com/sitemap-0.xml
  reason: not-a-software-company
  state: none
created: '2026-09-04'
description: 'Voom Medical Devices, Inc. is an orthopedic medical device and surgical innovation company founded by bunion surgeon Dr. Neal Blitz and headquartered in Brentwood, Tennessee. Voom designs implants and procedural systems for minimally invasive bunion surgery (MIBS) and foot-and-ankle reconstruction, including the patented Revcon non-compression dual-zone bone screw system, the Bunionplasty 360 Bunion Repair procedure, and the MIBS CoPilot Shift + Targeting Guide single-use sterile kit. The company sells to surgeons and hospitals, runs a surgeon training program, and operates the patient-facing Bunionplasty.com procedure site with a doctor locator. It is a physical device manufacturer: it publishes no developer portal, no API documentation and no machine-readable API contract on any host it controls.'
image: https://cdn.sanity.io/images/wu4qotw8/production/d23f8167eb501cf7de5bc1394a7ac4993baf8501-1200x627.jpg
layout: provider
modified: '2026-09-04'
name: Voom Medical Devices
nav: Providers
network: true
overview: 'Voom Medical Devices is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health Care, Orthopedics, and Surgery.


  Voom Medical Devices'' developer surface includes support and 10 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Voom Medical Devices Domain Security
  slug: voom-medical-devices-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voom-medical-devices
tags:
- Company
- Medical Devices
- Health Care
- Orthopedics
- Surgery
- Medical Technology
- Manufacturing
website: https://www.voommedicaldevices.com/
---
