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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/betternight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betternight.com/
- group: company
  title: ''
  type: Blog
  url: https://betternight.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://betternight.com/news?format=rss
- group: operate
  title: ''
  type: Support
  url: https://www.support.betternight.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betternight.com/privacy-policy
- group: operate
  title: ''
  type: ContactUs
  url: https://betternight.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://betternight.com/careers
- group: other
  title: ''
  type: Locations
  url: https://betternight.com/locations
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/betternight/
- group: start
  title: ''
  type: PatientPortal
  url: https://sleep.betternight.com/signin
- group: auth
  title: ''
  type: Compliance
  url: https://betternight.com/news/betternight-achieves-soc-2-certification-to-demonstrate-our-commitment-to-security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/betternight-llms.txt
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/betternight_stock/
coverage:
  checked: '2026-08-07'
  detail: BetterNight is a virtual-care sleep clinic and DME operator whose only software surfaces are two robots-disallowed single-page login apps (sleep. and admin. betternight.com) that answer HTTP 200 with the identical 63KB HTML shell for every path including /openapi.json and /.well-known/agent-card.json; the marketing site is Squarespace with no /developers, /api, or docs subdomain in DNS.
  evidence:
  - status: 404
    url: https://betternight.com/developers
  - status: 404
    url: https://betternight.com/api
  - status: 404
    url: https://betternight.com/llms.txt
  - status: 404
    url: https://betternight.com/.well-known/agent-card.json
  - status: 200
    url: https://sleep.betternight.com/openapi.json
  - status: 200
    url: https://sleep.betternight.com/robots.txt
  - status: 200
    url: https://admin.betternight.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: 'BetterNight is a San Diego, California virtual-care sleep health company that diagnoses and treats obstructive sleep apnea end to end: telemedicine consults with sleep physicians, home sleep testing devices shipped to the patient, board-certified interpretation and therapy recommendation, home delivery of PAP and oral appliance therapy, and ongoing coaching by sleep specialists and respiratory therapists. It also offers a cognitive behavioral therapy program for insomnia and remote patient monitoring of PAP adherence. The company sells to individuals as well as to physicians, cardiologists, ENT practices, clinics, health plans and ACOs, employers, and DOT/commercial transportation programs. It reports roughly 300 sleep health professionals, Joint Commission accreditation held for over 15 years, and SOC 2 Type II compliance, and in 2026 acquired Coastal Sleep Diagnostics and Epoch Sleep Centers. BetterNight is a healthcare services operator, not an API platform: it publishes
  no developer program, API documentation, or machine-readable specification.'
image: https://static1.squarespace.com/static/5de55dfd24b1dd71d89c17f4/t/646ba565a803c661e2f30a09/1684776297362/BN_Social-Preview_2023.jpg?format=1500w
layout: provider
modified: '2026-08-07'
name: BetterNight
nav: Providers
network: true
overview: 'BetterNight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Telehealth, and Sleep Health.


  BetterNight''s developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/betternight/refs/heads/main/screenshots/betternight-2026-08-07T162341.png
security:
- kind: domain-security
  name: Betternight Domain Security
  slug: betternight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: betternight
tags:
- Company
- Health
- Digital Health
- Telehealth
- Sleep Health
- Sleep Apnea
- Remote Patient Monitoring
- Medical Devices
- Virtual Care
website: https://betternight.com/
---
