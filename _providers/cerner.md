---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cerner Agentic Access
  operation_count: 11
  slug: cerner-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 12
apis:
- description: The Cerner Millennium DSTU2 FHIR API supports legacy SMART on FHIR applications and integrations with Meaningful Use 2015 CEHRT certification criteria, and remains available alongside the newer R4 imp
  name: Oracle Health Millennium FHIR DSTU2 API
  slug: oracle-health-fhir-dstu2-api
- description: 'The Oracle Health Code Console (formerly Cerner Code) is the developer portal used to register SMART on FHIR and system-level applications, configure redirect URIs and launch parameters, manage OAuth '
  name: Oracle Health Code Console (Developer Portal)
  slug: oracle-health-code-console
- description: Oracle Health Millennium supports the HL7 Bulk Data Access (Flat FHIR) specification for exporting group-level patient data in NDJSON format for population health, research, and payer-provider data ex
  name: Oracle Health Millennium Bulk FHIR API
  slug: oracle-health-bulk-fhir-api
- description: Cerner CareAware provides device and third-party application integration APIs for medical device data capture, bi-directional HL7 v2 messaging, and workflow embedding into Millennium, supporting medic
  name: Cerner CareAware Integration APIs
  slug: cerner-careaware
- description: Oracle Health implements the SMART on FHIR App Launch framework (standalone and EHR-launch) with OpenID Connect identity tokens, enabling third-party clinician and patient-facing applications to embed
  name: Oracle Health SMART on FHIR App Launch
  slug: oracle-health-smart-on-fhir
- description: FHIR server metadata and capability statements.
  name: Cerner (Oracle Health) Capability API
  slug: cerner-capability-api
- description: Patient conditions and problem-list entries.
  name: Cerner (Oracle Health) Condition API
  slug: cerner-condition-api
- description: FHIR conformance definitions and operations.
  name: Cerner (Oracle Health) Definitions API
  slug: cerner-definitions-api
- description: Patient encounter records.
  name: Cerner (Oracle Health) Encounter API
  slug: cerner-encounter-api
- description: Generic FHIR resource read/write operations.
  name: Cerner (Oracle Health) Generic API
  slug: cerner-generic-api
- description: Patient demographics and identifiers.
  name: Cerner (Oracle Health) Patient API
  slug: cerner-patient-api
- description: Patient procedures.
  name: Cerner (Oracle Health) Procedure API
  slug: cerner-procedure-api
arazzos:
- description: Locate a patient, create a FHIR resource against that patient, then update it by id.
  name: Cerner Oracle Health Clinical Resource Write-Back
  slug: cerner-clinical-resource-write-workflow
- description: Read the server metadata and CapabilityStatement, then enumerate supported operations and structure definitions.
  name: Cerner Oracle Health Conformance Discovery
  slug: cerner-conformance-discovery-workflow
- description: Discover server capabilities, locate a patient, then pull the patient's conditions, encounters, and procedures.
  name: Cerner Oracle Health SMART on FHIR Patient Retrieval
  slug: cerner-smart-on-fhir-patient-data-retrieval-workflow
artifact_total: 25
collections:
- collection_type: open
  name: Oracle Health Millennium Platform FHIR R4 API
  slug: open-cerner-oracle-health-fhir-r4-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cerner-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cerner-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cerner-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cerner-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cerner-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cerner-corporation
- group: company
  title: ''
  type: Website
  url: https://www.cerner.com
- group: other
  title: ''
  type: Corporate
  url: https://www.oracle.com/health/
- group: other
  title: ''
  type: Developer
  url: https://www.oracle.com/health/developer/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/en/industries/health/millennium-platform-apis/index.html
- group: other
  title: ''
  type: FHIR
  url: https://fhir.cerner.com/
- group: start
  title: ''
  type: CodeConsole
  url: https://code.cerner.com/
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/cerner
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
created: '2026-03-23'
description: Cerner is a global healthcare technology company that designs and develops electronic health record (EHR) and health information technology solutions for hospitals, clinics, and integrated delivery networks. Cerner was acquired by Oracle in June 2022 and is now branded as Oracle Health, with the Cerner Millennium EHR platform's developer program operating as the Oracle Health Developer Program. Millennium exposes HL7 FHIR R4 and DSTU2 APIs, SMART on FHIR app launching, Bulk FHIR, the CareAware device and integration APIs, and the Code Console developer portal for registering applications and obtaining sandbox and production credentials.
finops:
- name: Cerner Finops
  service_category: API
  slug: cerner-finops
graphqls:
- description: Cerner Millennium, now operated as Oracle Health, exposes clinical and administrative data through HL7 FHIR R4 REST APIs. There is no native GraphQL endpoint offered by Oracle Health or the Cerner Mil
  name: Cerner (Oracle Health) GraphQL
  slug: cerner-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cerner.png
layout: provider
modified: '2026-05-30'
name: Cerner (Oracle Health)
nav: Providers
network: true
overview: 'Cerner (Oracle Health) publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Capability API, Condition API, Definitions API, and 4 more. Tagged areas include Cerner Millennium, Code Console, EHR, Electronic Health Records, and FHIR.


  Cerner (Oracle Health)''s developer surface includes authentication, API reference, and 12 more developer resources.'
plans:
- name: Cerner Plans Pricing
  plan_count: 3
  slug: cerner-plans-pricing
press:
- date: '2026-05-25'
  title: Oracle explores Cerner sale to fund AI expansion
  url: https://www.linkedin.com/posts/timlynott_healthtech-healthcareit-ehr-activity-7423118955730493440-4Eci
- date: '2026-05-25'
  title: Oracle Cerner signs AI contract with FDA focused on ...
  url: https://fedscoop.com/oracle-cerner-fda-ai-contract/
- date: '2026-05-25'
  title: Oracle Buys Cerner
  url: https://www.prnewswire.com/news-releases/oracle-buys-cerner-301448252.html
- date: '2026-05-25'
  title: Oracle to launch new AI-backed EHR in 2025
  url: https://www.healthcaredive.com/news/oracle-new-ai-backed-ehr-2025/731398/
- date: '2026-05-25'
  title: Oracle must stop kicking the Cerner can down the road— ...
  url: https://www.hfsresearch.com/research/oracle-kicking-cerner-decisive/
random_paper: 7
rate_limits:
- limit_count: 5
  name: Cerner Rate Limits
  slug: cerner-rate-limits
scopes:
- name: Cerner Scopes
  scope_count: 4
  slug: cerner-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 42.4
  delta: -4.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 63.4
    developer_ergonomics: 17.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cerner/refs/heads/main/screenshots/cerner-2026-06-20T174140.png
security:
- kind: authentication
  name: Cerner Authentication
  slug: cerner-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cerner Domain Security
  slug: cerner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cerner Trust Center
  slug: cerner-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FIPS 140
slug: cerner
tags:
- Cerner Millennium
- Code Console
- EHR
- Electronic Health Records
- FHIR
- HL7
- Healthcare
- Interoperability
- OAuth 2.0
- Oracle Health
- Patient Access
- Provider Directory
- SMART on FHIR
- Fortune 1000
website: https://www.cerner.com
---
