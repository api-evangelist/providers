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
  band: agent-ready
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Medplum Agentic Access
  operation_count: 8
  slug: medplum-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 4
apis:
- description: FHIR-aware GraphQL endpoint at https://api.medplum.com/fhir/R4/$graphql. Supports typed nested queries, reverse-reference traversal (_reference), FHIRPath-style array filtering, and access-policy enfo
  name: Medplum GraphQL API
  slug: medplum-graphql-api
- description: 'Bots are TypeScript serverless functions (AWS Lambda-style) executed in response to FHIR Subscriptions, HTTP triggers, or scheduled cron. Bots are the backbone of Medplum integrations — HL7v2 to FHIR '
  name: Medplum Bots
  slug: medplum-bots
- description: 'FHIR Subscription resources that match a search criteria and dispatch real-time notifications via REST hooks (webhooks) or Websockets when matching resources are created or updated. Subscriptions are '
  name: Medplum Subscriptions
  slug: medplum-subscriptions
- description: The Fhir API from Medplum — 4 operation(s) for fhir.
  name: Medplum Fhir API
  slug: medplum-fhir-api
arazzos:
- description: Read a resource, update it, then inspect its version history and prior version.
  name: Medplum Amend Resource With History
  slug: medplum-amend-resource-with-history-workflow
- description: Locate a patient by name, read the Patient resource, then pull that patient's Observations.
  name: Medplum Clinical Data Query
  slug: medplum-clinical-data-query-workflow
- description: Create an Observation result, then assemble a DiagnosticReport that references it.
  name: Medplum Create Diagnostic Report
  slug: medplum-create-diagnostic-report-workflow
- description: Create a Bot resource, then create a Subscription that invokes the Bot on resource changes.
  name: Medplum Deploy Bot
  slug: medplum-deploy-and-run-bot-workflow
- description: Create a FHIR R4 resource, read it back by id, update it, then search the resource type for it.
  name: Medplum FHIR Resource CRUD
  slug: medplum-fhir-resource-crud-workflow
- description: Find a preliminary Observation, patch its status to final, and read it back to confirm.
  name: Medplum Finalize Observation
  slug: medplum-finalize-observation-workflow
- description: Search a resource type, and if a match is found read it for audit then delete it.
  name: Medplum Find And Delete Resource
  slug: medplum-find-and-delete-resource-workflow
- description: Create a Patient, then record a vital-sign Observation that references that patient.
  name: Medplum Register Patient With Observation
  slug: medplum-register-patient-with-observation-workflow
- description: Create a FHIR resource, update it to mint a new version, read its history, then read a specific version.
  name: Medplum FHIR Resource Versioning
  slug: medplum-resource-versioning-workflow
- description: Create a Practitioner, create an Encounter linking the patient and practitioner, then read it back.
  name: Medplum Schedule Encounter
  slug: medplum-schedule-encounter-workflow
- description: Search for a Patient by identifier and update it if found, otherwise create it.
  name: Medplum Upsert Patient
  slug: medplum-upsert-patient-workflow
artifact_total: 74
collections:
- collection_type: postman
  name: Medplum - OpenAPI 3.0
  slug: postman-medplum-openapi-original
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/medplum-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/medplum-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/medplum-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/medplum-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medplum-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/medplum-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/medplum/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/medplum-amend-resource-with-history-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/medplum-create-diagnostic-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/medplum-deploy-and-run-bot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/medplum-finalize-observation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/medplum-find-and-delete-resource-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/medplum-register-patient-with-observation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/medplum-schedule-encounter-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/medplum-upsert-patient-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.medplum.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.medplum.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.medplum.com/docs/tutorials
- group: docs
  title: ''
  type: APIReference
  url: https://www.medplum.com/docs/api
- group: auth
  title: ''
  type: Authentication
  url: https://www.medplum.com/docs/auth
- group: build
  title: ''
  type: SDKs
  url: https://www.medplum.com/docs/sdk/core
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@medplum/core
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@medplum/react
- group: build
  title: ''
  type: CLI
  url: https://www.medplum.com/docs/cli
