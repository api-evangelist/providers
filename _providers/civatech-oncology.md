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
  url: https://civatechoncology.com/
- group: company
  title: ''
  type: About
  url: https://civatechoncology.com/about/
- group: other
  title: ''
  type: Products
  url: https://civatechoncology.com/products/
- group: operate
  title: ''
  type: Contact
  url: https://civatechoncology.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://civatechoncology.com/faq/
- group: company
  title: ''
  type: News
  url: https://civatechoncology.com/headlines/
- group: other
  title: ''
  type: RSS
  url: https://civatechoncology.com/feed/
- group: company
  title: ''
  type: Investors
  url: https://civatechoncology.com/investors/
- group: other
  title: ''
  type: Patents
  url: https://civatechoncology.com/civa-patents/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/civatech-oncology-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/civatech-oncology-llms.txt
coverage:
  checked: '2026-08-09'
  detail: CivaTech Oncology manufactures implantable brachytherapy radiation sources (CivaSheet, CivaString, CivaDerm); its entire 28-page WordPress site is product, clinical and investor marketing with no developer section, and every contract probe against civatechoncology.com — /openapi.json, /swagger.json, /graphql, /api-docs, /llms.txt and all eight /.well-known/ paths including both agent-card locations — returned 404.
  evidence:
  - status: 404
    url: https://civatechoncology.com/openapi.json
  - status: 404
    url: https://civatechoncology.com/.well-known/agent-card.json
  - status: 404
    url: https://civatechoncology.com/llms.txt
  - status: 200
    url: https://civatechoncology.com/page-sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: CivaTech Oncology is a Durham, North Carolina medical device manufacturer that develops polymer-encapsulated low dose rate (LDR) brachytherapy radiation sources for the treatment of solid tumors. Its FDA-cleared product line includes CivaSheet, a flexible, bioabsorbable, unidirectional planar source that can be custom-sized in the operating room and shields healthy tissue; CivaString, a polymer-encapsulated brachytherapy seed used for prostate and other localized cancers; and CivaDerm for dermatological applications. The company markets to radiation oncologists and surgical teams across pancreatic, sarcoma, colorectal, gynecologic, head and neck, lung and prostate indications, and its research has been supported by NIH/NCI and SBIR programs. It publishes no public developer program, API, SDK, or machine-readable specification.
image: https://civatechoncology.com/wp-content/uploads/2022/02/cropped-Icon-CivaTech-192x192.png
layout: provider
modified: '2026-08-09'
name: CivaTech Oncology
nav: Providers
network: true
overview: 'CivaTech Oncology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Oncology, Brachytherapy, and Radiation Therapy.


  CivaTech Oncology''s developer surface includes FAQ, product news, and 9 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 3.3
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Civatech Oncology Domain Security
  slug: civatech-oncology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: civatech-oncology
tags:
- Company
- Medical Devices
- Oncology
- Brachytherapy
- Radiation Therapy
- Healthcare
- Cancer Treatment
- Life Sciences
website: https://civatechoncology.com/
---
