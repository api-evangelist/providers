---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    error_semantics: documented
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
  score: 6.3
  scored_at: '2026-09-05'
api_count: 5
apis:
- baseURL: https://api.fhir.nhsd.healthdirect.org.au/v4
  baseurl_source: declared
  description: Real-time, read-only HL7 FHIR API over the National Health Services Directory, aligned to the HL7 AU Provider Directory (AU-PD) implementation guide. Supports querying Organization, HealthcareService,
  name: NHSD FHIR API
  slug: nhsd-fhir-api
- description: Read-only HL7 FHIR bulk data export for retrieving large NHSD datasets at a specified frequency, for integrators that need the full directory rather than real-time single-record lookups.
  name: NHSD FHIR Bulk Data Export
  slug: nhsd-fhir-bulk-data-export
- description: HL7 FHIR write/inbound interface for approved data-contributing sources to submit and maintain health service and practitioner records in the National Health Services Directory.
  name: NHSD FHIR Ingestion & Data Acquisition Hub
  slug: nhsd-ingestion-hub
- description: API that surfaces real-time appointment availability and booking integration from certified provider booking platforms (AutoMed, HealthEngine, HotDoc, MedAdvisor, Medi2Apps) within the National Health
  name: NHSD Provider Appointments API
  slug: nhsd-provider-appointments-api
- description: Embeddable, responsive NHSD search component that third parties can deploy on websites and mobile apps to let consumers find health services and practitioners, backed by the National Health Services D
  name: NHSD Search Widget
  slug: nhsd-widget
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/healthdirect-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthdirect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://about.healthdirect.gov.au/
- group: company
  title: ''
  type: ConsumerWebsite
  url: https://www.healthdirect.gov.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://about.healthdirect.gov.au/what-we-do/portfolio/nhsd/integration-hub
- group: docs
  title: ''
  type: Documentation
  url: https://about.healthdirect.gov.au/what-we-do/portfolio/nhsd/integration-hub/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://build.fhir.nhsd.healthdirect.org.au/v4/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://about.healthdirect.gov.au/what-we-do/portfolio/nhsd/integration-hub/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://healthdirect-serviceline.atlassian.net/servicedesk/customer/portal/3/group/12/create/44
- group: operate
  title: ''
  type: Support
  url: https://about.healthdirect.gov.au/what-we-do/portfolio/nhsd/integration-hub/technical-support
- group: company
  title: ''
  type: Blog
  url: https://about.healthdirect.gov.au/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/healthdirect-australia
- group: commercial
  title: ''
  type: TermsOfService
  url: https://about.healthdirect.gov.au/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.healthdirect.gov.au/privacy-policy
- group: build
  title: ''
  type: PostmanCollection
  url: collections/nhsd-developers-portal.postman_collection.json
- group: auth
  title: ''
  type: Security
  url: https://www.healthdirect.gov.au/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/healthdirect-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/healthdirect-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/healthdirect-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/healthdirect-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/healthdirect-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/healthdirect-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/healthdirect-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://about.healthdirect.gov.au/what-we-do/portfolio/nhsd/integration-hub/standards
- group: design
  title: ''
  type: DataModel
  url: data-model/healthdirect-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/healthdirect-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/healthdirect-components.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/healthdirect-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/healthdirect-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-24'
description: Healthdirect Australia is a national, government-owned, not-for-profit organisation that operates core Australian digital-health infrastructure and consumer health services on behalf of the Commonwealth, states, and territories. It runs the free healthdirect symptom checker and health advice service and, most relevant to developers, delivers the National Health Services Directory (NHSD) — the authoritative national directory of health services and practitioners, covering more than 400,000 service and practitioner records. Healthdirect exposes the NHSD to government, commercial, and clinical software developers through standards-based HL7 FHIR APIs (aligned to the HL7 AU Provider Directory / AU-PD implementation guide, using SNOMED CT-AU terminology and G-NAF geocoded addresses), a FHIR bulk data export, a FHIR ingestion/data-acquisition hub for contributing sources, an embeddable NHSD search widget, and a Provider Appointments API that surfaces real-time appointment availability
  from certified booking platforms. Integration is gated behind a formal onboarding and test-environment registration process, and APIs are secured with OAuth 2.0 client-credentials plus an API key. Home market is Australia.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24T18:00:00Z'
name: Healthdirect Australia
nav: Providers
network: true
overview: 'Healthdirect Australia publishes 1 API on the [APIs.io](https://apis.io/) network: NHSD FHIR API. Tagged areas include Healthcare, Australia, FHIR, HL7, and Interoperability.


  Healthdirect Australia''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 23 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 70.8
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 38.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthdirect/refs/heads/main/screenshots/healthdirect-2026-07-25T220837.png
security:
- kind: authentication
  name: Healthdirect Authentication
  slug: healthdirect-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Healthdirect Domain Security
  slug: healthdirect-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Healthdirect Vulnerability Disclosure
  slug: healthdirect-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: healthdirect
tags:
- Healthcare
- Australia
- FHIR
- HL7
- Interoperability
- Provider Directory
- National Health System
- Health Services Directory
- Telehealth
- Digital Health
- Appointments
website: https://about.healthdirect.gov.au/
---
