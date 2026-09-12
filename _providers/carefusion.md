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
  scored_at: '2026-09-12'
api_count: 2
apis:
- description: The Alaris Infusion Interoperability solution connects the Alaris System (large-volume pump modules and syringe modules) to hospital EMR platforms so that physician infusion orders flow wirelessly int
  name: Alaris Infusion Interoperability
  slug: alaris-infusion-interoperability
- description: 'Pyxis MedStation and Pyxis ES automated dispensing cabinets integrate with hospital pharmacy information systems and EMRs so that medication profiles, inventory, and dispense events are synchronized. '
  name: Pyxis Automated Dispensing Integration
  slug: pyxis-automated-dispensing
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.bd.com/
- group: operate
  title: ''
  type: Support
  url: https://www.bd.com/en-us/support
- group: operate
  title: ''
  type: Contact
  url: https://www.bd.com/en-us/support/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bd.com/en-us/about-bd/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bd.com/en-us/about-bd/policies/privacy-policy-statement
- group: auth
  title: ''
  type: Security
  url: https://www.bd.com/en-us/about-bd/cybersecurity?active-tab=3
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/carefusion-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/carefusion-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/carefusion-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/carefusion-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/carefusion-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carefusion-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carefusion-domain-security.yml
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
modified: '2026-09-06'
name: CareFusion (BD)
nav: Providers
network: true
overview: 'CareFusion (BD) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automated Dispensing, BD, CareFusion, Connected Devices, and EMR Integration.


  CareFusion (BD)''s developer surface includes support and 14 more developer resources.'
plans:
- name: Carefusion Plans Pricing
  plan_count: 0
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
- limit_count: 0
  name: Carefusion Rate Limits
  slug: carefusion-rate-limits
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 66.7
    operational_transparency: 10.5
  previous_composite: 26.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/carefusion/refs/heads/main/screenshots/carefusion-2026-06-20T174000.png
security:
- kind: domain-security
  name: Carefusion Domain Security
  slug: carefusion-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Carefusion Vulnerability Disclosure
  slug: carefusion-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Carefusion Trust Center
  slug: carefusion-trust-center
  summary_line: ISO/IEC 27001:2022, UL 2900-2-1 (UL Cybersecurity Assurance Program), SOC 2+ (Security, Availability), MDS2 (Manufacturer Disclosure Statement for Medical Device Security)
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
website: https://www.bd.com/
---
