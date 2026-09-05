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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spr-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sprpainrelief.com/
- group: operate
  title: ''
  type: Support
  url: https://www.sprpainrelief.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.sprpainrelief.com/news-press-releases
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sprpainrelief.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sprpainrelief.com/terms-use
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spr-therapeutics-llms.txt
coverage:
  checked: '2026-08-29'
  detail: SPR Therapeutics manufactures the SPRINT percutaneous nerve-stimulation device; its entire web estate is a Drupal marketing and clinical-evidence site, and the only software it ships is a consumer patient app and the credentialed SPRcare reimbursement portal, so there is no API, developer portal or machine-readable contract to profile.
  evidence:
  - status: 404
    url: https://www.sprpainrelief.com/openapi.json
  - status: 404
    url: https://www.sprpainrelief.com/.well-known/agent-card.json
  - status: 404
    url: https://www.sprpainrelief.com/llms.txt
  - status: 404
    url: https://www.sprpainrelief.com/graphql
  - status: 0
    url: https://api.sprtherapeutics.com/
  reason: not-a-software-company
  state: none
created: '2026-08-29'
description: 'SPR Therapeutics, Inc. is a Cleveland, Ohio medical device company that develops and commercializes the SPRINT Peripheral Nerve Stimulation (PNS) System, a non-opioid, minimally invasive percutaneous therapy for chronic and acute pain. SPRINT is the only percutaneous PNS device FDA-cleared for both chronic and acute pain that does not require permanent implantation: leads are placed in an outpatient procedure without surgery, incisions or anesthesia and deliver up to 60 days of therapy. The company was acquired by Medtronic plc on 2026-07-16 for $650 million and now operates within the Medtronic Neuromodulation Operating Unit. SPR is a device manufacturer rather than a software vendor: it publishes no public API, developer portal, SDK or machine-readable contract. Its only software surfaces are the consumer SPRINT PNS Patient App and the credentialed SPRcare provider reimbursement portal, neither of which exposes a public integration.'
image: https://www.sprpainrelief.com/sites/default/files/styles/meta/public/2024-11/Banner.jpg
layout: provider
modified: '2026-08-29'
name: SPR Therapeutics
nav: Providers
network: true
overview: 'SPR Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Neuromodulation, and Pain Management.


  SPR Therapeutics'' developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 4
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
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Spr Therapeutics Domain Security
  slug: spr-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spr-therapeutics
tags:
- Company
- Medical Devices
- Healthcare
- Neuromodulation
- Pain Management
- Neurotechnology
- Medical Technology
website: https://www.sprpainrelief.com/
---
