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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vori-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vori-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.vorihealth.com/
- group: company
  title: ''
  type: About
  url: https://www.vorihealth.com/about
- group: operate
  title: ''
  type: Support
  url: https://www.vorihealth.com/faq
- group: company
  title: ''
  type: Blog
  url: https://www.vorihealth.com/resources
- group: start
  title: ''
  type: Login
  url: https://app.vorihealth.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vorihealth.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vorihealth.com/legal/privacy-policy
- group: other
  title: ''
  type: x-MobileApp
  url: https://apps.apple.com/us/app/vori-health/id1534621456
- group: other
  title: ''
  type: x-MobileApp
  url: https://play.google.com/store/apps/details?id=com.voyahealth.app
- group: company
  title: ''
  type: Careers
  url: https://www.vorihealth.com/careers
- group: operate
  title: ''
  type: PressReleases
  url: https://www.vorihealth.com/press
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vori-health
coverage:
  checked: '2026-09-04'
  detail: 'Vori Health is a licensed medical practice that ships real software — iOS, Android and web patient apps — but no developer program of any kind: its only API host, api.vorihealth.com (an AWS API Gateway at d-n836o9gegb.execute-api.us-east-1.amazonaws.com), returns the same 403 {"message":"Missing Authentication Token"} for /openapi.json, /graphql, /fhir/metadata, every /.well-known/ path and a nonsense control path alike, all 230 URLs in the company sitemap are clinical or marketing pages with no /developers, /api or /docs entry, app.vorihealth.com is an Angular SPA that answers 200 with the same HTML shell for every path, and github.com/vorihealth and github.com/vori-health both 404.'
  evidence:
  - status: 403
    url: https://api.vorihealth.com/openapi.json
  - status: 403
    url: https://api.vorihealth.com/zzz-nonexistent-control-9f3a
  - status: 404
    url: https://www.vorihealth.com/openapi.json
  - status: 404
    url: https://www.vorihealth.com/.well-known/agent-card.json
  - status: 404
    url: https://www.vorihealth.com/llms.txt
  - status: 404
    url: https://github.com/vorihealth
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: Vori Health is a nationwide, virtual-first musculoskeletal (MSK) medical practice headquartered in Nashville, Tennessee and founded in 2020 by neurosurgeon Dr. Ryan Grant (co-founder and CEO) and orthopedic surgeon Dr. Mary O'Connor (co-founder and Chief Medical Officer), formerly chair of orthopedics at Mayo Clinic in Florida. It treats back, neck and joint pain through physician-led, integrated care teams that pair board-certified physiatrists licensed in all 50 states with physical therapists, registered dietitians and health coaches, delivered virtually and in person through a patient mobile and web application, and sold to employers, health plans, benefits consultants and risk-bearing provider groups as a value-based alternative to surgery-first MSK care. The company raised a $53M Series B led by NEA with AlleyCorp, Intermountain Ventures, Echo Health Ventures and Max Ventures participating, and partners with payers and enablers including Humana, Pearl Health, Allstate
  Benefits, Marpai, Contigo Health, WholeHealth Living, Firefly Health and Ophelia.
image: https://cdn.prod.website-files.com/607dd1658eb71ebcf9c05549/60833690431161c82dac845c_webclip-256x256.png
layout: provider
modified: '2026-09-04'
name: Vori Health
nav: Providers
network: true
overview: 'Vori Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Digital Health, Musculoskeletal, and Telehealth.


  Vori Health''s developer surface includes support, engineering blog, and 12 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Vori Health Domain Security
  slug: vori-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vori-health
tags:
- Company
- Health Care
- Digital Health
- Musculoskeletal
- Telehealth
- Virtual Care
- Physical Therapy
- Orthopedics
- Employer Benefits
- Value-Based Care
- United States
website: https://www.vorihealth.com/
---
