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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buildcheck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildcheck.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://buildcheck.com/#priser
- group: start
  title: ''
  type: SignUp
  url: https://app.buildcheck.com/login?mode=register
- group: start
  title: ''
  type: Login
  url: https://app.buildcheck.com/
created: '2026-07-17'
description: Buildcheck is a Sweden-based cloud software platform that simplifies self-inspections and quality checklists for construction and infrastructure projects. The service uses AI to automatically generate project-specific inspection and control plans from uploaded building documents, then lets field teams document work on a mobile app with photo capture and digital signatures, share progress with clients through shareable links, and export organized PDF reports. It offers company-branded templates, role-based access, SSO and other enterprise features. Buildcheck was founded by Anders Jacobson (previously Next One Technology) and Johnny Wulcan (founder of Byggplanen). It is surfaced in the API Evangelist network as a company profile; no public developer API or API documentation has been found on its site as of this enrichment pass.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buildcheck.png
layout: provider
modified: '2026-07-18'
name: Buildcheck
nav: Providers
network: true
overview: 'Buildcheck is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, ConTech, Inspection, and Quality Assurance.


  Buildcheck''s developer surface includes pricing, signup flow, and 3 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buildcheck/refs/heads/main/screenshots/buildcheck-2026-07-25T204045.png
security:
- kind: domain-security
  name: Buildcheck Domain Security
  slug: buildcheck-domain-security
  summary_line: TLSv1.3
slug: buildcheck
tags:
- Company
- Construction
- ConTech
- Inspection
- Quality Assurance
- Field Service
- Checklists
- Software-as-a-Service
- Artificial Intelligence
- Sweden
website: https://buildcheck.com/
---
