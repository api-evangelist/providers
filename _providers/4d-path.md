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
  url: security/4d-path-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://4dpath.com/
- group: company
  title: ''
  type: About
  url: https://4dpath.com/about-us/
- group: other
  title: ''
  type: Team
  url: https://4dpath.com/our-teams/
- group: other
  title: ''
  type: Platform
  url: https://4dpath.com/platform/
- group: other
  title: ''
  type: Research
  url: https://4dpath.com/publications-posters/
- group: other
  title: ''
  type: Validation
  url: https://4dpath.com/clinical-validation/
- group: company
  title: ''
  type: Blog
  url: https://4dpath.com/news-events/
- group: company
  title: ''
  type: BlogFeeds
  url: https://4dpath.com/feed/
- group: company
  title: ''
  type: Investors
  url: https://4dpath.com/investors/
- group: operate
  title: ''
  type: Contact
  url: https://4dpath.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://4dpath.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://4dpath.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/4d-path/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/4DPath
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/4d-path-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 4D Path ships the QPOR reader as a software-as-a-medical-device product consumed by pathologists inside PathPresenter's ClinPx whole-slide viewer, and 4dpath.com is a WordPress marketing site with no developer, API, documentation or integration section anywhere in its nav or sitemap; the one API-shaped host that resolves in DNS, api.4dpath.com, is an Azure Web App that answers Microsoft's stock 404 page for its own root and for every contract path probed, including /openapi.json and /swagger/v1/swagger.json.
  evidence:
  - status: 200
    url: https://4dpath.com/
  - status: 404
    url: https://4dpath.com/openapi.json
  - status: 404
    url: https://4dpath.com/llms.txt
  - status: 404
    url: https://4dpath.com/.well-known/agent-card.json
  - status: 404
    url: https://api.4dpath.com/
  - status: 404
    url: https://api.4dpath.com/swagger/v1/swagger.json
  - status: 404
    url: https://api.github.com/orgs/4dpath
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 4D Path, Inc. is a Newton, Massachusetts computational-pathology company founded in 2016 that builds the Q-plasia OncoReader (QPOR) platform, a patented, cloud-based precision oncology and computer-aided cancer diagnostic system. Rather than conventional image-classification AI, QPOR applies statistical physics and cancer biology to digitized H&E-stained whole-slide biopsy and resection images to measure and quantify cell-cycle deregulation and tumor immune microenvironment dynamics, producing biomarker profiling, grading and therapy-response prediction without additional molecular assays such as IHC, FISH, RNA-Seq or NGS. Its lead software-as-a-medical-device product, 4D Q-plasia OncoReader Breast, received FDA Breakthrough Device Designation in November 2020, and the company has partnered with PathPresenter to distribute the reader inside the ClinPx clinical workflow platform. 4D Path publishes no public developer program, API reference, SDK or machine-readable contract of
  any kind — see x-coverage.
image: https://4dpath.com/wp-content/uploads/2024/06/4D-Path_logo.png
layout: provider
modified: '2026-09-05'
name: 4D Path
nav: Providers
network: true
overview: '4D Path is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Digital Pathology, Oncology, and Cancer Diagnostics.


  4D Path''s developer surface includes engineering blog and 15 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.4
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
    developer_ergonomics: 1.2
    discoverability: 50.0
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
  name: 4D Path Domain Security
  slug: 4d-path-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 4d-path
tags:
- Company
- Health Care
- Digital Pathology
- Oncology
- Cancer Diagnostics
- Medical Imaging
- Artificial Intelligence
- Precision Medicine
- Software As A Medical Device
- Life Sciences
- Massachusetts
website: https://4dpath.com/
---
