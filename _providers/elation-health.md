---
access_model:
  confidence: medium
  label: Paid · Partner / sandbox onboarding
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - authentication
  - documentation
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.2
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 455
  human_in_the_loop: 0
  name: Elation Health Agentic Access
  operation_count: 846
  slug: elation-health-agentic-access
  summary_line: 846 operations · 455 acting
api_count: 32
apis:
- description: OAuth2 token endpoint for the Elation API v2.0. Partners exchange client credentials (and legacy password grant) for a bearer access token, optionally scoped with apiv2, act_as_user, or system/{resour
  name: Elation OAuth API
  slug: oauth-api
- description: Read and write patient demographic and clinical profile data - patients, allergies, problems, medications, vitals, and related clinical records - via the Elation API v2.0.
  name: Elation Patient Profile API
  slug: patient-profile-api
- description: Create, retrieve, and manage clinical visit notes and their documentation, including note signing, via the Elation API v2.0.
  name: Elation Visit Notes API
  slug: visit-notes-api
- description: Manage patient documents and document-based clinical data - the largest surface of the Elation API v2.0 - including uploads, retrieval, tagging, and document workflows.
  name: Elation Patient Document API
  slug: patient-document-api
- description: Create and manage clinical orders - laboratory, imaging, and other diagnostic orders, plus related order workflows - via the Elation API v2.0.
  name: Elation Orders API
  slug: orders-api
- description: Manage appointments, appointment types, and provider schedules for a practice via the Elation API v2.0.
  name: Elation Scheduling API
  slug: scheduling-api
- description: Manage billing data - bills, billing codes, and outstanding balances - for a practice via the Elation API v2.0.
  name: Elation Billing API
  slug: billing-api
- description: Manage insurance companies and insurance plans, and related payer reference data, via the Elation API v2.0.
  name: Elation Insurance API
  slug: insurance-api
- description: Premium patient insurance API for managing patient policies, insurance card images, and running insurance eligibility checks and full eligibility reports via the Elation API v2.0.
  name: Elation Patient Insurance API (Premium) & Eligibility
  slug: patient-insurance-api
- description: Manage practice-level entities - practices, physicians/providers, service locations, and related organizational data - via the Elation API v2.0.
  name: Elation Practice API
  slug: practice-api
- description: Manage application users and their access within a practice via the Elation API v2.0.
  name: Elation User Management API
  slug: user-management-api
- description: Manage message threads and thread members for provider and patient messaging workflows via the Elation API v2.0.
  name: Elation Messaging API
  slug: messaging-api
- description: Subscribe to and manage webhook event subscriptions and published events, enabling near-real-time notifications on clinical and administrative changes via the Elation API v2.0.
  name: Elation Event Subscription API
  slug: event-subscription-api
- description: Retrieve shared reference and lookup data used across the Elation platform via the Elation API v2.0.
  name: Elation Reference Data API
  slug: reference-data-api
- description: Retrieve care gap definitions and quality-program care-gap data for value-based care workflows. Served from a dedicated care-gaps service host.
  name: Elation Care Gaps API
  slug: care-gaps-api
- description: Interact with data imports into a practice - submitting and managing bulk clinical and administrative data imports - via the Elation Import API.
  name: Elation Import API
  slug: import-api
- description: Elation Health API Settings from Elation Health — 218 path(s) described in OpenAPI.
  name: Elation Health API Settings
  slug: elation-api-settings
- description: Allergy and drug intolerance tracking
  name: Elation Health Allergies API
  slug: elation-allergies-api
- description: Scheduling and appointment management
  name: Elation Health Appointments API
  slug: elation-appointments-api
- description: OAuth2 token management
  name: Elation Health Authentication API
  slug: elation-authentication-api
- description: Billing codes and bill management
  name: Elation Health Billing API
  slug: elation-billing-api
- description: Insurance company, plan, and policy management
  name: Elation Health Insurance API
  slug: elation-insurance-api
- description: Laboratory order management
  name: Elation Health Lab Orders API
  slug: elation-lab-orders-api
- description: Medication and prescription management
  name: Elation Health Medications API
  slug: elation-medications-api
- description: Secure direct messaging
  name: Elation Health Messaging API
  slug: elation-messaging-api
- description: Patient profile management
  name: Elation Health Patients API
  slug: elation-patients-api
- description: Provider and staff management
  name: Elation Health Physicians API
  slug: elation-physicians-api
- description: Practice administration
  name: Elation Health Practices API
  slug: elation-practices-api
- description: Patient problem list management
  name: Elation Health Problems API
  slug: elation-problems-api
- description: Clinical encounter documentation
  name: Elation Health Visit Notes API
  slug: elation-visit-notes-api
- description: The complete, provider-published OpenAPI 3.1.0 description of the Elation Health API v2.0 - 201 paths and 419 operations across the Patient Profile, Patient Document, Orders, Scheduling, Billing, Insu
  name: Elation Health API (Full v2.0)
  slug: elation-api-full
- description: HL7 FHIR R4 (v4.0.1) API with US Core v5.0.1 and SMART on FHIR 1.0.0 support, used for standards-based interoperability and ONC / CMS 21st Century Cures Act certified health IT use cases. Exposed to r
  name: Elation FHIR R4 API
  slug: fhir-api
artifact_total: 88
asyncapis:
- description: ''
  name: Elation Health Events Webhooks
  slug: elation-health-events-webhooks
collections:
- collection_type: postman
  name: API Authentication
  slug: postman-elation-api-authentication
- collection_type: postman
  name: Billing API
  slug: postman-elation-billing-api
- collection_type: postman
  name: Care Gaps API
  slug: postman-elation-care-gaps-api-1
- collection_type: postman
  name: Elation Import API
  slug: postman-elation-elation-import-api
- collection_type: postman
  name: Event Subscription API
  slug: postman-elation-event-subscription-api
- collection_type: postman
  name: Insurance API
  slug: postman-elation-insurance-api
- collection_type: postman
  name: Messaging API
  slug: postman-elation-messaging-api
- collection_type: postman
  name: Orders API
  slug: postman-elation-orders-api
- collection_type: postman
  name: Patient Document API
  slug: postman-elation-patient-document-api
- collection_type: postman
  name: Patient Profile API
  slug: postman-elation-patient-profile-api
- collection_type: postman
  name: Practice API
  slug: postman-elation-practice-api
- collection_type: postman
  name: '[Premium] Patient Insurance API'
  slug: postman-elation-premium-patient-insurance-api
- collection_type: postman
  name: Reference Data API
  slug: postman-elation-reference-data-api
- collection_type: postman
  name: Scheduling API
  slug: postman-elation-scheduling-api
- collection_type: postman
  name: User Management API
  slug: postman-elation-user-management-api
- collection_type: postman
  name: Visit Notes API
  slug: postman-elation-visit-notes-api
- collection_type: open
  name: API Authentication
  slug: open-elation-api-authentication
- collection_type: open
  name: API Settings
  slug: open-elation-api-settings
- collection_type: open
  name: Billing API
  slug: open-elation-billing-api
- collection_type: open
  name: Care Gaps API
  slug: open-elation-care-gaps-api-1
- collection_type: open
  name: Elation Import API
  slug: open-elation-elation-import-api
- collection_type: open
  name: Event Subscription API
  slug: open-elation-event-subscription-api
- collection_type: open
  name: Elation Health REST Allergies API
  slug: open-elation-health-allergies-api
- collection_type: open
  name: Elation Health REST Allergies Appointments API
  slug: open-elation-health-appointments-api
- collection_type: open
  name: Elation Health REST Allergies Authentication API
  slug: open-elation-health-authentication-api
- collection_type: open
  name: Elation Health REST Allergies Lab Orders API
  slug: open-elation-health-lab-orders-api
- collection_type: open
  name: Elation Health REST Allergies Medications API
  slug: open-elation-health-medications-api
- collection_type: open
  name: Elation Health REST Allergies Patients API
  slug: open-elation-health-patients-api
- collection_type: open
  name: Elation Health REST Allergies Physicians API
  slug: open-elation-health-physicians-api
- collection_type: open
  name: Elation Health REST Allergies Practices API
  slug: open-elation-health-practices-api
- collection_type: open
  name: Elation Health REST Allergies Problems API
  slug: open-elation-health-problems-api
- collection_type: open
  name: Insurance API
  slug: open-elation-insurance-api
- collection_type: open
  name: Messaging API
  slug: open-elation-messaging-api
- collection_type: open
  name: Orders API
  slug: open-elation-orders-api
- collection_type: open
  name: Patient Document API
  slug: open-elation-patient-document-api
- collection_type: open
  name: Patient Profile API
  slug: open-elation-patient-profile-api
- collection_type: open
  name: Practice API
  slug: open-elation-practice-api
- collection_type: open
  name: '[Premium] Patient Insurance API'
  slug: open-elation-premium-patient-insurance-api
- collection_type: open
  name: Reference Data API
  slug: open-elation-reference-data-api
- collection_type: open
  name: Scheduling API
  slug: open-elation-scheduling-api
- collection_type: open
  name: User Management API
  slug: open-elation-user-management-api
- collection_type: open
  name: Visit Notes API
  slug: open-elation-visit-notes-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/elation-health/overview
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/elation-health-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/elation-health-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/elation-health-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elation-health-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elation-health-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elation-health-problem-types.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.elationhealth.com/solutions/ehr/
- group: design
  title: ''
  type: Conformance
  url: conformance/elation-health-conformance.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/elation-health-tool-crosswalk.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/elation-health-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/elation-health-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/elation-health-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elation-health-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elation-health-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elation-health-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/elation-health-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elation-health-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.elationhealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.elationhealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.elationhealth.com/docs/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.elationhealth.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.elationhealth.com/docs/getting-started-2
- group: auth
  title: ''
  type: Authentication
  url: https://docs.elationhealth.com/docs/oauth
- group: design
  title: ''
  type: Webhooks
  url: https://docs.elationhealth.com/docs/webhooks
- group: other
  title: ''
  type: ModelContextProtocol
  url: https://docs.elationhealth.com/docs/mcp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elationemr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elationhealth/
- group: company
  title: ''
  type: Blog
  url: https://www.elationhealth.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elationhealth.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.elationhealth.com/contact-us/sandbox/
- group: operate
  title: ''
  type: Support
  url: https://www.elationhealth.com/contact-us/
- group: operate
  title: ''
  type: StatusPage
  url: https://elationhealth.statuspage.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elationhealth.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elationhealth.com/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.elationhealth.com/reference/api-overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/elationemr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elationhealth
- group: company
  title: ''
  type: Blog
  url: https://www.elationhealth.com/resources/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elationhealth.com/contact-us/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://elationhealth.statuspage.io
- group: other
  title: ''
  type: X
  url: https://x.com/elationhealth
- group: commercial
  title: ''
  type: Plans
  url: plans/elation-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elation-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/elation-health-finops.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/elation-health-a2a.yml
- group: build
  title: ''
  type: Examples
  url: examples/elation-health-patient-example.json
- group: build
  title: ''
  type: Examples
  url: examples/elation-health-appointment-example.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/elation-health-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/elation-health-jsonschema-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/elation-health-patient-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/elation-health-context.jsonld
- group: agent
  title: ''
  type: AgentSkill
  url: skills/elation-health-provider-published-skill.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.elationhealth.com/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://help.elationhealth.com/articles/rest/overview/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://help.elationhealth.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.elationhealth.com/articles/rest/overview/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://help.elationhealth.com/articles/rest/overview/oauth
- group: auth
  title: ''
  type: OAuthScopes
  url: https://help.elationhealth.com/articles/rest/overview/scopes
- group: design
  title: ''
  type: Webhooks
  url: https://help.elationhealth.com/articles/rest/overview/webhooks
- group: other
  title: ''
  type: ModelContextProtocol
  url: https://help.elationhealth.com/articles/rest/overview/mcp-server
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.elationhealth.com/articles/rest/changelog/changelog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.elationhealth.com/
- group: operate
  title: ''
  type: Support
  url: https://help.elationhealth.com/articles/rest/overview/getting-help
- group: auth
  title: ''
  type: Compliance
  url: https://help.elationhealth.com/compliance-quality
created: '2026-07-24'
description: Elation Health is a United States clinical-first electronic health record (EHR/EMR) and healthcare technology company, founded in 2010 and headquartered in San Francisco, California, serving independent primary care practices, value-based care organizations, digital health startups, and health-tech partners. Beyond its provider-facing EHR, Elation ships a broad, well-documented public REST API (v2.0) that lets partners read and write clinical and administrative data - patient profiles and demographics, allergies and problems, visit notes, clinical and lab/imaging orders, patient documents, scheduling, billing, insurance and eligibility, messaging, practice and user management, care gaps, and data import - authenticated with OAuth2. The API is documented on a ReadMe developer portal backed by machine-readable OpenAPI definitions, augmented with event subscription webhooks and a Model Context Protocol (MCP) server for agentic access. Elation also operates login-gated HL7 FHIR
  R4 and SMART-on-FHIR interoperability endpoints for ONC/CMS 21st Century Cures Act information-blocking compliance, exposed to registered applications rather than anonymously. Positioned as an independent challenger to the US EHR duopoly, Elation targets the primary-care and value-based-care segment of the largest, most commercial healthcare-API market.
examples:
- key_count: 18
  name: Elation Health Appointment Example
  slug: elation-health-appointment-example
- key_count: 25
  name: Elation Health Patient Example
  slug: elation-health-patient-example
finops:
- name: Elation Health Finops
  service_category: ''
  slug: elation-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: Patient
  property_count: 43
  slug: elation-health-patient
jsonld:
- class_count: 28
  name: Elation Health Context
  property_count: 69
  slug: elation-health-context
layout: provider
mcp_servers:
- description: ''
  name: Elation Health MCP Server
  slug: elation-health-mcp-server
modified: '2026-08-14'
name: Elation Health
nav: Providers
network: true
overview: 'Elation Health publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Elation OAuth API, Elation Patient Profile API, Elation Visit Notes API, and 28 more. Tagged areas include Healthcare, United States, EHR, EMR, and FHIR.


  The Elation Health catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Elation Health''s developer surface includes sandbox, changelog, authentication, documentation, API reference, getting-started guide, engineering blog, and 59 more developer resources.'
plans:
- name: Elation Health Plans Pricing
  plan_count: 3
  slug: elation-health-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Elation Health Rate Limits
  slug: elation-health-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Elation Health API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: elation-health-jsonschema-spectral-rules
scopes:
- name: Elation Health Scopes
  scope_count: 154
  slug: elation-health-scopes
  summary_line: 154 scopes · clientCredentials/password
score:
  band: exemplar
  composite: 83.8
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 55.3
    contract_quality: 71.0
    developer_ergonomics: 76.2
    discoverability: 92.6
    governance: 55.3
    operational_transparency: 42.1
  previous_composite: 83.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 92.9
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 92.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elation-health/refs/heads/main/screenshots/elation-health-2026-07-25T213054.png
security:
- kind: authentication
  name: Elation Health Authentication
  slug: elation-health-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Elation Health Domain Security
  slug: elation-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elation-health
tags:
- Healthcare
- United States
- EHR
- EMR
- FHIR
- HL7
- Interoperability
- SMART on FHIR
- Primary Care
- Value-Based Care
- Eligibility
- Clinical Data
- Scheduling
- e-Prescribing
- Digital Health
website: https://www.elationhealth.com/
---
