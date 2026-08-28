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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instylla-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://instylla.com/
- group: company
  title: ''
  type: About
  url: https://instylla.com/about/
- group: company
  title: ''
  type: Blog
  url: https://instylla.com/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://instylla.com/feed/
- group: operate
  title: ''
  type: ContactUs
  url: https://instylla.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://instylla.com/careers/
- group: other
  title: ''
  type: CaseStudies
  url: https://instylla.com/case-studies/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instylla/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/instylla
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/instylla_stock/
coverage:
  checked: '2026-08-23'
  detail: Instylla is an FDA-PMA medical device manufacturer whose product is an injectable hydrogel embolic agent, not software; its entire web presence is a seven-page WordPress marketing site (Solutions / Clinical Study / Case Studies / About / News / Careers / Contact) whose only login is a clinical "Study Portal" for trial sites, and the full Wayback URL inventory for instylla.com contains no developer, docs or API path ever.
  evidence:
  - status: 202
    url: https://instylla.com/openapi.json
  - status: 202
    url: https://instylla.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/search/repositories?q=instylla
  - status: 404
    url: https://pypi.org/pypi/instylla/json
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Instylla, Inc. is a privately held medical device company headquartered in Bedford, Massachusetts, founded in 2017 by Incept LLC to develop next-generation resorbable liquid embolic agents for interventional radiology, with initial clinical applications in interventional oncology and peripheral hemostasis. Its flagship product, the Embrace Hydrogel Embolic System, received U.S. FDA premarket approval (PMA) in August 2025 for the embolization of hypervascular tumors in peripheral arteries of 5 mm or less, and began commercial use in January 2026; the company also markets the FDA-cleared Tembo Embolic System. Embrace is delivered as two injectable polyethylene-glycol precursors that crosslink in the vessel lumen into a soft hydrogel and then resorb by hydrolysis over roughly eleven months. Instylla is a device manufacturer rather than a software vendor: it publishes no developer program, no public API, and no machine-readable interface contract.'
image: https://instylla.com/wp-content/uploads/2021/08/Instyla-Social-Share-Image-v2.jpg
layout: provider
modified: '2026-08-23'
name: Instylla
nav: Providers
network: true
overview: 'Instylla is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Interventional Radiology, and Oncology.


  Instylla''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 4.4
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Instylla Domain Security
  slug: instylla-domain-security
  summary_line: TLSv1.3 · DMARC
slug: instylla
tags:
- Company
- Medical Devices
- Healthcare
- Interventional Radiology
- Oncology
- Embolization
- Life Sciences
- Biomaterials
website: https://instylla.com/
---
