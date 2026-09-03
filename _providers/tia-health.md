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
  url: security/tia-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tiahealth.com/
- group: company
  title: ''
  type: About
  url: https://tiahealth.com/about/
- group: company
  title: ''
  type: Blog
  url: https://tiahealth.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://tiahealth.com/support/
- group: operate
  title: ''
  type: Contact
  url: https://tiahealth.com/contact/
- group: start
  title: ''
  type: Login
  url: https://app.tiahealth.com/auth/login/tiaHealth;patientLogin=true
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tiahealth.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tiahealth.com/tia-privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://tiahealth.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://book.tiahealth.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tia-health-llms.txt
created: '2026-07-24'
description: Tia Health is a Canadian telehealth platform that connects patients with licensed Canadian providers - family doctors, nurse practitioners, specialists, and naturopaths - for on-demand virtual care by phone, video, and secure messaging. Its services span virtual walk-in and family-practice appointments, prescription renewals, sick notes, lab requisitions, and mental health therapy (via partner Focus Mental Wellness), with visits covered by provincial health plans in Ontario (OHIP), British Columbia (MSP), and Alberta (AHCIP) and paid options elsewhere. Tia Health is part of the WELL Health Technologies Corp. clinic network, one of the largest outpatient networks in Canada. As of this review Tia Health is a consumer-facing virtual-care product with no public developer portal, no documented REST/OpenAPI, and no exposed HL7 FHIR CapabilityStatement or SMART-on-FHIR configuration; interoperability in the Canadian market is stewarded federally through Canada Health Infoway's pan-Canadian
  FHIR (CA Core / CA Baseline) specifications, which this platform does not publicly surface.
image: https://tiahealth.com/wp-content/uploads/2020/11/Tia-Health-RGB-Colour.png
layout: provider
modified: '2026-07-24'
name: Tia Health
nav: Providers
network: true
overview: 'Tia Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Canada, Telehealth, Virtual Care, and Digital Health.


  Tia Health''s developer surface includes engineering blog, support, pricing, signup flow, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tia-health/refs/heads/main/screenshots/tia-health-2026-09-02T163658.png
security:
- kind: domain-security
  name: Tia Health Domain Security
  slug: tia-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tia-health
tags:
- Healthcare
- Canada
- Telehealth
- Virtual Care
- Digital Health
- Primary Care
- Mental Health
- Prescriptions
website: https://tiahealth.com/
---
