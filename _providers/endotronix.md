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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/endotronix-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/endotronix-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/endotronix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/endotronix-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://endotronix.com/
- group: company
  title: ''
  type: About
  url: https://endotronix.com/about-endotronix/
- group: operate
  title: ''
  type: Support
  url: https://endotronix.com/contact-endotronix/
- group: company
  title: ''
  type: Blog
  url: https://endotronix.com/heart-failure-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://endotronix.com/heart-failure-news/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://endotronix.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://endotronix.com/privacy-policy/
- group: docs
  title: ''
  type: Manuals
  url: https://endotronix.com/manuals/
- group: other
  title: ''
  type: Resources
  url: https://endotronix.com/resources/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/endotronix_stock/
coverage:
  checked: '2026-08-12'
  detail: Endotronix ships the Cordella system as a regulated end-user medical device platform — an implant, a patient tablet app and the myCordella clinician portal — and its entire published web surface is 19 marketing, clinical-evidence and IFU pages with no developer portal, API reference, SDK or spec anywhere; api., developer. and data.endotronix.com do not even resolve in DNS.
  evidence:
  - status: 404
    url: https://endotronix.com/openapi.json
  - status: 404
    url: https://endotronix.com/.well-known/agent-card.json
  - status: 404
    url: https://endotronix.com/llms.txt
  - status: 200
    url: https://endotronix.com/page-sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Endotronix, Inc. is a Naperville, Illinois medical device and digital health company founded in 2007 and acquired by Edwards Lifesciences in July 2024, where it now operates as a wholly owned subsidiary. Endotronix builds the Cordella Heart Failure System, an integrated remote heart-failure management platform combining an implantable wireless pulmonary artery (PA) pressure sensor — granted FDA premarket approval in June 2024 — with a patient-facing myCordella tablet application, connected home vitals peripherals (blood pressure cuff, weight scale, pulse oximeter), and the myCordella Patient Management Portal, a cloud-based web application clinicians use to review transmitted PA pressure, vitals and symptom data and to titrate guideline-directed medical therapy. The company publishes clinical evidence (PROACTIVE-HF), instructions for use and device manuals, but operates no public developer program: there is no developer portal, API reference, SDK, webhook catalog or machine-readable
  specification on any Endotronix host.'
layout: provider
modified: '2026-08-12'
name: Endotronix
nav: Providers
network: true
overview: 'Endotronix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Digital Health, Remote Patient Monitoring, and Cardiology.


  Endotronix''s developer surface includes support, engineering blog, and 12 more developer resources.'
plans:
- name: Endotronix Plans Pricing
  plan_count: 0
  slug: endotronix-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Endotronix Rate Limits
  slug: endotronix-rate-limits
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/endotronix/refs/heads/main/screenshots/endotronix-2026-09-02T145359.png
security:
- kind: domain-security
  name: Endotronix Domain Security
  slug: endotronix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: endotronix
tags:
- Company
- Medical Devices
- Digital Health
- Remote Patient Monitoring
- Cardiology
- Heart Failure
- Healthcare
- Connected Devices
website: https://endotronix.com/
---
