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
  url: security/nilo-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nilohealth.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://nilohealth.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://nilohealth.com/resources/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nilohealth.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.nilohealth.com/terms-of-use
- group: start
  title: ''
  type: Login
  url: https://app.nilohealth.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@nilohealth.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/nilo-health-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://nilohealth.com/trust/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nilo-health
created: '2026-07-17'
description: Nilo Health (nilo.health) is a Berlin-based employee mental health platform that helps businesses support their workforce's mental well-being. Founded in 2019 by Ines Raeth, Catalina Turlea and Jonas Keil, nilo gives teams access to 500+ psychologists for 1:1 video counseling in 50+ languages, alongside self-guided digital programs, group roundtables, and an HR analytics dashboard. It is delivered to employers as a company benefit (SaaS) rather than through a public developer API; there is no published developer portal, API reference, SDKs, or OpenAPI at this time. nilo integrates with HR platforms such as Personio and Lano via partner marketplaces, and publishes a trust center citing ISO/IEC 27001. The company is backed by Speedinvest and was added to the API Evangelist network as a Speedinvest portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nilo-health.png
layout: provider
modified: '2026-07-20'
name: Nilo Health
nav: Providers
network: true
overview: 'Nilo Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mental Health, Health, HR, and Employee Benefits.


  Nilo Health''s developer surface includes pricing, engineering blog, support, and 8 more developer resources.'
random_paper: 17
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
  delta: 0.0
  facets:
    access_clarity: 14.5
    commercial_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 7.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nilo-health/refs/heads/main/screenshots/nilo-health-2026-08-07T185301.png
security:
- kind: domain-security
  name: Nilo Health Domain Security
  slug: nilo-health-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Nilo Health Trust Center
  slug: nilo-health-trust-center
  summary_line: ISO/IEC 27001
slug: nilo-health
tags:
- Company
- Mental Health
- Health
- HR
- Employee Benefits
- Wellbeing
- Telehealth
- Software-as-a-Service
website: https://nilohealth.com/
---
