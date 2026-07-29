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
- acting_count: 17
  human_in_the_loop: 0
  name: Particle Health Agentic Access
  operation_count: 59
  slug: particle-health-agentic-access
  summary_line: 59 operations · 17 acting
api_count: 17
apis:
- description: OAuth 2 client-credentials JWT issuance.
  name: Particle Health Authentication API
  slug: particle-health-authentication-api
- description: Batch query orchestration over patient cohorts.
  name: Particle Health Batches API
  slug: particle-health-batches-api
- description: C-CDA clinical document retrieval.
  name: Particle Health CCDA API
  slug: particle-health-ccda-api
- description: Incremental change retrieval since a previous query.
  name: Particle Health Deltas API
  slug: particle-health-deltas-api
- description: Document upload, retrieval, and deletion.
  name: Particle Health Documents API
  slug: particle-health-documents-api
- description: FHIR R4 resource search and read.
  name: Particle Health FHIR API
  slug: particle-health-fhir-api
- description: Query result file download.
  name: Particle Health Files API
  slug: particle-health-files-api
- description: Flat (normalized columnar) clinical data domains.
  name: Particle Health Flat API
  slug: particle-health-flat-api
- description: HL7v2 ADT messages.
  name: Particle Health HL7v2 API
  slug: particle-health-hl7v2-api
- description: Directory search over connected network organizations.
  name: Particle Health NetworkParticipants API
  slug: particle-health-networkparticipants-api
- description: Project-level webhook notification configuration.
  name: Particle Health Notifications API
  slug: particle-health-notifications-api
- description: Patient demographic registration and lookup.
  name: Particle Health Patients API
  slug: particle-health-patients-api
- description: Project and service-account management.
  name: Particle Health Projects API
  slug: particle-health-projects-api
- description: Patient provider mapping across the network.
  name: Particle Health ProviderMap API
  slug: particle-health-providermap-api
- description: One-time network query orchestration.
  name: Particle Health Queries API
  slug: particle-health-queries-api
- description: Real-time encounter, transition, and ADT alerts.
  name: Particle Health Signal API
  slug: particle-health-signal-api
- description: Patient subscription management for Signal.
  name: Particle Health Subscriptions API
  slug: particle-health-subscriptions-api
arazzos:
- description: Register a patient, subscribe to encounter (ADT) notifications, trigger a sandbox event, and retrieve the resulting HL7 v2 messages.
  name: Particle Health ADT Event Subscription
  slug: particle-health-adt-subscription-workflow
- description: Submit a clinical document to the network, then retrieve it and list all documents on file for the patient.
  name: Particle Health Clinical Document Exchange
  slug: particle-health-clinical-document-exchange-workflow
- description: Create a FHIR Patient, run a FHIR-native network query, poll for completion, then search and read individual US Core resources.
  name: Particle Health FHIR R4 Resource Query
  slug: particle-health-fhir-r4-resource-query-workflow
- description: Register a patient, run a network query, then discover which providers and organizations hold records for that patient.
  name: Particle Health Network Provider Discovery
  slug: particle-health-network-provider-discovery-workflow
- description: Authenticate, register a patient demographic, run a national query across the health information networks, poll until the query completes, then collect the aggregated clinical record.
  name: Particle Health National Patient Record Retrieval
  slug: particle-health-patient-record-retrieval-workflow
artifact_total: 52
collections:
- collection_type: postman
  name: Particle Health Authentication API
  slug: postman-particle-health-authentication-api
- collection_type: postman
  name: Particle Health Authentication Batches API
  slug: postman-particle-health-batches-api
- collection_type: postman
  name: Particle Health Authentication CCDA API
  slug: postman-particle-health-ccda-api
- collection_type: postman
  name: Particle Health Authentication Deltas API
  slug: postman-particle-health-deltas-api
- collection_type: postman
  name: Particle Health Authentication Documents API
  slug: postman-particle-health-documents-api
- collection_type: postman
  name: Particle Health Authentication FHIR API
  slug: postman-particle-health-fhir-api
- collection_type: postman
  name: Particle Health Authentication Files API
  slug: postman-particle-health-files-api
- collection_type: postman
  name: Particle Health Authentication Flat API
  slug: postman-particle-health-flat-api
- collection_type: postman
  name: Particle Health Authentication HL7v2 API
  slug: postman-particle-health-hl7v2-api
- collection_type: postman
  name: Particle Health Authentication NetworkParticipants API
  slug: postman-particle-health-networkparticipants-api
- collection_type: postman
  name: Particle Health Authentication Notifications API
  slug: postman-particle-health-notifications-api
- collection_type: postman
  name: Particle Health Authentication Patients API
  slug: postman-particle-health-patients-api
- collection_type: postman
  name: Particle Health Authentication Projects API
  slug: postman-particle-health-projects-api
- collection_type: postman
  name: Particle Health Authentication ProviderMap API
  slug: postman-particle-health-providermap-api