- group: start
  title: ''
  type: Console
  url: https://app.medplum.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.medplum.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.medplum.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medplum.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.medplum.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/medplum
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/medplum/medplum
- group: operate
  title: ''
  type: Support
  url: mailto:support@medplum.com
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/medplum
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: design
  title: ''
  type: SpectralRules
  url: rules/medplum-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/medplum-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/medplum-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/medplum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/medplum-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/medplum-finops.yml
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
created: '2026-05-25'
description: Medplum is an Apache 2.0 open-source, FHIR-native developer platform for shipping clinical software. It bundles a FHIR R4 datastore, REST and GraphQL APIs, a TypeScript SDK, React component library, OAuth 2.0 / SMART on FHIR authentication, declarative Access Policies, Subscriptions, and TypeScript-based serverless Bots — sold as a hosted service at api.medplum.com and as a self-hostable monorepo on GitHub. Medplum is HIPAA, SOC 2 Type II, and ONC-certified.
examples:
- key_count: 6
  name: Medplum Bot Hl7 To Fhir Example
  slug: medplum-bot-hl7-to-fhir-example
- key_count: 4
  name: Medplum Graphql Patient Query Example
  slug: medplum-graphql-patient-query-example
- key_count: 7
  name: Medplum Observation Bloodpressure Example
  slug: medplum-observation-bloodpressure-example
- key_count: 7
  name: Medplum Patient Create Example
  slug: medplum-patient-create-example
- key_count: 6
  name: Medplum Subscription Webhook Example
  slug: medplum-subscription-webhook-example
features:
- description: PostgreSQL-backed datastore that natively models FHIR R4 resources, including search, history, and versioning.
  name: FHIR-Native Datastore
- description: Dual API surface — FHIR REST and FHIR-aware GraphQL — sharing the same authorization, schema, and access policies.
  name: REST + GraphQL APIs
- description: AWS Lambda-style TypeScript functions executed by Subscriptions, HTTP, or cron triggers; the integration backbone of Medplum.
  name: Bots (Serverless TypeScript Functions)
- description: FHIR Subscription resources dispatch real-time notifications when matching resources change.
  name: Subscriptions (Webhooks + Websockets)
- description: Declarative resource- and field-level authorization rules attached to ProjectMembership.
  name: Access Policies
- description: Standards-based authentication and authorization, supporting SMART App Launch 2.0.0 and Bulk Data 2.0.0.
  name: SMART on FHIR + OAuth 2.0
- description: '@medplum/core, @medplum/react, and @medplum/react-hooks provide typed client and reusable UI primitives.'
  name: TypeScript SDK and React Components
- description: Bridges local clinical systems (HL7v2, DICOM, MLLP) to Medplum cloud.
  name: On-Premise Agent
- description: First-class CDK constructs for self-hosting Medplum on AWS.
  name: AWS CDK Deployment
finops:
- name: Medplum Finops
  service_category: API / Developer Platform
  slug: medplum-finops
graphqls:
- description: FHIR-aware GraphQL endpoint at https://api.medplum.com/fhir/R4/$graphql. Supports typed nested queries, reverse-reference traversal (_reference), FHIRPath-style array filtering, and access-policy enfo
  name: Medplum GraphQL API
  slug: medplum-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medplum.png
integrations:
- description: First-class deployment on AWS via CDK, with Bots running on Lambda and storage on RDS PostgreSQL.
  name: AWS
- description: Bidirectional HL7v2 messaging via the Medplum on-premise Agent.
  name: HL7v2
- description: Real-time clinical-context synchronization protocol support.
  name: FHIRcast
- description: Billing and payment integration examples for revenue cycle.
  name: Stripe
- description: SMS, voice, and messaging integration patterns via Bots.
  name: Twilio
- description: Patient consent and document-signing integration examples.
  name: DocuSeal / DocuSign
- description: Transactional email integration patterns via Bots.
  name: SendGrid / Mailgun
- description: Cross-platform FHIR data exchange examples.
  name: AWS HealthLake
json_schemas:
- name: Bot
  property_count: 28
  slug: medplum-bot
