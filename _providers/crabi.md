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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crabi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crabi.com
- group: start
  title: ''
  type: SignUp
  url: https://cotizador.crabi.com/quoter/contract/data/vehicle-info
- group: start
  title: ''
  type: Login
  url: https://login.crabi.com/log-in
- group: operate
  title: ''
  type: Support
  url: https://crabi.com/preguntas-frecuentes
- group: company
  title: ''
  type: Blog
  url: https://crabi.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crabi.com/legal/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crabi.com/avisodeprivacidad
created: '2026-07-17'
description: Crabi is a Mexican digital auto-insurance company (insurtech) offering fully online vehicle policies purchasable in about fifteen minutes from a mobile device. Coverage spans material damage, theft, third-party civil liability, medical expenses, and roadside and legal assistance across 27 Mexican states, sold and serviced through its mobile apps, online quoter (cotizador), and customer login portal. The company is regulated in Mexico by the CNSF and CONDUSEF and is a portfolio company of 500 Global. Crabi publishes no public developer API, documentation, or SDKs; this profile captures its identity and public web surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crabi.png
layout: provider
modified: '2026-07-18'
name: Crabi
nav: Providers
network: true
overview: 'Crabi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Auto Insurance, and Mexico.


  Crabi''s developer surface includes signup flow, support, engineering blog, and 5 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crabi/refs/heads/main/screenshots/crabi-2026-07-25T210628.png
security:
- kind: domain-security
  name: Crabi Domain Security
  slug: crabi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crabi
tags:
- Company
- Insurance
- Insurtech
- Auto Insurance
- Mexico
- Financial-Services
- Fintech
- Mobile
website: https://crabi.com
---
