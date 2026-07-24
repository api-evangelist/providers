---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Nhs Api Agentic Access
  operation_count: 53
  slug: nhs-api-agentic-access
  summary_line: 53 operations · 23 acting
api_count: 13
apis:
- description: Retrieve documents held at a patient's registered GP practice, such as letters, discharge summaries, and other clinical documents stored in GP systems. Used alongside the Access Record Structured API.
  name: GP Connect Access Document - FHIR API
  slug: gp-connect-access-document-fhir-api
- description: Real-time tracking of prescriptions within the Electronic Prescription Service. Enables authorised users to retrieve details about prescription status and dispensation progress without writing to EPS.
  name: EPS Prescription Tracker - FHIR API
  slug: eps-prescription-tracker-fhir-api
- description: Send booking and referral information between NHS service providers using the NHS Booking and Referral Standard (BaRS). Enables sharing of clinical and administrative data to support transfer of care.
  name: Booking and Referral - FHIR API
  slug: booking-and-referral-fhir-api
- description: Retrieve NHS-approved health information content (conditions, medicines, treatments, live well articles) for syndication into third-party apps and services. Returns structured content with HTML and me
  name: NHS Website Content API
  slug: nhs-website-content-api
- description: Access data from the NHS Waiting List Minimum Data Set (WLMDS), the national electronic database of NHS patient waiting list records. Supports performance monitoring and patient pathway management for
  name: Elective Waiting List API
  slug: elective-waiting-list-api
- description: The CodeSystem API from NHS API — 2 operation(s) for codesystem.
  name: NHS API CodeSystem API
  slug: nhs-api-codesystem-api
- description: The List{id} API from NHS API — 1 operation(s) for list{id}.
  name: NHS API List{id} API
  slug: nhs-api-list-id-api
- description: The Metadata API from NHS API — 1 operation(s) for metadata.
  name: NHS API Metadata API
  slug: nhs-api-metadata-api
- description: The Organization API from NHS API — 2 operation(s) for organization.
  name: NHS API Organization API
  slug: nhs-api-organization-api
- description: The OrganizationAffiliation API from NHS API — 2 operation(s) for organizationaffiliation.
  name: NHS API OrganizationAffiliation API
  slug: nhs-api-organizationaffiliation-api
- description: The R4 API from NHS API — 6 operation(s) for r4.
  name: NHS API R4 API
  slug: nhs-api-r4-api
- description: The STU3 API from NHS API — 32 operation(s) for stu3.
  name: NHS API STU3 API
  slug: nhs-api-stu3-api
- description: The ValueSet API from NHS API — 2 operation(s) for valueset.
  name: NHS API ValueSet API
  slug: nhs-api-valueset-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nhs-api-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nhs-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nhs-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nhs-api-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://digital.nhs.uk/developer
- group: other
  title: ''
  type: APICatalogue
  url: https://digital.nhs.uk/developer/api-catalogue
- group: docs
  title: ''
  type: Documentation
  url: https://digital.nhs.uk/developer/guides-and-documentation
- group: auth
  title: ''
  type: Authentication
  url: https://digital.nhs.uk/developer/guides-and-documentation/security-and-authorisation
- group: start
  title: ''
  type: GettingStarted
  url: https://digital.nhs.uk/developer/guides-and-documentation/onboarding-process
- group: other
  title: ''
  type: DigitalAssurance
  url: https://digital.nhs.uk/developer/assurance/digital-assurance-for-apis-and-services
- group: operate
  title: ''
  type: Community
  url: https://developer.community.nhs.uk/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/NHSDigital
- group: other
  title: ''
  type: APIPolicies
  url: https://digital.nhs.uk/developer/guides-and-documentation/api-policies-and-best-practice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onboarding.prod.api.platform.nhs.uk/PolicyPages/TermsOfUsePolicy
- group: operate
  title: ''
  type: Status
  url: https://status.digital.nhs.uk/
- group: operate
  title: ''
  type: RateLimits
  url: /rate-limits/nhs-api-rate-limits.md
- group: commercial
  title: ''
  type: Plans
  url: /plans/nhs-api-plans.md
- group: commercial
  title: ''
  type: FinOps
  url: /finops/nhs-api-finops.md
created: '2026-06-13'
description: NHS England's API management platform provides FHIR R4 and REST APIs for healthcare interoperability across the NHS. The platform covers GP Connect (appointment management and access record), Personal Demographics Service, Electronic Prescription Service, Summary Care Records, NHS login (OpenID Connect for citizens), Booking and Referral, Organisation Data Service, and content syndication. APIs are managed via NHS England's Apigee-based API platform and are targeted at system suppliers, NHS organisations, and accredited third-party healthcare application developers.
examples:
- key_count: 7
  name: E Referral Worklist Response
  slug: e-referral-worklist-response
- key_count: 7
  name: Organisation Search Response
  slug: organisation-search-response
- key_count: 10
  name: Patient Demographics Response
  slug: patient-demographics-response
image: https://digital.nhs.uk/svg/nhs-logo.svg
json_schemas:
- name: NHS Organisation (ODS FHIR R4)
  property_count: 10
  slug: nhs-organisation
- name: NHS Patient Demographics (PDS FHIR R4)
  property_count: 12
  slug: nhs-patient-demographics
jsonld:
- class_count: 0
  name: Nhs Api Context
  property_count: 0
  slug: nhs-api
layout: provider
modified: '2026-06-13'
name: NHS API
nav: Providers
network: true
overview: 'NHS API publishes 8 APIs on the [APIs.io](https://apis.io/) network, including CodeSystem API, List{id} API, Metadata API, and 5 more. Tagged areas include Healthcare, FHIR, NHS, UK, and HL7.


  The NHS API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NHS API''s developer surface includes authentication, developer portal, documentation, getting-started guide, status page, and 13 more developer resources.'
random_paper: 25
rules:
- name: NHS API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nhs-api-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.8
  delta: 2.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 52.9
    developer_ergonomics: 43.5
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 5.3
  previous_composite: 43.6
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 58.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Nhs Api Authentication
  slug: nhs-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nhs Api Domain Security
  slug: nhs-api-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Nhs Api Vulnerability Disclosure
  slug: nhs-api-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: nhs-api
tags:
- Healthcare
- FHIR
- NHS
- UK
- HL7
- Electronic Prescriptions
- Patient Demographics
- GP Connect
- NHS Login
- Interoperability
website: https://digital.nhs.uk/developer
---
