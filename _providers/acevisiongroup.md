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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acevisiongroup-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acevisiongroup-llms.txt
- group: company
  title: ''
  type: Website
  url: https://acevisiongroup.com/
- group: company
  title: ''
  type: About
  url: https://acevisiongroup.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://acevisiongroup.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ace-vision-group/
- group: other
  title: ''
  type: x-secondary-market-listing
  url: https://equityzen.com/company/acevisiongroup
coverage:
  checked: '2026-09-06'
  detail: Ace Vision Group is a pre-commercial ophthalmic laser device manufacturer whose entire public presence is a four-page WordPress brochure site (home, about, technology, contact) with no developer section, no API reference and no machine-readable contract at any host; its VisioLite Er:YAG laser is still under development and not cleared for commercial sale, so the product is hardware, not software.
  evidence:
  - status: 200
    url: https://acevisiongroup.com/
  - status: 200
    url: https://acevisiongroup.com/technology/
  - status: 404
    url: https://acevisiongroup.com/openapi.json
  - status: 404
    url: https://acevisiongroup.com/.well-known/agent-card.json
  - status: 404
    url: https://acevisiongroup.com/llms.txt
  - status: 200
    url: https://acevisiongroup.com/sitemap_index.xml
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: Ace Vision Group, Inc. (AVG) is a Boston, Massachusetts based emerging medical laser device company founded in 2006 by vision scientist AnnMarie Hipsley, DPT, PhD. The company develops the VisioLite Er:YAG ophthalmic laser system and Laser Scleral Microporation (LSM), a non-contact therapeutic procedure intended to treat age-related eye dysfunction such as presbyopia by micro-porating the sclera to restore the eye's natural dynamic range of focus. The VisioLite system remains under development and has not been approved or cleared for commercial sale in the United States, European Union, United Kingdom or other jurisdictions. Ace Vision Group publishes a four-page corporate website and operates no developer program, public API, SDK or machine-readable interface of any kind.
image: https://acevisiongroup.com/app/uploads/2026/02/logo_color_wo_moto.png
layout: provider
modified: '2026-09-06'
name: Ace Vision Group
nav: Providers
network: true
overview: Ace Vision Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Ophthalmology, Healthcare, and Lasers.
random_paper: 6
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acevisiongroup Domain Security
  slug: acevisiongroup-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: acevisiongroup
tags:
- Company
- Medical Devices
- Ophthalmology
- Healthcare
- Lasers
- Medical Technology
- Life Sciences
- Presbyopia
website: https://acevisiongroup.com/
---