- collection_type: postman
  name: Particle Health Authentication Queries API
  slug: postman-particle-health-queries-api
- collection_type: postman
  name: Particle Health Authentication Signal API
  slug: postman-particle-health-signal-api
- collection_type: postman
  name: Particle Health Authentication Subscriptions API
  slug: postman-particle-health-subscriptions-api
- collection_type: open
  name: Particle Health API
  slug: open-particle-health
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/particle-health/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/particle-health-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/particle-health-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/particle-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/particle-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/particle-health-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ParticleHealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/particle-health
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/particle_health
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCMT35sx6GKvA1mzMP6qyVkw
- group: company
  title: ''
  type: Website
  url: https://particlehealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.particlehealth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.particlehealth.com/reference/getting-started
- group: other
  title: ''
  type: Developer
  url: https://docs.particlehealth.com/docs/getting-started-for-developers
- group: start
  title: ''
  type: Sandbox
  url: https://docs.particlehealth.com/docs/test-patient-sandbox
- group: operate
  title: ''
  type: StatusPage
  url: https://status.particlehealth.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.particlehealth.com/docs/
- group: other
  title: ''
  type: Glossary
  url: https://docs.particlehealth.com/docs/glossary
- group: company
  title: ''
  type: Blog
  url: https://particlehealth.com/blog
- group: other
  title: ''
  type: Resources
  url: https://particlehealth.com/resources
- group: operate
  title: ''
  type: Contact
  url: https://particlehealth.com/contact
- group: operate
  title: ''
  type: Support
  url: ''
- group: auth
  title: ''
  type: ComplianceContact
  url: ''
- group: operate
  title: ''
  type: MediaContact
  url: ''
- group: operate
  title: ''
  type: PressReleases
  url: https://particlehealth.com/blog
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/particlehealth/particle-health-api
- group: agent
  title: ''
  type: LLMs
  url: https://docs.particlehealth.com/llms.txt
- group: design
  title: ''
  type: JSONLD
  url: json-ld/particle-health-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/particle-health-patient-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/particle-health-query-schema.json
- group: commercial
  title: ''
  type: Plans
  url: plans/particle-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/particle-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/particle-health-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/particle-health-vocabulary.yml
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
created: '2026-05-24'
description: Particle Health is a healthcare data interoperability platform that aggregates patient medical records from across the US healthcare system into a single RESTful API. Particle is connected to all three nationwide health information exchange networks (Carequality, CommonWell, eHealth Exchange), TEFCA / QHIN partners, state HIEs (Healthix in New York, Manifest MedEx in California), and Surescripts for pharmacy data. The platform exposes patient demographics, clinical resources, and document retrieval via FHIR R4, C-CDA, Flat, and Deltas formats, layered with deduplication, normalization, AI summarization (Particle Snapshot), real-time encounter and transition alerts (Particle Signal), and longitudinal patient journey tracking (Particle Navigator). Customer segments include value-based care organizations, payers, health systems, primary and specialty providers, and digital health developers.
finops:
- name: Particle Health Finops
  service_category: API
  slug: particle-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/particle-health.png
json_schemas:
- name: Particle Health Patient
  property_count: 10
  slug: particle-health-patient
- name: Particle Health Query
  property_count: 9
  slug: particle-health-query
jsonld:
- class_count: 0
  name: Particle Health Context
  property_count: 9
  slug: particle-health-context
layout: provider
modified: '2026-05-24'
name: Particle Health
nav: Providers
network: true
overview: 'Particle Health publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Batches API, CCDA API, and 14 more. Tagged areas include ADT, C-CDA, Care Coordination, Carequality, and Clinical Data.


  The Particle Health catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Particle Health''s developer surface includes authentication, YouTube channel, documentation, API reference, sandbox, changelog, engineering blog, and 24 more developer resources.'
plans:
- name: Particle Health Plans Pricing
  plan_count: 3
  slug: particle-health-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 3
  name: Particle Health Rate Limits
  slug: particle-health-rate-limits
rules:
- name: Particle Health API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: particle-health-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.8
  delta: -7.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 59.7
    developer_ergonomics: 43.5
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 61.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 35.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/particle-health/refs/heads/main/screenshots/particle-health-2026-06-20T191425.png
security:
- kind: authentication
  name: Particle Health Authentication
  slug: particle-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Particle Health Domain Security
  slug: particle-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Particle Health Vulnerability Disclosure
  slug: particle-health-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Particle Health Trust Center
  slug: particle-health-trust-center
  summary_line: SOC 2, HIPAA
slug: particle-health
tags:
- ADT
- C-CDA
- Care Coordination
- Carequality
- Clinical Data
- CommonWell
- Deltas
- eHealth Exchange
- EHR
- FHIR
- Health Data
- Health Information Exchange
- Healthcare
- HIE
- HL7
- HL7v2
- Interoperability
- Medical Records
- Patients
- Pharmacy
- QHIN
- Surescripts
- TEFCA
- USCDI
website: https://particlehealth.com/
---
