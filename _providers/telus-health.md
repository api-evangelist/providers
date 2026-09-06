---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: GraphQL API for the TELUS Collaborative Health Record (CHR) that lets partners build integrations against clinic data. Queries retrieve and mutations create or update CHR records (patients, appointmen
  name: TELUS CHR Enterprise API
  slug: telus-chr-enterprise-api
- description: TELUS Patient Chart FHIR R4 implementation guide, published by TELUS, containing 89 StructureDefinition profiles and extensions under the http://telus.com/fhir/patientChart canonical. Profiles cover p
  name: TELUS Patient Chart FHIR API
  slug: telus-patient-chart-fhir-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telus-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.telus.com/en/health
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.inputhealth.com/en/articles/6483215-chr-enterprise-api
- group: docs
  title: ''
  type: Documentation
  url: https://help.inputhealth.com/en/articles/6483215-chr-enterprise-api
- group: docs
  title: ''
  type: APIReference
  url: http://apidocs.inputhealth.com/voyager.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.inputhealth.com/en/articles/6368814-enterprise-api-onboarding-overview
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telus-health
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/telus-health-chr
- group: auth
  title: ''
  type: Authentication
  url: authentication/telus-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/telus-health-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/telus-health-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/telus-health-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/telus-health-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/telus-health-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/telus-health-llms.txt
created: '2026-07-24'
description: TELUS Health is the digital-health division of TELUS, one of Canada's largest telecommunications and technology companies, and the country's leading health-IT provider. It operates the PS Suite, Med Access, and cloud-native Collaborative Health Record (CHR) electronic medical records used across Canadian primary care, along with pharmacy management, virtual care, and employer/benefits health services. Its documented public integration surface is the CHR Enterprise API, a GraphQL endpoint secured with RS512-signed JWT bearer tokens that exposes clinic data (patients, appointments, encounters, clinical documents and more) for partner-built add-ons, complemented by the TELUS Patient Chart FHIR R4 implementation guide, a package of 89 published StructureDefinition profiles under the http://telus.com/fhir/patientChart canonical for standards-based patient-record exchange out of TELUS EMRs, and the Omara Health Exchange FHIR interoperability platform. Home market is Canada, where
  healthcare is province-fragmented and FHIR interoperability is stewarded federally by Canada Health Infoway. Both API surfaces are documented but gated behind a partner or CHR-domain agreement.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: TELUS Health
nav: Providers
network: true
overview: 'TELUS Health publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Canada, EMR, EHR, and FHIR.


  TELUS Health''s developer surface includes documentation, API reference, getting-started guide, authentication, and 12 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 37.2
    developer_ergonomics: 51.8
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 28.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telus-health/refs/heads/main/screenshots/telus-health-2026-09-02T162751.png
security:
- kind: authentication
  name: Telus Health Authentication
  slug: telus-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Telus Health Domain Security
  slug: telus-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: telus-health
tags:
- Healthcare
- Canada
- EMR
- EHR
- FHIR
- HL7
- Interoperability
- GraphQL
- e-Prescribing
- Pharmacy
- Digital Health
- Clinical Data
website: https://www.telus.com/en/health
---
