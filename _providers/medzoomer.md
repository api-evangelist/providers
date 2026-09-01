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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://medzoomer.com/
- group: start
  title: ''
  type: Portal
  url: https://pharmacy.medzoomer.com/login
- group: start
  title: ''
  type: Login
  url: https://pharmacy.medzoomer.com/login
- group: operate
  title: ''
  type: Support
  url: https://medzoomer.com/get-help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://medzoomer.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://medzoomer.com/terms-of-use/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medzoomer-domain-security.yml
created: '2026-07-17'
description: Medzoomer is an on-demand prescription delivery platform that connects pharmacies, healthcare providers, and patients through a secure, HIPAA-compliant network of verified couriers. Founded in 2019 and headquartered in Tampa, Florida, the company handles last-mile medication logistics, including controlled substances (Schedule II-V), with tamper-evident packaging, FDA/TSA-approved envelopes, and real-time order tracking. Pharmacies and couriers operate through dedicated web and mobile applications, and the platform is backed by Techstars, UnitedHealthcare Accelerator, and other investors. Medzoomer operates a private pharmacy integration API but publishes no public developer documentation, SDKs, or OpenAPI at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medzoomer.png
layout: provider
modified: '2026-07-20'
name: Medzoomer
nav: Providers
network: true
overview: 'Medzoomer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmacy, Prescription Delivery, Healthcare, and Logistics.


  Medzoomer''s developer surface includes developer portal, support, and 5 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medzoomer/refs/heads/main/screenshots/medzoomer-2026-08-07T172416.png
security:
- kind: domain-security
  name: Medzoomer Domain Security
  slug: medzoomer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: medzoomer
tags:
- Company
- Pharmacy
- Prescription Delivery
- Healthcare
- Logistics
- Last Mile Delivery
- Couriers
- HIPAA
website: https://medzoomer.com/
---
