---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 4
  human_in_the_loop: 0
  name: Health Gorilla Agentic Access
  operation_count: 22
  slug: health-gorilla-agentic-access
  summary_line: 22 operations · 4 acting
api_count: 10
apis:
- description: Raw clinical document content.
  name: Health Gorilla Binary API
  slug: health-gorilla-binary-api
- description: FHIR server capability discovery.
  name: Health Gorilla CapabilityStatement API
  slug: health-gorilla-capabilitystatement-api
- description: Patient insurance coverage / eligibility.
  name: Health Gorilla Coverage API
  slug: health-gorilla-coverage-api
- description: Structured lab and radiology results.
  name: Health Gorilla DiagnosticReport API
  slug: health-gorilla-diagnosticreport-api
- description: Clinical document metadata.
  name: Health Gorilla DocumentReference API
  slug: health-gorilla-documentreference-api
- description: Individual result observations.
  name: Health Gorilla Observation API
  slug: health-gorilla-observation-api
- description: Patient demographics and patient-scoped record retrieval.
  name: Health Gorilla Patient API
  slug: health-gorilla-patient-api
- description: Ordering and rendering providers.
  name: Health Gorilla Practitioner API
  slug: health-gorilla-practitioner-api
- description: Parent diagnostic orders nesting individual ServiceRequest tests.
  name: Health Gorilla RequestGroup API
  slug: health-gorilla-requestgroup-api
- description: Diagnostic (lab and radiology) order requests.
  name: Health Gorilla ServiceRequest API
  slug: health-gorilla-servicerequest-api
arazzos:
- description: Locate a patient, search their insurance Coverage resources, then read a single Coverage for full plan detail.
  name: Health Gorilla Coverage Retrieval
  slug: health-gorilla-coverage-workflow
- description: Confirm server capabilities, locate a patient, then place a laboratory order as a ServiceRequest grouped inside a RequestGroup.
  name: Health Gorilla FHIR Lab Order
  slug: health-gorilla-lab-order-workflow
- description: Locate a patient, read the Patient resource, then pull the complete US Core record with the Patient $everything operation.
  name: Health Gorilla Patient Everything
  slug: health-gorilla-patient-everything-workflow
- description: Locate a patient, then pull their US Core laboratory DiagnosticReports, read one report, and retrieve the discrete result Observations.
  name: Health Gorilla Lab Results Retrieval
  slug: health-gorilla-results-retrieval-workflow
artifact_total: 21
collections:
- collection_type: open
  name: Health Gorilla FHIR R4 API
  slug: open-health-gorilla
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/health-gorilla-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/health-gorilla-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/health-gorilla-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/healthgorilla
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/health-gorilla
- group: company
  title: ''
  type: Website
  url: https://www.healthgorilla.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.healthgorilla.com
- group: commercial
  title: ''
  type: Plans
  url: plans/health-gorilla-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/health-gorilla-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/health-gorilla-finops.yml
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
created: '2026-06-21'
description: Health Gorilla operates a national health-data interoperability network and a FHIR-first API suite for healthcare developers. Its HL7 FHIR R4 REST API provides access to patient records, person-authorized record retrieval across national exchange networks (QHIN / TEFCA), diagnostic (lab and radiology) ordering and results, clinical documents, and coverage/eligibility data under OAuth 2.0.
finops:
- name: Health Gorilla Finops
  service_category: Healthcare Interoperability
  slug: health-gorilla-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/health-gorilla.png
layout: provider
modified: '2026-06-21'
name: Health Gorilla
nav: Providers
network: true
overview: 'Health Gorilla publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Binary API, CapabilityStatement API, Coverage API, and 7 more. Tagged areas include Health, Interoperability, FHIR, Clinical Data, and Lab Ordering.


  Health Gorilla''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Health Gorilla Plans Pricing
  plan_count: 3
  slug: health-gorilla-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 3
  name: Health Gorilla Rate Limits
  slug: health-gorilla-rate-limits
score:
  band: thin
  composite: 34.2
  delta: -3.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.1
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/health-gorilla/refs/heads/main/screenshots/health-gorilla-2026-07-25T220828.png
security:
- kind: authentication
  name: Health Gorilla Authentication
  slug: health-gorilla-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Health Gorilla Domain Security
  slug: health-gorilla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: health-gorilla
tags:
- Health
- Interoperability
- FHIR
- Clinical Data
- Lab Ordering
website: https://www.healthgorilla.com
---
