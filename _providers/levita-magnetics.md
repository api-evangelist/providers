---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
- group: company
  title: ''
  type: Website
  url: https://www.levita.com/
- group: company
  title: ''
  type: Blog
  url: https://www.levita.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.levita.com/feed
- group: operate
  title: ''
  type: Support
  url: https://www.levita.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.levita.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.levita.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/levita-magnetics-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/levita-magnetics-domain-security.yml
coverage:
  checked: '2026-08-25'
  detail: Levita Magnetics ships a regulated surgical robot (MARS) and a magnetic retractor system to hospitals, and the only machine-readable endpoint on any host it controls is the stock WordPress /wp-json/ CMS API behind its marketing site — there is no developer portal, no API reference, no GitHub organization and no published contract of any kind.
  evidence:
  - status: 404
    url: https://www.levita.com/openapi.json
  - status: 404
    url: https://www.levita.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/levita-magnetics
  - status: 404
    url: https://www.magneticsurgery.com/openapi.json
  - status: 200
    url: https://www.levita.com/wp-json/
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: Levita Magnetics is a Mountain View, California medical device company, founded by minimally invasive surgeon Dr. Alberto Rodriguez-Navarro and co-founded by Nicolas Luksic, with an additional office in Santiago, Chile. It develops Magnetic Surgery — the Levita Magnetic Surgical System, in which an external magnet placed on the patient's skin controls a shaftless detachable retractor to enable reduced-port laparoscopic procedures — and the MARS (Magnetic-Assisted Robotic Surgery) platform launched in 2023, an FDA-cleared surgical robotic system used in abdominal and, more recently, pediatric procedures. The MARS platform is built on RTI Connext (the DDS real-time connectivity standard) internally, and Levita has demonstrated AI-guided autonomous camera control during surgery. Levita ships regulated surgical hardware and its embedded control software to hospitals; it operates no public developer program, publishes no API documentation, and exposes no machine-readable API contract
  on any host it controls.
image: https://www.levita.com/wp-content/uploads/2023/11/levita-social-logo.png
layout: provider
modified: '2026-08-25'
name: Levita Magnetics
nav: Providers
network: true
overview: 'Levita Magnetics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Surgical Robotics, Healthcare, and Robotics.


  Levita Magnetics'' developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/levita-magnetics/refs/heads/main/screenshots/levita-magnetics-2026-09-02T150243.png
security:
- kind: domain-security
  name: Levita Magnetics Domain Security
  slug: levita-magnetics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: levita-magnetics
tags:
- Company
- Medical Devices
- Surgical Robotics
- Healthcare
- Robotics
- Minimally Invasive Surgery
- Medical Technology
- Hardware
website: https://www.levita.com/
---
