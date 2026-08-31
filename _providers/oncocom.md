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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oncocom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onco.com
- group: company
  title: ''
  type: Blog
  url: https://blog.onco.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onco.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onco.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://onco.com/contact-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oncocom-llms.txt
created: '2026-07-17'
description: Onco.com is a comprehensive cancer care platform operated by Apollo Hospitals Enterprise Ltd that connects cancer patients across India with oncologists and treatment services. The platform offers priority expert oncology consultations, pan-India cancer medicine delivery at discounted rates, diagnostic testing and imaging, curated treatment packages with negotiated hospital rates, and the CanWin peer support group for survivors and caregivers. Onco.com reports a network of 400+ oncologists and 23+ treatment centers, having served more than 100,000 patients. It also publishes extensive patient-education content covering many cancer types (breast, lung, blood, prostate, colon, and others) through its About Cancer library and blog. This profile was surfaced as an Accel portfolio company; the platform is consumer/patient facing and does not publish a public developer API, developer portal, or machine-readable API specification.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oncocom.png
layout: provider
modified: '2026-07-20'
name: Onco.com
nav: Providers
network: true
overview: 'Onco.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Oncology, Cancer Care, and Telehealth.


  Onco.com''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oncocom/refs/heads/main/screenshots/oncocom-2026-08-07T190224.png
security:
- kind: domain-security
  name: Oncocom Domain Security
  slug: oncocom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oncocom
tags:
- Company
- Healthcare
- Oncology
- Cancer Care
- Telehealth
- Patient Support
- Diagnostics
- India
website: https://onco.com
---
