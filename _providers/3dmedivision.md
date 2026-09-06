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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.3dmedivision.com/
- group: company
  title: ''
  type: Blog
  url: https://www.3dmedivision.com/news.html
- group: operate
  title: ''
  type: PressReleases
  url: https://www.3dmedivision.com/press-releases.html
- group: operate
  title: ''
  type: Support
  url: https://www.3dmedivision.com/contact.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.3dmedivision.com/privacy-policy.html
- group: other
  title: ''
  type: x-downloads
  url: https://www.3dmedivision.com/downloads.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/3d-medivision/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.3dmedivision.com/ir.html
- group: other
  title: ''
  type: x-secondary-market-listing
  url: https://equityzen.com/company/3dmedivision/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3dmedivision-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3dmedivision-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 3D Medivision sells 3D surgical camera hardware and subscription video-education products (Veterflix, VGTC, VET-TV, Veter VR); its site has no developer, API or integration section at all, its Veterflix learning platform runs as a tenant on the third-party Airklass LMS, and it has no GitHub organization or package in any public registry.
  evidence:
  - status: 200
    url: https://www.3dmedivision.com/sitemap.xml
  - status: 404
    url: https://www.3dmedivision.com/openapi.json
  - status: 404
    url: https://www.3dmedivision.com/.well-known/api-catalog
  - status: 404
    url: https://www.3dmedivision.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/3dmedivision
  - status: 404
    url: https://registry.npmjs.org/veterflix
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '3D Medivision (쓰리디메디비젼) is a Seoul, South Korea medical imaging and medical-education company founded around 3D surgical video capture. It builds 3D/2D camera systems, recorders and monitors that mount to surgical microscopes and endoscopes so a procedure can be recorded stereoscopically and streamed to surgeons in another room, hospital or country. On top of that hardware it operates a set of end-user education products: Veterflix and Global Veterflix (video-on-demand veterinary courses, webinars and 3D canine anatomy), VGTC (live 3D surgery streaming plus hands-on courses in Incheon), VET-TV (a 3D anatomy lecture system for large-group teaching), Veter VR (VR-based veterinary training) and Surgflix for human surgery. The company sells hardware, subscriptions and training — it does not operate a public developer program, and no public API, SDK, webhook surface or machine-readable API contract was found on any host it controls.'
image: https://www.3dmedivision.com/uploads/4/3/9/3/43934531/published/2-1.png
layout: provider
modified: '2026-09-05'
name: 3D Medivision
nav: Providers
network: true
overview: '3D Medivision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Medical Imaging, Surgical Video, and Veterinary.


  3D Medivision''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.2
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 3Dmedivision Domain Security
  slug: 3dmedivision-domain-security
  summary_line: TLSv1.3
slug: 3dmedivision
tags:
- Company
- Medical Devices
- Medical Imaging
- Surgical Video
- Veterinary
- Education
- Video On Demand
- Virtual Reality
- Health Care
- South Korea
website: https://www.3dmedivision.com/
---
