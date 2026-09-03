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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://commonsclinic.com/
- group: company
  title: ''
  type: Blog
  url: https://commonsclinic.com/blog/
- group: operate
  title: ''
  type: Contact
  url: https://commonsclinic.com/booking-request/
- group: other
  title: ''
  type: Locations
  url: https://commonsclinic.com/locations/
- group: other
  title: ''
  type: Services
  url: https://commonsclinic.com/what-we-treat/
- group: other
  title: ''
  type: HowItWorks
  url: https://commonsclinic.com/how-it-works/
- group: other
  title: ''
  type: Physicians
  url: https://commonsclinic.com/physicians/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://commonsclinic.com/privacy-policy/
- group: commercial
  title: ''
  type: PrivacyPractices
  url: https://commonsclinic.com/privacy-practices/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://commonsclinic.com/terms-and-conditions/
- group: other
  title: ''
  type: DoNotSell
  url: https://commonsclinic.com/do-not-sell/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commons-clinic
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/company/commons-clinic/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/commons-clinic-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commons-clinic-domain-security.yml
coverage:
  checked: '2026-08-09'
  detail: Commons Clinic sells clinical care, not software — nine Southern California orthopedic and spine clinics plus its own surgery center — and the only thing a patient or partner can transact with online is a booking-request form; there is no api., developer., docs. or portal. hostname in DNS, every developer path on commonsclinic.com returns the WordPress 404 template, and the sole machine-readable artifacts on the host are a Rank Math generated /llms.txt and the stock WordPress core REST API at /wp-json/ (the one live subdomain, my.commonsclinic.com, is a noindex appointment-guide SPA whose catch-all answers 200 with the same HTML shell for /openapi.json and /.well-known/agent-card.json alike — not a contract).
  evidence:
  - status: 404
    url: https://commonsclinic.com/openapi.json
  - status: 404
    url: https://commonsclinic.com/developers
  - status: 404
    url: https://commonsclinic.com/.well-known/agent-card.json
  - status: 200
    url: https://commonsclinic.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: 'Commons Clinic is a Santa Monica, California physician-led specialty care group founded in 2021 that operates multi-specialty musculoskeletal clinics across Southern California — Santa Monica, Marina del Rey, Beverly Hills, Torrance, Westlake Village, Lakewood and two Long Beach sites — plus its own ambulatory surgery center, the Marina Orthopedic & Spine Institute. The group treats orthopedic, spine, sports medicine, joint replacement and chronic pain conditions with on-site imaging, physical and occupational therapy, injections and surgery under one roof, and has extended into a bundled preventive diagnostics program marketed as Wholebody. It is venture-backed and its stock trades on private secondary markets. Commons Clinic is a care delivery organization, not an API provider: it publishes no developer program, no API documentation, and no machine-readable API contract. The only machine-readable artifacts on its host are a Rank Math generated llms.txt and the stock WordPress
  core REST API behind its marketing site.'
image: https://commonsclinic.com/wp-content/uploads/2024/09/commonspreview-1024x425.jpg
layout: provider
modified: '2026-08-09'
name: Commons Clinic
nav: Providers
network: true
overview: 'Commons Clinic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Orthopedics, Spine, and Sports Medicine.


  Commons Clinic''s developer surface includes engineering blog and 14 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commons-clinic/refs/heads/main/screenshots/commons-clinic-2026-09-02T145126.png
security:
- kind: domain-security
  name: Commons Clinic Domain Security
  slug: commons-clinic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: commons-clinic
tags:
- Company
- Healthcare
- Orthopedics
- Spine
- Sports Medicine
- Musculoskeletal
- Physical Therapy
- Surgery
- Pain Management
- Preventive Health
- Clinics
website: https://commonsclinic.com/
---
