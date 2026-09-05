---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://clarapath.com/
- group: company
  title: ''
  type: Blog
  url: https://clarapath.com/news-insights
- group: operate
  title: ''
  type: Support
  url: https://clarapath.com/support-resources/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clarapath.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clarapath.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clarapath-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clarapath-domain-security.yml
coverage:
  checked: '2026-08-09'
  detail: Clarapath ships its software only inside the SectionStar instrument and behind a customer-portal login; clarapath.com publishes an llms.txt and a 14-URL sitemap with no developer or documentation page, and the only API-named host, api.clarapath.com, is the Strapi CMS that backs the marketing site — its /documentation, /api and /graphql endpoints all return Strapi 404 JSON.
  evidence:
  - status: 200
    url: https://clarapath.com/llms.txt
  - status: 200
    url: https://clarapath.com/sitemap.xml
  - status: 404
    url: https://api.clarapath.com/documentation
  - status: 404
    url: https://api.clarapath.com/graphql
  - status: 404
    url: https://clarapath.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: Clarapath is a medical robotics company headquartered in Hawthorne, New York that automates the tissue sectioning step of the clinical histopathology workflow. Its FDA-registered SectionStar platform pairs patented tape-transfer sectioning with precision robotics, integrated optics and sensors, and computational quality control to turn paraffin blocks into standardized slides with quantitative quality metrics. The company also ships the TrimStar Pro trimming system, a HistoStation data repository for sample and image traceability, remote Telehistology operation, and histology consulting services for hospital, reference, and veterinary laboratories.
image: https://api.clarapath.com/uploads/logo_cabbdd513c.png
layout: provider
modified: '2026-08-09'
name: Clarapath
nav: Providers
network: true
overview: 'Clarapath is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Robotics, and Pathology.


  Clarapath''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clarapath/refs/heads/main/screenshots/clarapath-2026-09-02T145056.png
security:
- kind: domain-security
  name: Clarapath Domain Security
  slug: clarapath-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clarapath
tags:
- Company
- Healthcare
- Medical Devices
- Robotics
- Pathology
- Histology
- Laboratory Automation
- Diagnostics
- Life Sciences
website: https://clarapath.com/
---