- name: Condition
  property_count: 34
  slug: medplum-condition
- name: Encounter
  property_count: 32
  slug: medplum-encounter
- name: MedicationRequest
  property_count: 43
  slug: medplum-medicationrequest
- name: Observation
  property_count: 46
  slug: medplum-observation
- name: Organization
  property_count: 19
  slug: medplum-organization
- name: Patient
  property_count: 27
  slug: medplum-patient
- name: Practitioner
  property_count: 19
  slug: medplum-practitioner
- name: Subscription
  property_count: 16
  slug: medplum-subscription
json_structures:
- name: Medplum Patient Structure
  property_count: 8
  slug: medplum-patient-structure
jsonld:
- class_count: 18
  name: Medplum Context
  property_count: 2
  slug: medplum-context
layout: provider
mcp_servers:
- description: ''
  name: medplum-mcp.yml
  slug: medplum-mcpyml
modified: '2026-07-27'
name: Medplum
nav: Providers
network: true
overview: 'Medplum publishes 1 API on the [APIs.io](https://apis.io/) network: Fhir API. Tagged areas include Healthcare, FHIR, Open Source, Developer Platform, and HIPAA.


  The Medplum catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Medplum''s developer surface includes authentication, documentation, getting-started guide, API reference, CLI, developer console, pricing, and 33 more developer resources.'
plans:
- name: Medplum Plans Pricing
  plan_count: 6
  slug: medplum-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 4
  name: Medplum Rate Limits
  slug: medplum-rate-limits
rules:
- name: Medplum API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: medplum-jsonschema-spectral-rules
- name: Medplum API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: medplum-rules
score:
  band: strong
  composite: 65.9
  delta: -7.8
  facets:
    commercial_clarity: 78.9
    contract_quality: 69.4
    developer_ergonomics: 84.8
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 73.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/medplum/refs/heads/main/screenshots/medplum-2026-06-20T185123.png
security:
- kind: authentication
  name: Medplum Authentication
  slug: medplum-authentication
  summary_line: http/openIdConnect · 3 schemes
- kind: domain-security
  name: Medplum Domain Security
  slug: medplum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Medplum Vulnerability Disclosure
  slug: medplum-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Medplum Trust Center
  slug: medplum-trust-center
  summary_line: SOC 2, HIPAA, GDPR, CSA STAR
slug: medplum
solutions:
- description: Build production EHR systems on top of Medplum.
  name: Custom EHR
- description: Reference patient-facing portal application.
  name: Patient Portal
- description: Reference provider-facing clinical application.
  name: Provider Portal
- description: Solution pattern for LLM-driven clinical documentation pipelines.
  name: AI-Powered Clinical Scribe
- description: Solution pattern for cohort identification and outcome tracking.
  name: Population Health Platform
- description: Solution pattern for automating claims, coverage, and billing workflows.
  name: Revenue Cycle Management
tags:
- Healthcare
- FHIR
- Open Source
- Developer Platform
- HIPAA
- SMART on FHIR
- Clinical
- Interoperability
use_cases:
- description: Build custom electronic health records on top of FHIR-native storage and React UI components.
  name: Custom EHR Development
- description: Ship patient-facing portals using SMART on FHIR auth and the Medplum React component library.
  name: Patient Engagement Portals
- description: Capture clinical notes, run them through LLM pipelines via Bots, and persist structured FHIR resources.
  name: AI Scribe and Clinical Documentation
- description: Receive legacy HL7v2 ADT, ORU, and SIU messages via the on-premise Agent and convert them to FHIR with Bots.
  name: HL7v2 to FHIR Integration
- description: Use Bulk Data 2.0 exports and GraphQL aggregations for cohort and population-level analysis.
  name: Population Health and Analytics
- description: Model longitudinal care plans, tasks, and questionnaires with FHIR-native resources.
  name: Care Management Workflows
- description: Automate claim, coverage, and explanation-of-benefit workflows with Bots and Subscriptions.
  name: Revenue Cycle Automation
website: https://www.medplum.com
---
