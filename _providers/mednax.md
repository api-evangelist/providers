---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.pediatrix.com
- group: company
  title: ''
  type: About
  url: https://www.pediatrix.com/about
- group: operate
  title: ''
  type: ContactUs
  url: https://www.pediatrix.com/contact-us
- group: operate
  title: ''
  type: Support
  url: https://www.pediatrix.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.joinpediatrix.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://mednax.gcs-web.com/
- group: company
  title: ''
  type: Newsroom
  url: https://mednax.gcs-web.com/news-releases
- group: operate
  title: ''
  type: PressReleases
  url: https://www.pediatrix.com/about/for-media
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pediatrix.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pediatrix.com/notice-of-privacy-practices
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pediatrix
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@pediatrixmedicalgroup
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/pediatrixmed/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mednax-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mednax-domain-security.yml
coverage:
  checked: '2026-09-04'
  detail: Pediatrix Medical Group (the former MEDNAX) is a physician services organization running clinical practices, and mednax.com now 302s to www.pediatrix.com, whose 5,758-URL sitemap contains no developer, API or integration page — its only software product, BabySteps Cloud, is a NICU documentation tool sold to hospital partners with no published contract, and every /.well-known/, /openapi.json and /llms.txt path 404s on the live host.
  evidence:
  - status: 302
    url: https://www.mednax.com/
  - status: 200
    url: https://www.pediatrix.com/
  - status: 404
    url: https://www.pediatrix.com/openapi.json
  - status: 404
    url: https://www.pediatrix.com/llms.txt
  - status: 404
    url: https://www.pediatrix.com/.well-known/security.txt
  - status: 404
    url: https://www.pediatrix.com/.well-known/agent-card.json
  - status: 200
    url: https://www.pediatrix.com/for-hospitals/babysteps-cloud
  reason: not-a-software-company
  state: none
created: '2026-04-07'
description: 'Pediatrix Medical Group, Inc. (NYSE: MD) — known as MEDNAX until its 2022 rebrand, and still reachable at mednax.com, which now redirects to www.pediatrix.com — is a US physician services organization delivering neonatal, maternal-fetal, pediatric cardiology, pediatric surgery and other pediatric subspecialty care through affiliated practices at hospitals and clinics across the country. Its one software product, BabySteps Cloud, is a cloud clinical documentation tool for NICUs that feeds the Pediatrix Clinical Data Warehouse and is sold to hospital partners as an end-user product. As of a 2026-09-04 probe pass Pediatrix publishes no public API, developer portal, machine-readable specification, or /.well-known/ discovery document. The MEDNAX Radiology Solutions / vRad business covered by this repository''s older press and blog archive was sold to Radiology Partners in December 2020 and is no longer part of this company.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mednax.png
layout: provider
modified: '2026-09-04'
name: Pediatrix Medical Group (formerly MEDNAX)
nav: Providers
network: true
overview: 'Pediatrix Medical Group (formerly MEDNAX) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Healthcare, Health Care Services, Physician Services, and Pediatrics.


  Pediatrix Medical Group (formerly MEDNAX)''s developer surface includes support, YouTube channel, and 13 more developer resources.'
press:
- date: '2026-05-25'
  title: Sorna Corporation - Latest News - SornaCorp
  url: https://pressroom.prlog.org/SornaCorp/
- date: '2026-05-25'
  title: In the News
  url: https://www.radpartners.com/in-the-news/
- date: '2026-05-25'
  title: Mednax
  url: https://www.itnonline.com/company/mednax
- date: '2026-05-25'
  title: MEDNAX Radiology Solutions Launches Artificial Intelligence ...
  url: https://mednax.gcs-web.com/news-releases/news-release-details/mednax-radiology-solutions-launches-artificial-intelligence
- date: '2026-05-25'
  title: Press Releases | Pediatrix Medical Group, Inc.
  url: https://mednax.gcs-web.com/news-releases
random_paper: 7
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mednax/refs/heads/main/screenshots/mednax-2026-06-20T185120.png
security:
- kind: domain-security
  name: Mednax Domain Security
  slug: mednax-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mednax
tags:
- Fortune 1000
- Healthcare
- Health Care Services
- Physician Services
- Pediatrics
- Neonatology
- Hospitals
- Telehealth
website: https://www.pediatrix.com
---
