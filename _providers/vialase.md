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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.vialase.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vialase.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.vialase.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vialase.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vialase/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vialase-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vialase-llms.txt
coverage:
  checked: '2026-09-02'
  detail: ViaLase manufactures a single clinical-stage ophthalmic capital device — the ViaLuxe femtosecond laser with its ViaLens patient interface and ViaVue gonio camera — whose only data connectivity is a Bluetooth-paired tablet at the bedside; vialase.com is an eleven-page WordPress marketing and clinical-education site with no api./developer./docs./status./portal./trust. hostname anywhere in DNS, and the only machine-readable JSON served on the domain is the stock WordPress core REST API at /wp-json/, which is CMS scaffolding rather than a product API.
  evidence:
  - status: 404
    url: https://www.vialase.com/openapi.json
  - status: 404
    url: https://www.vialase.com/graphql
  - status: 404
    url: https://www.vialase.com/llms.txt
  - status: 404
    url: https://www.vialase.com/.well-known/agent-card.json
  - status: 404
    url: https://www.vialase.com/.well-known/security.txt
  - status: 404
    url: https://www.vialase.com/.well-known/api-catalog
  - status: 200
    url: https://www.vialase.com/wp-json/
  - status: 200
    url: https://www.vialase.com/
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: 'ViaLase, Inc. is a globally-minded, venture and strategic capital-backed, clinical stage medical technology company headquartered in Aliso Viejo, California, founded and led by Tibor Juhasz, PhD. The company develops the ViaLuxe Laser System, which combines femtosecond laser technology with micron-resolution OCT image guidance to perform femtosecond laser image-guided high-precision trabeculotomy (FLigHT) — a noninvasive, non-incisional procedure that creates drainage apertures through the trabecular meshwork to lower intraocular pressure in patients with open-angle glaucoma. The system pairs the ViaLuxe laser with the ViaLens patient interface and the ViaVue gonio camera. The company closed an approximately $40 million Series C financing in April 2024 with participation from Venture Investors Health Fund, Arboretum Ventures and Falcon Vision. The ViaLase Laser received CE Mark approval in the European Union in 2024 for adult patients with primary open-angle glaucoma and is
  under evaluation in a US IDE clinical trial; it is not approved for sale in the United States. ViaLase is a medical device manufacturer rather than a software vendor: it publishes no public API, developer portal, SDK, or machine-readable specification, and vialase.com is a WordPress marketing and clinical-education site.'
image: https://www.vialase.com/wp-content/uploads/2024/07/vialase-social-image.png
layout: provider
modified: '2026-09-02'
name: ViaLase
nav: Providers
network: true
overview: 'ViaLase is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, MedTech, and Ophthalmology.


  ViaLase''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 3
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Vialase Domain Security
  slug: vialase-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vialase
tags:
- Company
- Medical Devices
- Healthcare
- MedTech
- Ophthalmology
- Glaucoma
- Femtosecond Laser
- Surgical Devices
- Clinical Trials
- Medical Imaging
website: https://www.vialase.com/
---
