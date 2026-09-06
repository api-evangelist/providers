---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spencer-health-solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spencerhealthsolutions.com/
- group: company
  title: ''
  type: Blog
  url: https://spencerhealthsolutions.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://spencerhealthsolutions.com/feed/
- group: company
  title: ''
  type: News
  url: https://spencerhealthsolutions.com/in-the-news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spencerhealthsolutions.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://spencerhealthsolutions.com/cookie-policy/
- group: operate
  title: ''
  type: Support
  url: https://helloimspencer.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://careers.smartrecruiters.com/SpencerHealthSolutions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spencerhealth
- group: company
  title: ''
  type: Twitter
  url: https://x.com/spencerhealth
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC59gkouh9OXcZYtEBfQMnDA
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/spencerhealthsolutions
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/spencerhealthsolutions
- group: build
  title: ''
  type: Packages
  url: packages/spencer-health-solutions-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spencer-health-solutions-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://spencerhealthsolutions.com/platform/certifications-compliance-and-data-standards/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spencer-health-solutions-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/spencer-health-solutions-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spencer-health-solutions-rate-limits.yml
coverage:
  checked: '2026-08-28'
  detail: Spencer Health Solutions ships a physical medication dispenser plus two managed front-ends (spencerAssist app, spencerCare portal) and no developer surface at all — Certificate Transparency for spencerhealthsolutions.com lists only blog., email., go. and www., so no api., docs., developer. or portal. host has ever existed, and the company has no GitHub organization and zero public Bitbucket repositories.
  evidence:
  - status: 200
    url: https://api.certspotter.com/v1/issuances?domain=spencerhealthsolutions.com&include_subdomains=true
  - status: 200
    url: https://api.github.com/search/users?q=spencer+health+solutions
  - status: 200
    url: https://api.bitbucket.org/2.0/repositories/spencerhealthsolutions
  - status: 202
    url: https://spencerhealthsolutions.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-28'
description: Spencer Health Solutions is a Morrisville, North Carolina medical device and digital health company behind spencer®, an in-home smart medication dispenser that combines automated multi-dose dispensing from pharmacy-prepared refills with telehealth, patient surveys and connected Bluetooth biometric devices. The spencer platform pairs the countertop device with spencerAssist®, a mobile app for patients and caregivers, and spencerCare™, a web portal that lets healthcare professionals run real-time alerts, telehealth visits and longitudinal real-world data collection. The company sells into three markets — care management for home care and senior living, patient support programs for pharmaceutical manufacturers, and decentralized clinical trials, where the spencer SmartHub™ serves as the in-home trial partner — and reports a 97% medication adherence rate across more than 5,800 patients in the United States, Canada and Europe. Spencer Health Solutions publishes no public developer
  program, API reference or machine-readable contract; the platform is delivered as a managed device and portal offering through direct commercial and partner agreements, including a 2025 partnership with PharMerica.
image: https://spencerhealthsolutions.com/wp-content/uploads/2024/10/getsitelogo.png
layout: provider
modified: '2026-08-28'
name: Spencer Health Solutions
nav: Providers
network: true
overview: 'Spencer Health Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Medication Management, and Medication Adherence.


  Spencer Health Solutions'' developer surface includes engineering blog, product news, support, YouTube channel, and 16 more developer resources.'
plans:
- name: Spencer Health Solutions Plans Pricing
  plan_count: 0
  slug: spencer-health-solutions-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Spencer Health Solutions Rate Limits
  slug: spencer-health-solutions-rate-limits
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spencer-health-solutions/refs/heads/main/screenshots/spencer-health-solutions-2026-09-02T160411.png
security:
- kind: domain-security
  name: Spencer Health Solutions Domain Security
  slug: spencer-health-solutions-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spencer-health-solutions
tags:
- Company
- Health
- Healthcare
- Medication Management
- Medication Adherence
- Medical Devices
- Digital Health
- Telehealth
- Remote Patient Monitoring
- Clinical Trials
- Patient Engagement
- Care Management
- Real-World Data
website: https://spencerhealthsolutions.com/
---
