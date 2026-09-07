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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abmrespiratorycare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abmrc.com/
- group: company
  title: ''
  type: Blog
  url: https://abmrc.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://abmrc.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://abmrc.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abmrc.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abmrc.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abmrc/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abmrespiratorycare-llms.txt
coverage:
  checked: '2026-09-06'
  detail: ABM Respiratory Care builds BiWaze airway-clearance and cough-assist hardware sold through demo requests and reimbursement channels, and its whole public presence is a WordPress marketing site at abmrc.com plus a WordPress eIFU manuals portal at eifu.abmrc.com — no api/developer/docs/ status subdomain resolves, and the only machine-readable endpoint on either host is the default WordPress core REST API at /wp-json/, which is CMS scaffolding rather than a product API.
  evidence:
  - status: 404
    url: https://abmrc.com/openapi.json
  - status: 404
    url: https://abmrc.com/llms.txt
  - status: 404
    url: https://abmrc.com/.well-known/agent-card.json
  - status: 404
    url: https://eifu.abmrc.com/openapi.json
  - status: 200
    url: https://abmrc.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'ABM Respiratory Care (ABMRC, LLC — operating with Advanced Biomechanics Private Limited in Bangalore, India and Advanced Bio Machines PTE LTD in Singapore, with US headquarters in Eagan, Minnesota) is a privately held respiratory medical device manufacturer founded by CTO Vinay Joshi and led by CEO Greg Miller. It designs, manufactures and sells airway clearance and lung ventilation hardware under the BiWaze brand — BiWaze Clear (oscillation and lung expansion therapy) and BiWaze Cough (mechanical insufflation-exsufflation) — in both hospital and home-care configurations, sold through direct sales, demo requests and reimbursement channels rather than self-service signup. ABM Respiratory Care is a physical device company: it publishes no developer portal, no public API, no SDK and no machine-readable specification, and its entire public web surface is a WordPress marketing site at abmrc.com plus a separate WordPress electronic instructions-for-use portal at eifu.abmrc.com.'
image: https://abmrc.com/wp-content/uploads/2025/11/product-001.webp
layout: provider
modified: '2026-09-06'
name: ABM Respiratory Care
nav: Providers
network: true
overview: 'ABM Respiratory Care is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, MedTech, and Respiratory Care.


  ABM Respiratory Care''s developer surface includes engineering blog, support, and 7 more developer resources.'
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
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: domain-security
  name: Abmrespiratorycare Domain Security
  slug: abmrespiratorycare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: abmrespiratorycare
tags:
- Company
- Medical Devices
- Healthcare
- MedTech
- Respiratory Care
- Airway Clearance
- Mechanical Ventilation
- Pulmonology
- Home Health
- Hospital Equipment
website: https://abmrc.com/
---
