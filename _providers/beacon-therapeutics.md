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
- group: company
  title: ''
  type: Website
  url: https://www.beacontx.com/
- group: company
  title: ''
  type: About
  url: https://www.beacontx.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.beacontx.com/news-and-events/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.beacontx.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://www.beacontx.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beacontx.com/privacy-statement/
- group: company
  title: ''
  type: Careers
  url: https://www.beacontx.com/careers/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beacon-therapeutics-domain-security.yml
coverage:
  checked: '2026-08-06'
  detail: Beacon Therapeutics is a clinical-stage AAV gene therapy developer whose entire public surface is a 14-page WordPress marketing site (pipeline, clinical trials, disease focus, careers) — /developers, /api, /openapi.json, /llms.txt and every /.well-known/ path return a hard 404, and the product is a retinal therapeutic, not software.
  evidence:
  - status: 404
    url: https://www.beacontx.com/developers
  - status: 404
    url: https://www.beacontx.com/openapi.json
  - status: 404
    url: https://www.beacontx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.beacontx.com/.well-known/security.txt
  - status: 404
    url: https://www.beacontx.com/llms.txt
  - status: 200
    url: https://www.beacontx.com/sitemap_index.xml
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: Beacon Therapeutics is a clinical-stage ophthalmic gene therapy company founded in 2023 to save and restore the sight of people living with rare and prevalent retinal diseases that lead to blindness. Built around adeno-associated virus (AAV) gene therapy, the company delivers functional copies of mutated genes into retinal cells so the body can produce the missing therapeutic protein. Its lead clinical program, laru-zova (laruparetigene zovaparvovec), targets X-linked retinitis pigmentosa (XLRP), alongside preclinical programs in dry age-related macular degeneration (dAMD) and cone-rod dystrophy (CRD), the latter in-licensed from the University of Oxford. Beacon operates across the United Kingdom and the United States, with a corporate base in London and a US presence in the Cambridge, Massachusetts area. It is a therapeutics developer, not a software or data platform company, and publishes no public API, SDK or developer program.
image: https://www.beacontx.com/wp-content/themes/beacon/assets/images/favicon/apple-touch-icon.png
layout: provider
modified: '2026-08-06'
name: Beacon Therapeutics
nav: Providers
network: true
overview: 'Beacon Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Gene Therapy, Ophthalmology, and Clinical Trials.


  Beacon Therapeutics'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beacon-therapeutics/refs/heads/main/screenshots/beacon-therapeutics-2026-08-07T162225.png
security:
- kind: domain-security
  name: Beacon Therapeutics Domain Security
  slug: beacon-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: beacon-therapeutics
tags:
- Company
- Biotechnology
- Gene Therapy
- Ophthalmology
- Clinical Trials
- Life Sciences
- Rare Disease
- Pharmaceuticals
website: https://www.beacontx.com/
---
