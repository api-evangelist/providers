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
api_count: 1
apis:
- description: apps.health is WELL Health's digital health marketplace through which third-party apps and services integrate with WELL's network of EMRs (OSCAR Pro, Profile), which support HL7 FHIR and other interop
  name: apps.health EMR Integration (FHIR)
  slug: apps-health-integration
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/well-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://well.company/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apps.health/for-developers
- group: docs
  title: ''
  type: Documentation
  url: https://apps.health/for-developers
- group: start
  title: ''
  type: GettingStarted
  url: https://apps.health/how-to-get-your-product-on-apps-health/
- group: design
  title: ''
  type: Conformance
  url: conformance/well-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/well-health-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://well.company/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://well.company/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apps.health/terms
- group: operate
  title: ''
  type: Support
  url: https://well.company/contact/
created: '2026-07-24'
description: 'WELL Health Technologies Corp (TSX: WELL, OTCQX: WHTCF) is a Vancouver, Canada-headquartered healthcare technology company that is Canada''s largest outpatient medical clinic owner-operator and a leading multi-disciplinary digital health service provider. It runs two synergistic channels: an omni-channel patient services business operating 115+ multidisciplinary clinics across Canada plus US telehealth and anesthesia operations, and a virtual-services / practitioner-enablement platform serving 44,000+ providers through the OSCAR Pro EMR, billing and revenue-cycle tools, eReferral, digital booking, and ePharma. Its programmatic surface is the apps.health marketplace, through which third-party digital health apps integrate with WELL''s network of EMRs (OSCAR Pro, Profile) using HL7 FHIR and other interoperability standards. As of this review WELL exposes no self-serve public developer portal, sandbox, OpenAPI, or FHIR CapabilityStatement; integration is FHIR-based but gated behind
  a partner/contact process. Home market is Canada, positioned in a province-fragmented healthcare landscape coordinated federally by Canada Health Infoway''s pan-Canadian FHIR (CA Core / CA Baseline) specifications.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: WELL Health Technologies
nav: Providers
network: true
overview: 'WELL Health Technologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Canada, EMR, EHR, and FHIR.


  WELL Health Technologies'' developer surface includes documentation, getting-started guide, engineering blog, support, and 7 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 24.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 41.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/well-health/refs/heads/main/screenshots/well-health-2026-09-02T170603.png
security:
- kind: domain-security
  name: Well Health Domain Security
  slug: well-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: well-health
tags:
- Healthcare
- Canada
- EMR
- EHR
- FHIR
- HL7
- Interoperability
- Digital Health
- Telehealth
- ePharma
- Clinics
website: https://well.company/
---
