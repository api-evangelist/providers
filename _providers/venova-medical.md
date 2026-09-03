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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://venovamedical.com/
- group: company
  title: ''
  type: Blog
  url: https://venovamedical.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://venovamedical.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/venova-medical-inc
- group: start
  title: ''
  type: ClinicalTrial
  url: https://clinicaltrials.gov/study/NCT05757726
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/venova-medical-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/venova-medical-domain-security.yml
coverage:
  checked: '2026-09-02'
  detail: Venova Medical is a clinical-stage manufacturer of a percutaneous AV fistula device; its entire web presence is a four-page WordPress/Divi marketing site with no developer, docs or API section, and every contract-discovery path probed on venovamedical.com returned the site's 404 template.
  evidence:
  - status: 404
    url: https://venovamedical.com/openapi.json
  - status: 404
    url: https://venovamedical.com/.well-known/api-catalog
  - status: 404
    url: https://venovamedical.com/.well-known/agent-card.json
  - status: 404
    url: https://venovamedical.com/.well-known/security.txt
  - status: 200
    url: https://venovamedical.com/page-sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: 'Venova Medical, Inc. is a privately held, clinical-stage medical device company in Los Gatos, California, developing minimally invasive vascular access technology for patients on hemodialysis. Its Velocity Percutaneous AVF System is a next-generation percutaneous arteriovenous fistula (pAVF) device intended to create a functional dialysis access with fewer reinterventions and faster maturation than a surgically created fistula, targeting the stenosis at the artery-vein junction that is the most common barrier to AVF success. The company is running the VENOS clinical program (VENOS-2 early feasibility, VENOS-3 IDE pivotal) toward FDA approval; the Velocity System remains investigational and is not FDA cleared or approved. Venova is backed by ShangBay Capital, Banyan Pacific, Aphelion Capital, Cardeation, Kofa Healthcare, Catalyst Health Ventures, Cadence Growth Capital and Mirae Asset Capital Life Science. Venova publishes no public API, developer portal, SDK or machine-readable
  specification: it is a physical medical device manufacturer, not a software provider.'
image: https://venovamedical.com/wp-content/uploads/2023/02/Venova-Logo.png
layout: provider
modified: '2026-09-02'
name: Venova Medical
nav: Providers
network: true
overview: 'Venova Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Hemodialysis, and Vascular Access.


  Venova Medical''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Venova Medical Plans Pricing
  plan_count: 0
  slug: venova-medical-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Venova Medical Rate Limits
  slug: venova-medical-rate-limits
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Venova Medical Domain Security
  slug: venova-medical-domain-security
  summary_line: TLSv1.3
slug: venova-medical
tags:
- Company
- Medical Devices
- Healthcare
- Hemodialysis
- Vascular Access
- Nephrology
- Interventional Cardiology
- Clinical Stage
- Life Sciences
website: https://venovamedical.com/
---
