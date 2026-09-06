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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/410medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://410medical.com/
- group: company
  title: ''
  type: About
  url: https://410medical.com/410-medical/
- group: other
  title: ''
  type: Products
  url: https://410medical.com/about/
- group: company
  title: ''
  type: Blog
  url: https://410medical.com/blog/
- group: company
  title: ''
  type: BlogFeeds
  url: https://410medical.com/feed/
- group: company
  title: ''
  type: News
  url: https://410medical.com/news/
- group: other
  title: ''
  type: CaseStudies
  url: https://410medical.com/case-study/
- group: learn
  title: ''
  type: Training
  url: https://410medical.com/training-videos/
- group: other
  title: ''
  type: Patents
  url: https://410medical.com/patents/
- group: company
  title: ''
  type: Careers
  url: https://410medical.com/careers/
- group: operate
  title: ''
  type: ContactUs
  url: https://410medical.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://410medical.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://410medical.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/410-medical
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LifeFlow__
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/LifeFlowRapidInfuser/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/lifeflow/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/410medical
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/410medical-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 410 Medical manufactures a mechanical, single-use handheld infuser (LifeFlow / LifeFlow PLUS) and its entire web presence is one WordPress marketing, clinical-evidence and training site — every conventional developer host (api./developer./docs./status./portal./ dev./app./store..410medical.com) is NXDOMAIN, all fourteen named /.well-known/ and APIs.json root paths 404 on both the apex and www hosts, and the only machine-readable endpoint on the domain is the default WordPress core REST API at /wp-json/, whose nineteen namespaces are WP core plus off-the-shelf plugins (Wordfence, AIOSEO, Relevanssi, The Events Calendar, Redirection, Flywheel) with not one first-party namespace, so it is CMS scaffolding rather than a product API.
  evidence:
  - status: 404
    url: https://410medical.com/openapi.json
  - status: 404
    url: https://410medical.com/.well-known/agent-card.json
  - status: 404
    url: https://410medical.com/.well-known/security.txt
  - status: 404
    url: https://410medical.com/apis.json
  - status: 200
    url: https://410medical.com/wp-json/
  - status: 200
    url: https://410medical.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: '410 Medical, Inc. is a privately held medical device company headquartered in Durham, North Carolina, founded in 2013 by pediatric intensivist Dr. Mark Piehl and named for the pediatric septic shock guideline of four 10 ml/kg fluid boluses. It designs, engineers and assembles the LifeFlow family of handheld rapid infusers — LifeFlow for crystalloid resuscitation and LifeFlow PLUS for blood and blood components — which let a single clinician deliver a unit of blood or 500 ml of fluid in under two minutes without a pump or pressure bag. LifeFlow received FDA clearance in 2016 and is used by hospital emergency departments, trauma centers, pediatric and obstetric units, EMS agencies, fire departments and military and public safety teams for sepsis, trauma, hemorrhagic shock and postpartum hemorrhage. 410 Medical is a physical medical device manufacturer: it publishes no public API, developer portal, SDK, OpenAPI or any other machine-readable specification, and its entire web surface
  is a WordPress marketing, clinical-evidence and training site.'
image: https://410medical.com/wp-content/uploads/2026/07/LifeFlow-O-1.png
layout: provider
modified: '2026-09-05'
name: 410 Medical
nav: Providers
network: true
overview: '410 Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, MedTech, and Emergency Medicine.


  410 Medical''s developer surface includes engineering blog, product news, training material, support, and 16 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 410Medical Domain Security
  slug: 410medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 410medical
tags:
- Company
- Medical Devices
- Healthcare
- MedTech
- Emergency Medicine
- Critical Care
- Resuscitation
- Emergency Medical Services
- Blood Transfusion
- Trauma
- Pediatrics
- Obstetrics
website: https://410medical.com/
---
