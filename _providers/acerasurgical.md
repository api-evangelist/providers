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
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://acera-surgical.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acera-surgical.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://acera-surgical.com/contact-us/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acerasurgical-domain-security.yml
coverage:
  checked: '2026-09-06'
  detail: Acera Surgical manufactures physical implantable regenerative wound-care devices (Restrata electrospun nanofiber matrices, Cerafix dural repair); its entire public site is a five-page ASP.NET marketing brochure with no developer, integration, or documentation section, and the host answers every unknown path — including every /.well-known/ document — with a soft-200 copy of the homepage.
  evidence:
  - status: 200
    url: https://acera-surgical.com/
  - status: 200
    url: https://acera-surgical.com/.well-known/security.txt
  - status: 200
    url: https://acera-surgical.com/openapi.json
  - status: 200
    url: https://acera-surgical.com/llms.txt
  - status: 200
    url: https://acera-surgical.com/zzz-this-path-does-not-exist-9f3a
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'Acera Surgical Inc. is a St. Louis, Missouri bioscience company founded in 2013 that develops and commercializes fully engineered, 100% synthetic materials for regenerative wound care and soft tissue repair, built on a proprietary electrospun nanofiber technology platform. Its Restrata product family — Restrata Sheet, Restrata Meshed and Restrata MiniMatrix — is a fully resorbable synthetic matrix used to treat hard-to-heal and complex wounds in acute care settings, and its Cerafix implant addresses dural repair and cerebrospinal fluid leakage. Acera was acquired by Solventum Corporation on December 23, 2025 for $725 million in cash plus up to $125 million in milestone payments, and now sits inside Solventum''s Medical segment MedSurg portfolio. Acera is a medical device manufacturer, not a software company: it publishes no API, developer portal, SDK, or machine-readable interface of any kind.'
image: https://acera-surgical.com/site/user/images/acera_asc_pos_rgb_2000px.png
layout: provider
modified: '2026-09-06'
name: Acera Surgical
nav: Providers
network: true
overview: 'Acera Surgical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Regenerative Medicine, Wound Care, and Biotechnology.


  Acera Surgical''s developer surface includes support and 3 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: domain-security
  name: Acerasurgical Domain Security
  slug: acerasurgical-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: acerasurgical
tags:
- Company
- Medical Devices
- Regenerative Medicine
- Wound Care
- Biotechnology
- Surgical
- Life Sciences
- Healthcare
website: https://acera-surgical.com/
---
