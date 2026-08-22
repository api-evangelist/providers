---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The Alaris Infusion Interoperability solution connects the Alaris System (large-volume pump modules and syringe modules) to hospital EMR platforms so that physician infusion orders flow wirelessly int
  name: Alaris Infusion Interoperability
  slug: alaris-infusion-interoperability
- description: 'Pyxis MedStation and Pyxis ES automated dispensing cabinets integrate with hospital pharmacy information systems and EMRs so that medication profiles, inventory, and dispense events are synchronized. '
  name: Pyxis Automated Dispensing Integration
  slug: pyxis-automated-dispensing
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carefusion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bd.com/en-us/products-and-solutions/brand-families/carefusion
- group: other
  title: ''
  type: Alaris Product Page
  url: https://www.bd.com/en-us/products-and-solutions/products/product-families/alaris-infusion-system
- group: other
  title: ''
  type: Pyxis Product Page
  url: https://www.bd.com/en-us/products-and-solutions/products/product-families/bd-pyxis-medstation-es-system
- group: other
  title: ''
  type: BD Corporate Site
  url: https://www.bd.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.bd.com/en-us/about-bd/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bd.com/en-us/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bd.com/en-us/our-company/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bd1/
- group: other
  title: ''
  type: X
  url: https://x.com/BDandCo
created: '2026-03-23'
description: CareFusion is a medical technology brand, acquired by BD (Becton, Dickinson and Company) in 2015, best known for the Alaris infusion system and the Pyxis automated dispensing product line. CareFusion does not expose a public developer API; instead, its devices and dispensing systems interoperate with hospital EMRs and pharmacy systems over HL7 v2 messaging, smart-pump interoperability middleware, and vendor-managed integration services. The Alaris Infusion Interoperability program wirelessly transmits orders from EMRs (such as Epic and Cerner) into Alaris large-volume and syringe modules and returns infusion status back to the EMR in near real time, using the Alaris Guardrails drug library as a safety layer.
finops:
- name: Carefusion Finops
  service_category: API
  slug: carefusion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carefusion.png
layout: provider
modified: '2026-04-23'
name: CareFusion (BD)
nav: Providers
network: true
overview: CareFusion (BD) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automated Dispensing, BD, CareFusion, Connected Devices, and EMR Integration.
plans:
- name: Carefusion Plans Pricing
  plan_count: 3
  slug: carefusion-plans-pricing
press:
- date: '2026-05-25'
  title: Becton Dickinson to buy CareFusion for $12 billion in cash, ...
  url: https://www.reuters.com/article/business/becton-dickinson-to-buy-carefusion-for-12-billion-in-cash-stock-idUSKCN0HU0U3/
- date: '2026-05-25'
  title: Becton Dickinson Completes Acquisition Of CareFusion
  url: https://www.prnewswire.com/news-releases/becton-dickinson-completes-acquisition-of-carefusion-300051582.html
- date: '2026-05-25'
  title: Becton Dickinson releases 1st joint BD-CareFusion product
  url: https://www.massdevice.com/becton-dickinson-releases-1st-joint-bd-carefusion-product/
- date: '2026-05-25'
  title: BD to Acquire CareFusion, But Not Without Controversy
  url: https://www.mddionline.com/business/bd-to-acquire-carefusion-but-not-without-controversy
- date: '2026-05-25'
  title: 5 takeaways from Becton Dickinson's $24B acquisition of ...
  url: https://medcitynews.com/2017/04/5-takeaways-becton-dickinsons-24b-acquisition-c-r-bard/
random_paper: 0
rate_limits:
- limit_count: 5
  name: Carefusion Rate Limits
  slug: carefusion-rate-limits
score:
  band: emerging
  composite: 11.3
  delta: -3.5
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carefusion/refs/heads/main/screenshots/carefusion-2026-06-20T174000.png
security:
- kind: domain-security
  name: Carefusion Domain Security
  slug: carefusion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carefusion
tags:
- Automated Dispensing
- BD
- CareFusion
- Connected Devices
- EMR Integration
- Healthcare
- HL7
- Infusion Pumps
- Medical Devices
- Pyxis
- Smart Pumps
website: https://www.bd.com/en-us/products-and-solutions/brand-families/carefusion
---
