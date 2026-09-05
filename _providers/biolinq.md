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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/biolinq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biolinq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.biolinq.com/biolinq-news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/6310feecd52f6e2e081df17e/63767368eaae7f190195aea9_Biolinq-June-2022-Privacy-Policy.pdf
- group: operate
  title: ''
  type: Contact
  url: https://www.biolinq.com/biolinq-contact
- group: other
  title: ''
  type: Technology
  url: https://www.biolinq.com/technology
- group: company
  title: ''
  type: Careers
  url: https://www.biolinq.com/biolinq-careers
- group: other
  title: ''
  type: Team
  url: https://www.biolinq.com/biolinq-team
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/biolinq/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/biolinq_stock/
coverage:
  checked: '2026-08-07'
  detail: Biolinq ships the Shine biosensor and a companion consumer mobile app only — its entire public web presence is an 11-page Webflow marketing site whose /support page reads "Intentionally left blank", and api/developer/docs/app.biolinq.com all fail to resolve in DNS.
  evidence:
  - status: 200
    url: https://www.biolinq.com/support
  - status: 404
    url: https://www.biolinq.com/openapi.json
  - status: 404
    url: https://www.biolinq.com/.well-known/agent-card.json
  - status: 404
    url: https://www.biolinq.com/llms.txt
  - status: 0
    url: https://api.biolinq.com/
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: Biolinq Incorporated is a San Diego, California medical device and digital health company founded in 2012 that develops intradermal biowearable sensors. Its lead product, Biolinq Shine, is an autonomous needle-free continuous glucose sensor built on an array of electrochemical microsensors that sit just below the surface of the skin, combined with an accelerometer and an ambient light sensor so a single wearable measures glucose alongside activity and sleep. The sensor carries an on-body LED color indicator for time-in-range and pairs with a companion mobile application for trends and insights. The FDA granted Biolinq Shine De Novo classification for adults with type 2 diabetes not on insulin therapy, with a planned US market launch. Biolinq publishes no public developer program, API documentation, or machine-readable API contract; its public web presence is a corporate marketing site.
image: https://cdn.prod.website-files.com/6310feecd52f6e2e081df17e/633c9a9b7cdf016ec08ae0d3_biolinq-logo-white%203.png
layout: provider
modified: '2026-08-07'
name: Biolinq
nav: Providers
network: true
overview: 'Biolinq is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Medical Devices, and Wearables.


  Biolinq''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/biolinq/refs/heads/main/screenshots/biolinq-2026-08-07T162503.png
security:
- kind: domain-security
  name: Biolinq Domain Security
  slug: biolinq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biolinq
tags:
- Company
- Health
- Digital Health
- Medical Devices
- Wearables
- Biosensors
- Continuous Glucose Monitoring
- Diabetes
website: https://www.biolinq.com/
---
