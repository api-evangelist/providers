---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Jane App Agentic Access
  operation_count: 43
  slug: jane-app-agentic-access
  summary_line: 43 operations · 15 acting
api_count: 1
apis:
- description: 'Retrieve, list, and free-text search patient records for the practitioner''s accessible patients within a clinic. Free-text search is a POST-body endpoint so PII does not leak into query strings. Part '
  name: Jane Patients API
  slug: jane-patients-api
- description: Retrieve and list one-on-one appointment bookings for a clinic, with filtering by patient, staff member, location, treatment, and time window. Part of the Jane Developer Platform REST API.
  name: Jane Appointments API
  slug: jane-appointments-api
- description: Read clinic reference and scheduling data — locations, staff members, disciplines, treatments, and company details — that underpin booking and practice configuration. Part of the Jane Developer Platfo
  name: Jane Practice and Scheduling API
  slug: jane-scheduling-api
- description: Create, read, update, and list clinical medical-record data for a patient — observations, care plans and care plan activities, and medications (including full medication change history). Part of the J
  name: Jane Medical Records API
  slug: jane-medical-records-api
- description: 'Upload document files (PDF, JPEG, PNG up to 50 MB) to receive a document ID that can be referenced in other API calls, and retrieve a previously uploaded document. Part of the Jane Developer Platform '
  name: Jane Documents API
  slug: jane-documents-api
- description: Register, list, retrieve, and deregister webhook subscriptions so partners receive signed event notifications for a clinic. The signing secret is returned only once at registration. Part of the Jane D
  name: Jane Webhooks API
  slug: jane-webhooks-api
- description: Create, read, update, delete, and list Jane Extensions, and browse the catalog of approved extensions available to clinics. This is the management surface for the partner integrations built on the Jan
  name: Jane Extensions API
  slug: jane-extensions-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The Appointments API from Jane — 2 operation(s) for appointments.
  name: Jane Appointments API
  slug: jane-app-appointments-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The CarePlans API from Jane — 4 operation(s) for careplans.
  name: Jane Care Plans API
  slug: jane-app-careplans-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The Catalog API from Jane — 2 operation(s) for catalog.
  name: Jane Catalog API
  slug: jane-app-catalog-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The Company API from Jane — 1 operation(s) for company.
  name: Jane Company API
  slug: jane-app-company-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The Disciplines API from Jane — 2 operation(s) for disciplines.
  name: Jane Disciplines API
  slug: jane-app-disciplines-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The DocumentUploads API from Jane — 2 operation(s) for documentuploads.
  name: Jane Document Uploads API
  slug: jane-app-documentuploads-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The Extensions API from Jane — 2 operation(s) for extensions.
  name: Jane Extensions API
  slug: jane-app-extensions-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The Locations API from Jane — 2 operation(s) for locations.
  name: Jane Locations API
  slug: jane-app-locations-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The Medications API from Jane — 3 operation(s) for medications.
  name: Jane Medications API
  slug: jane-app-medications-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The Observations API from Jane — 2 operation(s) for observations.
  name: Jane Observations API
  slug: jane-app-observations-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The Patients API from Jane — 3 operation(s) for patients.
  name: Jane Patients API
  slug: jane-app-patients-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The StaffMembers API from Jane — 2 operation(s) for staffmembers.
  name: Jane Staff Members API
  slug: jane-app-staffmembers-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The Treatments API from Jane — 2 operation(s) for treatments.
  name: Jane Treatments API
  slug: jane-app-treatments-api
- baseURL: https://jdpdocsdemo.jane.qa
  baseurl_source: spec
  description: The Webhooks API from Jane — 2 operation(s) for webhooks.
  name: Jane Webhooks API
  slug: jane-app-webhooks-api
artifact_total: 28
asyncapis:
- description: ''
  name: Jane App Webhooks
  slug: jane-app-webhooks
collections:
- collection_type: open
  name: JDP API
  slug: open-jane-app-jdp
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/jane-app-capability-edges.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/jane-app-mcp.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/jane-app-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jane-app-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jane-app-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jane-app-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jane-app-scopes.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/jane-app-jdp-openapi.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jane-app-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jane-app-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://jane.statuspage.io/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jane-app-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jane-app-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://jane.app/security-and-trust
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jane-app-well-known.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/jane-app-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jane-app-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/jane-app-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/jane-app-jdp-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/jane-app-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://jane.app/contact
- group: company
  title: ''
  type: Website
  url: https://jane.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.jane.app/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.jane.app/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.jane.app/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.jane.app/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/janeapp
- group: commercial
  title: ''
  type: Pricing
  url: https://jane.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://jane.app/blog
- group: auth
  title: ''
  type: Security
  url: https://jane.app/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jane.app/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jane.app/terms
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jane-app-llms.txt
created: '2026-07-24'
description: 'Jane is a cloud-based practice management platform for health and wellness clinics, headquartered in North Vancouver, Canada, with regional data residency across Canada, the USA, the United Kingdom, and Australia. Jane combines online booking, scheduling, charting and clinical documentation (including AI-assisted notes), insurance billing, payments, patient intake, a patient mobile app, and telehealth in a single system used by interdisciplinary clinics — physiotherapy, massage therapy, chiropractic, counselling, midwifery, and more. The Jane Developer Platform (developers.jane.app) exposes a documented REST API that lets approved Technology Partners build "Jane Extensions" — practitioner-authorized integrations that read and write clinic data. Authentication is OAuth 2.0 with PKCE over OpenID Connect (Keycloak realms), using RS256 JWT bearer access tokens and granular scopes (e.g. observations:read). The API is date-versioned in the URL path and is per-clinic (https://<clinic>/api/YYYY-MM-DD/),
  covering patients, appointments, locations, staff, disciplines, treatments, medical records (observations, care plans, medications), document uploads, webhooks, and extension management. Jane is not FHIR/HL7-based: it is a proprietary REST practice-management API rather than a SMART-on-FHIR EHR interoperability surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Jane
nav: Providers
network: true
overview: 'Jane publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Care Plans API, Catalog API, and 11 more. Tagged areas include Healthcare, Canada, Practice Management, EHR, and EMR.


  The Jane catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Jane''s developer surface includes authentication, sandbox, support, documentation, API reference, getting-started guide, pricing, and 27 more developer resources.'
random_paper: 3
scopes:
- name: Jane App Scopes
  scope_count: 30
  slug: jane-app-scopes
  summary_line: 30 scopes · authorizationCode
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 66.3
    developer_ergonomics: 47.0
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 57.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 76.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jane-app/refs/heads/main/screenshots/jane-app-2026-07-25T223058.png
security:
- kind: authentication
  name: Jane App Authentication
  slug: jane-app-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Jane App Domain Security
  slug: jane-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Jane App Trust Center
  slug: jane-app-trust-center
  summary_line: SOC 2, PCI DSS
slug: jane-app
tags:
- Healthcare
- Canada
- Practice Management
- EHR
- EMR
- Scheduling
- Clinical Documentation
- Telehealth
- Health and Wellness
- REST API
- Authentication
- Webhook
website: https://jane.app/
---
