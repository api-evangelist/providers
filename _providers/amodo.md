---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://amodo.eu'', ''status'': 301, ''note'': ''declared website redirects to https://www.cmtelematics.com/cmt-acquires-amodo/ — a different registrable domain (amodo.eu -> cmtelematics.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amodo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amodo.eu
- group: other
  title: ''
  type: Company
  url: https://www.cmtelematics.com/cmt-acquires-amodo/
created: '2026-07-17'
description: Amodo was a European connected-insurance and telematics company founded in Zagreb, Croatia, that helped insurers and brokers build and distribute personalized usage-based insurance (UBI) products. Its Connected Insurance Platform combined a mobile telematics SDK, driver-behavior scoring, customer segmentation, and profiling analytics to power models ranging from try-before-you-buy to pay-as-you-drive and pay-per-mile. Over roughly nine years Amodo ran nearly 50 telematics programs worldwide with insurers including AIG, Porsche Versicherungs, Tower Insurance, and P&V, and was named one of the Financial Times' top five insurtech companies. Backed by Speedinvest, Amodo was acquired by Cambridge Mobile Telematics (CMT) in March 2023 and folded into CMT's European operations; the amodo.eu domain now redirects to CMT, and the company no longer maintains an independent public developer or API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amodo.png
layout: provider
modified: '2026-07-17'
name: Amodo
nav: Providers
network: true
overview: Amodo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Telematics, and Usage-Based Insurance.
random_paper: 3
score:
  band: minimal
  composite: 2.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amodo/refs/heads/main/screenshots/amodo-2026-07-25T200109.png
security:
- kind: domain-security
  name: Amodo Domain Security
  slug: amodo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amodo
tags:
- Company
- Insurance
- Insurtech
- Telematics
- Usage-Based Insurance
- Connected Insurance
- Mobile SDK
- Acquired
website: https://amodo.eu
---
