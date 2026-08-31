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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/otolith-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://otolithlabs.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/otolith-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Otolith Labs makes one prescription physical medical device (the OtoBand vertigo wearable) and its entire web presence is a WordPress marketing, investor and clinical-trial site — there is no developer subdomain (api./app./developer./docs./portal.otolithlabs.com are all NXDOMAIN), no GitHub organization, and the only machine-readable endpoint on the domain is the default WordPress core REST API at /wp-json/, which is CMS scaffolding rather than a product API.
  evidence:
  - status: 404
    url: https://otolithlabs.com/openapi.json
  - status: 404
    url: https://otolithlabs.com/.well-known/agent-card.json
  - status: 404
    url: https://otolithlabs.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/otolithlabs
  - status: 200
    url: https://otolithlabs.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Otolith Labs, Inc. (trading as Otolith) is a privately held, clinical-stage medical device company headquartered at 200 Massachusetts Ave NW in Washington, D.C., founded in 2015 by Sam Owen and developing a non-invasive wearable headband — the OtoBand — that applies calibrated mechanical vibration to the vestibular system, a technique the company calls non-invasive Vestibular Resonance Therapy (nVRT) or vestibular masking, to reduce the symptoms of chronic vertigo and vestibular migraine without surgery, medication, or patient-specific calibration. The device holds an FDA Breakthrough Device designation, has been evaluated in clinical work spanning 600+ subjects, and is being studied for cybersickness in virtual reality. Otolith Labs is backed by Morningside Ventures, Mark Cuban Companies and a group of ENT physician investors. It is a physical medical device manufacturer: it publishes no public API, developer portal, SDK, or machine-readable specification, and its only web
  surface is a WordPress marketing, investor and clinical-trial site.'
image: https://otolithlabs.com/wp-content/uploads/2022/03/Otolith-Horiztonal-Logo-in-Color-1.webp
layout: provider
modified: '2026-08-26'
name: Otolith
nav: Providers
network: true
overview: Otolith is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, MedTech, and Wearables.
random_paper: 15
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Otolith Domain Security
  slug: otolith-domain-security
  summary_line: TLSv1.3 · DMARC
slug: otolith
tags:
- Company
- Medical Devices
- Healthcare
- MedTech
- Wearables
- Neurotechnology
- Vestibular Disorders
- Vertigo
- Clinical Trials
- Digital Health
website: https://otolithlabs.com/
---
