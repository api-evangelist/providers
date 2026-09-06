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
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/disclo-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/disclo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.disclo.com/
- group: company
  title: ''
  type: Website
  url: https://www.disclo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.disclo.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.disclo.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.disclo.com/privacy
- group: start
  title: ''
  type: Login
  url: https://secure.disclo.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.disclo.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.disclo.com/resources
created: '2026-07-17'
description: Disclo is a workplace-accommodations software platform that powers end-to-end management of ADA, FMLA, and state-leave requests, medical-certification verification, and the interactive accommodation process for employers. The HIPAA- and SOC 2-compliant portal automates accommodation workflows and compliance documentation, adds AI-assisted medical-certification review (Disclo Verify) and candidate accommodations for recruiting (Disclo Hire), and integrates with 50+ HRIS and ATS systems. Disclo is a private B2B SaaS company backed by Bain Capital Ventures and General Catalyst; it operates a secure customer portal (secure.disclo.com) and does not currently publish a public developer API, SDKs, or OpenAPI. Access is enterprise, demo/sales-led rather than self-serve.
image: https://www.disclo.com/favicon.png
layout: provider
modified: '2026-07-18'
name: Disclo
nav: Providers
network: true
overview: 'Disclo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workplace Accommodations, Disability, HR Tech, and ADA Compliance.


  Disclo''s developer surface includes pricing, support, engineering blog, and 7 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/disclo/refs/heads/main/screenshots/disclo-2026-07-25T212055.png
security:
- kind: domain-security
  name: Disclo Domain Security
  slug: disclo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Disclo Trust Center
  slug: disclo-trust-center
  summary_line: SOC 2, HIPAA
slug: disclo
tags:
- Company
- Workplace Accommodations
- Disability
- HR Tech
- ADA Compliance
- FMLA
- Leave Management
- Medical Certification
- HRIS Integration
- Health Data
website: https://www.disclo.com/
---
