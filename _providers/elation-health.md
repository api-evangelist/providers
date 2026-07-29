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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 455
  human_in_the_loop: 0
  name: Elation Health Agentic Access
  operation_count: 846
  slug: elation-health-agentic-access
  summary_line: 846 operations · 455 acting
api_count: 16
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
artifact_total: 38
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
created: '2026-07-24'
description: Elation Health is a United States clinical-first electronic health record (EHR/EMR) and healthcare technology company, founded in 2010 and headquartered in San Francisco, California, serving independent primary care practices, value-based care organizations, digital health startups, and health-tech partners. Beyond its provider-facing EHR, Elation ships a broad, well-documented public REST API (v2.0) that lets partners read and write clinical and administrative data - patient profiles and demographics, allergies and problems, visit notes, clinical and lab/imaging orders, patient documents, scheduling, billing, insurance and eligibility, messaging, practice and user management, care gaps, and data import - authenticated with OAuth2. The API is documented on a ReadMe developer portal backed by machine-readable OpenAPI definitions, augmented with event subscription webhooks and a Model Context Protocol (MCP) server for agentic access. Elation also operates login-gated HL7 FHIR
  R4 and SMART-on-FHIR interoperability endpoints for ONC/CMS 21st Century Cures Act information-blocking compliance, exposed to registered applications rather than anonymously. Positioned as an independent challenger to the US EHR duopoly, Elation targets the primary-care and value-based-care segment of the largest, most commercial healthcare-API market.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: elation-health-mcp.yml
  slug: elation-health-mcpyml
modified: '2026-07-24'
name: Elation Health
nav: Providers
network: true
overview: 'Elation Health publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Elation OAuth API, Elation Patient Profile API, Elation Visit Notes API, and 13 more. Tagged areas include Healthcare, United States, EHR, EMR, and FHIR.


  The Elation Health catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Elation Health''s developer surface includes sandbox, changelog, authentication, documentation, API reference, getting-started guide, engineering blog, and 29 more developer resources.'
random_paper: 63
scopes:
- name: Elation Health Scopes
  scope_count: 5
  slug: elation-health-scopes
  summary_line: 5 scopes · clientCredentials/password
score:
  band: strong
  composite: 58.8
  delta: -2.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 51.6
    developer_ergonomics: 73.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 44.7
  previous_composite: 60.8
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 76.3
  schema_version: 0.6
  scored_at: '2026-07-28'
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
