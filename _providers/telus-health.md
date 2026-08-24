---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: GraphQL API for the TELUS Collaborative Health Record (CHR) that lets partners build integrations against clinic data. Queries retrieve and mutations create or update CHR records (patients, appointmen
  name: TELUS CHR Enterprise API
  slug: telus-chr-enterprise-api
- description: TELUS Patient Chart FHIR R4 implementation guide, published by TELUS, containing 89 StructureDefinition profiles and extensions under the http://telus.com/fhir/patientChart canonical. Profiles cover p
  name: TELUS Patient Chart FHIR API
  slug: telus-patient-chart-fhir-api
artifact_total: 5
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
mcp_servers:
- description: ''
  name: TELUS Health MCP Server
  slug: telus-health-mcp-server
modified: '2026-07-24'
name: TELUS Health
nav: Providers
network: true
overview: 'TELUS Health publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Canada, EMR, EHR, and FHIR.


  TELUS Health''s developer surface includes documentation, API reference, getting-started guide, authentication, and 12 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 28.8
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 38.9
    developer_ergonomics: 44.6
    discoverability: 77.8
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 28.8
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
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
