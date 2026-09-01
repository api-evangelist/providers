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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://shoulderinnovations.com/
- group: company
  title: ''
  type: Blog
  url: https://shoulderinnovations.com/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shoulderinnovations.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://shoulderinnovations.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://shoulderinnovations.com/careers/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.shoulderinnovations.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shoulder-innovations/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shoulder-innovations-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shoulder-innovations-llms.txt
coverage:
  checked: '2026-08-27'
  detail: Shoulder Innovations sells shoulder implants and one first-party clinical application, ProVoyance, which is delivered to surgeons through a login portal at portal.si.genesisplanningsoftware.com that answers HTTP 200 with the same 1463-byte React shell for every path including /openapi.json and every /.well-known/ path - there is no developer site, no API reference and no machine-readable contract on any host it serves.
  evidence:
  - status: 404
    url: https://shoulderinnovations.com/openapi.json
  - status: 404
    url: https://shoulderinnovations.com/developers
  - status: 404
    url: https://shoulderinnovations.com/.well-known/agent-card.json
  - status: 200
    url: https://portal.si.genesisplanningsoftware.com/openapi.json
  - status: 404
    url: https://api.github.com/orgs/shoulder-innovations
  reason: no-developer-program
  state: none
created: '2026-08-27'
description: Shoulder Innovations is a commercial-stage medical technology company headquartered in Grand Rapids, Michigan, focused exclusively on the shoulder surgical care market. Founded in 2009 by Dr. Steve Gunther, it develops the InSet(R) shoulder arthroplasty portfolio - the InSet Glenoid, InSet Total Shoulder and InSet Reverse Shoulder systems, the I-Series humeral stems and a streamlined one- and two-tray instrument system - built around inset glenoid fixation designed to reduce the "rocking horse" forces implicated in glenoid implant failure. It also publishes ProVoyance(R) Shoulder, a first-party AI/ML pre-operative planning application that turns CT imaging into 3D bone reconstructions and is delivered to surgeons through a customer login portal. The company listed publicly in July 2025 under the ticker SI. It ships no public API, SDK, webhook surface or developer program; ProVoyance is an end-user clinical application, not a platform.
image: https://shoulderinnovations.com/wp-content/uploads/2025/01/shoulder_innovations_white_logo-1-1-1024x258.png
layout: provider
modified: '2026-08-27'
name: Shoulder Innovations
nav: Providers
network: true
overview: 'Shoulder Innovations is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Medical Technology, Health, and Orthopedics.


  Shoulder Innovations'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Shoulder Innovations Domain Security
  slug: shoulder-innovations-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shoulder-innovations
tags:
- Company
- Medical Devices
- Medical Technology
- Health
- Orthopedics
- Surgery
- Shoulder Arthroplasty
- Implants
- Surgical Planning Software
- Healthcare
website: https://shoulderinnovations.com/
---
